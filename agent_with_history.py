# agent_with_history.py
import os
import json
import shutil
from datetime import datetime
from pathlib import Path

# import your existing classes
from memento import Memory, Agent

CHATS_DIR = Path("chats")
BACKUPS_DIR = Path("backups")
MEMORY_FILE = Path("memory.json")

# ensure folders exist
CHATS_DIR.mkdir(exist_ok=True)
BACKUPS_DIR.mkdir(exist_ok=True)

def timestamp():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

class ChatHistoryManager:
    def __init__(self, chats_dir=CHATS_DIR):
        self.chats_dir = Path(chats_dir)
        self.session_file = None

    def start_session(self):
        name = f"{timestamp()}.json"
        self.session_file = self.chats_dir / name
        self._write_json(self.session_file, [])
        return self.session_file

    def append_message(self, role, text):
        if self.session_file is None:
            self.start_session()
        data = self._read_json(self.session_file)
        data.append({"role": role, "text": text, "time": datetime.now().isoformat()})
        self._write_json(self.session_file, data)

    def list_sessions(self):
        files = sorted(self.chats_dir.glob("*.json"), reverse=True)
        return files

    def read_session(self, file_ref):
        file_path = self._resolve_file(file_ref)
        return self._read_json(file_path)

    def export_session_text(self, file_ref, out_path=None):
        file_path = self._resolve_file(file_ref)
        messages = self._read_json(file_path)
        out_path = out_path or (file_path.with_suffix(".txt"))
        with open(out_path, "w", encoding="utf-8") as f:
            for m in messages:
                prefix = "You" if m["role"] == "user" else "AI" if m["role"] == "assistant" else m["role"]
                time = m.get("time", "")
                f.write(f"[{time}] {prefix}: {m['text']}\n\n")
        return out_path

    def _resolve_file(self, file_ref):
        # accept index or filename
        if isinstance(file_ref, int):
            files = self.list_sessions()
            try:
                return files[file_ref]
            except IndexError:
                raise FileNotFoundError("No session at that index.")
        else:
            p = Path(file_ref)
            if p.exists():
                return p
            # try in chats dir
            cand = self.chats_dir / file_ref
            if cand.exists():
                return cand
            raise FileNotFoundError(f"Session file not found: {file_ref}")

    @staticmethod
    def _read_json(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def _write_json(path, data):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

# Utility functions for memory manipulation (best-effort)
def backup_memory(memory_path=MEMORY_FILE):
    if memory_path.exists():
        bname = BACKUPS_DIR / f"memory_backup_{memory_path.stem}_{timestamp()}{memory_path.suffix}"
        shutil.copy2(memory_path, bname)
        return bname
    return None

def clear_memory(memory_path=MEMORY_FILE):
    backup_memory(memory_path)
    if not memory_path.exists():
        # nothing to clear; create empty structure (dict)
        memory_path.write_text(json.dumps({}), encoding="utf-8")
        return
    with open(memory_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, list):
        new = []
    elif isinstance(data, dict):
        new = {}
    else:
        new = {}
    with open(memory_path, "w", encoding="utf-8") as f:
        json.dump(new, f, indent=2, ensure_ascii=False)

def remove_message_from_memory_text(message_text, memory_path=MEMORY_FILE, max_matches=10):
    """
    Best-effort: load memory.json, recursively remove string elements or dict entries that contain message_text.
    Creates a backup before modifying.
    Returns number of removals.
    """
    if not memory_path.exists():
        # If file does not exist, create empty {}
        memory_path.write_text("{}", encoding="utf-8")
        return 0

    backup = backup_memory(memory_path)

    # Try reading the JSON safely
    try:
        with open(memory_path, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:   # file is empty
                data = {}
            else:
                data = json.loads(content)
    except Exception:
        # If file is corrupted, reset to {}
        data = {}

    removed_count = 0

    def recurse(obj):
        nonlocal removed_count
        if isinstance(obj, list):
            new_list = []
            for item in obj:
                if isinstance(item, str):
                    if message_text in item and removed_count < max_matches:
                        removed_count += 1
                        continue
                    else:
                        new_list.append(item)
                elif isinstance(item, (list, dict)):
                    new_list.append(recurse(item))
                else:
                    new_list.append(item)
            return new_list
        elif isinstance(obj, dict):
            new_dict = {}
            for k, v in obj.items():
                if isinstance(v, str):
                    if message_text in v and removed_count < max_matches:
                        removed_count += 1
                        continue
                    else:
                        new_dict[k] = v
                elif isinstance(v, (list, dict)):
                    new_dict[k] = recurse(v)
                else:
                    new_dict[k] = v
            return new_dict
        else:
            return obj

    new_data = recurse(data)

    with open(memory_path, "w", encoding="utf-8") as f:
        json.dump(new_data, f, ensure_ascii=False, indent=2)

    return removed_count


    removed_count = 0

    def recurse(obj):
        nonlocal removed_count
        if isinstance(obj, list):
            new_list = []
            for item in obj:
                if isinstance(item, str):
                    if message_text in item and removed_count < max_matches:
                        removed_count += 1
                        continue
                    else:
                        new_list.append(item)
                elif isinstance(item, (list, dict)):
                    new_item = recurse(item)
                    new_list.append(new_item)
                else:
                    new_list.append(item)
            return new_list
        elif isinstance(obj, dict):
            new_dict = {}
            for k, v in obj.items():
                # check keys too? only values for safety
                if isinstance(v, str):
                    if message_text in v and removed_count < max_matches:
                        removed_count += 1
                        continue
                    else:
                        new_dict[k] = v
                elif isinstance(v, (list, dict)):
                    new_dict[k] = recurse(v)
                else:
                    new_dict[k] = v
            return new_dict
        else:
            return obj

    new_data = recurse(data)

    with open(memory_path, "w", encoding="utf-8") as f:
        json.dump(new_data, f, ensure_ascii=False, indent=2)

    return removed_count

# ---------------- Main interactive loop ----------------
def main():
    memory = Memory(str(MEMORY_FILE))
    agent = Agent(model="llama3", memory=memory)  # adjust model name if needed

    history = ChatHistoryManager()
    current_session = history.start_session()
    print(f"Started session: {current_session}")

    current_messages = []  # in-memory session for quick access

    try:
        while True:
            user_input = input("You: ").strip()
            if not user_input:
                continue

            # Command handling
            if user_input.startswith("/"):
                parts = user_input.split()
                cmd = parts[0].lower()

                if cmd == "/history" or cmd == "/his":
                    if len(parts) == 1 or parts[1] == "list":
                        sessions = history.list_sessions()
                        if not sessions:
                            print("No saved sessions yet.")
                        else:
                            for i, f in enumerate(sessions):
                                print(f"[{i}] {f.name}")
                    elif parts[1] in ("show", "view"):
                        if len(parts) < 3:
                            print("Usage: /history show <index|filename>")
                        else:
                            ref = parts[2]
                            try:
                                ref_val = int(ref) if ref.isdigit() else ref
                                msgs = history.read_session(ref_val)
                                for m in msgs:
                                    who = "You" if m["role"] == "user" else "AI"
                                    print(f"[{m.get('time','')}] {who}: {m['text']}")
                            except Exception as e:
                                print("Error reading session:", e)
                    elif parts[1] == "export":
                        if len(parts) < 3:
                            print("Usage: /history export <index|filename>")
                        else:
                            ref = parts[2]
                            try:
                                ref_val = int(ref) if ref.isdigit() else ref
                                out = history.export_session_text(ref_val)
                                print("Exported to:", out)
                            except Exception as e:
                                print("Error exporting session:", e)
                    else:
                        print("Unknown /history subcommand.")
                    continue

                if cmd == "/save":
                    out = history.export_session_text(current_session)
                    print("Session saved as text:", out)
                    continue

                if cmd in ("/exit", "/quit"):
                    print("Exiting. Session auto-saved.")
                    history.export_session_text(current_session)
                    break

                if cmd == "/forget" and len(parts) >= 2 and parts[1] == "last":
                    # remove last user message from current session + memory.json
                    # get last user message from in-memory messages; fallback to file
                    last_user = None
                    for m in reversed(current_messages):
                        if m["role"] == "user":
                            last_user = m["text"]
                            break
                    if not last_user:
                        # try reading last session file
                        data = history._read_json(current_session)
                        for m in reversed(data):
                            if m.get("role") == "user":
                                last_user = m["text"]
                                break
                    if not last_user:
                        print("No user message found to forget.")
                        continue

                    print("Backing up memory and attempting to remove occurrences of the last user message from memory.json...")
                    matches = remove_message_from_memory_text(last_user)
                    print(f"Removed {matches} matching entries from memory.json (best-effort).")
                    # also remove from current session file
                    sess = history._read_json(current_session)
                    new_sess = []
                    skipped = 0
                    for m in sess:
                        if m.get("role") == "user" and m.get("text") == last_user and skipped == 0:
                            skipped += 1
                            continue
                        new_sess.append(m)
                    history._write_json(current_session, new_sess)
                    # update in-memory list too
                    for i in range(len(current_messages) - 1, -1, -1):
                        if current_messages[i]["role"] == "user" and current_messages[i]["text"] == last_user:
                            current_messages.pop(i)
                            break
                    print("Removed last user message from current session file.")
                    continue

                if cmd == "/reset":
                    b = backup_memory()
                    clear_memory()
                    print(f"memory.json backed up to {b} and cleared.")
                    continue

                print("Unknown command. Available: /history, /save, /forget last, /reset, /exit")
                continue

            # Normal chat flow
            current_messages.append({"role": "user", "text": user_input, "time": datetime.now().isoformat()})
            history.append_message("user", user_input)

            response = agent.chat(user_input)  # your agent call
            print("AI:", response)

            current_messages.append({"role": "assistant", "text": response, "time": datetime.now().isoformat()})
            history.append_message("assistant", response)

    except KeyboardInterrupt:
        print("\nInterrupted. Saving session...")
        history.export_session_text(current_session)

if __name__ == "__main__":
    main()

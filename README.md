# 🧠 AI Memento Project

A simple **AI memory assistant** built with Python.  
This bot can **remember facts about you**, **recall past conversations**, **summarize chat history**, and now even **change personality** and **tell time/date**.

---

##  Features by Day

###  Day 1–6
- Basic AI chatbot loop.
- Memory system using `memory.json`.
- Logs conversations to `chat_log.txt`.

###  Day 7
- Custom memory handling.
- Natural responses instead of repeating input.
- Chat logging improvements.

###  Day 8
- Added GitHub **tags per day** (day7, day8, …) for version snapshots.
- Organized `.gitignore` to avoid committing runtime files.

###  Day 9
- **Learns facts**: Name, Age, City, Hobby.
- **Answers questions** about remembered facts.
- **Summarizes recent chat history** with `history` / `recall` / `summary`.
- **Polite fallback** responses.
- **Reset memory** with `reset`.

###  Day 10 (Latest)
- **Personality modes**: friendly, formal, funny.
- **Date & time awareness**: answers questions like *“What’s the time?”* or *“What’s today’s date?”*.
- Keeps all previous memory and history features.
- More natural, engaging, and playful responses.

---

##  Example Usage

ou: set personality funny
AI: Haha, Personality switched to funny mode 😂

You: My name is Aliya
AI: 😊 Got it, your name is Aliya. I'll remember that.

You: What’s the time?
AI: 🤪 The current time is 16:42:10.

You: My hobby is painting
AI: Haha, Cool! I'll remember that your hobby is painting 😂

You: What did we talk about?
AI: Here’s a summary:
You: My name is Aliya
AI: Got it, your name is Aliya. I'll remember that.
You: My hobby is painting
AI: Cool! I'll remember that your hobby is painting.


---

##  Project Files
- `agent.py` → Main chatbot code  
- `memory.json` → Stores remembered facts  
- `chat_log.txt` → Stores chat history  
- `.gitignore` → Keeps memory/log files out of GitHub  

---

##  GitHub Tags
- `day7` → Custom memory & logging  
- `day8` → Git tags setup & cleanup  
- `day9` → Conversation history + smarter responses  
- `day10` → Personality modes + time/date awareness  

---

##  Next Steps (Future Ideas)
- Add **AI mood tracking** (happy, sad, neutral).  
- Add **reminders & alarms**.  
- Integrate **voice input/output** for hands-free interaction.

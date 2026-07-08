# AI Team Coach – Group Project Collaboration Assistant

> **Hackathon Theme:** EDU-04 – Group Projects Still Suck  
> **Solution:** An AI-powered assistant that helps teams communicate, coordinate, and stay accountable during group projects and hackathons.

---

## 📌 Problem Statement

Group projects and hackathons are difficult because teams often struggle with:

- Important questions going unanswered during meetings
- People talking over each other in voice calls
- Important ideas getting lost in long discussions
- Nobody clearly remembering final decisions
- Uneven task assignment – some overloaded, others with little work
- Missed deadlines due to poor progress tracking
- Forgetting what was discussed in previous meetings

These issues reduce productivity and make collaboration inefficient.

---

## 🚀 Our Solution: AI Team Coach

**AI Team Coach** is an intelligent collaboration assistant designed for student teams and hackathon participants.

With permission, it assists teams during voice meetings and group chats by:
- Understanding and summarizing discussions
- Organizing information (action items, decisions, ideas)
- Tracking project progress and deadlines
- Improving accountability and coordination

It acts like an intelligent project coordinator, **not** a replacement for teamwork.

---

## 🧰 Tech Stack

- **Frontend:** Streamlit (Python)
- **Backend:** Python
- **AI Integration:** OpenAI API (GPT-3.5/4)
- **Data Storage:** JSON file (`meetings.json`)
- **Version Control:** Git

---

## 📁 File Structure

```
.
├── .vscode/             # VS Code workspace settings
├── .gitignore           # Git ignore rules
├── SETUP.md             # Detailed setup instructions
├── app.py               # Main application logic + Streamlit UI
├── meetings.json        # Persistent storage for meeting data
├── .env                 # Environment variables (not committed)
└── README.md            # This file
```

---

## 🔧 Setup Instructions

### Step 1: Clone the repository

```bash
git clone https://github.com/yourusername/ai-team-coach.git
cd ai-team-coach
```

### Step 2: Create a virtual environment (recommended)

```bash
python -m venv venv
```

**On Windows:**
```bash
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

### Step 3: Install dependencies

```bash
pip install streamlit openai python-dotenv
```

### Step 4: Set up your OpenAI API key

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_api_key_here
```

⚠️ **Important:** Never commit your API key to version control!

### Step 5: Run the application

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`.

---

## 📋 Usage Guide

1. **Start a new meeting** – Enter a meeting name and agenda
2. **Add participants** – Optionally list team members
3. **Record discussion points** – Type key takeaways or questions
4. **Get AI summaries** – Click "Generate Summary" to receive an AI-powered digest of the discussion, including action items, decisions, and unresolved questions
5. **Track tasks** – Assign tasks to specific members with deadlines
6. **View history** – All meetings are saved in `meetings.json` and can be revisited

---

## 🤖 How AI is Used

- **Summarization:** Condenses long discussions into bullet points
- **Action Item Extraction:** Identifies tasks and assigns them to named individuals
- **Decision Tracking:** Highlights final decisions and unresolved issues
- **Follow-up Reminders:** Suggests follow-up questions or next steps

---

## 🔮 Future Enhancements

- Voice-to-text integration for real-time transcription
- Integration with Slack/Teams for automated meeting notes
- Dashboard for visual progress tracking
- User authentication and multi-team support
- Mobile app support

---


Made with ❤️ for the NYC Hackathon 2026 – EDU-04 Theme

# AI Team Coach - Complete Beginner Setup

You have **ZERO** ML/DL skills. That's fine. Here's exactly what to do.

---

## Step 1: Get Python Installed
**Check if you already have Python:**
```bash
python --version
```

If you don't, download from: https://www.python.org/downloads/
- Click "Download Python 3.11" (or latest)
- Run the installer
- ✅ Check "Add Python to PATH"

---

## Step 2: Create a Project Folder
```bash
mkdir ai-team-coach
cd ai-team-coach
```

---

## Step 3: Install Required Libraries
Copy-paste this into your terminal:
```bash
pip install streamlit openai python-dotenv
```

This downloads 3 tools:
- **streamlit** = Makes a web interface (no HTML/CSS needed)
- **openai** = Talks to OpenAI's AI
- **python-dotenv** = Keeps your API key safe

---

## Step 4: Get Your OpenAI API Key (FREE TIER AVAILABLE)
1. Go to https://platform.openai.com/api-keys
2. Sign up with your email
3. Create a new API key
4. Copy it (looks like: `sk-abc123...`)

> **Cost**: OpenAI charges, but free tier gives $5 credit. For a hackathon, it's basically free.

---

## Step 5: Put Your API Key In The Code
Open `app.py` and find this line:
```python
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY_HERE"
```

Replace with:
```python
OPENAI_API_KEY = "sk-your-actual-key-here"
```

---

## Step 6: Run The App
```bash
streamlit run app.py
```

You'll see:
```
You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168...
```

Open `http://localhost:8501` in your browser. **Done!**

---

## What You Can Do Now

### Test It
1. Go to "New Meeting" tab
2. Paste this:
```
Sarah: We need to fix the login bug by Friday
Tom: I'll handle the backend code
Priya: I'll do the testing
Tom: Can we also add dark mode?
Sarah: That's nice-to-have, not required
```
3. Click "Analyze This Meeting"
4. Watch the AI extract decisions, tasks, and questions!

### Use It For Your Hackathon
- Copy meeting transcripts → Paste in app → Get AI summary
- Save all summaries → Never forget what was decided
- Track who has what tasks

---

## Troubleshooting

### "ModuleNotFoundError: No module named 'streamlit'"
You skipped Step 3. Run:
```bash
pip install streamlit openai python-dotenv
```

### "API key not valid" error
Your API key is wrong. Get a new one from https://platform.openai.com/api-keys

### "Connection error"
Your internet is off, or OpenAI is down. Try again in a few seconds.

### Streamlit won't start
Make sure you're in the right folder:
```bash
cd ai-team-coach
streamlit run app.py
```

---

## How It Works (Simple Explanation)

```
You paste text
     ↓
Code sends it to OpenAI (cloud)
     ↓
OpenAI's AI reads it
     ↓
AI sends back summary
     ↓
Streamlit shows it on screen
```

That's it. **You're not building AI. You're using AI.**

---

## Next Steps (Optional Features for Your Hackathon)

Want to add audio? Replace this:
```python
# In the audio upload section, add this function:
def transcribe_audio(audio_file):
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript["text"]
```

Want to export as PDF? Add:
```bash
pip install fpdf
```

Want to keep a leaderboard of who did the most work? Add a counter in the analysis section.

---

**You've got this!**

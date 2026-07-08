import streamlit as st
import json
from datetime import datetime
import openai
from dotenv import load_dotenv
import os
# Set your API keys here (get from openai.com)
load_dotenv()
OPENAI_API_KEY = os.getenv("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")


# File to save meeting notes
MEETINGS_FILE = "meetings.json"

# Load previous meetings from file
def load_meetings():
    if os.path.exists(MEETINGS_FILE):
        with open(MEETINGS_FILE, "r") as f:
            return json.load(f)
    return []

# Save meetings to file
def save_meetings(meetings):
    with open(MEETINGS_FILE, "w") as f:
        json.dump(meetings, f, indent=2)

# Ask AI to analyze the discussion
def analyze_discussion(discussion_text):
    """Send text to OpenAI and get analysis back"""
    
    prompt = f"""
You are a helpful meeting coordinator. Analyze this meeting discussion and provide:

1. KEY DECISIONS - What was decided?
2. ACTION ITEMS - What tasks came up? Who should do them?
3. QUESTIONS UNANSWERED - What questions did NOT get answered?
4. TEAM MEMBERS MENTIONED - Who was involved?

Meeting text:
{discussion_text}

Format your response as clear sections with bullet points.
"""
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=[
                {"role": "system", "content": "You are a helpful meeting assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        return response['choices'][0]['message']['content']
    
    except Exception as e:
        return f"Error: {str(e)}\n\nMake sure you set your OpenAI API key correctly!"

# ======= STREAMLIT UI =======
st.set_page_config(page_title="AI Team Coach", layout="wide")

st.title("AI Team Coach")
st.write("Get meeting summaries, track tasks, and improve team coordination")

# Tabs
tab1, tab2, tab3 = st.tabs([" New Meeting", " Past Meetings", "Setup"])

# ========== TAB 1: NEW MEETING ==========
with tab1:
    st.header("Create a Meeting Summary")
    
    # Choosing input method
    input_method = st.radio("How do you want to input the meeting?", 
                            ["Paste text", "Upload audio"])
    
    if input_method == "Paste text":
        discussion = st.text_area(
            "Paste your meeting notes or transcript:",
            height=200,
            placeholder="Example: Tom said we need to fix the login bug by Friday. Sarah will design the mockups..."
        )
        
        if st.button(" Analyze This Meeting", type="primary"):
            if discussion.strip():
                st.info("Analyzing with AI... this takes a few seconds")
                analysis = analyze_discussion(discussion)
                
                st.markdown("##Meeting Analysis")
                st.markdown(analysis)
                
                # Save to history
                meeting = {
                    "date": datetime.now().isoformat(),
                    "discussion": discussion,
                    "analysis": analysis
                }
                meetings = load_meetings()
                meetings.append(meeting)
                save_meetings(meetings)
                
                st.success("Meeting saved!")
            else:
                st.warning("Please paste some text first!")
    
    else:  # Audio upload
        st.info("Audio requires API setup (see Setup tab) - for now, copy the transcript and use 'Paste text'")

# ========== TAB 2: PAST MEETINGS ==========
with tab2:
    st.header("Your Meeting History")
    
    meetings = load_meetings()
    
    if not meetings:
        st.info("No meetings saved yet. Create one in the 'New Meeting' tab!")
    else:
        st.write(f"Total meetings: {len(meetings)}")
        
        for i, meeting in enumerate(reversed(meetings)):
            with st.expander(f"Meeting {len(meetings) - i} - {meeting['date'][:10]}"):
                st.write("**Original Discussion:**")
                st.text(meeting['discussion'][:300] + "..." if len(meeting['discussion']) > 300 else meeting['discussion'])
                
                st.write("**AI Analysis:**")
                st.markdown(meeting['analysis'])

# ========== TAB 3: SETUP ==========
with tab3:
    st.header("Setup Instructions")
    
    st.subheader("Get Your OpenAI API Key")
    st.write("""
    - Go to https://platform.openai.com/api-keys
    - Sign up (it's free to start)
    - Create a new API key
    - Copy it
    """)
    
    st.subheader("Put It In Your Code")
    st.code("""
# In app.py, replace this line:
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY_HERE"

# With your actual key:
OPENAI_API_KEY = "sk-abc123..."
    """)
    
    st.subheader("Run This App")
    st.code("streamlit run app.py", language="bash")
    
    st.success("That's it! You're ready to go!")

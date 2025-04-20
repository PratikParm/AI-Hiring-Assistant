import sys
import asyncio

if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import streamlit as st
from llm_utils import load_model
from prompts import *

st.set_page_config(page_title="TalentScout - AI Hiring Assistant")
st.title("🤖 TalentScout AI Hiring Assistant")

# Initialize session state
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.answers = []
    st.session_state.tech_stack = ""
    st.session_state.questions_generated = False
    st.session_state.chat_history = []
    # Add greeting and first question
    st.session_state.chat_history.append(("assistant", GREETING))
    st.session_state.chat_history.append(("assistant", INFO_PROMPTS[0]))

pipe = load_model()

def generate_response(prompt):
    print('Got prompt:', prompt)
    # Show a spinner while generating response
    with st.spinner("Thinking..."):
        res = pipe.ask(prompt)
    return res.strip()

import re

def validate_input(step, user_input):
    if step == 0:  # Full name
        return len(user_input.split()) >= 2, "Please enter your full name."

    elif step == 1:  # Email
        pattern = r"[^@]+@[^@]+\.[^@]+"
        return re.match(pattern, user_input), "Please enter a valid email address."

    elif step == 2:  # Phone number
        pattern = r"^\+?\d{10,15}$"
        return re.match(pattern, user_input), "Please enter a valid phone number (10–15 digits)."

    elif step == 3:  # Years of experience
        return user_input.isdigit() and 0 <= int(user_input) <= 50, "Please enter a valid number of years."

    elif step == 4:  # Position
        return len(user_input.strip()) > 0, "Please enter the position you’re applying for."

    elif step == 5:  # Location
        return len(user_input.strip()) > 0, "Please enter your location."

    elif step == 6:  # Tech stack
        return len(user_input.strip()) > 0, "Please mention at least one technology."

    return True, ""

def handle_input(user_input):
    print('Handling input')
    # End conversation if user uses ending keywords
    if any(k in user_input.lower() for k in END_KEYWORDS):
        st.session_state.chat_history.append(("User", user_input))
        st.session_state.chat_history.append(("assistant", "Thanks for your time! We'll reach out soon. 👋"))
        st.session_state.step = -1
        return

    # Collect info prompts
    if st.session_state.step < len(INFO_PROMPTS):
        is_valid, error_message = validate_input(st.session_state.step, user_input)
        if not is_valid:
            st.session_state.chat_history.append(("User", user_input))
            st.session_state.chat_history.append(("assistant", f"⚠️ {error_message}"))
            return

        st.session_state.answers.append(user_input)
        st.session_state.chat_history.append(("User", user_input))
        st.session_state.step += 1

    elif not st.session_state.questions_generated:
        print('generating questions')
        st.session_state.tech_stack = user_input
        st.session_state.chat_history.append(("User", user_input))
        st.session_state.questions_generated = True
        prompt = generate_tech_questions_prompt(user_input)
        response = generate_response(prompt)
        st.session_state.chat_history.append(("assistant", response))
    else:
        print('ending')
        st.session_state.chat_history.append(("User", user_input))
        st.session_state.chat_history.append(("assistant", "Thanks for your answers! Your responses have been recorded."))

# Always show greeting on first load
if not st.session_state.chat_history:
    st.chat_message("assistant").write(GREETING)
    st.chat_message("assistant").write(INFO_PROMPTS[0])

# Handle user input
user_input = st.chat_input("Your response...")
if user_input:
    handle_input(user_input)

    # Show next prompt after user responds
    if st.session_state.step != -1:
        if st.session_state.step < len(INFO_PROMPTS):
            st.session_state.chat_history.append(("assistant", INFO_PROMPTS[st.session_state.step]))
        elif not st.session_state.questions_generated:
            st.session_state.chat_history.append(("assistant", "Which tech stack are you proficient in? (e.g., Python, React, MySQL, etc.)"))



# Display full chat history (to retain previous questions and answers)
for speaker, msg in st.session_state.chat_history:
    st.chat_message(speaker.lower()).write(msg)

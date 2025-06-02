# AI-Hiring-Assistant Project Report

## Introduction

**AI-Hiring-Assistant** (also referred to as "TalentScout - AI Hiring Assistant") is an interactive web-based tool designed to streamline the candidate screening process for technical job applications. The assistant leverages modern natural language processing (NLP) and large language models (LLMs) to automate the initial stages of hiring, such as gathering candidate details and generating personalized technical interview questions.

## Project Overview

- Repository: PratikParm/AI-Hiring-Assistant
- Interface: Streamlit web application
- Core functionality:
  - Conducts an interactive chat with candidates to collect personal and professional information.
  - Automatically generates technical questions based on the candidate’s stated technology stack.
  - Stores candidate responses for further review.

## Approach & Architecture

### 1. Interactive Candidate Chat

- The main app (`app.py`) uses Streamlit to deliver a chat-like experience.
- The chat starts with a greeting and sequentially asks for:
  - Full name
  - Email
  - Phone number
  - Years of experience
  - Position applied for
  - Location
  - Technology stack

- Input validation is performed for each step (e.g., checking for valid email/phone formats).

### 2. Dynamic Question Generation

- After gathering basic info, the assistant requests the candidate’s technology stack (e.g., Python, React).
- It then uses a prompt template to generate 3–5 technical interview questions tailored to the provided tech stack and mixes basic to advanced levels.
- The prompt for question generation is handled by the `generate_tech_questions_prompt` function in `prompts.py`.

### 3. LLM Integration

- The project includes a local LLM server (`model_server.py`) running a text generation model (e.g., GPT-2 via HuggingFace Transformers).
- Communication with the LLM is managed by `llm_utils.py`, which wraps the model server in a subprocess, sending prompts and receiving responses in real time.
- The `generate_response` function in the app handles the interaction between the Streamlit UI and the LLM backend.

### 4. Data Handling

- Candidate data (name, email, responses, etc.) is stored in a structured dictionary (`data_store.py`).
- The application supports updating and retrieving candidate information for further processing.

### 5. Extensibility & Testing

- The architecture is modular, with clear separations for UI (`app.py`), language model utilities (`llm_utils.py`), prompts (`prompts.py`), and data storage (`data_store.py`).
- There is a simple test wrapper (`testwrapper.py`) to interact with the LLM directly for debugging or development purposes.

## Features

- Conversational UI: Simulates a chat with an AI hiring assistant.
- Validation: Ensures data quality for essential candidate information.
- Personalized Questioning: Generates technical questions specific to each candidate’s expertise.
- LLM-based Reasoning: Leverages modern language models for question creation and conversation.
- Extensible Design: Easily adaptable to support more steps, additional data collection, or different LLMs.

## Conclusion

The AI-Hiring-Assistant project is a practical demonstration of applying conversational AI and LLMs to automate and personalize the candidate screening process. Its architecture enables real-time, context-aware interactions, and its modular codebase supports further enhancements for more advanced hiring workflows or deeper analytics.

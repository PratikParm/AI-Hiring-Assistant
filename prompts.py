GREETING = "Hi there! I'm TalentScout's AI Hiring Assistant 👋\n\nLet’s get started with a few basic questions to know you better."

END_KEYWORDS = ["exit", "quit", "goodbye", "bye", "stop"]

INFO_PROMPTS = [
    "What is your full name?",
    "Can you share your email address?",
    "What's your phone number?",
    "How many years of experience do you have?",
    "What position are you applying for?",
    "Where are you currently based?"
]

def generate_tech_questions_prompt(tech_stack):
    return f"""You are a technical interviewer. Generate 3–5 technical interview questions for a candidate based on the following tech stack: {tech_stack}.
    
Please include a mix of difficulty levels (basic to advanced)."""
# test_wrapper.py
from llm_utils import load_model

model = load_model()
while True:
    prompt = input("You: ")
    reply = model.ask(prompt)
    print("Bot:", reply)

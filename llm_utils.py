import subprocess
import json

class LLMWrapper:
    def __init__(self):
        self.process = subprocess.Popen(
            ["python", "model_server.py"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True,
            bufsize=1
        )

        
    def ask(self, prompt):
        try:
            print(f"[LLMWrapper] Sending prompt: {prompt}")
            self.process.stdin.write(prompt + "\n")
            self.process.stdin.flush()

            # Wait and read the output line
            response_line = self.process.stdout.readline()
            print(f"[LLMWrapper] Received line: {response_line}")

            if not response_line:
                return "⚠️ No response from model server."

            data = json.loads(response_line)
            return data.get("result", "⚠️ No 'result' key in response.")

        except Exception as e:
            return f"⚠️ Error: {e}"


llm = None

def load_model():
    global llm
    if llm is None:
        llm = LLMWrapper()
    return llm

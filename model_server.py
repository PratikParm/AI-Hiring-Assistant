from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch
import sys
import json

def main():
    model_name = "gpt2"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenizer.pad_token = tokenizer.eos_token

    device = "cuda" if torch.cuda.is_available() else "cpu"

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto" if device == "cuda" else None,
        torch_dtype=torch.float16 if device == "cuda" else torch.float32
    )

    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=1.2
    )

    for line in sys.stdin:
        prompt = line.strip()
        if not prompt:
            continue
        try:
            output = pipe(prompt, max_new_tokens=150)
            generated = output[0]["generated_text"]
            response = generated[len(prompt):].strip()
            print(json.dumps({"result": response}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()

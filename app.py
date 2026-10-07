from transformers import pipeline

print("Loading the small language model...")
generator = pipeline(
    "text-generation",
    model="distilgpt2"
)

print("\nMini SLM Chatbot")
print("Type 'exit' to quit.\n")

while True:
    prompt = input("You: ").strip()

    if prompt.lower() == "exit":
        print("Goodbye!")
        break

    if not prompt:
        continue

    result = generator(
        prompt,
        max_new_tokens=60,
        do_sample=True,
        temperature=0.8,
        top_p=0.9,
        num_return_sequences=1
    )

    generated = result[0]["generated_text"]
    answer = generated[len(prompt):].strip()

    print("SLM:", answer or generated)
    print()

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "facebook/blenderbot-400M-distill"

# Load model (download on first run and reference local installation for consequent runs)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Conversation_history Let's initialize this list before any conversations occur
conversation_history = []

while True:
    # Encoding the conversation history
    history_string = "\n".join(conversation_history)

    # Fetch prompt from user
    input_text = input("> ")

    # Tokenization of user prompt and chat history
    inputs = tokenizer.encode_plus(history_string, input_text, return_tensors="pt")

    # Generate output from the model
    outputs = model.generate(**inputs)

    # Decode output
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
    print(response)

    # Update conversation history
    conversation_history.append(input_text)
    conversation_history.append(response)

from transformers import AutoTokenizer, AutoModelForCausalLM, BertTokenizer, BertForSequenceClassification
import torch

MODEL_NAME = r"C:\Users\<Your_UserName>\.cache\huggingface\hub\models--tiiuae--falcon-rw-1b\snapshots\e4b9872bb803165eb22f0a867d4e6a64d34fce19"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
model.eval()

bert_tokenizer = BertTokenizer.from_pretrained("bert_banking_classifier")
bert_model = BertForSequenceClassification.from_pretrained("bert_banking_classifier")
bert_model.eval()

id2label = bert_model.config.id2label

def classify_intent(text):
    inputs = bert_tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=128)
    with torch.no_grad():
        outputs = bert_model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
    pred_class = torch.argmax(probs, dim=1).item()
    return id2label[pred_class]

def generate_response(user_input):
    prompt = f"User: {user_input}\nResponse:"
    input_ids = tokenizer.encode(prompt, return_tensors="pt")

    with torch.no_grad():
        output = model.generate(
            input_ids,
            max_length=300,
            pad_token_id=tokenizer.eos_token_id,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.7
        )

    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    if generated_text.lower().startswith(prompt.lower()):
        generated_text = generated_text[len(prompt):].strip()

    sentences = [s.strip() for s in generated_text.split('.')]
    seen = set()
    unique_sentences = []
    for s in sentences:
        if s and s not in seen:
            unique_sentences.append(s)
            seen.add(s)

    cleaned_response = '. '.join(unique_sentences).strip()

    if cleaned_response and cleaned_response[-1] not in ".!?":
        cleaned_response += "."

    return cleaned_response

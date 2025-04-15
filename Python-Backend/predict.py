from transformers import BertTokenizer, BertForSequenceClassification
import torch

tokenizer = BertTokenizer.from_pretrained("bert_banking_classifier")
model = BertForSequenceClassification.from_pretrained("bert_banking_classifier")
model.eval()

id2label = model.config.id2label

def predict(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=128)
    with torch.no_grad():
        outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
    pred_class = torch.argmax(probs, dim=1).item()
    return id2label[pred_class]

print(predict("What is bond ladder?"))

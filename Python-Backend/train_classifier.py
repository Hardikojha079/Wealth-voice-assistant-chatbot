import pandas as pd
from datasets import Dataset
from transformers import BertTokenizer, BertForSequenceClassification, Trainer
from transformers import TrainingArguments
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import numpy as np
from sklearn.metrics import accuracy_score, f1_score

df = pd.read_csv("augmented_wealth_management_qa.csv")

df = df.rename(columns={"question": "text", "answer": "label"})

le = LabelEncoder()
df['label'] = le.fit_transform(df['label'])

id2label = dict(enumerate(le.classes_))
label2id = {v: k for k, v in id2label.items()}


train_df, val_df = train_test_split(df, test_size=0.30, stratify=df['label'], random_state=42)


train_dataset = Dataset.from_pandas(train_df)
val_dataset = Dataset.from_pandas(val_df)

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

def tokenize(batch):
    return tokenizer(batch['text'], padding='max_length', truncation=True, max_length=128)

train_dataset = train_dataset.map(tokenize)
val_dataset = val_dataset.map(tokenize)

model = BertForSequenceClassification.from_pretrained(
    "bert-base-uncased",
    num_labels=len(label2id),
    id2label=id2label,
    label2id=label2id
)

def compute_metrics(p):
    preds = np.argmax(p.predictions, axis=1)
    return {
        'accuracy': accuracy_score(p.label_ids, preds),
        'f1': f1_score(p.label_ids, preds, average='weighted')
    }

training_args = TrainingArguments(
    output_dir="./results",
    eval_strategy="epoch",
    save_strategy="epoch",
    logging_dir="./logs",
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=5,
    load_best_model_at_end=True,
    metric_for_best_model="accuracy",
    logging_steps=10,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    tokenizer=tokenizer,
    compute_metrics=compute_metrics
)

trainer.train()

trainer.save_model("bert_banking_classifier")
tokenizer.save_pretrained("bert_banking_classifier")

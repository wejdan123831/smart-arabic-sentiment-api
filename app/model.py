# app/model.py

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "CAMeL-Lab/bert-base-arabic-camelbert-mix-sentiment"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

def analyze_sentiment(text: str):
    inputs = tokenizer(text, return_tensors="pt", truncation=True)

    with torch.no_grad():
        outputs = model(**inputs)

    probs = torch.softmax(outputs.logits, dim=-1)
    idx = torch.argmax(probs, dim=-1).item()
    label = model.config.id2label[idx]

    return label, probs.tolist()[0]

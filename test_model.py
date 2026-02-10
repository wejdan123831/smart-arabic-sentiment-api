from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "CAMeL-Lab/bert-base-arabic-camelbert-mix-sentiment"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

def analyze_sentiment(text: str):
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    outputs = model(**inputs)
    probs = torch.softmax(outputs.logits, dim=1)
    predicted_class = torch.argmax(probs, dim=1).item()
    return predicted_class, probs.tolist()

texts = [
    "الأكل كان لذيذ",
    "الخدمة سيئة جداً"
]

id2label = model.config.id2label

for t in texts:
    label, confidence = analyze_sentiment(t)
    print(f"النص: {t}")
    print(f"التصنيف:{ id2label[label]}")
    print(f"الثقة: {confidence}")
    print("-" * 40)

# app/main.py

from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
import pandas as pd
import io

from app.model import analyze_sentiment
from app.utils import detect_text_column
from app.ai_summary import generate_ai_summary
from app.error_handler import register_exception_handlers
from app.config import MAX_FILE_SIZE
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Smart Arabic Sentiment API")



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)



register_exception_handlers(app)


class TextRequest(BaseModel):
    text: str



@app.post("/predict")
def predict(request: TextRequest):

    label, confidence = analyze_sentiment(request.text)

    return {
        "text": request.text,
        "sentiment": label,
        "confidence": confidence
    }


@app.post("/analyze-file")
async def analyze_file(file: UploadFile = File(...)):

    contents = await file.read()

    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(status_code=413, detail="File too large")

    filename = file.filename.lower()

    if filename.endswith(".csv"):
        df = pd.read_csv(io.BytesIO(contents))
    elif filename.endswith(".xlsx") or filename.endswith(".xls"):
        df = pd.read_excel(io.BytesIO(contents))
    else:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    text_column = detect_text_column(df)

    sentiments = []

    # 
    for text in df[text_column].astype(str):
        label, _ = analyze_sentiment(text)
        sentiments.append(label)

    df["sentiment"] = sentiments

    summary = df["sentiment"].value_counts().to_dict()

    ai_summary = generate_ai_summary(summary)

    return {
        "filename": file.filename,
        "used_column": text_column,
        "total_comments": len(df),
        "analysis": summary,
        "ai_summary": ai_summary
   }
from fastapi.staticfiles import StaticFiles


app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
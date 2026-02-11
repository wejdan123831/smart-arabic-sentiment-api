# app/utils.py

import pandas as pd

POSSIBLE_TEXT_COLUMNS = [
    "text", "comment", "review", "feedback",
    "تعليق", "تقييم", "ملاحظة", "الرأي"
]

def detect_text_column(df: pd.DataFrame):
    for col in df.columns:
        if col.strip().lower() in POSSIBLE_TEXT_COLUMNS:
            return col
    return df.columns[0]

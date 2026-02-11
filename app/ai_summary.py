# app/ai_summary.py

def generate_ai_summary(summary_dict: dict):

    positive = summary_dict.get("positive", 0)
    negative = summary_dict.get("negative", 0)
    neutral = summary_dict.get("neutral", 0)

    if positive > negative:
        return "بشكل عام، الآراء إيجابية مع وجود بعض الملاحظات البسيطة."
    elif negative > positive:
        return "يوجد نسبة سلبية ملحوظة وتحتاج مراجعة وتحسين."
    else:
        return "الآراء متقاربة بين الإيجابي والسلبي."


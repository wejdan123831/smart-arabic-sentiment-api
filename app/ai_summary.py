# app/ai_summary.py

def generate_ai_summary(summary_dict: dict):

    positive = summary_dict.get("positive", 0)
    negative = summary_dict.get("negative", 0)
    neutral = summary_dict.get("neutral", 0)

    total = positive + negative + neutral

    if total == 0:
        return "لا توجد بيانات كافية لإنشاء ملخص."

    pos_ratio = round((positive / total) * 100, 1)
    neg_ratio = round((negative / total) * 100, 1)
    neu_ratio = round((neutral / total) * 100, 1)

    # 🔎 تحليل أعمق
    if pos_ratio >= 70:
        insight = "مستوى رضا مرتفع جداً يعكس تجربة إيجابية واضحة."
        recommendation = "يوصى بالحفاظ على نفس مستوى الخدمة مع تحسينات طفيفة."
    elif pos_ratio >= 50:
        insight = "يوجد رضا عام، لكن هناك بعض الملاحظات التي يمكن تحسينها."
        recommendation = "تحليل التعليقات السلبية قد يساعد في رفع مستوى الرضا."
    elif neg_ratio >= 50:
        insight = "نسبة سلبية مرتفعة تشير إلى وجود مشكلات جوهرية."
        recommendation = "يوصى بمراجعة أسباب عدم الرضا واتخاذ إجراءات تصحيحية."
    else:
        insight = "الآراء متوازنة نسبياً بين الإيجابية والحيادية."
        recommendation = "يمكن تعزيز التجربة لزيادة نسبة الآراء الإيجابية."

    return (
        f"📊 تحليل النتائج:\n"
        f"- إيجابي: {pos_ratio}%\n"
        f"- محايد: {neu_ratio}%\n"
        f"- سلبي: {neg_ratio}%\n\n"
        f"🔎 الاستنتاج: {insight}\n"
        f"💡 التوصية: {recommendation}"
    )

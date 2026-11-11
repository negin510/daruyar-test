import re

def parse_prescription(text):
    """
    این تابع متن نسخه الکترونیک را دریافت کرده و لیستی از دیکشنری‌ها برمی‌گرداند.
    """
    results = []
    
    # الگوهای جستجو
    drug_pattern = r"([آ-یa-zA-Z\s]+)\s*(\d+)\s*(?:میلی‌گرم|mg|گرم)?"
    time_pattern = r"ساعت\s*(\d{1,2})"
    condition_pattern = r"(ناشتا|قبل از ناهار|قبل از شام|همراه با غذا|قبل از ورزش|بعد از ورزش|قبل از خواب|بعد از غذا|همراه با آب|با معده خالی|قبل از غذا|بعد از حمام|بعد از شستشو)"

    drugs = re.findall(drug_pattern, text)
    times = re.findall(time_pattern, text)
    conditions = re.findall(condition_pattern, text)

    if drugs:
        for i, drug in enumerate(drugs):
            item = {
                "name": drug[0].strip(),
                "dose": drug[1],
                "time": times[i] if i < len(times) else "نامشخص",
                "condition": conditions[i] if i < len(conditions) else "نامشخص"
            }
            results.append(item)
            
    return results

if name == "main":
    sample_text = "متفورمین ۵۰۰ ساعت ۸ ناشتا. پروتئین وی ۳۰ گرم بعد از ورزش. آتورواستاتین ۲۰ قبل از خواب."
    print("متن ورودی:", sample_text)
    print("خروجی استخراج:", parse_prescription(sample_text))

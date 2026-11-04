# med_parser.py
# استخراج نام دارو از متن پیامک

import re

def extract_drug_names(text):
    """
    استخراج نام داروها از متن پیامک با استفاده از Regex
    """
    pattern = r"(متفورمین|لوزارتان|آتورواستاتین|انسولین|گلیبن‌کلامید)"
    matches = re.findall(pattern, text)
    return list(set(matches)) # حذف تکراری‌ها

def test_extract_drug_names():
    text = "بیمار گرامی، متفورمین ۵۰۰ و لوزارتان ۲۵ تجویز شد."
    result = extract_drug_names(text)
    assert "متفورمین" in result
    assert "لوزارتان" in result
    assert "آتورواستاتین" not in result

def test_empty_text():
    assert extract_drug_names("") == []

def test_no_drug():
    assert extract_drug_names("سلام، حال شما چطور است؟") == []

if name == "main":
    print("تست ۱:", end=" "); test_extract_drug_names(); print("موفق")
    print("تست ۲:", end=" "); test_empty_text(); print("موفق")
    print("تست ۳:", end=" "); test_no_drug(); print("موفق")
    print("هر ۳ تست موفق بودند.")

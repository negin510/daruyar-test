import pytest
from med_parser import parse_prescription

def test_drug_name_extraction():
    text = "متفورمین ۵۰۰"
    result = parse_prescription(text)
    assert result[0]['name'] == "متفورمین"

def test_dose_extraction():
    text = "متفورمین ۵۰۰"
    result = parse_prescription(text)
    assert result[0]['dose'] == "۵۰۰"

def test_time_extraction():
    text = "متفورمین ۵۰۰ ساعت ۸"
    result = parse_prescription(text)
    assert result[0]['time'] == "۸"

def test_condition_extraction():
    text = "متفورمین ۵۰۰ ناشتا"
    result = parse_prescription(text)
    assert result[0]['condition'] == "ناشتا"

def test_empty_text():
    text = ""
    result = parse_prescription(text)
    assert len(result) == 0

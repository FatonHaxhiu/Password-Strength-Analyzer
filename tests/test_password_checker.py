import pytest
from password_strength_checker import check_password_strength

def test_empty_password():
    result = check_password_strength("")
    assert result["score"] == 0
    assert result["strength"] == "Invalid"
    assert "Password cannot be empty." in result["feedback"]

def test_short_password():
    result = check_password_strength("pass")
    assert result["score"] < 50
    assert result["strength"] == "Weak"
    assert "Password too short" in " ".join(result["feedback"])

def test_strong_password():
    result = check_password_strength("A1b@cD3eF4gH!")
    assert result["score"] >= 80
    assert result["strength"] == "Strong"
    assert not result["feedback"] or "Great password!" in result["feedback"]

def test_moderate_password():
    result = check_password_strength("Password123")
    assert 50 <= result["score"] < 80
    assert result["strength"] == "Medium"
    assert "Add special characters." in result["feedback"]

def test_entropy_low():
    result = check_password_strength("aaaaaa")
    assert "too predictable" in " ".join(result["feedback"])
from password_strength_checker import check_password_strength


def test_empty_password():
    """Test empty password handling."""
    result = check_password_strength("")
    assert result["score"] == 0
    assert result["strength"] == "Invalid"
    assert "Password cannot be empty." in result["feedback"]


def test_short_password():
    """Test password shorter than 8 characters."""
    result = check_password_strength("abc123")
    assert result["score"] < 50
    assert "Password too short" in " ".join(result["feedback"])


def test_no_uppercase():
    """Test password without uppercase letters."""
    result = check_password_strength("abc123!@#")
    assert "Add uppercase letters." in result["feedback"]


def test_no_lowercase():
    """Test password without lowercase letters."""
    result = check_password_strength("ABC123!@#")
    assert "Add lowercase letters." in result["feedback"]


def test_no_numbers():
    """Test password without numbers."""
    result = check_password_strength("Abcdef!@#")
    assert "Add numbers." in result["feedback"]


def test_no_special_chars():
    """Test password without special characters."""
    result = check_password_strength("Abc123def")
    assert "Add special characters." in result["feedback"]


def test_strong_password():
    """Test a strong password with all character types."""
    result = check_password_strength("Ab1@xyz789")
    assert result["score"] >= 80
    assert result["strength"] == "Strong"


def test_entropy_low():
    """Test password with low entropy."""
    result = check_password_strength("aaaaaa")
    assert "too predictable" in " ".join(result["feedback"])

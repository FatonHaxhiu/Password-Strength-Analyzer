import re
import math


def check_password_strength(password):
    """Evaluate password strength based on length, character types, and entropy."""
    if not password:
        return {"score": 0, "strength": "Invalid", "feedback": ["Password cannot be empty."]}

    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 30
    elif len(password) >= 8:
        score += 15
    else:
        feedback.append("Password too short, use at least 8 characters.")

    # Character type checks
    if re.search(r"[A-Z]", password):
        score += 20
    else:
        feedback.append("Add uppercase letters.")
    if re.search(r"[a-z]", password):
        score += 20
    else:
        feedback.append("Add lowercase letters.")
    if re.search(r"[0-9]", password):
        score += 15
    else:
        feedback.append("Add numbers.")
    if re.search(r"[^A-Za-z0-9]", password):
        score += 15
    else:
        feedback.append("Add special characters.")

    # Entropy calculation
    charset_size = 0
    if re.search(r"[a-z]", password):
        charset_size += 26
    if re.search(r"[A-Z]", password):
        charset_size += 26
    if re.search(r"[0-9]", password):
        charset_size += 10
    if re.search(r"[^A-Za-z0-9]", password):
        charset_size += 32
    entropy = math.log2(charset_size ** len(password)) if charset_size > 0 else 0
    if entropy < 50:
        feedback.append("Password is too predictable, try a more complex combination.")

    # Strength label
    strength = "Weak" if score < 50 else "Medium" if score < 80 else "Strong"
    return {"score": score, "strength": strength, "feedback": feedback}


def main():
    """Main function to run the CLI tool."""
    print("Password Strength Analyzer")
    password = input("Enter a password: ")
    result = check_password_strength(password)
    print(f"\nScore: {result['score']}/100")
    print(f"Strength: {result['strength']}")
    feedback = ", ".join(result['feedback']) if result['feedback'] else "Great password!"
    print(f"Feedback: {feedback}")


if __name__ == "__main__":
    main()

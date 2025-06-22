# Password Strength Analyzer

![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Platform](https://img.shields.io/badge/Platform-WSL2%20%7C%20Linux-lightgrey)
[![CI/CD](https://github.com/FatonHaxhiu/Password-Strength-Analyzer/workflows/CI/CD/badge.svg)](https://github.com/FatonHaxhiu/Password-Strength-Analyzer/actions)

A Python-based tool to evaluate password strength based on length, character diversity, entropy, and common patterns. It provides a score (0-100) and feedback to help users create secure passwords. The project includes a command-line interface (CLI) and an optional Flask web interface.

## Features
- **Password Evaluation**: Assesses passwords based on:
  - Length (minimum 8 characters, 12+ for bonus points).
  - Character types (uppercase, lowercase, numbers, special characters).
  - Entropy (randomness measure).
- **Feedback**: Provides a strength score and suggestions (e.g., "Add special characters").
- **CLI Interface**: Simple command-line tool for quick checks.
- **Web Interface**: Optional Flask-based web app for browser-based password checking.
- **Automated Testing**: Unit tests with `pytest` ensure reliability.
- **CI/CD**: GitHub Actions runs tests and linting (`flake8`) on every push/pull request.

## Prerequisites
- Python 3.7+ (tested with 3.9)
- Git
- (Optional) A web browser for the Flask interface
- (Optional) WSL on Windows for development (commands below are WSL-compatible)

## Setup Instructions

1. **Clone the Repository**:
   git clone https://github.com/FatonHaxhiu/Password-Strength-Analyzer.git
   cd Password-Strength-Analyzer

Create and Activate a Virtual Environment:
- python3 -m venv venv
- source venv/bin/activate  # On Windows/WSL, use `venv\Scripts\activate` if needed

Install Dependencies:
- pip install -r requirements.txt
- Usage Instructions

Run the CLI tool:
- python password_strength_checker.py

Example output:
-Password Strength Analyzer

Enter a password: A1b@cD3eF!
- Score: 95/100
- Strength: Strong
- Feedback: Great password!
- Flask Web Interface

Launch the Flask web app to check passwords via a browser:
- python app.py
- Open http://localhost:5000 in your browser.
- Enter a password to receive a strength score and feedback.
- Running Tests

Run unit tests to verify functionality:
- pytest tests/ -v


Contributions are welcome! 
To contribute:

- Fork the repository.
- Create a feature branch (git checkout -b feature/your-feature).
- Commit changes (git commit -m "Add your feature").
- Push to the branch (git push origin feature/your-feature).
- Open a pull request with a clear description

License

This project is licensed under the MIT License. See the LICENSE file for details.


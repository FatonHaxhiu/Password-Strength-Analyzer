# Password Strength Analyzer

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
Copy and paste the following commands to set up the project:

1. **Clone the Repository**:
   git clone https://github.com/FatonHaxhiu/Password-Strength-Analyzer.git
   cd Password-Strength-Analyzer

Create and Activate a Virtual Environment:
python3 -m venv venv
source venv/bin/activate  # On Windows/WSL, use `venv\Scripts\activate` if needed

Install Dependencies:
pip install -r requirements.txt

Usage Instructions

Run the CLI tool:
python password_strength_checker.py

Example output:
Password Strength Analyzer
Enter a password: A1b@cD3eF!
Score: 95/100
Strength: Strong
Feedback: Great password!

MIT License

Copyright (c) 2025 Faton Haxhiu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
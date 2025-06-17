from flask import Flask, render_template, request
from password_strength_checker import check_password_strength


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    """Handle GET and POST requests for password strength checking."""
    if request.method == 'POST':
        password = request.form.get('password')
        result = check_password_strength(password)
        return render_template('result.html', result=result)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
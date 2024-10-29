from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # HTML-код
    html_content = """
    <!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enter Your Name</title>
</head>
<body>
    <h1>Enter Your Name</h1>
    <form action="/" method="POST">
        <input type="text" name="name" placeholder="Name">
        <button type="submit">Submit</button>
    </form>
</body>
</html>


    """
    return html_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
# app.py
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Зберігатиме ім'я користувача
user_name = ""

@app.route('/', methods=['GET', 'POST'])
def index():
    global user_name
    if request.method == 'POST':
        user_name = request.form['name']  # Отримуємо ім'я з форми
        return redirect(url_for('greet_user'))
    return render_template('index.html')

@app.route('/greet')
def greet_user():
    return f"Hello, {user_name}!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')

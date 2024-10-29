from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # HTML-код
    html_content = """
    <html<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Me</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            color: #333;
            text-align: center;
            margin: 0;
            padding: 0;
        }
        h1 {
            color: #4CAF50;
            cursor: pointer;
        }
        p {
            font-size: 1.2em;
        }
        #date {
            margin-top: 20px;
            font-style: italic;
            color: #555;
        }
    </style>
</head>
<body>
    <h1 onclick="changeColor()">My name is Nikita Yakovenko.</h1>
    <p>I am a student of the Kyiv Professional College of Communications.</p>
    <p>I am studying on 121 speciality ‘Software Development’.</p>
    <p id="date"></p>

    <script>
        // Відображення поточної дати
        function showDate() {
            const dateElement = document.getElementById('date');
            const today = new Date();
            const options = { year: 'numeric', month: 'long', day: 'numeric' };
            dateElement.textContent = `Today's date is ${today.toLocaleDateString('en-US', options)}.`;
        }

        // Зміна кольору заголовка при натисканні
        function changeColor() {
            const header = document.querySelector('h1');
            header.style.color = header.style.color === 'blue' ? '#4CAF50' : 'blue';
        }

        // Виклик функції для відображення дати при завантаженні сторінки
        showDate();
    </script>
</body>
</html>

    """
    return html_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
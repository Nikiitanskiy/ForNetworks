from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # HTML-код
    html_content = """
    <html>
        <head>
            <title>About Me</title>
        </head>
        <body>
            <h1>My name is Nikita Yakovenko.</h1>
            <p>I am a student of the Kyiv Professional College of Communications.</p>
            <p>I am studying on 121 speciality ‘Software Development’.</p>
        </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
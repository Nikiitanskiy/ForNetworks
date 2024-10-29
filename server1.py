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
import requests

def get_html_from_server():
    # URL сервера
    url = 'http://127.0.0.1:5000/'

    try:
        # Відправляємо GET-запит на сервер
        response = requests.get(url)

        # Перевіряємо статус-код відповіді
        if response.status_code == 200:
            # Виводимо отриманий HTML-код
            print("Отримано HTML-код:")
            print(response.text)
        else:
            print(f"Помилка: статус-код {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Виникла помилка при підключенні до сервера: {e}")

if __name__ == "__main__":
    get_html_from_server()

import requests

def get_info():
    response = requests.get(url="https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11")

    with open("Info.txt", "w", encoding="utf-8") as f:
        f.write(response.text)

    return response.text


def main():
    print(get_info())


if __name__ == "__main__":
    main()
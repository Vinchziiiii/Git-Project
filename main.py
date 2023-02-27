import requests


def get_info():
    try:
        response = requests.get(url="https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11")
    except Exception as err:
        print(f'Что-то пошло не так: {err}')
    else:
        data = response.json()

    return data


def pars_js(data_list):
    eur = data_list[0]
    usd = data_list[1]

    print(f'''
            {usd.get("ccy")}
             Купівля - {usd.get("buy").split('.')[0]} грн. {(usd.get("buy").split('.')[1])[:2]} коп.
             Продаж - {usd.get("sale").split('.')[0]} грн. {(usd.get("sale").split('.')[1])[:2]} коп.
            {eur.get("ccy")}
             Купівля - {eur.get("buy").split('.')[0]} грн. {(eur.get("buy").split('.')[1])[:2]} коп.
             Продаж - {eur.get("sale").split('.')[0]} грн. {(usd.get("sale").split('.')[1])[:2]} коп.

    ''')




def main():
    inc_data = get_info()
    pars_js(inc_data)


if __name__ == "__main__":
    main()

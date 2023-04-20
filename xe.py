import requests
import re
import datetime
from mongo import insert_log


def get_historic_rates(currency, date):
    sess = requests.session()
    # html_resp = sess.get(f"https://www.xe.com/currencytables/?from=JPY&date=2023-04-18")
    html_resp = sess.get(f"https://www.xe.com/currencytables/?from={currency}&date={date}")
    pattern = 'historicRates\"\:\[(.*?)\]'
    text_data = re.findall(pattern, html_resp.text)
    str_data = text_data[0]
    str_data = str_data.replace('null', 'None')
    dict_data = eval(str_data)

    for log_data in dict_data:
        log_data['time'] = date
        insert_log(log_data)
    # print(dict_data)
    return


if __name__ == "__main__":
    print("go run")
    today = datetime.datetime.today()
    test_time = today - datetime.timedelta(days=1)
    now = test_time.strftime("%Y-%m-%d")
    get_historic_rates('USD', now)

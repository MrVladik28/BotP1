import requests
import time
from pprint import pprint

API_URL: str = 'https://api.telegram.org/bot' # имя метода, доступного в API.
BOT_TOKEN: str = "6277154966:AAGvDhJnNRQZ3KUlgy1luuk1cTqqD7fop2Y" # токен вашего бота
TEXT: str = 'Привет это мои первые слова, я был изготовлен одним тупым человеком и из за этого я тупой'
MAX_COUNTER: int = 100 # это количество итераций цикла, в котором мы получаем апдейты от сервера.

offset: int = -1
counter: int = 0
chat_id: int


while counter < MAX_COUNTER:

    print('attempt =', counter)  #Чтобы видеть в консоли, что код живет

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
    #https://api.telegram.org/bot6277154966:AAGvDhJnNRQZ3KUlgy1luuk1cTqqD7fop2Y/getUpdates?offset=111269856

    if updates['result']:
        pprint(updates["result"])
        pprint(updates["result"][0]["update_id"])
        pprint(updates["result"][1]["update_id"])


        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')


    time.sleep(1)
    counter += 1
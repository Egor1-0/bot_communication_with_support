import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
# Установите соединение с Google Sheets

clients_db = {}

def connect_to_google_sheets():
    scope = "" #здесь должен быть список с сылками 
    creds = ServiceAccountCredentials.from_json_keyfile_name('pachbot.json', scope)
    client = gspread.authorize(creds)
    return client.open('Обращения').sheet1  # Имя вашей таблицы


# Сохранение данных в Google Таблицы
def save_to_google_sheets(user_id, product, issue):
    sheet = connect_to_google_sheets()
    sheet.append_row([user_id, product, issue])\
        


# Функция для сохранения данных в файл
def save_data():
    with open('clients_data.json', 'w') as f:
        json.dump(clients_db, f)



# Функция для загрузки данных из файла
def load_data():
    global clients_db
    try:
        with open('clients_data.json', 'r') as f:
            clients_db = json.load(f)
    except FileNotFoundError:
        clients_db = {}


def load_data_from_google_sheets():
    clients_db = connect_to_google_sheets().get_all_values()
    return clients_db
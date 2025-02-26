class Url:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    COURIER_URL = BASE_URL + '/api/v1/courier'
    LOGIN_URL = BASE_URL + '/api/v1/courier/login'
    ORDERS_URL = BASE_URL + '/api/v1/orders'

class DataForOrder:
    CREATE_ORDER_BODY = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": ["BLACK"]
    }

VALID_CREDS = {
        "login": "kirpit_qa",
        "password": "12345",
        "first_name": "kir_first_name"
    }

PASSWORD_AND_EMPTY_LOGIN = {
    "login": "",
    "password": VALID_CREDS['password']
}

LOGIN_AND_EMPTY_PASSWORD = {
    "login": VALID_CREDS['login'],
    "password": ""
}

LOGIN_ONLY = {
        "login": VALID_CREDS['login']
    }

PASS_ONLY = {
        "password": VALID_CREDS['password']
    }

LOGIN_AND_BAD_PASSWORD = {
    "login": VALID_CREDS['login'],
    "password": VALID_CREDS['first_name']
}

PASSWORD_AND_BAD_LOGIN = {
    "login": VALID_CREDS['first_name'],
    "password": VALID_CREDS['password']
}
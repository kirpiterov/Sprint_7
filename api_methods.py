import allure
import requests
from data import *



class Courier:
    @staticmethod
    def create_courier(payload):
        with allure.step(f'Отправляем POST request создания курьера на ручку: {Url.COURIER_URL}'):
            return requests.post(Url.COURIER_URL, data=payload)

    @staticmethod
    def login_courier(payload):
        with allure.step(f'Отправляем POST request для логина курьера на ручку: {Url.LOGIN_URL}'):
            return requests.post(Url.LOGIN_URL, json = payload)

    @staticmethod
    def get_courier_id(login, password):
        payload = {
            "login": login,
            "password": password
        }
        r = requests.post(Url.LOGIN_URL, json = payload)
        with allure.step(f'Отправляем POST request получения id курьера на ручку: {Url.LOGIN_URL}'):
            return r.json()['id']

    @staticmethod
    def delete_courier(courier_id):
        with allure.step(f'Отправляем DELETE request удаления курьера на ручку: {Url.COURIER_URL}/{courier_id}'):
            return requests.delete(f'{Url.COURIER_URL}/{courier_id}')

class Order:
    def create_order(self, body):
        with allure.step(f'Отправляем POST request создания заказа на ручку: {Url.ORDERS_URL}'):
            return requests.post(Url.ORDERS_URL, json = body)

    def cancel_order(self, track):
        with allure.step(f'Отправляем PUT request отмены заказа на ручку: {Url.ORDERS_URL}/cancel'):
            return requests.put(f'{Url.ORDERS_URL}/cancel', params={'track': track})

    def get_order_list(self, params):
        with allure.step(f'Отправляем GET request получения списка заказов на ручку: {Url.ORDERS_URL}'):
            return requests.get(Url.ORDERS_URL, params = params)

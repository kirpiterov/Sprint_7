import allure
import pytest

from data import *
from api_methods import Courier

class TestCreateCourier:
    @allure.title('Тест успешного создания курьера')
    def test_create_courier__success(self, register_courier):
        assert register_courier

    @allure.title('Тест невозможности создания одинаковых курьеров')
    def test_create_same_couriers__fail_code_409(self, register_courier):
        #сохраняем креды первого созданного курьера
        c1_login = register_courier[0]
        c1_password = register_courier[1]
        c1_firstname = register_courier[2]
        payload = {
            "login": c1_login,
            "password": c1_password,
            "firstName": c1_firstname
        }
        with allure.step(f'Пытаемся создать второго курьера с кредами первого: логин = {c1_login}, пароль = {c1_password}'):
            assert Courier.create_courier(payload).status_code == 409

    @allure.title('Тест обязательности логина и пароля для создания курьера')
    @pytest.mark.parametrize('payload', [LOGIN_ONLY, PASS_ONLY])
    def test_create_courier_only_login_or_password_submitted__fail_code_400(self, payload):
        with allure.step(f'Пытаемся создать курьера с реквизитами: {payload}'):
            assert Courier.create_courier(payload).status_code == 400

    @allure.title('Тест правильного кода ответа')
    def test_create_courier__success_code_201(self, valid_courier_register):
        assert valid_courier_register.status_code == 201

    @allure.title('Тест правильного тела ответа')
    def test_create_courier_responce_body__success(self, valid_courier_register):
        assert valid_courier_register.json() == {'ok': True}

    @allure.title('Тест возврата ошибки при отсутствии обязательного параметра для создания курьера')
    @pytest.mark.parametrize('payload', [PASSWORD_AND_EMPTY_LOGIN, LOGIN_AND_EMPTY_PASSWORD])
    def test_create_courier_responce_required_field_is_empty__fail_code_400(self, payload):
        with allure.step(f'Пытаемся создать курьера с реквизитами: {payload}'):
            assert Courier.create_courier(LOGIN_AND_EMPTY_PASSWORD).status_code == 400
            assert Courier.create_courier(PASSWORD_AND_EMPTY_LOGIN).status_code == 400

    @allure.title('Тест возврата ошибки при попытке создать курьера с уже существующим логином')
    def test_create_courier_with_same_login__fail_code_409(self, register_courier):
        # сохраняем креды первого созданного курьера
        c1_login = register_courier[0]
        payload = {
            "login": c1_login,
            "password": VALID_CREDS['password'],
            "firstName": VALID_CREDS['first_name']
        }
        with allure.step(f'Пытаемся создать курьера с логином:{c1_login}'):
            assert Courier.create_courier(payload).status_code == 409
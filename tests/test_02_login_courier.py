import allure
import pytest

from data import *
from api_methods import Courier


class TestLoginCourier:
    @allure.title('Тест успешной авторизации курьера')
    def test_login_courier__success_code_200(self, register_courier):
        payload = {
            "login": register_courier[0],
            "password": register_courier[1]
        }
        with allure.step(f'Пытаемся авторизовать курьера с логином:{register_courier[0]} паролем: {register_courier[1]}'):
            assert Courier().login_courier(payload).status_code == 200

    @allure.title('Тест необходимости передачи всех обязательных полей для авторизации')
    @pytest.mark.parametrize('payload', [LOGIN_ONLY, PASS_ONLY])
    def test_login_courier_only_login_or_password_submitted__fail(self, valid_courier_register, payload):
        with allure.step(f'Пытаемся авторизовать курьера передачей в теле: {payload}'):
            assert Courier().login_courier(LOGIN_ONLY).status_code == 504
            assert Courier().login_courier(PASS_ONLY).status_code == 400

    @allure.title('Тест возврата ошибки, если для авторизации неправильно указан логин или пароль')
    @pytest.mark.parametrize('payload', [LOGIN_AND_BAD_PASSWORD, PASSWORD_AND_BAD_LOGIN])
    def test_login_courier_with_bad_login_or_pass__fail_code_404(self, valid_courier_register, payload):
        with allure.step(f'Пытаемся авторизовать курьера с неправильными кредами: {payload}'):
            assert Courier().login_courier(payload).status_code == 404

    @allure.title('Тест возврата ошибки авторизации при пустых значениях обязательных полей')
    @pytest.mark.parametrize('payload', [PASSWORD_AND_EMPTY_LOGIN, LOGIN_AND_EMPTY_PASSWORD])
    def test_login_courier_only_login_submitted__fail_code_400(self, valid_courier_register, payload):
        with allure.step(f'Пытаемся авторизовать курьера передачей в теле пустых значений: {payload}'):
            assert Courier().login_courier(PASSWORD_AND_EMPTY_LOGIN).status_code == 400
            assert Courier().login_courier(LOGIN_AND_EMPTY_PASSWORD).status_code == 400

    @allure.title('Тест возврата ошибки при попытке авторизации несуществующим пользователем')
    def test_login_courier_by_not_existing_courier__fail_code_400(self, register_courier_without_delete):
        #сохраняем креды созданного курьера
        login = register_courier_without_delete[0]
        password = register_courier_without_delete[1]
        payload = {
            "login":  login,
            "password": password
        }
        #удаляем созданного курьера
        courier_id = Courier().get_courier_id(login, password)
        Courier().delete_courier(courier_id)
        #используем креды удаленного курьера для попытки авторизации
        assert Courier().login_courier(payload).status_code == 404

    @allure.title('Тест отдачи id сервисом при успешной авторизации курьера')
    def test_login_courier_returns_id_success(self, register_courier):
        payload = {
            "login": register_courier[0],
            "password": register_courier[1]
        }
        with allure.step(f'Проверяем отдачи id сервисом при авторизации курьера (логин: {register_courier[0]} пароль: {register_courier[1]})'):
            assert Courier().login_courier(payload).json()['id']

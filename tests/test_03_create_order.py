import allure
import pytest

from data import *
from api_methods import Courier

class TestCreateOrder:
    @allure.title('Тест возможности указать один из цветов — BLACK или GREY, оба или ни одного цвета')
    @pytest.mark.parametrize('create_order_fixture_param_colors', [["BLACK"], ["GREY"], ["BLACK","GREY"], [""]], indirect=True)
    def test_create_order_with_variable_colors_or_without_colors__success_201(self, create_order_fixture_param_colors):
        with allure.step(f'Пытаемся создать заказ со значением цвета: {create_order_fixture_param_colors}'):
            assert create_order_fixture_param_colors.status_code == 201 and create_order_fixture_param_colors.json()['track']

    @allure.title('Тест проверки наличия track в теле ответа (при успешном создании)')
    def test_create_order_return_track_in_body__success_201(self, create_order_fixture):
        assert create_order_fixture.json()['track'] and create_order_fixture.status_code == 201

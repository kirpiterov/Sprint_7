import allure
from api_methods import Order


class TestGetOrderList:
    @allure.title('Тест получения списка всех заказов (параметры не указываем)')
    def test_get_order_list_has_orders__success_200(self):
        assert (Order().get_order_list(params='').status_code == 200
                and Order().get_order_list(params='').json()['orders'])
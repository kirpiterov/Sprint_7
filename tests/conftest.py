import pytest
import helpers
from data import *
from api_methods import Courier, Order


@pytest.fixture
def register_courier():
    register = helpers.register_new_courier_and_return_login_password()
    print(register)
    yield register
    #удаление курьера по id
    courier_id = Courier().get_courier_id(register[0],register[1])
    Courier().delete_courier(courier_id)

@pytest.fixture
def valid_courier_register():
    payload = VALID_CREDS
    yield Courier().create_courier(payload)
    #удаление курьера по id
    courier_id = Courier().get_courier_id(VALID_CREDS['login'],VALID_CREDS['password'])
    Courier().delete_courier(courier_id)

@pytest.fixture
def register_courier_without_delete():
    register = helpers.register_new_courier_and_return_login_password()
    print(register)
    return register

@pytest.fixture
def create_order_fixture():
    body = DataForOrder.CREATE_ORDER_BODY
    new_order = Order().create_order(body)
    track = new_order.json()['track']
    #print(new_order)
    yield new_order
    #отмена заказа по track
    Order().cancel_order(track)

@pytest.fixture
#ожидается передача в фикстуру параметра param = body (для заказа)
def create_order_fixture_param_colors(request):
    body = DataForOrder.CREATE_ORDER_BODY
    body['color'] = request.param
    new_order = Order().create_order(body)
    track = new_order.json()['track']
    #print(new_order)
    yield new_order
    #отмена заказа по track
    Order().cancel_order(track)



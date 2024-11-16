import random
import allure
import requests
from constants.urls import Url


def create_order_ingredient():
    response = requests.get(Url.INGREDIENT_DATA)
    order = []
    list_of_buns = []
    list_of_fillings = []
    list_of_sauces = []
    list_of_all_ingredients = response.json()["data"]
    for ingredient in list_of_all_ingredients:
        if ingredient["type"] == "bun":
            list_of_buns.append(ingredient["_id"])
        if ingredient["type"] == "main":
            list_of_fillings.append(ingredient["_id"])
        if ingredient["type"] == "sauce":
            list_of_sauces.append(ingredient["_id"])
    order.append(random.choice(list_of_buns))
    order.append(random.choice(list_of_fillings))
    order.append(random.choice(list_of_sauces))
    return order


@allure.step("Создаём заказ через API")
def create_order(token):
    headers = {"Authorization": token}
    ingredients = create_order_ingredient()
    payload = {"ingredients": ingredients}
    response = requests.post(Url.CREATE_ORDER, data=payload, headers=headers)
    return str(response.json()["order"]["number"])

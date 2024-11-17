import allure
import requests
from constants.urls import Url
from helpers.generators import generate_user_data


@allure.step("Создаём пользователя")
def create_user():
    user_data = generate_user_data()
    payload = {
        "email": user_data["email"],
        "password": user_data["password"],
        "name": user_data["name"],
    }
    requests.post(Url.CREATE_USER, data=payload)
    return user_data


@allure.step("Логинимся пользователем")
def user_login(user_data):
    payload = {"email": user_data["email"], "password": user_data["password"]}
    response = requests.post(Url.LOGIN, data=payload)
    response_json = response.json()
    token = response_json.get("accessToken")
    return token


@allure.step("Удаляем пользователя")
def delete_user(token):
    response = requests.delete(Url.DELETE_USER, headers={"Authorization": token})
    if response.json()["success"]:
        with allure.step(f"Пользователь успешно удалён {response.text}"):
            pass
    else:
        with allure.step(
            f"При удалении пользователя что-то пошло не так: {response.text}"
        ):
            pass

import configuration
import data
import requests


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.NEW_Main_User,
                         json=body,
                         headers=data.headers)


def new_token_user():
    response = post_new_user(data.user_body)
    tok = response.json()["authToken"]
    return tok


def post_new_client_kit(kit_body, auth_token):
    telo = data.headers.copy()
    telo["Authorization"] = "Bearer" + str(auth_token)
    return requests.post(configuration.URL_SERVICE + configuration.NEW_Main_Kits,
                         json=kit_body,
                         headers=telo)






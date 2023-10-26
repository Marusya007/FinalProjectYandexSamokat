import configuration
import requests
import data


# Анастасия Маслова, 9-я когорта — Финальный проект. Инженер по тестированию плюс

# запрос на создание заказа
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,  # подставляем полный url
                         json=order_body)  # тут тело


response = post_new_order(data.order_body)

print(response.status_code)
print(response.json())


# сохранение номера трека заказа
def get_order_track():
    track = post_new_order(data.order_body).json()["track"]

    return track


# запрос на получение заказа по треку заказа
def get_order_using_order_track(order_body, track):
    headers = data.order_track.copy()
    headers["track"] = "track" + str(track)
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_USING_ORDER_TRACK + str(track),
                        json=order_body, headers=headers)


response = get_order_using_order_track(data.order_body, track=get_order_track())

print(response.status_code)
print(response.json())

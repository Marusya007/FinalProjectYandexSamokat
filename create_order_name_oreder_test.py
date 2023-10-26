import sender_stand_request
import data


# Анастасия Маслова, 9-я когорта — Финальный проект. Инженер по тестированию плюс
# тест на получение заказа по номеру трека
def test_receiving_order_by_track():
    track = sender_stand_request.get_order_track()
    sender_stand_request.get_order_using_order_track(data.order_body, track)
    act = sender_stand_request.get_order_using_order_track(data.order_body, track).status_code
    exp = 200
    assert act == 200

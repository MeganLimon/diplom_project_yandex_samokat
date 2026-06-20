import sender_stand_request
import data

def get_new_order_track():
    response = sender_stand_request.post_new_order(data.order_body)
    return response.json()["track"]
# Мэган Мазуревская, 43-я когорта - финальный проект. Инженер по тестированию плюс
def test_get_order_by_track_number():
    order_response = sender_stand_request.post_new_order(data.order_body)
    track = order_response.json()["track"]
    response = sender_stand_request.get_order_by_track(track)
    print(response.status_code)
    assert response.status_code == 200 
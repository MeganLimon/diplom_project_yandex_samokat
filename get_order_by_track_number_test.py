import sender_stand_request
import data

# Мэган Мазуревская, 43-я когорта - финальный проект. Инженер по тестированию плюс
# Проверяет, что после создания заказа его можно получить по треку
def test_get_order_by_track_number():
    order_response = sender_stand_request.post_new_order(data.order_body)
    track = order_response.json()["track"]
    response = sender_stand_request.get_order_by_track(track)
   
    assert response.status_code == 200 
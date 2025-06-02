import json
from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    json_str = json.dumps(serializer.data)
    return json_str.encode()


def deserialize_car_object(json_bytes: bytes) -> Car:
    json_str = json_bytes.decode()
    data = json.loads(json_str)
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()

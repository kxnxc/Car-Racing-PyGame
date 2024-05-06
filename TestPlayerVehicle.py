import pytest
import pygame
from model.PlayerVehicle import PlayerVehicle
from model.Vehicle import Vehicle

pygame.init()


@pytest.fixture
def test_image():
    return pygame.Surface((100, 100))


def test_vehicle_creation(test_image):
    vehicle = Vehicle(test_image, 50, 50)
    assert isinstance(vehicle, Vehicle), \
        "Об'єкт має бути екземпляром класу Vehicle"
    assert vehicle.image is not None, \
        "Vehicle повинен мати зображення"
    assert vehicle.rect.center == (50, 50), \
        "Координати центру мають бути (50, 50)"


def test_player_vehicle_creation(test_image):
    player_vehicle = PlayerVehicle(50, 50)
    assert isinstance(player_vehicle, PlayerVehicle), \
        "Об'єкт повинен бути екземпляром класу PlayerVehicle"
    assert player_vehicle.image is not None, \
        "PlayerVehicle повинен мати зображення"
    assert player_vehicle.rect.center == (50, 50), \
        "Координати центру мають бути (50, 50)"

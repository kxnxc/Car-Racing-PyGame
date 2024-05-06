import unittest
import pygame
from model.PlayerVehicle import PlayerVehicle
from model.Vehicle import Vehicle


class TestPlayerVehicle(unittest.TestCase):
    def setUp(self):
        self.test_image = pygame.Surface((100, 100))

    def test_vehicle_creation(self):
        vehicle = Vehicle(self.test_image, 50, 50)
        self.assertIsInstance(vehicle, Vehicle)
        self.assertIsNotNone(vehicle.image)
        self.assertEqual(vehicle.rect.center, (50, 50))

    def test_player_vehicle_creation(self):
        player_vehicle = PlayerVehicle(50, 50)
        self.assertIsInstance(player_vehicle, PlayerVehicle)
        self.assertIsNotNone(player_vehicle.image)
        self.assertEqual(player_vehicle.rect.center, (50, 50))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()

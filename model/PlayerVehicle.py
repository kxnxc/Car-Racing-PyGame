import pygame.image
import model.Vehicle


class PlayerVehicle(model.Vehicle.Vehicle):
    def __init__(self, x, y):
        image = pygame.image.load('images/car.png')
        super().__init__(image, x, y)

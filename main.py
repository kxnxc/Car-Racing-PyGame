import pygame
from constants.MapEdges import MapEdges
from model.PlayerVehicle import PlayerVehicle
from constants.Coordinates import Coordinates


pygame.init()

screen = pygame.display.set_mode(MapEdges.SCREEN_SIZE)
pygame.display.set_caption('Car Racing Game')

road = (100, 0, MapEdges.ROAD_WIDTH, MapEdges.WINDOW_HEIGHT)
left_edge_marker = (95, 0, MapEdges.MARKER_WIDTH, MapEdges.WINDOW_HEIGHT)
right_edge_marker = (395, 0, MapEdges.MARKER_WIDTH, MapEdges.WINDOW_HEIGHT)

lane_marker_move_y = 0

clock = pygame.time.Clock()
fps = 120

gameover = False
speed = 2
score = 0

player_group = pygame.sprite.Group()
vehicle_group = pygame.sprite.Group()

player = PlayerVehicle(Coordinates.PLAYER_X, Coordinates.PLAYER_Y)
player_group.add(player)

image_filenames = ['pickup_truck.png', 'semi_trailer.png', 'taxi.png', 'van.png']
vehicle_images = []

for image_filename in image_filenames:
    image = pygame.image.load('images/' + image_filename)
    vehicle_images.append(image)

crash = pygame.image.load('images/crash.png')
crash_rect = crash.get_rect()

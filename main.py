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



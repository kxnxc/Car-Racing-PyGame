import random
import pygame
from pygame import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_y, K_n
from constants.Colors import Colors
from constants.MapEdges import MapEdges
from model.PlayerVehicle import PlayerVehicle
from constants.Coordinates import Coordinates
from model.Vehicle import Vehicle

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

image_filenames = ['pickup_truck.png',
                   'semi_trailer.png', 'taxi.png', 'van.png']
vehicle_images = []

for image_filename in image_filenames:
    image = pygame.image.load('images/' + image_filename)
    vehicle_images.append(image)

crash = pygame.image.load('images/crash.png')
crash_rect = crash.get_rect()

running = True

while running:

    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:

            if event.key == K_LEFT and player.rect.center[0] \
                    > Coordinates.LEFT_LANE:
                player.rect.x -= 100
            elif event.key == K_RIGHT and player.rect.center[0] \
                    < Coordinates.RIGHT_LANE:
                player.rect.x += 100

            for vehicle in vehicle_group:
                if pygame.sprite.collide_rect(player, vehicle):

                    gameover = True

                    if event.key == K_LEFT:
                        player.rect.left = vehicle.rect.right
                        crash_rect.center = [player.rect.left,
                                             (player.rect.center[1]
                                              + vehicle.rect.center[1]) / 2]
                    elif event.key == K_RIGHT:
                        player.rect.right = vehicle.rect.left
                        crash_rect.center = [player.rect.right,
                                             (player.rect.center[1]
                                              + vehicle.rect.center[1]) / 2]

    screen.fill(Colors.GREEN)

    pygame.draw.rect(screen, Colors.GRAY, road)

    pygame.draw.rect(screen, Colors.YELLOW, left_edge_marker)
    pygame.draw.rect(screen, Colors.YELLOW, right_edge_marker)

    lane_marker_move_y += speed * 2
    if lane_marker_move_y >= MapEdges.MARKER_HEIGHT * 2:
        lane_marker_move_y = 0
    for y in range(MapEdges.MARKER_HEIGHT * -2,
                   MapEdges.WINDOW_HEIGHT, MapEdges.MARKER_HEIGHT * 2):
        pygame.draw.rect(screen, Colors.WHITE,
                         (Coordinates.LEFT_LANE + 45, y + lane_marker_move_y,
                          MapEdges.MARKER_WIDTH, MapEdges.MARKER_HEIGHT))
        pygame.draw.rect(screen, Colors.WHITE,
                         (Coordinates.CENTER_LANE + 45, y + lane_marker_move_y,
                          MapEdges.MARKER_WIDTH, MapEdges.MARKER_HEIGHT))

    player_group.draw(screen)

    if len(vehicle_group) < 2:

        add_vehicle = True
        for vehicle in vehicle_group:
            if vehicle.rect.top < vehicle.rect.height * 1.5:
                add_vehicle = False

        if add_vehicle:
            lane = random.choice(Coordinates.LANES)

            image = random.choice(vehicle_images)
            vehicle = Vehicle(image, lane, MapEdges.WINDOW_HEIGHT / -2)
            vehicle_group.add(vehicle)

    for vehicle in vehicle_group:
        vehicle.rect.y += speed

        if vehicle.rect.top >= MapEdges.WINDOW_HEIGHT:
            vehicle.kill()

            score += 1

            if score > 0 and score % 5 == 0:
                speed += 1

    vehicle_group.draw(screen)

    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    text = font.render('Score: ' + str(score), True, Colors.WHITE)
    text_rect = text.get_rect()
    text_rect.center = (50, 400)
    screen.blit(text, text_rect)

    if pygame.sprite.spritecollide(player, vehicle_group, True):
        gameover = True
        crash_rect.center = [player.rect.center[0], player.rect.top]

    if gameover:
        screen.blit(crash, crash_rect)

        pygame.draw.rect(screen, Colors.RED,
                         (0, 50, MapEdges.WINDOW_WIDTH, 100))

        font = pygame.font.Font(pygame.font.get_default_font(), 16)
        text = font.render('Game over. Play again? (Enter Y or N)',
                           True, Colors.WHITE)
        text_rect = text.get_rect()
        text_rect.center = (MapEdges.WINDOW_WIDTH / 2, 100)
        screen.blit(text, text_rect)

    pygame.display.update()

    while gameover:

        clock.tick(fps)

        for event in pygame.event.get():

            if event.type == QUIT:
                gameover = False
                running = False

            if event.type == KEYDOWN:
                if event.key == K_y:
                    gameover = False
                    speed = 2
                    score = 0
                    vehicle_group.empty()
                    player.rect.center = [Coordinates.PLAYER_X,
                                          Coordinates.PLAYER_Y]
                elif event.key == K_n:
                    gameover = False
                    running = False

pygame.quit()

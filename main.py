import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Spaceship-Game')
clock = pygame.time.Clock()
player = pygame.Surface((50, 50))
player_pos = [350, 700]
playerColor = (255, 0, 255)
player.fill(playerColor)
backgroundcolor = (0, 0, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            print("Move right")
            player_pos[0] += 50
        elif keys[pygame.K_LEFT]:
            print("Move left")
            player_pos[0] -= 50

    screen.fill(backgroundcolor)
    pygame.draw.rect(screen, playerColor,
                     (player_pos[0], player_pos[1], 50, 50))

    print(player_pos)
    pygame.display.update()
    clock.tick(60)

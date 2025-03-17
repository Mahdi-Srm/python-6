

import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("drew rectangle")

color = [(255, 255, 0), (255, 85, 0), (255, 0, 200), (0, 0, 0), (255, 255, 255)]
yellow = (255, 255, 0)
orange = (255, 85, 0)
pink = (255, 0, 200)
black = (0, 0, 0)
white = (255, 255, 255)

bg_color = color[3]
color_index = 4

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                color_index = 0
            elif event.key == pygame.K_2:
                color_index = 1
            elif event.key == pygame.K_3:
                color_index = 2

    screen.fill(bg_color)
    pygame.draw.rect(screen, color[color_index], (350, 250, 100, 100))
    pygame.display.flip()

pygame.quit()
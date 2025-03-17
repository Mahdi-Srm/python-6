import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("drew rectangle")

yellow = (255, 255, 0)
orange = (255, 85, 0)
pink = (255, 0, 200)
black = (0, 0, 0)
white = (255, 255, 255)

bg_color = black
color = white

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                color = yellow
            elif event.key == pygame.K_2:
                color = orange
            elif event.key == pygame.K_3:
                color = pink

    screen.fill(bg_color)
    pygame.draw.rect(screen, color, (350, 250, 100, 100))
    pygame.display.flip()

pygame.quit()
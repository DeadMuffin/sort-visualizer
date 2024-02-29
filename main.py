import pygame
from menu import create_sort_menu

# pygame setup
pygame.init()
FPS = 60
WIDTH = 1080
HEIGHT = 720
running = True
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Menu setup
sort_menu = create_sort_menu(WIDTH, HEIGHT, screen)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(FPS)
    real_fps = clock.get_fps()
    pygame.display.set_caption(f"Sort Visualizer - FPS: {int(real_fps)}")

    pygame.display.flip()
    screen.fill((30, 30, 30))
    sort_menu.mainloop(screen)
pygame.quit()

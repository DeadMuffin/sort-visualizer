import random
import pygame
import sorting

# pygame setup
pygame.init()
WIDTH = 1700
HEIGHT = 1100
RECT_WIDTH = 20
PRINT_DELAY = 0.1
dt = 0
running = True
heightMap = []
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


for x in range(0, WIDTH, RECT_WIDTH):
    heightMap.append(random.randrange(int(HEIGHT/10), HEIGHT))

sorting.show(heightMap, RECT_WIDTH, screen, PRINT_DELAY, [])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        sorting.merge_sort(heightMap, RECT_WIDTH, screen, PRINT_DELAY)
        print(f"correctly sorted:  {sorted(heightMap) == heightMap}")
    dt = clock.tick(60) / 1000
pygame.quit()

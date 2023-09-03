import pygame
from random import randrange
RES = 700
SIZE = 25
x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = (randrange(0, RES, SIZE), randrange(0, RES, SIZE))
dris = {'W': True, 'S': True, 'A': True, 'D': True}
length = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 10

pygame.init()
sc = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()

while True:
    sc.fill(pygame.Color('black'))
    
    [(pygame.draw.rect(sc, pygame.Color('green'), pygame.Rect(i, j, SIZE - 2, SIZE - 2))) for i, j in snake]
    pygame.draw.rect(sc, pygame.Color('red'), pygame.Rect(apple[0], apple[1], SIZE, SIZE))
    
    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[-length:]

    if snake[-1] == apple:
        apple = (randrange(0, RES, SIZE), randrange(0, RES, SIZE))
        length += 1

    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
        break


    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dris['W']:
        dris = {'W': True, 'S': False, 'A': True, 'D': True}
        dx, dy = 0, -1
    if key[pygame.K_s] and dris['S']:
        dx, dy = 0, 1
        dris = {'W': False, 'S': True, 'A': True, 'D': True}
    if key[pygame.K_a] and dris['A']:
        dx, dy = -1, 0
        dris = {'W': True, 'S': True, 'A': True, 'D': False}
    if key[pygame.K_d] and dris['D']:
        dx, dy = 1, 0
        dris = {'W': True, 'S': True, 'A': False, 'D': True}

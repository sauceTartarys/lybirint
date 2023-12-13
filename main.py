import random
import time
import pygame
import gold
import oliver
from Enemy import Enemy
from wall import Wall
pygame.init()

window = pygame.display.set_mode((800,500))
pygame.mixer.init()
pygame.mixer.music.load("jungles.ogg")
pygame.mixer.music.play(-1)

fps = pygame.time.Clock()

fone = pygame.image.load("background3.png")

fone = pygame.transform.scale(fone,(800,500))

wacawaca = oliver.oliver(50,50, 50,50, 1, "hero.png")
cyb = Enemy(200,200, 50,50, 1, "cyborg.png", 100,200,300,300)
golden = gold.gold(600, 200, 100, 100, "treasure.png")
game = True

walls = []
walls.append(Wall(220, 40, 100, 20,(255, 255, 0)))
walls.append(Wall(320, 40, 20, 360,(255, 255, 0)))
walls.append(Wall(330, 484, 100, 20,(250, 250, 0)))
walls.append(Wall(418, 101, 20, 500,(250, 250, 0)))
walls.append(Wall(419, 38, 100, 20,(250, 250, 0)))
walls.append(Wall(222, 0, 20, 50,(250, 250, 0)))


money_sound = pygame.mixer.Sound("money.ogg")

while game:

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            print(x, y)
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()

    wacawaca.muve()
    cyb.muve()

    for wall in walls:
        if wacawaca.hit_box.colliderect((wall.rect)):
            game = False

    if golden.hit_box.colliderect(wacawaca.hit_box):
        money_sound.play()

    window.fill((123,123,123))
    window.blit(fone,(0,0))
    wacawaca.render(window)
    golden.render(window)
    cyb.render(window)
    for wall in walls:
        wall.color = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
        wall.render(window)
    pygame.display.flip()
    fps.tick()
import pygame
import oliver
from Enemy import Enemy

pygame.init()

window = pygame.display.set_mode((800,500))
fps = pygame.time.Clock()

fone = pygame.image.load("background2.png")

fone = pygame.transform.scale(fone,(800,500))

wacawaca = oliver.oliver(50,50, 50,50, 1, "hero.png")
cyb = Enemy(100,100, 50,50, 1, "cyborg.png", 100,200,300,300)

game = True
while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()

    wacawaca.muve()


    window.fill((123,123,123))
    window.blit(fone,(0,0))
    wacawaca.render(window)
    cyb.render(window)
    pygame.display.flip()
    fps.tick()
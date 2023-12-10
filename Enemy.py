import pygame


class Enemy:
    def __init__(self, x, y,w,h, speed, texture, x1, y1, x2, y2):
        self.speed = speed
        self.texture = pygame.image.load(texture)
        self.hit_box = self.texture.get_rect()
        self.hit_box.x = x
        self.hit_box.y = y
        self.texture = pygame.transform.scale(self.texture,(w,h))
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


    def render(self, window):
        window.blit(self.texture,( self.hit_box.x,  self.hit_box.y))

    def muve(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_l]:
            self.hit_box.x += self.speed
        if keys[pygame.K_j]:
            self.hit_box.x -= self.speed
        if keys[pygame.K_i]:
            self.hit_box.y -= self.speed
        if keys[pygame.K_k]:
            self.hit_box.y += self.speed
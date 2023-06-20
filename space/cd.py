import pygame
from pygame.locals import *
from pygame.draw import *

pygame.init()

largura = 1200
altura = 620
tela = pygame.display.set_mode((largura,altura))

class Nave(pygame.sprite.Sprite):
    def init(self):
        pygame.sprite.Sprite.init(self)
        self.image = pygame.image.load('nave.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = largura // 2
        self.rect.bottom = altura - 10
        self.velocidade = 5
        self.escudo = 100  # Valor inicial do escudo de força

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= self.velocidade
        if keys[K_RIGHT]:
            self.rect.x += self.velocidade

    def receber_dano(self, dano):
        self.escudo -= dano
        if self.escudo <= 0:
            def desenhar_escudo(escudo):
    cor_verde = (0, 255, 0)
    cor_vermelha = (255, 0, 0)
    largura_escudo = escudo
    altura_escudo = 10
    pygame.draw.rect(tela, cor_verde, (10, 10, largura_escudo, altura_escudo))
    pygame.draw.rect(tela, cor_vermelha, (10 + largura_escudo, 10, 100 - largura_escudo, altura_escudo))
    nave = Nave()
clock = pygame.time.Clock()

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    nave.update()
    tela.fill((0, 0, 0))
    desenhar_escudo(nave.escudo)
    tela.blit(nave.image, nave.rect)
    pygame.display.flip()

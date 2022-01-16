import time

import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

width = 640
height = 480
x_snake = width/2
y_snake = height/2

tamanho = 20
x_eat=randint(0,620)
y_eat =randint(0,460)

x_controle = 20
y_controle = 0

nivel = 1
pontos = 0
cont = 0

fonte = pygame.font.SysFont('arial',30,True)
image = pygame.image.load('maca.png')
maca = pygame.transform.scale(image, (35,35))

lista_body = []
comprimento = 3

window = pygame.display.set_mode((width,height))
tempo = pygame.time.Clock()

game_over = False

def cresce (lista_body):
    for XeY in lista_body:
        pygame.draw.rect(window, (0,255,0),(XeY[0], XeY[1],20,20))

def start_game():
    global pontos,nivel,comprimento,x_snake,y_snake,lista_body,lista_head,x_eat,y_eat,game_over,cont
    pontos = 0
    cont = 0
    nivel = 1
    comprimento = 3

    x_snake = width / 2
    y_snake = height / 2

    lista_body = []
    lista_head = []

    x_eat = randint(0, 620)
    y_eat = randint(0, 460)

    game_over = False

while True:
    tempo.tick(nivel * 3)
    window.fill((0,0,0))

    mss = f'Nivel: {nivel}'
    txt_formatado = fonte.render(mss,True,(255,255,255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle > 0:
                    pass
                else:
                    x_controle = -20
                    y_controle = 0
            if event.key == K_d:
                if x_controle < 0:
                    pass
                else:
                    x_controle = 20
                    y_controle = 0
            if event.key == K_w:
                if y_controle > 0:
                    pass
                else:
                    y_controle = -20
                    x_controle = 0
            if event.key == K_s:
                if y_controle < 0:
                    pass
                else:
                    y_controle = 20
                    x_controle = 0

    x_snake = x_snake + x_controle
    y_snake = y_snake + y_controle

    snake = pygame.draw.rect(window,(0,255,0),(x_snake,y_snake,tamanho,20))
    eat = window.blit(maca,(x_eat, y_eat))

    '''eat = pygame.draw.rect(window, (255, 255, 0), (x_eat, y_eat, 20, 20))'''

    if snake.colliderect(eat):
        x_eat= randint(0, 625)
        y_eat = randint(0, 465)
        comprimento += 1
        pontos += 1
        cont += 1
        if cont == 3:
            nivel += 1
            cont = 0

    lista_head=[]
    lista_head.append(x_snake)
    lista_head.append(y_snake)

    lista_body.append(lista_head)

    if lista_body.count(lista_head) > 1 or x_snake == 640 or y_snake == 480 or x_snake == 0 or y_snake == 0:
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mss2 = 'Game over! Pressione a tecla SPACE para reiniciar.'
        mss3 = 'Você fez {} ponto(s).'.format(pontos)
        txt_formatado2 = fonte2.render(mss2, True, (0, 0, 0))
        txt_formatado3 = fonte2.render(mss3, True, (0, 0, 0))
        ret_txt = txt_formatado2.get_rect()
        ret_txt3 = txt_formatado3.get_rect()

        game_over = True
        while game_over:
            window.fill((255,0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        start_game()

            ret_txt.center = (width//2, height//2)
            window.blit(txt_formatado2,ret_txt)
            ret_txt3.center = (width // 2, 300)
            window.blit(txt_formatado3, ret_txt3)
            pygame.display.update()

    if x_snake > width:
        x_snake = 0
    if x_snake < 0:
        x_snake = width

    if len(lista_body) > comprimento:
        del lista_body[0]

    cresce(lista_body)

    window.blit(txt_formatado,(510,10))
    pygame.display.update()
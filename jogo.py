import pygame
import time
import random

pygame.init()


#CC
branco = (255, 255, 255)
preto = (0,0,0)
vermelho = (210, 50, 80)
verde = (0,255,0)
azul = (50,153,213)

largura_tela = 600
altura_tela = 400

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("JOGO DA COBRINHA")

clock = pygame.time.Clock()
velocidade_cobrinha = 10

fonte_estilo = pygame.font.SysFont("bahnschrift", 20)
fonte_pontuacao = pygame.font.SysFont("comicsansms", 30)

#vamos exibir o score
def pontuacao(score):
    valor = fonte_pontuacao.render("Pontuação: " + str(score), True, preto)
    tela.blit(valor, [0, 0])

#cobrinha
def cobrinha(tamanho_cobrinha, lista_segmentos):
    for x in lista_segmentos:
        pygame.draw.rect(tela, verde, [x[0], x[1], tamanho_cobrinha, tamanho_cobrinha])

#
def mensagem(msg, cor):
    mesg = fonte_estilo.render(msg, True, cor)
    tela.blit(mesg, [largura_tela / 6, altura_tela / 3])


#
def jogo():
    game_over = False
    fim_jogo = False

    #começar lado esquerdo embaixo tlv
    x1 = largura_tela / 2
    y1 = largura_tela / 2

    #movimento 
    x1_mover = 10
    y1_mover = 0

    #armazenar as coordenadas
    lista_segmentos = []
    comprimento_cobrinha = 1

    #onde a comida vai aparecer
    comida_x = round(random.randrange(0, largura_tela - 10) / 10.0) * 10.0
    comida_y = round(random.randrange(0, altura_tela - 10) / 10.0) * 10.0

    #continuação do jogo
    while not game_over:
        while fim_jogo:
            tela.fill(azul)
            mensagem("VOCÊ PERDEU! PRESSIONE Q PARA SAIR OU C PARA JOGAR NOVAMENTE.")
            pontuacao(comprimento_cobrinha - 1)
            pygame.display.update()
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    game_over = True
                    fim_jogo = False
                #se o usuario pressionar q ele da quit game se nao, continua
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        game_over = True
                        fim_jogo = False
                    if evento.key == pygame.K_c:
                        jogo()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and x1_mover == 0:
                    x1_mover = -10
                    y1_mover = 0
                elif evento.key == pygame.K_RIGHT and x1_mover == 0:
                    x1_mover = 10
                    y1_mover = 0
                elif evento.key == pygame.K_UP and y1_mover == 0:
                    y1_mover = -10
                    x1_mover = 0
                elif evento.key == pygame.K_DOWN and y1_mover == 0:
                    y1_mover = 10
                    x1_mover = 0
        if x1 >= largura_tela or x1 < 0 or y1 >= altura_tela or y1 < 0:
            fim_jogo = True
        x1 += x1_mover
        y1 += y1_mover
        tela.fill(azul)
        pygame.draw.rect(tela, vermelho, [comida_x, comida_y, 10, 10])
        lista_segmentos.append([x1, y1])
        if len(lista_segmentos) > comprimento_cobrinha:
            del lista_segmentos[0]

        for segmento in lista_segmentos[: -1]:
            if segmento == [x1, y1]:
                fim_jogo = True

        cobrinha(10, lista_segmentos)
        pontuacao(comprimento_cobrinha - 1)

        pygame.display.update()
        
        #quando cobrinha = comida, len(cobrinha += 1)
        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, largura_tela - 10) / 10.0) * 10.0
            comida_y = round(random.randrange(0, altura_tela - 10) / 10.0) * 10.0
            comprimento_cobrinha += 1
        
        clock.tick(velocidade_cobrinha)

    pygame.quit()
    quit()

jogo()
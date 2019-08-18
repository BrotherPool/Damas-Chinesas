import pygame

import time
import math
import random
import socket

from funcoes_aux import*
from send_receive_socket_cliente import*
import sys


IP = "127.0.0.1"
PORT = 1234

jogador_atual="GREEN"
my_username = ""



Chat=[]

minhas_pecas = ""
#RED ou GREEN
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)
    


tabuleiro=[[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1,  2, -1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1,  2,  2, -1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1,  2,  2,  2, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1,  0,  2,  2,  2, -1, -1, -1, -1, -1, -1],
           [-1,  0,  0,  0,  0,  2,  0,  0,  0,  0,  0,  0,  0,  0, -1],
           [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
           [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
           [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1, -1],
           [-1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1, -1],
           [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1, -1],
           [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
           [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
           [-1,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0, -1],
           [-1, -1, -1, -1, -1,  1,  1,  0,  1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1,  1,  1,  1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1,  1,  1, -1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1,  1, -1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]

##tabuleiro=[[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
##           [-1, -1, -1, -1, -1, -1, -1,  1, -1, -1, -1, -1, -1, -1, -1],
##           [-1, -1, -1, -1, -1, -1,  1,  1, -1, -1, -1, -1, -1, -1, -1],
##           [-1, -1, -1, -1, -1, -1,  1,  1,  1, -1, -1, -1, -1, -1, -1],
##           [-1, -1, -1, -1, -1,  1,  1,  1,  1, -1, -1, -1, -1, -1, -1],
##           [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1],
##           [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
##           [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
##           [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1, -1],
##           [-1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1, -1],
##           [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1, -1],
##           [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
##           [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
##           [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1],
##           [-1, -1, -1, -1, -1,  2,  2,  2,  2, -1, -1, -1, -1, -1, -1],
##           [-1, -1, -1, -1, -1, -1,  2,  2,  2, -1, -1, -1, -1, -1, -1],
##           [-1, -1, -1, -1, -1, -1,  2,  2, -1, -1, -1, -1, -1, -1, -1],
##           [-1, -1, -1, -1, -1, -1, -1,  2, -1, -1, -1, -1, -1, -1, -1],
##           [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]

tabuleiro_orig=[[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1,  1, -1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1,  1,  1, -1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1,  1,  1,  1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1,  1,  1,  1,  1, -1, -1, -1, -1, -1, -1],
           [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1],
           [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
           [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
           [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1, -1],
           [-1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1, -1],
           [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1, -1],
           [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
           [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
           [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1],
           [-1, -1, -1, -1, -1,  2,  2,  2,  2, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1,  2,  2,  2, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1,  2,  2, -1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1,  2, -1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]






##jogador 2=vermelho
##jogador 1=verde

Circ_Verde = pygame.image.load("Elipse_1.png")
Circ_Verme = pygame.image.load("Elipse_2.png")
Circ_Azul = pygame.image.load("Elipse_3.png")




cinza=128,128,128,255
verde=0,200,0,255
vermelho=200,0,0,255
vermelho_forte=255,0,0,255
azul=0,0,200,255
azul_forte=0,0,255,255

peca_bloqueada=(0,0)

branco=255,255,255,255
Cor_Circ_Verde=(26, 162, 26, 255)
Cor_Circ_Verme=(195, 26, 26, 255)
Cor_Circ_Azul=(65, 122, 162, 255)
fundo = pygame.image.load("tabuleiro.png")

(Tam_X_Elipse,Tam_Y_Elipse)=Circ_Verde.get_rect().size


Plot_x=0
Plot_y=0
aux=0
auy=0
peca_atual=0;













    
    



    


def Att_Tabuleiro(tabuleiro_att,screen):
    cinza=128,128,128,255
    screen.fill(cinza)
    screen.blit(fundo,(0,0))
    jogador_vermelho = pygame.image.load("icon_jogador_vermelho.png")
    jogador_verde = pygame.image.load("icon_jogador_verde.png")
    resize_x_red=216
    resize_x_green=209
    resize_y=200
    jogador_vermelho = pygame.transform.scale(jogador_vermelho, (resize_x_red, resize_y))
    jogador_verde = pygame.transform.scale(jogador_verde, (resize_x_green, resize_y))
    tam_matriz = (len(tabuleiro_att), len(tabuleiro_att[0]))
    
    pygame.draw.rect(screen,vermelho,(((400)-75),800,150,50))
    message_display((400),(825),"Desistir",20,(255,255,255,255))
    pygame.draw.rect(screen,azul,(((600)-75),800,150,50))
    message_display((600),(825),"Passar a vez",20,(255,255,255,255))
    
    font = pygame.font.Font('freesansbold.ttf',30)
    
    if(minhas_pecas=="GREEN"):
        screen.blit(jogador_verde,(100-(resize_x_green/2),900-(resize_y/2)))
##        message_display(100+(resize_x_green/2)+40,900+20,my_username,40,(0,255,0,255))
        txt = font.render(my_username, True, (0,255,0,255))
        screen.blit(txt, (80+(resize_x_green/2), 900))
    elif(minhas_pecas=="RED"):
        screen.blit(jogador_vermelho,(100-(resize_x_red/2),900-(resize_y/2)))
        txt = font.render(my_username, True, (255,0,0,255))
        screen.blit(txt, (100+(resize_x_red/2), 900))
##        message_display(100+(resize_x_red/2)+40,900+20,my_username,40,(255,0,0,255))
    
    
    if(jogador_atual=="GREEN"):
        message_display(100,60,"Jogador atual: ",20,(0,0,0,255))
        screen.blit(Circ_Verde,(180,40))
    elif(jogador_atual=="RED"):
        message_display(100,60,"Jogador atual: ",20,(0,0,0,255))
        screen.blit(Circ_Verme,(180,40))
    i=0
    j=0
    for i in range(0,tam_matriz[0]):
        for j in range(0,tam_matriz[1]):
            if(tabuleiro_att[i][j]==1):
                screen.blit(Circ_Verde,(return_x_e_y_correspondete_tabela(j,i)))
            elif(tabuleiro_att[i][j]==2):
                screen.blit(Circ_Verme,(return_x_e_y_correspondete_tabela(j,i)))
            elif(tabuleiro_att[i][j]==3):
                screen.blit(Circ_Azul,(return_x_e_y_correspondete_tabela(j,i)))
    pygame.display.update(pygame.Rect(0, 0, 800, 800))    
##    pygame.display.update(pygame.Rect(800, 0, 800, 100))
##    pygame.display.update(pygame.Rect(800, 700, 800, 300))
##    pygame.display.update(pygame.Rect(1600, 0, 100, 1000))


                





def criacao_tela_de_vitoria(screen,ganhador):
    mario = pygame.image.load("mario.png")
    luigi = pygame.image.load("luigi.png")
    mario_triste = pygame.image.load("mario_triste.png")
    luigi_triste = pygame.image.load("luigi_triste.png")
    mario = pygame.transform.scale(mario, (344, 600))
    luigi = pygame.transform.scale(luigi, (431, 600))
    mario_triste = pygame.transform.scale(mario_triste, (515, 600))
    luigi_triste = pygame.transform.scale(luigi_triste, (353, 600))
    screen.fill(cinza)
    largura, altura = screen.get_size()
    if(ganhador=="GREEN" and minhas_pecas=="GREEN"):
        texto="Você ganhou"
        screen.blit(luigi,(altura/2-(luigi.get_size()[0]/2),largura/2-(luigi.get_size()[1]/2)-200))
    elif(ganhador=="RED" and minhas_pecas=="RED"):
        texto="Você ganhou"
        screen.blit(mario,(altura/2-(mario.get_size()[0]/2),largura/2-(mario.get_size()[1]/2)-200))
    elif(ganhador=="GREEN" and minhas_pecas=="RED"):
        texto="Você perdeu"
        screen.blit(mario_triste,(altura/2-(mario_triste.get_size()[0]/2),largura/2-(mario_triste.get_size()[1]/2)-200))
    elif(ganhador=="RED" and minhas_pecas=="GREEN"):
        texto="Você perdeu"
        screen.blit(luigi_triste,(altura/2-(luigi_triste.get_size()[0]/2),largura/2-(luigi_triste.get_size()[1]/2)-200))
    
    
    
    pygame.draw.rect(screen,vermelho,(((400)-75),800,150,50))
    message_display((400),(825),"Fechar",20,(255,255,255,255))
    pygame.draw.rect(screen,azul,(((600)-75),800,150,50))
    message_display((600),(825),"Jogar denovo",20,(255,255,255,255))
    message_display(largura/2,altura/2+200,texto,35,(0,0,0,255))
    pygame.display.update()



def tela_de_vitoria(ganhador):
    sair=True
    global Chat,jogador_atual
    largura=1000;
    altura=1000;
    bloqueia=False
    pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Damas Chinesas")
    pygame.display.flip()
    screen = pygame.display.get_surface()
    criacao_tela_de_vitoria(screen,ganhador)
    flag=False
    while sair:
        pygame.display.update()
        for event in pygame.event.get():
            try:
                username,message=receive(client_socket)
                
                if(define_tipo_acao(message)=="RANDOM"):
                    jogador_atual=escolha_aleatoria_jogador()
                    send("PODE_COMECAR_DENOVO "+jogador_atual,client_socket)
                    sair=False
                    print("Aki foi a parte do random: "+jogador_atual)
                    tela_de_jogo()
                elif(define_tipo_acao(message)=="PODE_COMECAR_DENOVO"):
                    sair=False
                    args=message.split()
                    jogador_atual=args[1]
                    print("Aki foi a parte do random: "+jogador_atual)
                    tela_de_jogo()
##                elif(define_tipo_acao(message)=="CONECTADO"):
##                    print("Servidor se conectou comigo")
            except:
                pass
             
                                               
            if event.type==pygame.MOUSEMOTION and bloqueia==False:
                
                mouse=pygame.mouse.get_pos()
                if( (400+75)>mouse[0]>(400-75) and 800+50>mouse[1]>800):
                    pygame.draw.rect(screen,vermelho_forte,(((400)-75),800,150,50))
                    message_display((400),(825),"Fechar",20,(255,255,255,255))
                elif((600+75)>mouse[0]>(600-75) and 800+50>mouse[1]>800):
                    pygame.draw.rect(screen,azul_forte,(((600)-75),800,150,50))
                    message_display((600),(825),"Jogar denovo",20,(255,255,255,255))
                else:
                    pygame.draw.rect(screen,vermelho,(((400)-75),800,150,50))
                    message_display((400),(825),"Fechar",20,(255,255,255,255))
                    pygame.draw.rect(screen,azul,(((600)-75),800,150,50))
                    message_display((600),(825),"Jogar denovo",20,(255,255,255,255))
                
            elif event.type==pygame.MOUSEBUTTONDOWN and bloqueia==False:
                mouse=pygame.mouse.get_pos()
                if event.button==1:
                    if( (400+75)>mouse[0]>(400-75) and 800+50>mouse[1]>800):
                        sair=False
                        pygame.display.quit()
                    elif((600+75)>mouse[0]>(600-75) and 800+50>mouse[1]>800):
                        Chat=[]
                        send("RANDOM",client_socket)
                        bloqueia=True


            
        


    






def func_ganhou(ganhador):
    if(ganhador=="GREEN"):
        zera_matriz(tabuleiro, tabuleiro_orig)
        
        tela_de_vitoria("GREEN")
    elif(ganhador=="RED"):
        zera_matriz(tabuleiro, tabuleiro_orig)
        
        tela_de_vitoria("RED")



def att_chat(update_rect,screen):
    altura=0;
    global Chat
    pygame.draw.rect(screen,(255,255,255,255),[800,100,800,600])
    font = pygame.font.Font('freesansbold.ttf',15)
    for i in Chat:
        txt = font.render(i, True, (0,0,0,255))
        screen.blit(txt, (810, 120+altura-10))
        altura+=30;
    pygame.display.update(update_rect)

def att_mensagem(text,screen):
    font = pygame.font.Font('freesansbold.ttf',15)
    pygame.draw.rect(screen,(255,255,255,255),[800,720,800,200])
    txt = font.render(text, True, (0,0,0,255))
    screen.blit(txt, (810, 740))
    pygame.display.update(pygame.Rect(800, 700, 800, 300))



def criacao_tela_de_jogo():
    screen=pygame.display.get_surface()
    largura=1700;
    altura=1000;
    
    pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Damas Chinesas")
##    pygame.display.flip()
    screen=pygame.display.get_surface()
    Att_Tabuleiro(tabuleiro,screen)
    pygame.draw.rect(screen,(255,255,255,255),[800,100,800,600])
    pygame.draw.rect(screen,(255,255,255,255),[800,720,800,200])


def criacao_tela_de_colocar_nome():
    global jogador_atual,my_username,minhas_pecas
    Conectado=False
    largura=700;
    altura=300;
    nome=''
    font = pygame.font.Font('freesansbold.ttf',25)
    cor_adversario=""
    bloqueio_cor=True
    bloqueio_teclado=False
    pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Tela inicial")
    screen = pygame.display.get_surface()
    screen.fill(cinza)
##    pygame.display.flip()
    screen=pygame.display.get_surface()
    largura_input_box=400
    altura_input_box=50
    y_da_input_box=altura/2-altura_input_box/2
    x_da_input_box=largura/2-largura_input_box/2
    pygame.draw.rect(screen,(255,255,255,255),[x_da_input_box+75,y_da_input_box-100,largura_input_box,altura_input_box])
    pygame.draw.rect(screen,(125,0,0,255),[(largura/2-50)-100,(altura/2+50),100,50])
    pygame.draw.rect(screen,(0,125,0,255),[(largura/2-50)+100,(altura/2+50),100,50])
    message_display(x_da_input_box-20,y_da_input_box-75,"Nome:",50,(0,255,255,255))
    message_display(largura/2,altura/2,"Escolha sua cor:",50,(0,255,255,255))
    sair=False
    while(sair==False):
        pygame.display.update()
        for event in pygame.event.get():
            try:
                username,message=receive(client_socket)
                
                if(define_tipo_acao(message)=="COR_ADVERSARIO"):
                    args=message.split()
                    cor_adversario=args[1]
                    if(minhas_pecas!=""):
                        jogador_atual=escolha_aleatoria_jogador()
                        send("PODE_COMECAR "+jogador_atual,client_socket)
                        sair=True
                        tela_de_jogo()
                   
                elif(define_tipo_acao(message)=="PODE_COMECAR"):
                    sair=True
                    args=message.split()
                    jogador_atual=args[1]
                    tela_de_jogo()
##                elif(define_tipo_acao(message)=="CONECTADO"):
##                    print("Servidor se conectou comigo")
            except:
                pass
            if event.type == pygame.KEYDOWN and bloqueio_teclado==False:
                    
        ##              K_RETURN é o enter, quando aperta imprime a mensagem
                    if event.key == pygame.K_RETURN and nome!="":
                        my_username=nome
                        send(my_username,client_socket)
                        while(Conectado==False):
                            try:
                                message=receive2(client_socket)
                                if(message=="CONECTADO"):
                                    print("CONECTADO COM O SERVER")
                                    message_display(largura/2,altura/2+125,"Aguardando o outro jogador se conectar...",20,(0,0,0,255))
                                    pygame.display.update()
                                    
                                elif(message=="DESCONECT"):
                                    print("NÃO PODE SE CONECTAR")
                                    Conectado=True
                                    sair=True
                                elif(message=="READY2GO."):
                                    Conectado=True
                                    pygame.draw.rect(screen,cinza,[0,(altura/2+50)+50,largura,50])
                                    
                            except:
                                pass
                        bloqueio_teclado=True
                        bloqueio_cor=False
                    elif event.key == pygame.K_BACKSPACE:
                        nome = nome[:-1]
                        txt = font.render(nome, True, (0,0,0,255))
                        pygame.draw.rect(screen,(255,255,255,255),[x_da_input_box+75,y_da_input_box-100,largura_input_box,altura_input_box])
                        screen.blit(txt, (x_da_input_box+75, y_da_input_box-100+15))
                    elif(len(nome)<21):
                        nome += event.unicode
                        txt = font.render(nome, True, (0,0,0,255))
                        pygame.draw.rect(screen,(255,255,255,255),[x_da_input_box+75,y_da_input_box-100,largura_input_box,altura_input_box])
                        screen.blit(txt, (x_da_input_box+75, y_da_input_box-100+15))
            elif event.type==pygame.MOUSEMOTION and bloqueio_cor==False:
                    mouse=pygame.mouse.get_pos()
                    #verde
                    if((largura/2-50)+200>mouse[0]>(largura/2-50)+100 and (altura/2+100)>mouse[1]>(altura/2+50) and cor_adversario!="GREEN"):
                        pygame.draw.rect(screen,(0,255,0,255),[(largura/2-50)+100,(altura/2+50),100,50])
                    #vermelho
                    elif((largura/2-50)>mouse[0]>(largura/2-150) and (altura/2+100)>mouse[1]>(altura/2+50)and cor_adversario!="RED"):
                        pygame.draw.rect(screen,(255,0,0,255),[(largura/2-50)-100,(altura/2+50),100,50])
                    else:
                        pygame.draw.rect(screen,(0,125,0,255),[(largura/2-50)+100,(altura/2+50),100,50])
                        pygame.draw.rect(screen,(125,0,0,255),[(largura/2-50)-100,(altura/2+50),100,50])
            elif event.type==pygame.MOUSEBUTTONDOWN and bloqueio_cor==False:
                mouse=pygame.mouse.get_pos()
                if event.button==1:
                    #verde
                    if( (largura/2-50)+200>mouse[0]>(largura/2-50)+100 and (altura/2+100)>mouse[1]>(altura/2+50) and nome!=''and cor_adversario!="GREEN"):
                        minhas_pecas="GREEN"
                        
                        send("COR_ADVERSARIO GREEN",client_socket)
                        bloqueio_cor=True
                        if(cor_adversario==""):
                            message_display(largura/2,altura/2+125,"Aguardando o outro jogador escolher a cor...",20,(0,0,0,255))
                    #vermelho
                    elif((largura/2-50)>mouse[0]>(largura/2-150) and (altura/2+100)>mouse[1]>(altura/2+50) and nome!=''and cor_adversario!="RED"):
                        minhas_pecas="RED"
 
                        send("COR_ADVERSARIO RED",client_socket)
                        bloqueio_cor=True
                        if(cor_adversario==""):
                            message_display(largura/2,altura/2+125,"Aguardando o outro jogador escolher a cor...",20,(0,0,0,255))
            
    

def tela_de_jogo():
    global jogador_atual
    sair= True
    screen=pygame.display.get_surface()
    flag=False
    
    nome_do_jogador=my_username+": "
    text=''
    font = pygame.font.Font('freesansbold.ttf',15)
    tam_nome_jogador=len(nome_do_jogador)
    altura_texto=0
    update_rect = pygame.Rect(800, 100, 800, 600)
    clock = pygame.time.Clock()
    criacao_tela_de_jogo()
    att_chat(update_rect,screen)
    att_mensagem(text,screen)
    print("Isso já é na tela de jogo: "+jogador_atual)
    
    
    while sair:
        pygame.display.update()
        for event in pygame.event.get():            
            try:
                username,message=receive(client_socket)
                if(define_tipo_acao(message)=="CHAT"):
                    username=username+": "
                    add_Lista_Chat(Chat,username+message[5:])
                    Att_Tabuleiro(tabuleiro,screen)
                    att_chat(update_rect,screen)
                    att_mensagem(text,screen)
                elif(define_tipo_acao(message)=="MOVE"):   
                    args=message.split()
                    troca_cor(tabuleiro,(int(args[1]),int(args[2])),(int(args[3]),int(args[4])))
                    Att_Tabuleiro(tabuleiro,screen)
                    att_chat(update_rect,screen)
                    att_mensagem(text,screen)
                elif(define_tipo_acao(message)=="TROCA_JOGADOR"):
                    jogador_atual=troca_jogador(jogador_atual)
                    Att_Tabuleiro(tabuleiro,screen)
                    att_chat(update_rect,screen)
                    att_mensagem(text,screen)
                elif(define_tipo_acao(message)=="GANHOU"):
                    args=message.split()
                    sair=False
                    zera_matriz(tabuleiro, tabuleiro_orig)
                    tela_de_vitoria(str(args[1]))    
            except:
                pass
            
            if(sair==True):                
                if event.type == pygame.KEYDOWN:
                    
        ##              K_RETURN é o enter, quando aperta imprime a mensagem
                    if event.key == pygame.K_RETURN:
                        add_Lista_Chat(Chat,my_username+": "+text)
                        pygame.draw.rect(screen,(255,255,255,255),[800,100,800,600])
                        send("CHAT "+text,client_socket)
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    elif(len(text)<=60):
                        text += event.unicode
                    Att_Tabuleiro(tabuleiro,screen)
                    att_chat(update_rect,screen)
                    att_mensagem(text,screen)
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    
                    mouse=pygame.mouse.get_pos()
                    if event.button==1:
                        if(screen.get_at(mouse)==(Cor_Circ_Verme)and minhas_pecas=="RED" and jogador_atual=="RED"):
                           if(flag==False):
                               Elimina_o_3_da_matriz(tabuleiro)
                               (aux,auy)=get_index_tabela(mouse[0],mouse[1])
                               peca_atual=(auy,aux)
                               pode_andar(tabuleiro,auy,aux)
                        elif(screen.get_at(mouse)==(Cor_Circ_Verde) and minhas_pecas=="GREEN" and jogador_atual=="GREEN"):
                           if(flag==False):
                               Elimina_o_3_da_matriz(tabuleiro)
                               (aux,auy)=get_index_tabela(mouse[0],mouse[1])
                               peca_atual=(auy,aux)
                               pode_andar(tabuleiro,auy,aux)
                        elif(screen.get_at(mouse)==(Cor_Circ_Azul)):
                           Elimina_o_3_da_matriz(tabuleiro)
                           (aux,auy)=get_index_tabela(mouse[0],mouse[1])
                           peca_destino=(auy,aux)
                           troca_cor(tabuleiro,peca_destino,peca_atual)
                           send("MOVE "+str(peca_destino[0])+" "+str(peca_destino[1])+" "+str(peca_atual[0])+" "+str(peca_atual[1]),client_socket)
                           flag=ainda_pode_andar(tabuleiro,peca_destino,peca_atual)
                           peca_atual=peca_destino
                           if(ganhou(tabuleiro)==1):
                                print("Verde ganhou")
                                send("GANHOU GREEN",client_socket)
                                func_ganhou("GREEN")
                                sair=False
                           elif(ganhou(tabuleiro)==2):
                               print("Vermelho ganhou")
                               send("GANHOU RED",client_socket)
                               func_ganhou("RED")
                               sair=False
                           if(flag==False and sair==True):
                               jogador_atual=troca_jogador(jogador_atual)
                               send("TROCA_JOGADOR",client_socket)                       
                        elif( (400+75)>mouse[0]>(400-75) and 800+50>mouse[1]>800 and minhas_pecas==jogador_atual):
                            ##DESISTIU
                            sair=False
                            zera_matriz(tabuleiro, tabuleiro_orig)
                            jogador_atual=troca_jogador(jogador_atual)
                            
                            send("GANHOU "+jogador_atual,client_socket)
                            func_ganhou(jogador_atual)
                        elif((600+75)>mouse[0]>(600-75) and 800+50>mouse[1]>800 and minhas_pecas==jogador_atual):
                            flag=False
                            Elimina_o_3_da_matriz(tabuleiro)
                            send("TROCA_JOGADOR",client_socket)
                            jogador_atual=troca_jogador(jogador_atual)
                    Att_Tabuleiro(tabuleiro,screen)
                    att_chat(update_rect,screen)
                    att_mensagem(text,screen)
                elif event.type==pygame.MOUSEMOTION:
                    mouse=pygame.mouse.get_pos()
                    if( (400+75)>mouse[0]>(400-75) and 800+50>mouse[1]>800 and minhas_pecas==jogador_atual):
                        pygame.draw.rect(screen,vermelho_forte,(((400)-75),800,150,50))
                        message_display((400),(825),"Desistir",20,(255,255,255,255))
                        pygame.display.update(pygame.Rect((((400)-75),800,150,50)))
                    elif((600+75)>mouse[0]>(600-75) and 800+50>mouse[1]>800 and minhas_pecas==jogador_atual):
                        pygame.draw.rect(screen,azul_forte,(((600)-75),800,150,50))
                        message_display((600),(825),"Passar a vez",20,(255,255,255,255))
                        pygame.display.update((((600)-75),800,150,50))
                    else:
                        pygame.draw.rect(screen,vermelho,(((400)-75),800,150,50))
                        message_display((400),(825),"Desistir",20,(255,255,255,255))
                        pygame.draw.rect(screen,azul,(((600)-75),800,150,50))
                        message_display((600),(825),"Passar a vez",20,(255,255,255,255))
                        pygame.display.update(pygame.Rect((((400)-75),800,150,50)))
                        pygame.display.update((((600)-75),800,150,50))

        clock.tick(60)




def animation_ganhador_sorteio():
    time1=time.time()
    time2=time1
    texto="WIN"
    if(jogador_atual=="GREEN"):
        message_display((300),475,texto,20,(0,0,0,255))
    elif(jogador_atual=="RED"):
        message_display((700),475,texto,20,(0,0,0,255))
    pygame.display.update()
    while(time2-time1<=3):
        time2=time.time()

##def tela_de_escolha_do_primeiro_jogador():
##    
##    altura=600;
##    largura=1000;
##    
##    pygame.display.set_mode((largura, altura))
##    pygame.display.set_caption("Sorteio do Jogador")
##    pygame.display.flip()
##    screen = pygame.display.get_surface()
##    sair=True
##    criacao_tela_de_escolha(screen)
##    flag=False
##    
##    while sair:
##        for event in pygame.event.get():
##            if event.type==pygame.MOUSEBUTTONDOWN:
##                if event.button==1:
##                    mouse=pygame.mouse.get_pos()
##                    if( (largura/2+50)>mouse[0]>(largura/2-50) and 450+50>mouse[1]>450):
##                        escolha_aleatoria_jogador()
##                        animation_ganhador_sorteio()
##                        sair=False
##                if event.button==3:
##                   pass
##            elif event.type==pygame.MOUSEMOTION:
##                mouse=pygame.mouse.get_pos()
##                if( (largura/2+50)>mouse[0]>(largura/2-50) and 450+50>mouse[1]>450):
##                    pygame.draw.rect(screen,azul_forte,(((largura/2)-50),450,100,50))
##                    message_display((largura/2),(475),"Vai",20,(255,255,255,255))
##                else:
##                    pygame.draw.rect(screen,azul,(((largura/2)-50),450,100,50))
##                    message_display((largura/2),(475),"Vai",20,(255,255,255,255))
##                
##
##
##
##            
##        pygame.display.update()
##
##    tela_de_jogo()




def text_objects(text, font,cor):
    textSurface = font.render(text, True, cor)
    return textSurface, textSurface.get_rect()
def message_display(x,y,text,size,cor):
    largeText = pygame.font.Font('freesansbold.ttf',size)
    TextSurf, TextRect = text_objects(text, largeText,cor)
    TextRect.center = (x,y)
    pygame.display.get_surface().blit(TextSurf, TextRect)
    
   
    

def criacao_tela_de_escolha():
    texto="Sorteio do primeiro jogador"
    
    largura, altura = screen.get_size()
    screen.fill(cinza)
    screen.blit(Circ_Verme,(((largura/2)+180),400))
    screen.blit(Circ_Verde,(((largura/2)-220),400))
    pygame.draw.rect(screen,verde,(((largura/2)-250),450,100,50))
    pygame.draw.rect(screen,vermelho,(((largura/2)+150),450,100,50))
    pygame.draw.rect(screen,azul,(((largura/2)-50),450,100,50))
    message_display((largura/2),(475),"Vai",20,(255,255,255,255))
    message_display(largura/2,altura/2,texto,35,(0,0,0,255))

if __name__ == "__main__":
    try:
        pygame.init();
        
        

    except:
        print("O modulo pygame não foi inicializado corretamente")
    pygame.display.init()
    criacao_tela_de_colocar_nome()
    pygame.quit()   
        



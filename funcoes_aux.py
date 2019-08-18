import math
import random

def get_index_vizinhos(num_x,num_y):
    if(num_x%2==0):
        return ((num_x-1,num_y),(num_x-1,num_y+1),(num_x,num_y+1),(num_x+1,num_y+1),(num_x+1,num_y),(num_x,num_y-1))
    else:
        return ((num_x-1,num_y-1),(num_x-1,num_y),(num_x,num_y+1),(num_x+1,num_y),(num_x+1,num_y-1),(num_x,num_y-1))

def intersecao(conjuntoA, conjuntoB):
        inter = (-1,-1)
        for x in conjuntoA:
            for y in conjuntoB:
                if x == y:
                    inter=x
        return inter
    
def pode_andar(tabuleiro,num_x,num_y):
    vizinhos=get_index_vizinhos(num_x,num_y)
    index=0;
    cor=tabuleiro[num_x][num_y]
    
    for i in vizinhos:
        if (tabuleiro[i[0]][i[1]]==0):
            tabuleiro[i[0]][i[1]]=3
        elif((tabuleiro[i[0]][i[1]]==3 or tabuleiro[i[0]][i[1]]==-1)):
            pass
        elif ((tabuleiro[i[0]][i[1]]==1 or tabuleiro[i[0]][i[1]]==2)):
            vizinhos2=get_index_vizinhos(i[0],i[1])
            index=vizinhos.index(i)
            if(tabuleiro[vizinhos2[index][0]][vizinhos2[index][1]]==0):
                tabuleiro[vizinhos2[index][0]][vizinhos2[index][1]]=3
                
def ainda_pode_andar(tabuleiro,peca_destino,peca_pulada):
    vizinhos=get_index_vizinhos(peca_destino[0],peca_destino[1])
    
    vizinhos3=get_index_vizinhos(peca_pulada[0],peca_pulada[1])
    inter=intersecao(vizinhos,vizinhos3)
    index=0;
    pode=False
    cor=tabuleiro[peca_destino[0]][peca_destino[1]]
    for j in vizinhos3:
        if(j==(peca_destino[0],peca_destino[1])):
            return False
    for i in vizinhos:
        if(tabuleiro[i[0]][i[1]]==3 or tabuleiro[i[0]][i[1]]==-1 or tabuleiro[i[0]][i[1]]==0 or i==inter):
            pass
        else:
            vizinhos2=get_index_vizinhos(i[0],i[1])
##            print(vizinhos2)
            index=vizinhos.index(i)
            if(tabuleiro[vizinhos2[index][0]][vizinhos2[index][1]]==0):
                tabuleiro[vizinhos2[index][0]][vizinhos2[index][1]]=3
                pode=True
    return pode

def troca_cor(tabuleiro,peca_destino,peca_anterior):
    cor=tabuleiro[peca_anterior[0]][peca_anterior[1]]
    tabuleiro[peca_destino[0]][peca_destino[1]]=cor
    tabuleiro[peca_anterior[0]][peca_anterior[1]]=0


#3 é igual a cor azul (cor que indica para onde a peça pode ir), ou seja está eliminando o azul do tabuleiro
def Elimina_o_3_da_matriz(tabuleiro):
    tam_matriz = (len(tabuleiro), len(tabuleiro[0]))
    i=0
    j=0
    for i in range(0,tam_matriz[0]):
        for j in range(0,tam_matriz[1]):
            if(tabuleiro[i][j]==3):
                tabuleiro[i][j]=0

#reseta o tabuleiro para o estado inicial
def zera_matriz(tabuleiro, tabuleiro_orig):
    tam_matriz = (len(tabuleiro), len(tabuleiro[0]))
    i=0
    j=0
    for i in range(0,tam_matriz[0]):
        for j in range(0,tam_matriz[1]):
            tabuleiro[i][j]=tabuleiro_orig[i][j]

#pega a posição de onde a bola está em relação a tabela, usando a posição x e y onde o mouse está localizado
#dessa forma, tendo a imagem sido feita sob medida e os espaçamentos de y sendo iguais a 40 e a posição y inicial é igual a 60, ou seja o ponto onde o y é o menor possível e ainda está dentro das bolas
#e os espaçamentos de x sendo iguais a 45 e a posição x inicial é igual a 134(caso a bola esteja em uma coluna par) ou 110(caso a bola esteja em uma coluna impar), ou seja o ponto onde o x é o menor possível e ainda está dentro das bolas      
def get_index_tabela(pos_x,pos_y):
    x=0;y=0;
    pos_y_inicial_da_bola_mais_a_cima=60
    espacamento_altura=40
    pos_x_inicial_da_bola_mais_a_esquerda_pares=134
    pos_x_inicial_da_bola_mais_a_esquerda_impares=110
    espacamento_largura=45
    y=math.ceil((pos_y-pos_y_inicial_da_bola_mais_a_cima)/espacamento_altura)
    if (y%2==0):
        x=math.ceil((pos_x-pos_x_inicial_da_bola_mais_a_esquerda_pares)/espacamento_largura) 
    else:
        x=math.ceil((pos_x-pos_x_inicial_da_bola_mais_a_esquerda_impares)/espacamento_largura)
    if(x<0):
        x=0
    elif(x>14):
        x=14
    if(y<0):
        y=0
    elif(y>18):
        y=18   
    return (x,y)

#retorna o x e o y (necessário para plotar as bolas na tela) correspondente aos indices da tabela
def return_x_e_y_correspondete_tabela(x,y):
    pos_x=0
    pos_y=60+(40*(y-1))
    if (y%2==0):
        pos_x=134+(45*(x-1))
    else:
        pos_x=110+(45*(x-1))
    return pos_x,pos_y


def troca_jogador(jogador_atual):
    
    if(jogador_atual=="RED"):
        return "GREEN"
    elif(jogador_atual=="GREEN"):
        return "RED"

def ganhou(tabuleiro):
    tam_matriz = (len(tabuleiro), len(tabuleiro[0]))
    ganhador=-1;
    count_vermelho=0
    count_verde=0
    for altura in range(1,5):
        for largura in range(5,9):
            if(tabuleiro[altura][largura]==2):
                count_vermelho+=1
    for altura in range(14,18):
        for largura in range(5,9):
            if(tabuleiro[altura][largura]==1):
                count_verde+=1
    if(count_vermelho==10):
        return 2
    elif(count_verde==10):
        return 1
    else:
        return -1

def define_tipo_acao(message):
##  MOVE CHAT
    return message.split()[0]

def add_Lista_Chat(Chat,mensagem):
    Chat.append(mensagem)
    if (len(Chat)>20):
        Chat.pop(0)

def escolha_aleatoria_jogador():
    aux=random.randrange(0,101,1)
    if(aux<50):
        return "GREEN"
    else:
        return "RED"

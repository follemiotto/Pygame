import pygame

#confirmacao de inicializacao
try:
    pygame.init()
except:
    print("falha sistemica de inicializacao")

#cores
branco=(255,255,255)
preto=(0,0,0)
vermelho=(255,0,0)
verde=(0,255,0)
azul=(0,0,255)
amarelo=(230,230,0)
laranja=(255,153,51)
roxo=(134,0,179)
back=(240,240,240)
bola=(153,77,0)

#tamanho da tela
largura=750
altura=700

#tamanho objetos
l_barra=200
a_barra=30
tamanho=30

#angulo da bola
aa=2.5
bb=2.5

#dados e tempo
contagem_tempo=pygame.time.Clock()
background=pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Breakout")

#situacao
quit=True
game_over=False
goal=False
levell=True

#fases
slec=[[25,250,"1"],[175,250,"2"],[325,250,"3"],[475,250,"4"],[625,250,"5"],[25,400,"6"],[175,400,"7"],[325,400,"8"],[475,400,"9"],[625,400,"10"]]

x1=[[0,0,verde],[75,0,verde],[150,0,verde],[225,0,verde],[300,0,verde],[375,0,verde],[450,0,verde],[525,0,verde],[600,0,verde],[675,0,verde],[0,50,verde],[75,50,verde],[150,50,verde],[225,50,verde],[300,50,verde],[375,50,verde],[450,50,verde],[525,50,verde],[600,50,verde],[675,50,verde],[0,100,verde],[75,100,verde],[150,100,verde],[225,100,verde],[300,100,verde],[375,100,verde],[450,100,verde],[525,100,verde],[600,100,verde],[675,100,verde],[0,150,verde],[75,150,verde],[150,150,verde],[225,150,verde],[300,150,verde],[375,150,verde],[450,150,verde],[525,150,verde],[600,150,verde],[675,150,verde],[0,200,verde],[75,200,verde],[150,200,verde],[225,200,verde],[300,200,verde],[375,200,verde],[450,200,verde],[525,200,verde],[600,200,verde],[675,200,verde],[0,250,verde],[75,250,verde],[150,250,verde],[225,250,verde],[300,250,verde],[375,250,verde],[450,250,verde],[525,250,verde],[600,250,verde],[675,250,verde]]

x2=[[0,0,vermelho],[75,0,amarelo],[150,0,amarelo],[225,0,amarelo],[300,0,amarelo],[375,0,amarelo],[450,0,amarelo],[525,0,amarelo],[600,0,amarelo],[675,0,vermelho],[0,50,vermelho],[75,50,amarelo],[150,50,preto],[225,50,amarelo],[300,50,amarelo],[375,50,amarelo],[450,50,amarelo],[525,50,preto],[600,50,amarelo],[675,50,vermelho],[0,100,vermelho],[75,100,amarelo],[150,100,amarelo],[225,100,amarelo],[300,100,preto],[375,100,preto],[450,100,amarelo],[525,100,amarelo],[600,100,amarelo],[675,100,vermelho],[0,150,amarelo],[75,150,vermelho],[150,150,amarelo],[225,150,amarelo],[300,150,amarelo],[375,150,amarelo],[450,150,amarelo],[525,150,amarelo],[600,150,vermelho],[675,150,amarelo],[0,200,amarelo],[75,200,amarelo],[150,200,vermelho],[225,200,amarelo],[300,200,amarelo],[375,200,amarelo],[450,200,amarelo],[525,200,vermelho],[600,200,amarelo],[675,200,amarelo],[0,250,amarelo],[75,250,amarelo],[150,250,amarelo],[225,250,preto],[300,250,preto],[375,250,preto],[450,250,preto],[525,250,amarelo],[600,250,amarelo],[675,250,amarelo]]

x3=[[0,0,amarelo],[75,0,azul],[150,0,amarelo],[225,0,amarelo],[300,0,amarelo],[375,0,amarelo],[450,0,amarelo],[525,0,amarelo],[600,0,azul],[675,0,amarelo],[0,50,amarelo],[75,50,amarelo],[150,50,azul],[225,50,amarelo],[300,50,amarelo],[375,50,amarelo],[450,50,amarelo],[525,50,azul],[600,50,amarelo],[675,50,amarelo],[0,100,amarelo],[75,100,amarelo],[150,100,amarelo],[225,100,azul],[300,100,preto],[375,100,preto],[450,100,azul],[525,100,amarelo],[600,100,amarelo],[675,100,amarelo],[0,150,amarelo],[75,150,amarelo],[150,150,amarelo],[225,150,amarelo],[300,150,azul],[375,150,azul],[450,150,amarelo],[525,150,amarelo],[600,150,amarelo],[675,150,amarelo],[0,200,amarelo],[75,200,amarelo],[150,200,amarelo],[225,200,amarelo],[300,200,azul],[375,200,azul],[450,200,amarelo],[525,200,amarelo],[600,200,amarelo],[675,200,amarelo],[0,250,amarelo],[75,250,amarelo],[150,250,amarelo],[225,250,azul],[300,250,amarelo],[375,250,amarelo],[450,250,azul],[525,250,amarelo],[600,250,amarelo],[675,250,amarelo]]

x4=[[0,0,verde],[75,0,verde],[150,0,verde],[225,0,amarelo],[300,0,amarelo],[375,0,amarelo],[450,0,amarelo],[525,0,verde],[600,0,verde],[675,0,verde],[0,50,verde],[75,50,verde],[150,50,amarelo],[225,50,amarelo],[300,50,azul],[375,50,azul],[450,50,amarelo],[525,50,amarelo],[600,50,verde],[675,50,verde],[0,100,verde],[75,100,amarelo],[150,100,amarelo],[225,100,azul],[300,100,azul],[375,100,azul],[450,100,azul],[525,100,amarelo],[600,100,amarelo],[675,100,verde],[0,150,verde],[75,150,amarelo],[150,150,amarelo],[225,150,azul],[300,150,azul],[375,150,azul],[450,150,azul],[525,150,amarelo],[600,150,amarelo],[675,150,verde],[0,200,verde],[75,200,verde],[150,200,amarelo],[225,200,amarelo],[300,200,azul],[375,200,azul],[450,200,amarelo],[525,200,amarelo],[600,200,verde],[675,200,verde],[0,250,verde],[75,250,verde],[150,250,verde],[225,250,amarelo],[300,250,amarelo],[375,250,amarelo],[450,250,amarelo],[525,250,verde],[600,250,verde],[675,250,verde]]

x5=[[0,0,roxo],[75,0,roxo],[150,0,roxo],[225,0,roxo],[300,0,roxo],[375,0,roxo],[450,0,roxo],[525,0,roxo],[600,0,roxo],[675,0,roxo],[0,50,preto],[75,50,vermelho],[150,50,preto],[225,50,vermelho],[300,50,preto],[375,50,vermelho],[450,50,preto],[525,50,vermelho],[600,50,preto],[675,50,vermelho],[0,100,vermelho],[75,100,amarelo],[150,100,vermelho],[225,100,amarelo],[300,100,vermelho],[375,100,amarelo],[450,100,vermelho],[525,100,amarelo],[600,100,vermelho],[675,100,amarelo],[0,150,amarelo],[75,150,vermelho],[150,150,amarelo],[225,150,vermelho],[300,150,amarelo],[375,150,vermelho],[450,150,amarelo],[525,150,vermelho],[600,150,amarelo],[675,150,vermelho],[0,200,vermelho],[75,200,preto],[150,200,vermelho],[225,200,preto],[300,200,vermelho],[375,200,preto],[450,200,vermelho],[525,200,preto],[600,200,vermelho],[675,200,preto],[0,250,roxo],[75,250,roxo],[150,250,roxo],[225,250,roxo],[300,250,roxo],[375,250,roxo],[450,250,roxo],[525,250,roxo],[600,250,roxo],[675,250,roxo]]

x6=[[0,0,amarelo],[75,0,azul],[150,0,laranja],[225,0,laranja],[300,0,laranja],[375,0,laranja],[450,0,laranja],[525,0,laranja],[600,0,azul],[675,0,amarelo],[0,50,amarelo],[75,50,amarelo],[150,50,laranja],[225,50,laranja],[300,50,laranja],[375,50,laranja],[450,50,laranja],[525,50,laranja],[600,50,amarelo],[675,50,amarelo],[0,100,laranja],[75,100,laranja],[150,100,amarelo],[225,100,laranja],[300,100,laranja],[375,100,laranja],[450,100,laranja],[525,100,amarelo],[600,100,laranja],[675,100,laranja],[0,150,laranja],[75,150,laranja],[150,150,laranja],[225,150,preto],[300,150,amarelo],[375,150,amarelo],[450,150,preto],[525,150,laranja],[600,150,laranja],[675,150,laranja],[0,200,laranja],[75,200,laranja],[150,200,laranja],[225,200,amarelo],[300,200,vermelho],[375,200,vermelho],[450,200,amarelo],[525,200,laranja],[600,200,laranja],[675,200,laranja],[0,250,laranja],[75,250,laranja],[150,250,laranja],[225,250,amarelo],[300,250,amarelo],[375,250,amarelo],[450,250,amarelo],[525,250,laranja],[600,250,laranja],[675,250,laranja]]

x7=[[0,0,verde],[75,0,verde],[150,0,verde],[225,0,roxo],[300,0,roxo],[375,0,roxo],[450,0,roxo],[525,0,verde],[600,0,verde],[675,0,verde],[0,50,azul],[75,50,verde],[150,50,verde],[225,50,roxo],[300,50,azul],[375,50,azul],[450,50,roxo],[525,50,verde],[600,50,verde],[675,50,azul],[0,100,azul],[75,100,roxo],[150,100,verde],[225,100,roxo],[300,100,roxo],[375,100,roxo],[450,100,roxo],[525,100,verde],[600,100,roxo],[675,100,azul],[0,150,roxo],[75,150,verde],[150,150,roxo],[225,150,roxo],[300,150,verde],[375,150,verde],[450,150,roxo],[525,150,roxo],[600,150,verde],[675,150,roxo],[0,200,roxo],[75,200,verde],[150,200,verde],[225,200,roxo],[300,200,verde],[375,200,verde],[450,200,roxo],[525,200,verde],[600,200,verde],[675,200,roxo],[0,250,roxo],[75,250,verde],[150,250,verde],[225,250,verde],[300,250,roxo],[375,250,roxo],[450,250,verde],[525,250,verde],[600,250,verde],[675,250,roxo]]

x8=[[0,0,amarelo],[75,0,amarelo],[150,0,amarelo],[225,0,vermelho],[300,0,vermelho],[375,0,amarelo],[450,0,azul],[525,0,azul],[600,0,azul],[675,0,amarelo],[0,50,preto],[75,50,amarelo],[150,50,vermelho],[225,50,amarelo],[300,50,amarelo],[375,50,azul],[450,50,amarelo],[525,50,amarelo],[600,50,amarelo],[675,50,amarelo],[0,100,amarelo],[75,100,vermelho],[150,100,vermelho],[225,100,amarelo],[300,100,azul],[375,100,azul],[450,100,amarelo],[525,100,amarelo],[600,100,amarelo],[675,100,preto],[0,150,amarelo],[75,150,vermelho],[150,150,vermelho],[225,150,amarelo],[300,150,azul],[375,150,azul],[450,150,amarelo],[525,150,amarelo],[600,150,amarelo],[675,150,preto],[0,200,preto],[75,200,amarelo],[150,200,vermelho],[225,200,amarelo],[300,200,amarelo],[375,200,azul],[450,200,amarelo],[525,200,amarelo],[600,200,amarelo],[675,200,amarelo],[0,250,amarelo],[75,250,amarelo],[150,250,amarelo],[225,250,vermelho],[300,250,vermelho],[375,250,amarelo],[450,250,azul],[525,250,azul],[600,250,azul],[675,250,amarelo]]

x9=[[0,0,verde],[75,0,preto],[150,0,amarelo],[225,0,preto],[300,0,verde],[375,0,verde],[450,0,preto],[525,0,amarelo],[600,0,preto],[675,0,verde],[0,50,azul],[75,50,roxo],[150,50,azul],[225,50,amarelo],[300,50,roxo],[375,50,roxo],[450,50,amarelo],[525,50,azul],[600,50,roxo],[675,50,azul],[0,100,roxo],[75,100,roxo],[150,100,roxo],[225,100,roxo],[300,100,roxo],[375,100,roxo],[450,100,roxo],[525,100,roxo],[600,100,roxo],[675,100,roxo],[0,150,verde],[75,150,roxo],[150,150,amarelo],[225,150,azul],[300,150,roxo],[375,150,roxo],[450,150,azul],[525,150,amarelo],[600,150,roxo],[675,150,verde],[0,200,azul],[75,200,roxo],[150,200,azul],[225,200,amarelo],[300,200,roxo],[375,200,roxo],[450,200,amarelo],[525,200,azul],[600,200,roxo],[675,200,azul],[0,250,roxo],[75,250,roxo],[150,250,roxo],[225,250,roxo],[300,250,roxo],[375,250,roxo],[450,250,roxo],[525,250,roxo],[600,250,roxo],[675,250,roxo]]

x10=[[0,0,vermelho],[75,0,preto],[150,0,roxo],[225,0,verde],[300,0,azul],[375,0,azul],[450,0,verde],[525,0,roxo],[600,0,preto],[675,0,vermelho],[0,50,vermelho],[75,50,amarelo],[150,50,azul],[225,50,azul],[300,50,laranja],[375,50,laranja],[450,50,azul],[525,50,azul],[600,50,amarelo],[675,50,vermelho],[0,100,vermelho],[75,100,amarelo],[150,100,roxo],[225,100,vermelho],[300,100,verde],[375,100,verde],[450,100,vermelho],[525,100,roxo],[600,100,amarelo],[675,100,vermelho],[0,150,vermelho],[75,150,amarelo],[150,150,verde],[225,150,azul],[300,150,verde],[375,150,verde],[450,150,azul],[525,150,verde],[600,150,amarelo],[675,150,vermelho],[0,200,vermelho],[75,200,preto],[150,200,azul],[225,200,roxo],[300,200,laranja],[375,200,laranja],[450,200,roxo],[525,200,azul],[600,200,preto],[675,200,vermelho],[0,250,vermelho],[75,250,amarelo],[150,250,roxo],[225,250,azul],[300,250,vermelho],[375,250,vermelho],[450,250,azul],[525,250,roxo],[600,250,amarelo],[675,250,vermelho]]

#todo texto
def texto(msg,color,gran,x,y):
    font=pygame.font.SysFont(None,gran)
    txt1=font.render(msg,True,color)
    background.blit(txt1,[x,y])

#recomeco de jogo
def re():
    quit=True
    game_over=False
    goal=False
    levell=True
    pos_x=275
    pos_y=670
    vel=0
    ball_x=360
    ball_y=640
    X=75
    Y=50
    aa=2.5
    bb=2.5
    an_x=aa
    an_y=-bb
    return quit,game_over,goal,pos_x,pos_y,vel,ball_x,ball_y,an_x,an_y,X,Y,aa,bb,levell

#menu de selecao
def select_level():

    quit,game_over,goal,pos_x,pos_y,vel,ball_x,ball_y,an_x,an_y,X,Y,aa,bb,levell=re()
    qw=False

    while levell:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit=False
                levell=False

            #escolha de nivel
            if event.type==pygame.MOUSEBUTTONDOWN:
                x_mouse=pygame.mouse.get_pos()[0]
                y_mouse=pygame.mouse.get_pos()[1]
                if 25<=x_mouse<=125 and 250<=y_mouse<=350:
                    qw=game(list(x1),0)
                elif 175<=x_mouse<=275 and 250<=y_mouse<=350:
                    qw=game(list(x2),8)
                elif 325<=x_mouse<=425 and 250<=y_mouse<=350:
                    qw=game(list(x3),2)
                elif 475<=x_mouse<=575 and 250<=y_mouse<=350:
                    qw=game(list(x4),0)
                elif 625<=x_mouse<=725 and 250<=y_mouse<=350:
                    qw=game(list(x5),10)
                elif 25<=x_mouse<=125 and 400<=y_mouse<=500:
                    qw=game(list(x6),2)
                elif 175<=x_mouse<=275 and 400<=y_mouse<=500:
                    qw=game(list(x7),0)
                elif 325<=x_mouse<=425 and 400<=y_mouse<=500:
                    qw=game(list(x8),4)
                elif 475<=x_mouse<=575 and 400<=y_mouse<=500:
                    qw=game(list(x9),4)
                elif 625<=x_mouse<=725 and 400<=y_mouse<=500:
                    qw=game(list(x10),4)
        if qw:
            break
        if levell:
            #informacao
            background.fill(branco)
            texto("selecao de fase",preto,100,110,50)
            for i in slec:
                pygame.draw.rect(background,preto,[i[0],i[1],100,100])
                texto(i[2],branco,100,i[0]+10,i[1]+20)
            pygame.display.update()

#in game
def game(nivel,x):

    #gerar situacao blocos
    k=[]
    for i in nivel:
        k.append(list(i))
    quit,game_over,goal,pos_x,pos_y,vel,ball_x,ball_y,an_x,an_y,X,Y,aa,bb,levell=re()

    while quit:

        #tela de fim de jogo
        while game_over:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    quit=False
                    game_over=False
                    levell=False
                    return True

                if event.type==pygame.MOUSEBUTTONDOWN:
                    x_mouse=pygame.mouse.get_pos()[0]
                    y_mouse=pygame.mouse.get_pos()[1]
                    #repetir
                    if 275<=x_mouse<=495 and 270<=y_mouse<=370:
                        quit,game_over,goal,pos_x,pos_y,vel,ball_x,ball_y,an_x,an_y,X,Y,aa,bb,levell=re()
                        k=[]
                        for i in nivel:
                            k.append(list(i))

                    #voltar
                    elif 275<=x_mouse<=495 and 395<=y_mouse<=495:
                        quit=False
                        game_over=False

            #informacao
            background.fill(branco)
            texto("DERROTA",vermelho,150,120,20)
            pygame.draw.rect(background,preto,[275,270,220,100])
            pygame.draw.rect(background,preto,[275,395,220,100])
            texto("Repetir",branco,80,285,295)
            texto("Voltar",branco,80,295,420)
            pygame.display.update()

        #tela de vitoria
        while goal:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    quit=False
                    goal=False
                    levell=False
                    return True

                if event.type==pygame.MOUSEBUTTONDOWN:
                    x_mouse=pygame.mouse.get_pos()[0]
                    y_mouse=pygame.mouse.get_pos()[1]
                    #repetir
                    if 275<=x_mouse<=495 and 270<=y_mouse<=370:
                        quit,game_over,goal,pos_x,pos_y,vel,ball_x,ball_y,an_x,an_y,X,Y,aa,bb,levell=re()
                        k=[]
                        for i in nivel:
                            k.append(list(i))

                    #voltar
                    elif 275<=x_mouse<=495 and 395<=y_mouse<=495:
                        quit=False
                        game_over=False

            #informacao
            background.fill(branco)
            texto("VITORIA",vermelho,150,120,20)
            pygame.draw.rect(background,preto,[275,270,220,100])
            pygame.draw.rect(background,preto,[275,395,220,100])
            texto("Repetir",branco,80,285,295)
            texto("Voltar",branco,80,295,420)
            pygame.display.update()

        #comandos in game
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit=False
                return True

            #movimentacao da barra
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    vel=-3

                if event.key==pygame.K_RIGHT:
                    vel=3

        if quit:

            #parada da barra
            background.fill(back)
            if pos_x>0 and pos_x<550:
                pos_x+=vel
            else:
                vel=0
                if pos_x<=0:
                    pos_x=1
                elif pos_x>=550:
                    pos_x=549

            #aparicao visual
            pygame.draw.rect(background,preto,[pos_x,pos_y,l_barra,a_barra])
            pygame.draw.rect(background,bola,[ball_x,ball_y,tamanho,tamanho])
            for i in k:
                pygame.draw.rect(background,i[2],[i[0],i[1],X,Y])

            #colisao bordas da tela e barra com a bola
            if vel!=0 or ball_x!=360 or ball_y!=640:
                ball_x+=an_x
                ball_y+=an_y
                if ball_x>=720:
                    an_x=-aa
                if ball_x<=0:
                    an_x=aa
                if ball_y<=0:
                    an_y=bb
                if ball_y>=640:

                    #colisao com a barra, alteracao de angulo
                    if pos_x<=ball_x<=pos_x+200 or pos_x<=ball_x+30<=pos_x+200:
                        if pos_x-30<=ball_x<pos_x-20:
                            aa=7.5
                            bb=2
                            an_x=-aa
                            ball_x=(ball_x//7.5)*7.5
                        elif pos_x-20<=ball_x<pos_x-10:
                            aa=5
                            bb=2
                            an_x=-aa
                            ball_x=(ball_x//5)*5
                        elif pos_x-10<=ball_x<pos_x+15:
                            aa=3
                            bb=2
                            an_x=-aa
                            ball_x=(ball_x//3)*3
                        elif pos_x+15<=ball_x<pos_x+55:
                            aa=2.5
                            bb=2.5
                            an_x=-aa
                            ball_x=(ball_x//2.5)*2.5
                        elif pos_x+55<=ball_x<pos_x+85:
                            aa=2.5
                            bb=5
                            an_x=-aa
                            ball_x=(ball_x//2.5)*2.5
                        elif pos_x+85<=ball_x<=pos_x+115:
                            aa=2.5
                            bb=5
                            an_x=aa
                            ball_x=(ball_x//2.5)*2.5
                        elif pos_x+115<ball_x<=pos_x+155:
                            aa=2.5
                            bb=2.5
                            an_x=aa
                            ball_x=(ball_x//2.5)*2.5
                        elif pos_x+155<ball_x<=pos_x+180:
                            aa=3
                            bb=2
                            an_x=aa
                            ball_x=(ball_x//3)*3
                        elif pos_x+180<ball_x<=pos_x+190:
                            aa=5
                            bb=2
                            an_x=aa
                            ball_x=(ball_x//5)*5
                        elif pos_x+190<ball_x<=pos_x+200:
                            aa=7.5
                            bb=2
                            an_x=aa
                            ball_x=(ball_x//7.5)*7.5
                        an_y=-bb
                    else:
                        game_over=True

            #colisao blocos
            for i in k:
                if an_x<0:
                    if an_y<0:
                        if ball_x==i[0]+X:
                            if i[1]<ball_y<i[1]+Y or i[1]<ball_y+tamanho<i[1]+Y:
                                an_x=aa
                                if i[2]==verde:
                                    k.remove(i)
                                elif i[2]==amarelo:
                                    i[2]=verde
                                elif i[2]==laranja:
                                    i[2]=amarelo
                                elif i[2]==vermelho:
                                    i[2]=laranja
                                elif i[2]==roxo:
                                    i[2]=vermelho
                                elif i[2]==azul:
                                    i[2]=roxo
                        elif ball_y==i[1]+Y:
                            if i[0]<=ball_x<=i[0]+X or i[0]<=ball_x+tamanho<=i[0]+X:
                                an_y=bb
                                if i[2]==verde:
                                    k.remove(i)
                                elif i[2]==amarelo:
                                    i[2]=verde
                                elif i[2]==laranja:
                                    i[2]=amarelo
                                elif i[2]==vermelho:
                                    i[2]=laranja
                                elif i[2]==roxo:
                                    i[2]=vermelho
                                elif i[2]==azul:
                                    i[2]=roxo
                    elif an_y>0:
                        if ball_x==i[0]+X:
                            if i[1]<ball_y<i[1]+Y or i[1]<ball_y+tamanho<i[1]+Y:
                                an_x=aa
                                if i[2]==verde:
                                    k.remove(i)
                                elif i[2]==amarelo:
                                    i[2]=verde
                                elif i[2]==laranja:
                                    i[2]=amarelo
                                elif i[2]==vermelho:
                                    i[2]=laranja
                                elif i[2]==roxo:
                                    i[2]=vermelho
                                elif i[2]==azul:
                                    i[2]=roxo
                        elif ball_y+tamanho==i[1]:
                            if i[0]<=ball_x<=i[0]+X or i[0]<=ball_x+tamanho<=i[0]+X:
                                an_y=-bb
                                if i[2]==verde:
                                    k.remove(i)
                                elif i[2]==amarelo:
                                    i[2]=verde
                                elif i[2]==laranja:
                                    i[2]=amarelo
                                elif i[2]==vermelho:
                                    i[2]=laranja
                                elif i[2]==roxo:
                                    i[2]=vermelho
                                elif i[2]==azul:
                                    i[2]=roxo
                elif an_x>0:
                    if an_y<0:
                        if ball_x+tamanho==i[0]:
                            if i[1]<ball_y<i[1]+Y or i[1]<ball_y+tamanho<i[1]+Y:
                                an_x=-aa
                                if i[2]==verde:
                                    k.remove(i)
                                elif i[2]==amarelo:
                                    i[2]=verde
                                elif i[2]==laranja:
                                    i[2]=amarelo
                                elif i[2]==vermelho:
                                    i[2]=laranja
                                elif i[2]==roxo:
                                    i[2]=vermelho
                                elif i[2]==azul:
                                    i[2]=roxo
                        if ball_y==i[1]+Y:
                            if i[0]<=ball_x<=i[0]+X or i[0]<=ball_x+tamanho<=i[0]+X:
                                an_y=bb
                                if i[2]==verde:
                                    k.remove(i)
                                elif i[2]==amarelo:
                                    i[2]=verde
                                elif i[2]==laranja:
                                    i[2]=amarelo
                                elif i[2]==vermelho:
                                    i[2]=laranja
                                elif i[2]==roxo:
                                    i[2]=vermelho
                                elif i[2]==azul:
                                    i[2]=roxo
                    elif an_y>0:
                        if ball_x+tamanho==i[0]:
                            if i[1]<ball_y<i[1]+Y or i[1]<ball_y+tamanho<i[1]+Y:
                                an_x=-aa
                                if i[2]==verde:
                                    k.remove(i)
                                elif i[2]==amarelo:
                                    i[2]=verde
                                elif i[2]==laranja:
                                    i[2]=amarelo
                                elif i[2]==vermelho:
                                    i[2]=laranja
                                elif i[2]==roxo:
                                    i[2]=vermelho
                                elif i[2]==azul:
                                    i[2]=roxo
                        if ball_y+tamanho==i[1]:
                            if i[0]<=ball_x<=i[0]+X or i[0]<=ball_x+tamanho<=i[0]+X:
                                an_y=-bb
                                if i[2]==verde:
                                    k.remove(i)
                                elif i[2]==amarelo:
                                    i[2]=verde
                                elif i[2]==laranja:
                                    i[2]=amarelo
                                elif i[2]==vermelho:
                                    i[2]=laranja
                                elif i[2]==roxo:
                                    i[2]=vermelho
                                elif i[2]==azul:
                                    i[2]=roxo

            #definir vitoria
            if len(k)==x:
                goal=True

            pygame.display.update()
            contagem_tempo.tick(60)

#menu inicial
def menu():
    main_menu=True
    while main_menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit=False
                main_menu=False

            if event.type==pygame.MOUSEBUTTONDOWN:
                    select_level()
                    main_menu=False

        if main_menu:
            background.fill(branco)
            texto("BREAKOUT",preto,150,90,275)
            pygame.display.update()

#chamada
menu()

pygame.quit()

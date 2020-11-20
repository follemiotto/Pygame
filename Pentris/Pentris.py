import pygame
import random

try:
    pygame.font.init()
except:
    print("falha sistemica de inicializacao")

#globais
screen_width = 800
screen_height = 800
play_width = 360
play_height = 720
top_left_x = (screen_width - play_width) // 2
top_left_y = screen_height - play_height
rows = 24
columns = 12

#pentominos

B = [['.....',
      '..0..',
      '..00.',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.00..',
      '.....'],
     ['.....',
      '.00..',
      '.00..',
      '..0..',
      '.....'],
     ['.....',
      '..00.',
      '.000.',
      '.....',
      '.....']]

D = [['.....',
      '..0..',
      '.00..',
      '.00..',
      '.....'],
     ['.....',
      '.00..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..00.',
      '.....']]

F = [['.....',
      '..00.',
      '.00..',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '.....',
      '..0..',
      '..00.',
      '.00..'],
     ['.....',
      '.0...',
      '.000.',
      '..0..',
      '.....']]

E = [['.....',
      '.00..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '...0.',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '..0..',
      '.00..',
      '..00.'],
     ['.....',
      '..0..',
      '.000.',
      '.0...',
      '.....']]

S = [['.....',
      '..00.',
      '..0..',
      '.00..',
      '.....'],
     ['.....',
      '.0...',
      '.000.',
      '...0.',
      '.....']]

Z = [['.....',
      '.00..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '...0.',
      '.000.',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '..0..'],
     ['.....',
      '00000',
      '.....',
      '.....',
      '.....']]

X = [['.....',
      '..0..',
      '.000.',
      '..0..',
      '.....']]

J = [['.....',
      '.0...',
      '.0000',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '..0..'],
     ['.....',
      '.....',
      '0000.',
      '...0.',
      '.....'],
     ['..0..',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '0000.',
      '.....',
      '.....'],
     ['..0..',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.0000',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '..0..']]

T = [['.....',
      '.000.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '...0.',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.000.',
      '.....'],
     ['.....',
      '.0...',
      '.000.',
      '.0...',
      '.....']]

U = [['.....',
      '.0.0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0.0.',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '.00..',
      '.....']]

V = [['.....',
      '.0...',
      '.0...',
      '.000.',
      '.....'],
     ['.....',
      '.000.',
      '.0...',
      '.0...',
      '.....'],
     ['.....',
      '.000.',
      '...0.',
      '...0.',
      '.....'],
     ['.....',
      '...0.',
      '...0.',
      '.000.',
      '.....']]

W = [['.....',
      '.0...',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..00.',
      '.00..',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..00.',
      '...0.',
      '.....'],
     ['.....',
      '...0.',
      '..00.',
      '.00..',
      '.....']]

N = [['.....',
      '...0.',
      '..00.',
      '..0..',
      '..0..'],
     ['.....',
      '.....',
      '000..',
      '..00.',
      '.....'],
     ['..0..',
      '..0..',
      '.00..',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..000',
      '.....',
      '.....']]

M = [['.....',
      '.0...',
      '.00..',
      '..0..',
      '..0..'],
     ['.....',
      '..00.',
      '000..',
      '.....',
      '.....'],
     ['..0..',
      '..0..',
      '..00.',
      '...0.',
      '.....'],
     ['.....',
      '.....',
      '..000',
      '.00..',
      '.....']]

Y = [['.....',
      '..0..',
      '.00..',
      '..0..',
      '..0..'],
     ['.....',
      '..0..',
      '0000.',
      '.....',
      '.....'],
     ['..0..',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.0000',
      '..0..',
      '.....']]

A = [['.....',
      '..0..',
      '..00.',
      '..0..',
      '..0..'],
     ['.....',
      '.....',
      '0000.',
      '..0..',
      '.....'],
     ['..0..',
      '..0..',
      '.00..',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.0000',
      '.....',
      '.....']]

#tetrominos

l = [['.....',
      '.....',
      '.00..',
      '..0..',
      '..0..'],
     ['.....',
      '..0..',
      '000..',
      '.....',
      '.....'],
     ['..0..',
      '..0..',
      '..00.',
      '.....',
      '.....'],
     ['.....',
      '.....',
      '..000',
      '..0..',
      '.....']]

j = [['.....',
      '.....',
      '..00.',
      '..0..',
      '..0..'],
     ['.....',
      '.....',
      '000..',
      '..0..',
      '.....'],
     ['..0..',
      '..0..',
      '.00..',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..000',
      '.....',
      '.....']]

t = [['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.000.',
      '.....',
      '.....']]

i = [['.....',
      '..0..',
      '..0..',
      '..0..',
      '..0..'],
     ['.....',
      '.....',
      '0000.',
      '.....',
      '.....']]

s = [['.....',
      '..00.',
      '.00..',
      '.....',
      '.....'],
     ['.....',
      '.0...',
      '.00..',
      '..0..',
      '.....']]

z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

o = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

#triminos

v = [['.....',
      '..0..',
      '..00.',
      '.....',
      '.....'],
     ['.....',
      '.....',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.00..',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.....',
      '.....']]

ii = [['.....',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.....',
      '.....']]

#bimino

II = [['.....',
      '.....',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.00..',
      '.....',
      '.....']]

#unimino

O = [['.....',
      '.....',
      '..0..',
      '.....',
      '.....']]


shapes = [B, D, F, E, S, Z, I, X, J, L, T, U, V, W, N, M, Y, A, l ,j, t, i, s, z, o, v, ii, II, O]
shape_colors = [(140, 255, 45), (255, 45, 109), (255, 165, 45), (59, 170, 255), (252, 23, 224), (208, 255, 23), (255, 23, 40), (175, 35, 252), (97, 49, 252), (255, 215, 23), (23, 253, 23), (0, 147, 137), (1, 44, 161), (58, 1, 164), (97, 214, 0), (214, 0, 65), (130, 0, 158), (209, 235, 0), (23, 235, 235), (102, 204, 0), (255, 51, 153), (255, 51, 51), (160, 160, 160), (150, 0, 0), (150, 150, 0), (153, 0, 76), (0, 102, 102), (255, 178, 102), (250, 250, 250)]


class Piece(object):
    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0


#seta as cores no grid baseado nos minos parados
def make_grid(locked_positions={}):
    grid = [[(0,0,0) for x in range(columns)] for x in range(rows)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j,i) in locked_positions:
                c = locked_positions[(j,i)]
                grid[i][j] = c
    return grid

#gira o mino
def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)

    return positions

#testa se o mino esta tentando se mover para onde nao devia
def valid_space(shape, grid):
    accepted_positions = [[(j, i) for j in range(columns) if grid[i][j] == (0,0,0)] for i in range(rows)]
    accepted_positions = [j for sub in accepted_positions for j in sub]
    formatted = convert_shape_format(shape)

    for pos in formatted:
        if pos not in accepted_positions:
            if pos[1] > -1:
                return False

    return True

#testa a derrota
def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False

#seleciona proximo mino
def get_shape():
    global shapes, shape_colors

    return Piece(5, 0, random.choice(shapes))

#desenha texto no centro da tela
def draw_text_middle(text, size, color, surface):
    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, 1, color)
    surface.blit(label, (top_left_x + play_width/2 - (label.get_width() / 2), top_left_y + play_height/2 - label.get_height()/2))

#desenha as linhas do grid de jogo
def draw_lines(surface, row, col):
    sx = top_left_x
    sy = top_left_y
    for i in range(row):
        pygame.draw.line(surface, (60,60,60), (sx, sy+ i*30), (sx + play_width, sy + i * 30))  # horizontal lines
    for j in range(col):
        pygame.draw.line(surface, (60,60,60), (sx + j * 30, sy), (sx + j * 30, sy + play_height))  # vertical lines

#ve se uma linha foi completada e coloca as outras para baixo
def clear_rows(grid, locked):
    inc = 0
    aux = 0
    ind = 0
    for i in range(len(grid)-1,-1,-1):
        row = grid[i]
        if (0, 0, 0) not in row:
            inc += 1
            ind = i
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue
        else:
            locked=move_rows(grid, locked, ind, inc-aux)
            aux=inc

    return inc

def move_rows(grid, locked, ind, inc):
    for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
        x, y = key
        if y < ind:
            newKey = (x, y + inc)
            locked[newKey] = locked.pop(key)
    return locked

# def clear_rows(grid, locked):
#     inc = 0
#     for i in range(len(grid)-1,-1,-1):
#         row = grid[i]
#         if (0, 0, 0) not in row:
#             inc += 1
#             ind = i
#             for j in range(len(row)):
#                 try:
#                     del locked[(j, i)]
#                 except:
#                     continue
#     if inc > 0:
#         for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
#             x, y = key
#             if y < ind:
#                 newKey = (x, y + inc)
#                 locked[newKey] = locked.pop(key)
#     return inc

#desenha o mino posto em 'seguinte'
def draw_next_shape(shape, surface):
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Seguinte', 1, (255,255,255))

    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, shape.color, (sx + j*30, sy + i*30, 30, 30), 0)

    surface.blit(label, (sx + 10, sy- 30))

#desenha em geral na tela de jogo: score, titulo, borda do jogo
def draw_window(surface, score):
    surface.fill((0,0,0))
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('PENTRIS', 1, (255,255,255))

    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 30))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j* 30, top_left_y + i * 30, 30, 30), 0)

    draw_lines(surface, rows, columns)
    pygame.draw.rect(surface, (0, 0, 255), (top_left_x, top_left_y, play_width, play_height), 5)
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Score: '+str(score), 1, (255,255,255))
    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 - 100
    surface.blit(label, (sx + 10, sy + 200))

def main():
    global grid

    locked_positions = {}  # (x,y):(255,0,0)
    grid = make_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    score = 0

    while run:
        fall_speed = 0.27

        grid = make_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()

        #mino caindo
        if fall_time/1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not (valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1

                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1

                elif event.key == pygame.K_UP:
                    current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)
                    if not valid_space(current_piece, grid):
                        current_piece.rotation = current_piece.rotation - 1 % len(current_piece.shape)

                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1
                if event.key == pygame.K_SPACE:
                    while True:
                        current_piece.y += 1
                        if not valid_space(current_piece, grid):
                            current_piece.y -= 1
                            break

        shape_pos = convert_shape_format(current_piece)

        #adiciona o mino atual ao grid
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        #mino tocando 'chao'
        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False

            score += 2**clear_rows(grid, locked_positions)-1

        draw_window(win,score)
        draw_next_shape(next_piece, win)
        pygame.display.update()

        if check_lost(locked_positions):
            run = False

    draw_text_middle("Game Over", 80, (250,250,250), win)
    pygame.display.update()
    pygame.time.delay(3000)


def main_menu():
    run = True
    while run:
        win.fill((0,0,0))
        font = pygame.font.SysFont('comicsans', 60)
        label = font.render('PENTRIS', 1, (255,255,255))
        win.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 30))
        draw_text_middle('Prime qualquer tecla para jogar', 50, (255, 255, 255), win)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                main()
    pygame.quit()


win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pentris')

main_menu()

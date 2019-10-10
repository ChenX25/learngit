#!/usr/bin/env python
# coding:utf-8
# filename: slide_puzzle.py
# 滑动拼图

import pygame, sys, random
from pygame.locals import *

BOARDWIDTH = 4
BOARDHEIGHT = 4     # 游戏板：4X4格
TILESIZE = 80       # 边长：80px

WINDOWWIDTH = 640
WINDOWHEIGHT = 480
FPS = 30        # 更新频率：30 frames/sec
BLANK = None    # 空格：移动空间

BLACK =         (  0,   0,   0)
WHITE =         (255, 255, 255)
DARKTURQUOISE = (  3,  54,  73)
GREEN =         (  0, 204,   0)

BGCOLOR = DARKTURQUOISE
TILECOLOR = GREEN
TEXTCOLOR = WHITE

BORDERCOLOR = WHITE
BASICFONTSIZE = 20
MESSAGECOLOR = WHITE

XMARGIN = int((WINDOWWIDTH - (TILESIZE * BOARDWIDTH + (BOARDWIDTH -1)))/2)       # 三条间隔线
YMARGIN = int((WINDOWHEIGHT - (TILESIZE * BOARDHEIGHT + (BOARDHEIGHT -1)))/2)

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, RESET_SURF, RESET_RECT, NEW_SURF, NEW_RECT, SOLVE_SURF, SOLVE_RECT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('滑动拼图')
    BASICFONT = pygame.font.SysFont('yuantittc', BASICFONTSIZE)

    RESET_SURF, RESET_RECT = make_text(' 重来 ', TEXTCOLOR, TILECOLOR, WINDOWWIDTH -120, WINDOWHEIGHT -120)
    NEW_SURF, NEW_RECT = make_text(' 新游戏 ', TEXTCOLOR, TILECOLOR, WINDOWWIDTH -120, WINDOWHEIGHT -80)
    SOLVE_SURF, SOLVE_RECT = make_text(' 完成 ', TEXTCOLOR, TILECOLOR, WINDOWWIDTH -120, WINDOWHEIGHT -40)

    main_board, solution_seq = generate_new_puzzle(80)     # 新游戏
    SOLVEDBOARD = get_starting_board()                     # 初始游戏板
    all_moves = []

    while True:
        slide_to = None
        msg = '滑动方式：点击方块或按方向键'
        if main_board == SOLVEDBOARD:
            msg = '已完成 !!!'
        draw_board(main_board, msg)

        check_for_quit()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                spotx, spoty = get_spot_clicked(main_board, event.pos[0], event.pos[1])   # 范围内点击

                if (spotx, spoty) == (None, None):
                    if RESET_RECT.collidepoint(event.pos):
                        reset_animation(main_board, all_moves)
                        all_moves = []
                    elif NEW_RECT.collidepoint(event.pos):
                        main_board, solution_seq = generate_new_puzzle(80)
                        all_moves = []
                    elif SOLVE_RECT.collidepoint(event.pos):
                        reset_animation(main_board, solution_seq + all_moves)
                        all_moves = []
                else:
                    blankx, blanky = get_blank_position(main_board)
                    if spotx == blankx +1 and spoty == blanky:
                        slide_to = LEFT
                    elif spotx == blankx -1 and spoty == blanky:
                        slide_to = RIGHT
                    elif spotx == blankx and spoty == blanky +1:
                        slide_to = UP
                    elif spotx == blankx and spoty == blanky -1:
                        slide_to = DOWN
                        
            elif event.type == KEYUP:
                if event.key in (K_LEFT, K_a) and is_valid_move(main_board, LEFT):
                    slide_to = LEFT
                elif event.key in (K_RIGHT, K_d) and is_valid_move(main_board, RIGHT):
                    slide_to = RIGHT
                elif event.key in (K_UP, K_w) and is_valid_move(main_board, UP):
                    slide_to = UP
                elif event.key in (K_DOWN, K_s) and is_valid_move(main_board, DOWN):
                    slide_to = DOWN

        if slide_to:
            slide_animation(main_board, slide_to, '滑动方式：点击方块或按方向键', 8)
            make_move(main_board, slide_to)      # 交换
            all_moves.append(slide_to)
            
        pygame.display.update()                  # 展示：更新游戏状态
        FPSCLOCK.tick(FPS)                       # 定时：控制更新频率


def terminate():       # 精简：代码重用
    pygame.quit()
    sys.exit()

def check_for_quit():
    for event in pygame.event.get(QUIT):       # X关闭窗口
        terminate()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:              # Esc键退出
            terminate()
        pygame.event.post(event)


def get_starting_board():
    counter = 1
    board = []
    for x in range(BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            column.append(counter)             # 棋盘坐标设置
            counter += BOARDWIDTH              # x列拼图序号
        board.append(column)
        counter -= BOARDWIDTH * (BOARDHEIGHT -1) + BOARDWIDTH -1   # y+4次，相差4格*3行+3格

    board[BOARDWIDTH -1][BOARDHEIGHT -1] = None   # 最后一格，设定为空格
    return board


def get_blank_position(board):
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            if board[x][y] == None:       # 遍历16格，获取空格坐标
                return (x, y)

def make_move(board, move):               # 根据空格的位置滑动拼图
    blankx, blanky = get_blank_position(board)
    if move == UP:
        board[blankx][blanky], board[blankx][blanky +1] = board[blankx][blanky +1], board[blankx][blanky]
    elif move == DOWN:
        board[blankx][blanky], board[blankx][blanky -1] = board[blankx][blanky -1], board[blankx][blanky]
    elif move == LEFT:
        board[blankx][blanky], board[blankx +1][blanky] = board[blankx +1][blanky], board[blankx][blanky]
    elif move == RIGHT:
        board[blankx][blanky], board[blankx -1][blanky] = board[blankx -1][blanky], board[blankx][blanky]

def is_valid_move(board, move):     # 当空格在边上时，滑动有所限制
    blankx, blanky = get_blank_position(board)
    
    return (move == UP and blanky != len(board[0]) -1) or \
           (move == DOWN and blanky != 0) or \
           (move == LEFT and blankx != len(board) -1) or \
           (move == RIGHT and blankx != 0)

def get_random_move(board, last_move):        # 用于生成新谜题
    valid_moves = [UP, DOWN, LEFT, RIGHT]
    
    if last_move == UP or not is_valid_move(board, DOWN):   
        valid_moves.remove(DOWN)
    if last_move == DOWN or not is_valid_move(board, UP):
        valid_moves.remove(UP)
    if last_move == LEFT or not is_valid_move(board, RIGHT):
        valid_moves.remove(RIGHT)
    if last_move == RIGHT or not is_valid_move(board, LEFT):
        valid_moves.remove(LEFT)
        
    return random.choice(valid_moves)



def get_left_top_of_tile(tile_x, tile_y):       # 拼图碎片左上角的像素坐标
    left = XMARGIN + (tile_x * TILESIZE) + (tile_x -1)
    top = YMARGIN + (tile_y * TILESIZE) + (tile_y -1)
    
    return (left, top)

def get_spot_clicked(board, x, y):       # 鼠标点击的像素坐标，所对应的碎片坐标
    for tile_x in range(len(board)):
        for tile_y in range(len(board[0])):
            left, top = get_left_top_of_tile(tile_x, tile_y)
            
            tile_rect = pygame.Rect(left, top, TILESIZE, TILESIZE)
            if tile_rect.collidepoint(x, y):
                return (tile_x, tile_y)
    return (None, None)


def draw_tile(tile_x, tile_y, number, adjx=0, adjy=0):   # 绘制拼图碎片
    left , top = get_left_top_of_tile(tile_x, tile_y)
    pygame.draw.rect(DISPLAYSURF, TILECOLOR, (left +adjx, top +adjy, TILESIZE, TILESIZE))
    text_surf = BASICFONT.render(str(number), True, TEXTCOLOR)     # BG的默认颜色？？
    text_rect = text_surf.get_rect()
    text_rect.center = left + int(TILESIZE / 2) + adjx, top + int(TILESIZE / 2) + adjy

    DISPLAYSURF.blit(text_surf, text_rect)         # COPY到界面上

def make_text(text, color, bgcolor, top, left):    # 文字的内容、位置
    text_surf = BASICFONT.render(text, True, color, bgcolor)   # 字体渲染
    text_rect = text_surf.get_rect()
    text_rect.topleft = (top, left)
    return (text_surf, text_rect)

def draw_board(board, message):      # 绘制界面
    DISPLAYSURF.fill(BGCOLOR)

    if message:
        text_surf, text_rect = make_text(message, MESSAGECOLOR, BGCOLOR, 20, 20)
        DISPLAYSURF.blit(text_surf, text_rect)

    for tile_x in range(len(board)):              # 绘制拼图碎片
        for tile_y in range(len(board[0])):
            if board[tile_x][tile_y]:
                draw_tile(tile_x, tile_y, board[tile_x][tile_y])

    left, top = get_left_top_of_tile(0, 0)        # 绘制边框
    width = BOARDWIDTH * TILESIZE
    height = BOARDHEIGHT * TILESIZE
    pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (left -5, top -5, width +12, height +12), 4)

    DISPLAYSURF.blit(RESET_SURF, RESET_RECT)      # 绘制按钮
    DISPLAYSURF.blit(NEW_SURF, NEW_RECT)
    DISPLAYSURF.blit(SOLVE_SURF, SOLVE_RECT)


def slide_animation(board, direction, message, animation_speed):   # 滑动的过程
    blankx, blanky = get_blank_position(board)
    if direction == UP:
        movex = blankx
        movey = blanky +1
    elif direction == DOWN:
        movex = blankx
        movey = blanky -1
    elif direction == LEFT:
        movex = blankx +1
        movey = blanky
    elif direction == RIGHT:
        movex = blankx -1
        movey = blanky

    draw_board(board, message)
    base_surf = DISPLAYSURF.copy()
    move_left, move_top = get_left_top_of_tile(movex, movey)
    pygame.draw.rect(base_surf, BGCOLOR, (move_left, move_top, TILESIZE, TILESIZE))   # 移动的对象变为空格

    for i in range(0, TILESIZE, animation_speed):
        check_for_quit()
        DISPLAYSURF.blit(base_surf, (0, 0))
        if direction == UP:
            draw_tile(movex, movey, board[movex][movey], 0, -i)     # 向上滑动：x值不变，y值逐渐减小
        if direction == DOWN:
            draw_tile(movex, movey, board[movex][movey], 0, i)
        if direction == LEFT:
            draw_tile(movex, movey, board[movex][movey], -i, 0)     # 向左滑动：x值逐渐减小，y值不变
        if direction == RIGHT:
            draw_tile(movex, movey, board[movex][movey], i, 0)

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def generate_new_puzzle(num_slides):
    board = get_starting_board()
    draw_board(board, '')
    pygame.display.update()
    pygame.time.wait(500)

    sequence = []
    last_move = None
    for i in range(num_slides):
        move = get_random_move(board, last_move)
        slide_animation(board, move, '新游戏生成中。。。', int(TILESIZE / 3))
        make_move(board, move)
        
        sequence.append(move)
        last_move = move
    return (board, sequence)

def reset_animation(board, all_moves):
    rev_moves = all_moves[:]
    rev_moves.reverse()

    for move in rev_moves:
        if move == UP:
            opposite_move = DOWN
        elif move == DOWN:
            opposite_move = UP
        elif move == LEFT:
            opposite_move = RIGHT
        elif move == RIGHT:
            opposite_move = LEFT

        slide_animation(board, opposite_move, '', int(TILESIZE /2))    # 滑动速度
        make_move(board, opposite_move)



if __name__ == '__main__':
    main()
    
        
        
    


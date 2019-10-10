#!/usr/bin/env python
# coding:utf-8
# filename: tic_tac_toe.py
# 三子棋游戏

import random

def draw_board(board):          # 设计棋盘样式
    print()
    print('\t %s | %s | %s ' % (board[7], board[8], board[9]))
    print('\t---+---+---')
    print('\t %s | %s | %s ' % (board[4], board[5], board[6]))
    print('\t---+---+---')
    print('\t %s | %s | %s ' % (board[1], board[2], board[3]))
    print()
    print('-' * 30)

def select_letters():           # 由玩家选择棋子
    player_letter = ''
    while player_letter not in ['O', 'X']:
        player_letter = input('请玩家选择棋子(X/O)：').upper()
    if player_letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def who_goes_first():           # 随机决定优先顺序
    computer = random.choice([0, 1])
    if computer == 0:
        return '对手'
    else:
        return '玩家'

def is_space_free(board, move):    # 是否空棋
    return board[move] == ' '
    
def get_player_move(board):       # 输入是否得当，超纲或重复
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
        move = input('玩家请落子(1-9)：')
    return int(move)

def make_move(board, letter, move):
    board[move] = letter

def get_random_move_from_the_list(board, play_list):
    possible_move = []
    for i in play_list:
        if is_space_free(board, i):
            possible_move.append(i)           # 可用，添加
    if len(possible_move) != 0:
        return random.choice(possible_move)   # 非空，随机选择
    else:
        return None
    
def get_computer_move(board, computer_letter, player_letter):
    
    for i in range(1, 10):
        copy = board[:]
        if is_space_free(copy, i):
            make_move(copy, computer_letter, i)
            if is_won(copy, computer_letter):
                return i
    for i in range(1, 10):
        copy = board[:]
        if is_space_free(copy, i):
            make_move(copy, player_letter, i)
            if is_won(copy, player_letter):
                return i
                                                               # 稍稍一改，不好赢
    move = get_random_move_from_the_list(board, [1, 3, 7, 9])
    if move != None:
        return move
    if is_space_free(board, 5):
        return 5
    return get_random_move_from_the_list(board, [2, 4, 6, 8])
            
    
def is_full(board):
    for i in range(1, 10):
        if is_space_free(board, i):             # 只有有空，就没满
            return False
    return True

    
def is_won(bo, le):
    return ((bo[7]==le and bo[8]==le and bo[9]==le) or
            (bo[4]==le and bo[5]==le and bo[6]==le) or
            (bo[1]==le and bo[2]==le and bo[3]==le) or
            (bo[7]==le and bo[4]==le and bo[1]==le) or
            (bo[8]==le and bo[5]==le and bo[2]==le) or
            (bo[9]==le and bo[6]==le and bo[3]==le) or
            (bo[7]==le and bo[5]==le and bo[3]==le) or
            (bo[9]==le and bo[5]==le and bo[1]==le))

def play_again():
    print()
    return input('游戏结束，是否再来一局(Yes/No)：').lower().strip().startswith('y')

def main():
    print('欢迎来到三子棋游戏乐园！！')
    print('请先了解棋盘位置：')
    draw_board([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    
    while True:
        board = [' '] *10
        player_letter, computer_letter = select_letters()
        turn = who_goes_first()
        print('该局由' + turn + '先行。')
        
        game_is_playing = True
        while game_is_playing:
            
            
            if turn == '玩家':
                draw_board(board)
                
                move = get_player_move(board)
                make_move(board, player_letter, move)
                
                if is_won(board, player_letter):
                    draw_board(board)
                    print('恭喜玩家赢得胜利，太棒了！！！！')
                    game_is_playing = False
                else:
                    if is_full(board):
                        draw_board(board)
                        print('该局为平局....')
                        break
                    else:
                        turn = '对手'
                
            else:
                move = get_computer_move(board, computer_letter, player_letter)
                make_move(board, computer_letter, move)
                if is_won(board, computer_letter):
                    draw_board(board)
                    print('对手获胜，你..输了')
                    game_is_playing = False
                else:
                    if is_full(board):
                        draw_board(board)
                        print('该局为平局....')
                        break
                    else:
                        turn = '玩家'
        
        
        if not play_again():
            break
        
    

if __name__ == '__main__':
    main()

    
        

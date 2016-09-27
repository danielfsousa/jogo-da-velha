#!/usr/bin/env python
# -*- coding: utf-8 -*-

class cores:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

quadro_principal = {7: ' ', 8: ' ', 9: ' ',
                    4: ' ', 5: ' ', 6: ' ',
                    1: ' ', 2: ' ', 3: ' '}

quadro_vencedor = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'],
                   ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'],
                   ['3', '5', '7'], ['1', '5', '9']]

instrucoes = {7: '7', 8: '8', 9: '9',
              4: '4', 5: '5', 6: '6',
              1: '1', 2: '2', 3: '3'}

def retorna_int(num):
    try:
        return int(num)
    except:
        return 0

def print_instrucoes():
    print('Digite um número de acordo com o local onde você deseja jogar.')
    print_quadro(instrucoes)

def print_quadro(board):
    print(cores.WARNING)
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' ')
    print('-+-+-+-+-+-')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' ')
    print('-+-+-+-+-+-')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' ')
    print(cores.ENDC)


def reiniciar_quadro(board):
    for key in board.keys():
        board[key] = ' '


def jogar(quadro, acao, jogador):
    simbolo = 'X' if (jogador == 1) else 'O'
    if quadro[int(acao)] == ' ':
        quadro[int(acao)] = simbolo
        return True
    else:
        return False

def trocar(jogador):
    if jogador == 1:
        return 2
    else:
        return 1

def verificar_vencedor():
    x = []
    o = []
    cont = 0

    for key, val in quadro_principal.items():
        if(quadro_principal[key] != ' '): cont += 1
        if(quadro_principal[key] == 'X'): x.append(str(key))
        if(quadro_principal[key] == 'O'): o.append(str(key))

    x_sorted = ''.join(x)
    o_sorted = ''.join(o)

    for i in range(len(quadro_vencedor)):
        num_certos_x = 0
        num_certos_o = 0

        for j in range(len(quadro_vencedor[i])):
            if x_sorted.find(quadro_vencedor[i][j]) > -1:
                num_certos_x += 1
            elif o_sorted.find(quadro_vencedor[i][j]) > -1:
                num_certos_o += 1

        if num_certos_x == 3:
            return 1  # Jogador 1 (X)
        if num_certos_o == 3:
            return 2  # Jogador 2 (O)

    if cont == 9:
        return -1  # Deu velha

    return 0  # Nenhum jogador

def comecar_jogo():

    jogador = 1

    while True:
        print_quadro(quadro_principal)
        print('Digite ' + cores.WARNING + '--inst' + cores.ENDC + ' para ver as instruções. Digite ' + cores.WARNING + '--rein' + cores.ENDC + ' para reiniciar o jogo. Digite ' + cores.WARNING + '--sair' + cores.ENDC + ' para sair.')
        print()
        print('Jogador ' + str(jogador) + ': Onde você quer jogar?')

        acao = input()

        if acao == '--inst':
            print_instrucoes()
            continue
        elif acao == '--sair':
            exit(0)
        elif acao == '--rein':
            reiniciar_quadro(quadro_principal)
            jogador = 1
            continue
        elif retorna_int(acao) in quadro_principal:
            if jogar(quadro_principal, acao, jogador):
                jogador = trocar(jogador)
        else:
            continue

        vencedor = verificar_vencedor()
        if vencedor != 0:
            if vencedor > 0:
                msg = 'Jogador ' + str(vencedor) + ' venceu!'
            if vencedor == -1:
                msg = 'Deu velha!'

            print_quadro(quadro_principal)
            print(cores.OKGREEN + msg)
            print(cores.ENDC)
            print('Deseja começar uma nova partida? (s/n)')
            sim_ou_nao = input()
            if sim_ou_nao == 's':
                reiniciar_quadro(quadro_principal)
                jogador = 1
            else:
                exit()

# Começar Jogo
comecar_jogo()
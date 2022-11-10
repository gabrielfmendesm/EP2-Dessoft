# imports
from baseperguntasrespostas import *
from funcoes import *

# base de perguntas e respostas
base_processada = transforma_base (quest)
lista_questoes = []

# id inicial
id = 1

# lista prêmios
lista_premios = [0.00, 1000.00, 5000.00, 10000.00, 30000.00, 50000.00, 100000.00, 300000.00, 500000.00, 1000000.00]


# tela inicial
print ('Olá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!''\n')
nome = input ('Qual seu nome? ')
print ('\n'f'Ok {nome.upper ()}, você tem direito a pular 3 vezes e 2 ajudas!')
print ('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!''\n')
inicio = input ('Aperte ENTER para continuar...')

# início do jogo
while True:
    if inicio == '':
        print ('\n''O jogo já vai começar! Lá vem a primeira questão!''\n')
        inicio2 = input ('Vamos começar com questões do nível FACIL!''\n''Aperte ENTER para continuar...')
        while True:
            if inicio2 == '':
                while True and id < 10:
                    if id < 3:
                        nivel_jogo = 'facil'
                    elif id < 7:
                        nivel_jogo = 'medio'
                    else:
                        nivel_jogo = 'dificil'
                    print('\n''\n')
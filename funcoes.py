from random import *

def transforma_base (lista):
    dicionario = {}
    for e in lista:
        for k, v in e.items():
            if k == 'nivel':
                if v in dicionario:
                    dicionario[v].append (e)
                else:
                    dicionario[v] = [e]
    return dicionario

def valida_questao (pergunta): 
    dicionario = {}
    for k in ('titulo', 'nivel', 'opcoes', 'correta'):
        if k not in pergunta:
            dicionario[k] = 'nao_encontrado'
    if len (pergunta.keys()) != 4:
        dicionario['outro'] = 'numero_chaves_invalido'
    if 'titulo' in pergunta: 
        if pergunta['titulo'].strip() == '':
            dicionario['titulo'] = 'vazio'
    if 'nivel' in pergunta:
        if pergunta['nivel'] not in ('facil', 'medio', 'dificil'):
            dicionario['nivel'] = 'valor_errado'
    if 'opcoes' in pergunta:
        if len (pergunta['opcoes'].keys()) == 4:
            for opçao, resposta in pergunta['opcoes'].items():
                if opçao in('A', 'B', 'C', 'D'):
                    if resposta.strip() == '':
                        if 'opcoes' not in dicionario:
                            dicionario['opcoes'] = {}
                            dicionario['opcoes'][opçao] = 'vazia'
                        else:
                            dicionario['opcoes'][opçao] = 'vazia'
                else:
                    dicionario['opcoes'] = 'chave_invalida_ou_nao_encontrada'
        else: 
            dicionario['opcoes'] = 'tamanho_invalido'
    if 'correta' not in dicionario:
        if pergunta['correta'] not in ('A', 'B', 'C', 'D'):
            dicionario['correta'] = 'valor_errado'
    return dicionario

def valida_questoes (lista):
    lista_questoes = []
    for i in lista:
        validado = valida_questao (i)
        lista_questoes.append (validado)
    return lista_questoes

def sorteia_questao (dicionario, nivel):
    questao = choice (dicionario[nivel])
    return (questao)

def sorteia_questao_inedita (dicionario, nivel, lista):
    while True:  
        questao = choice (dicionario[nivel])
        if questao not in lista:
            lista.append (questao)
            break
    return (questao)

def questao_para_texto (dicionario, id):
    return ('----------------------------------------'
    '\n'
    f"QUESTAO {id}"
    '\n'
    '\n'
    f"{dicionario['titulo']}"
    '\n'
    '\n'
    "RESPOSTAS:"
    '\n'
    f"A: {dicionario['opcoes'] ['A']}"
    '\n'
    f"B: {dicionario['opcoes']['B']}"
    '\n'
    f"C: {dicionario['opcoes']['C']}"
    '\n'
    f"D: {dicionario['opcoes']['D']}"
    )

def gera_ajuda (dicionario):
    lista_erradas = []
    lista_dicas = []
    resposta_correta = dicionario['correta']
    dicionario_questoes = dicionario['opcoes']
    for e in dicionario_questoes.values():
        if e != dicionario_questoes[resposta_correta]:
            lista_erradas.append (e)
    contador = choice (range (2))
    contador += 1
    for i in range (contador):
        lista_dicas.append (choice (lista_erradas))
    if len (lista_dicas) == 2:
        if lista_dicas[0] == lista_dicas[1]:
            del lista_dicas[1]
    if len (lista_dicas) == 2:        
        dica = (f'DICA:\nOpções certamente erradas: {lista_dicas[0]} | {lista_dicas[1]}')
    else:
        dica = (f'DICA:\nOpções certamente erradas: {lista_dicas[0]}')
    return dica
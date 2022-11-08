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
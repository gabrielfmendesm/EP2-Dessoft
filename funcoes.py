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
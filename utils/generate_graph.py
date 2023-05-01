# Cria um dicionário com os estados e adiciona no grafo
estados = {0: 'AC', 1: 'AL', 2: 'AM', 3: 'AP', 4: 'BA', 5: 'CE', 6: 'DF', 7: 'ES', 8: 'GO',
               9: 'MA', 10: 'MG', 11: 'MS', 12: 'MT', 13: 'PA', 14: 'PB', 15: 'PE', 16: 'PI', 17: 'PR',
               18: 'RJ', 19: 'RN', 20: 'RO', 21: 'RR', 22: 'RS', 23: 'SC', 24: 'SE', 25: 'SP', 26: 'TO'}

def generate_brasil_graph():
    # Cria um grafo vazio
    brasil = {}
    
    for estado in estados:
        brasil[estado] = set()

    # Cria arestas de um estado para seus adjacentes
    brasil[6].update([8])
    brasil[2].update([21, 20, 0])
    brasil[20].update([0, 12])
    brasil[0].update([12, 18])
    brasil[12].update([26, 8, 11])
    brasil[26].update([9, 13, 16])
    brasil[9].update([13, 16, 5])
    brasil[13].update([3, 21, 12, 9])
    brasil[3].update([13, 9])
    brasil[21].update([2, 13])
    brasil[5].update([16, 19, 14, 15, 4])
    brasil[15].update([16, 4, 1, 14])
    brasil[16].update([4, 26])
    brasil[4].update([26, 8, 10, 7, 24, 1])
    brasil[1].update([24, 15])
    brasil[10].update([8, 25, 18])
    brasil[11].update([25, 17, 12])
    brasil[25].update([18, 17, 10])
    brasil[18].update([7, 25])
    brasil[17].update([23, 25, 11])
    brasil[23].update([22, 17])
    brasil[22].update([23])
    brasil[24].update([4])

    return brasil

#Retorna o indice do estado
def encontrar_indice(estado):
    for index, uf in estados.items():
        if uf == estado:
            return index
    return None

def encontrar_estado(estado):
    for index, uf in estados.items():
        if uf == estado:
            return uf
    return None

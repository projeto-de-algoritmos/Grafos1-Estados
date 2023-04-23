import networkx as nx

def generate_brasil_graph():
    # Cria um grafo vazio usando o networkx
    brasil = nx.Graph()

    # Cria um Array com os estados e adiciona no grafo
    estados = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO',
               'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR',
               'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']
    for estado in estados:
        brasil.add_node(estado)

    # Cria arestas de um estado para seus adjacentes
    brasil.add_edge('AM', 'RR')
    brasil.add_edge('AM', 'RO')
    brasil.add_edge('AM', 'AC')
    brasil.add_edge('RO', 'AC')
    brasil.add_edge('RO', 'MT')
    brasil.add_edge('AC', 'MT')
    brasil.add_edge('AC', 'RJ')
    brasil.add_edge('MT', 'TO')
    brasil.add_edge('MT', 'GO')
    brasil.add_edge('MT', 'MS')
    brasil.add_edge('TO', 'MA')
    brasil.add_edge('TO', 'PA')
    brasil.add_edge('TO', 'PI')
    brasil.add_edge('MA', 'PA')
    brasil.add_edge('MA', 'PI')
    brasil.add_edge('MA', 'CE')
    brasil.add_edge('PA', 'AP')
    brasil.add_edge('PA', 'RR')
    brasil.add_edge('PA', 'MT')
    brasil.add_edge('PA', 'MA')
    brasil.add_edge('AP', 'PA')
    brasil.add_edge('AP', 'MA')
    brasil.add_edge('RR', 'AM')
    brasil.add_edge('RR', 'PA')
    brasil.add_edge('CE', 'PI')
    brasil.add_edge('CE', 'RN')
    brasil.add_edge('CE', 'PB')
    brasil.add_edge('CE', 'PE')
    brasil.add_edge('CE', 'BA')
    brasil.add_edge('PE', 'PI')
    brasil.add_edge('PE', 'BA')
    brasil.add_edge('PE', 'AL')
    brasil.add_edge('PE', 'PB')
    brasil.add_edge('PI', 'BA')
    brasil.add_edge('PI', 'TO')
    brasil.add_edge('BA', 'TO')
    brasil.add_edge('BA', 'GO')
    brasil.add_edge('BA', 'MG')
    brasil.add_edge('BA', 'ES')
    brasil.add_edge('BA', 'SE')
    brasil.add_edge('BA', 'AL')
    brasil.add_edge('AL', 'SE')
    brasil.add_edge('AL', 'PE')
    brasil.add_edge('MG', 'GO')
    brasil.add_edge('MG', 'SP')
    brasil.add_edge('MG', 'RJ')
    brasil.add_edge('MS', 'SP')
    brasil.add_edge('MS', 'PR')
    brasil.add_edge('MS', 'MT')
    brasil.add_edge('SP', 'RJ')
    brasil.add_edge('SP', 'PR')
    brasil.add_edge('SP', 'MG')
    brasil.add_edge('RJ', 'ES')
    brasil.add_edge('RJ', 'SP')
    brasil.add_edge('PR', 'SC')
    brasil.add_edge('PR', 'SP')
    brasil.add_edge('PR', 'MS')
    brasil.add_edge('SC', 'RS')
    brasil.add_edge('SC', 'PR')
    brasil.add_edge('RS', 'SC')
    brasil.add_edge('SE', 'BA')
    
    return brasil
    

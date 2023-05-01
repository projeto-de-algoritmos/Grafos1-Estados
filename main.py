from utils.generate_graph import generate_brasil_graph, encontrar_indice
from bfs import BFS

# Recebe o ponto inicial e final 
estado_inicial = str(input("Informe seu estado inicial:")).upper()
estado_final = str(input("Informe seu estado de destino:")).upper()

estado_inicial_index = encontrar_indice(estado_inicial)
estado_final_index = encontrar_indice(estado_final)

# Recebe o grafo do brasil
brasil = generate_brasil_graph()

# rota = nx.shortest_path(brasil, estado_inicial, estado_final)
rota = BFS(brasil, estado_inicial_index, estado_final_index)

print("Caminho usando o indice de cada estado")
print("Caminho: ", end='')
for estado in rota:
    print(f"-> {estado} ", end='')

# print(rota)




from utils.generate_graph import generate_brasil_graph
import networkx as nx

# Recebe o ponto inicial e final 
estado_inicial = str(input("Informe seu estado inicial:"))
estado_final = str(input("Informe seu estado de destino:"))

# Recebe o grafo do brasil
brasil = generate_brasil_graph()

rota = nx.shortest_path(brasil, estado_inicial, estado_final)

print("Caminho: ", end='')
for estado in rota:
    print(f"-> {estado} ", end='')

# print(rota)




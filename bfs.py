# BFS com modificação 
def BFS(adjList, start, dest, parent):

    # Fila de vértices a serem passados
    queue = []
  
    # Inicializa vetor auxilar que guarda a informação
    # se um vétice já foi visitado
    # visited = [False for i in 27];
    visited = []
    i = 0
    while i < 27:
        visited.append(False)
        i = i + 1
    

    # Inicializa o vetor que guarda o nó pai
    # possibilita guardar o caminho até chegar no objetivo
    i = 0
    while i < 27:
        parent[i] = -1;
        i = i + 1
    
    # O primeiro a ser visitado é o vértice de partida
    visited[start] = True;
    queue.append(start);
  
    # BFS padrão
    while (len(queue) != 0):
        u = queue[0];
        queue.pop(0);
        for i in range(len(adjList[u])):
         
            if (visited[adjList[u][i]] == False):
                visited[adjList[u][i]] = True;
                pred[adjList[u][i]] = u;
                queue.append(adjList[u][i]);
  
                # Para quando encontra o destino
                if (adjList[u][i] == dest):
                    return True;
    return False;

# Imprime menor caminho
def makePath(adjList, start, dest):
    
    parent= []

    # Vetor de pais
    #parent = [0 for i in 27]
    i=0
    while i < 27:
        parent.append(0)
        i = i + 1

    BFS(adjList, start, dest, parent)

    # Vetor que guarda o menor caminho
    path = []
    aux = dest
    path.append(aux)

    while(parent[aux] != -1):
        path.append(parent[aux])
        aux = parent[aux]

    # Imprime o caminho
    return path
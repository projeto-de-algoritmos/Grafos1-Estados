# BFS com modificação 
def BFS(adjList, start, dest, parent):

    # Fila de vértices a serem passados
    queue = []
  
    # Inicializa vetor auxilar que guarda a informação
    # se um vétice já foi visitado
    visited = [False for i in 27];
  
    # Inicializa o vetor que guarda o nó pai
    # possibilita guardar o caminho até chegar no objetivo
    for i in 27:
        parent[i] = -1;
    
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
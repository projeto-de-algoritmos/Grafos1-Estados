from queue import Queue

def BFS(graph, start, end):
    queue = Queue()
    queue.put((start, [start]))
    visited = set()
    visited.add(start)
    
    while not queue.empty():
        (current_node, path) = queue.get()
        
        if current_node == end:
            return path
        
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)                
                queue.put((neighbor, path + [neighbor]))
    
    return None
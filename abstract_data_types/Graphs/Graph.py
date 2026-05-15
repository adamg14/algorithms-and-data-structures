from collections import deque

class Vertex:
    def __init__(self, value, adjacent_verticies=None):
        self.value = value
        if adjacent_verticies is None:
            self.adjacent_verticies = []
        else:
            self.adjacent_verticies = adjacent_verticies
    
    # This will be a graph where relationships are mutual/reciprocal
    def add_adjacent_verticies(self, vertex):
        if not self.is_adjacent(vertex):
            self.adjacent_verticies.append(vertex.value)
        if not vertex.is_adjacent(self):
            vertex.adjacent_vertitices.append(self.value)

        return True


    def is_adjacent(self, vertex1):
        return (vertex1.value in self.adjacent_verticies)


    def dfs(self, search_value=None, current_vertex=None, visited=None):
        """implementation of depth first search and depth first traversion
        in a single function"""
        if visited is None:
            visited = {}

        if current_vertex is None:
            visited[self.value] = True
            current_vertex = self

        if search_value is not None:
            if current_vertex.value == search_value:
                return True
            
        visited[current_vertex.value] = True

        for vertex in current_vertex.adjacent_verticies:
            if visited.get(vertex.value):
                continue
            else:
                result = self.dfs(search_value, vertex, visited)
                if result:
                    return result
        
        if search_value is not None:
            return False
        
    
    def bfs(self, search_value=None, current_vertex=None, visited=None):
        if visited is None:
            visited = {}
        
        if current_vertex is None:
            current_vertex = self

        visited[current_vertex.value] = True

        queue = deque([current_vertex])
        
        while queue:
            current_vertex = queue.popleft()
            if search_value is not None:
                if search_value == current_vertex.value:
                    return True
            for vertex in current_vertex.adjacent_verticies:
                if visited.get(vertex.value):
                    continue
                else:
                    visited[vertex.value] = True
                    queue.append(vertex)
        
        if search_value is not None:
            return False
        

    def __str__(self):
        return f"Value: {self.value}"
    

alice = Vertex("Alice")
print(alice)
bob = Vertex("Bob")
alice.add_adjacent_verticies(bob)

print(alice.is_adjacent(bob))




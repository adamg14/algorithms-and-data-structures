class Vertex:
    def __init__(self, value, adjacent_verticies=[]):
        self.value = value
        self.adjacent_verticies = adjacent_verticies
    
    # This will be a graph where relationships are mutual/reciprocal
    def add_adjacent_verticies(self, vertex1):
        if self.is_adjacent(vertex1):
            return None
        else:
            self.add_adjacent_verticies(vertex1)
            if not vertex1.is_adjacent(vertex1):
                vertex1.adjacent_vertices.append(self)
    

    def is_adjacent(self, vertex1):
        return (vertex1 in self.adjacent_verticies)
        
    def __str__(self):
        return f"Value: {self.value}"


alice = Vertex("Alice")
print(alice)
bob = Vertex("Bob")
alice.add_adjacent_verticies(bob)

print(alice.is_adjacent(bob))

    


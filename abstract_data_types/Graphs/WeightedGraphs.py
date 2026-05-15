class WeightedGraphVertex:
    def __init__(self, value, adjacent_verticies=None):
        self.value = value
        if adjacent_verticies is None:
            self.adjacent_verticies = {}
        else:
            self.adjacent_verticies = adjacent_verticies
    

    def add_adjacent_vertex(self, vertex, weight) -> bool:
        # if already connected
        if self.is_adjacent(vertex):
            return False
        
        self.adjacent_verticies[vertex.value] = weight
        vertex.adjacent_verticies[vertex.value] = weight
        return True

    
    def is_adjacent(self, vertex) -> bool:
        return (vertex.value in self.add_adjacent_vertex)


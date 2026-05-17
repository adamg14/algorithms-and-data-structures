class WeightedGraphVertex:
    def __init__(self, value, adjacent_verticies=None):
        self.value = value
        if adjacent_verticies is None:
            self.adjacent_verticies = {}
        else:
            self.adjacent_verticies = adjacent_verticies
    

    def add_adjacent_vertex(self, vertex, weight) -> bool:
        # if the connection already exists - update the weight value
        self.adjacent_verticies[vertex] = weight
        return True

    
    def is_adjacent(self, vertex) -> bool:
        return (vertex in self.adjacent_verticies)
    

    def get_adjacent_vertexes(self):
        if len(self.adjacent_verticies) == 0:
            return None
        else:
            return self.adjacent_verticies
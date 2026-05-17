from WeightedGraphVertex import WeightedGraphVertex


class WeightedGraph:
    def __init__(self):
        # using a hash map to get O(1) retrieval
        self.vertexes = {}
    

    def add_vertex(self, new_vertex: WeightedGraphVertex) -> bool:
        self.vertexes[new_vertex.value] = new_vertex
        return True

    def get_vertex(self, input_vertex=None):
        # either a vertex or vertex value passed into this function
        return self.vertexes.get(input_vertex.value) or self.vertexes.get(input_vertex)


    def dijkstas_shortest_path(
            self,
            start_vertex: WeightedGraphVertex,
            end_vertex: WeightedGraphVertex
    ):
        visited_vertex = {}
        unvisited_vertex = []
        cheapest_price_table  = {}
        cheapest_previous_table = {}

        current_vertex = start_vertex
        # start vertex price set to 0 - as it costs nothing to get the start vertex
        cheapest_price_table[current_vertex] = 0

        while current_vertex:
            # set the visited flag to True for the current_vertex
            visited_vertex[current_vertex] = True

            # remove the current vertex from the unvisited vertex array
            if current_vertex in unvisited_vertex:
                unvisited_vertex.remove(current_vertex)
            
            for vertex, weight in current_vertex.adjacent_verticies.items():
                if not visited_vertex.get(vertex):
                    unvisited_vertex.append(vertex)
                weight = weight + cheapest_price_table[current_vertex]
                if vertex not in cheapest_price_table or weight < cheapest_price_table[vertex]:
                    cheapest_price_table[vertex] = weight
                    cheapest_previous_table[vertex.value] = current_vertex

            if len(unvisited_vertex) != 0:
                current_vertex = unvisited_vertex[0]
                unvisited_vertex = unvisited_vertex[1:]
            else:
                break

        shortest_path = []

        current_vertex = end_vertex
        print(cheapest_previous_table)
        print(end_vertex)
        while current_vertex.value != start_vertex.value:
            shortest_path.append(current_vertex)
            current_vertex = cheapest_previous_table[current_vertex.value]

        shortest_path.append(start_vertex)

        return list(reversed(list(map(lambda x: x.value, shortest_path))))




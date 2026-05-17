from WeightedGraphVertex import WeightedGraphVertex


class WeightedGraph:
    def __init__(self):
        self.vertexes = []
    

    def add_vertex(self, new_vertex: WeightedGraphVertex) -> bool:
        pass


    def get_vertex() -> WeightedGraphVertex:
        pass


    def dijkstas_shortes_path(
            self,
            start_vertex: WeightedGraphVertex,
            end_vertex: WeightedGraphVertex
    ):
        visited_vertex = {}
        unvisited_vertex = []

        cheapest_price_table  = {}



# def dijkstras_shortest_path(
#         start_vertex: WeightedGraphVertex,
#         destination_vertex: WeightedGraphVertex
#         ):
    
#     visited_vertex = {}
#     unvisited_vertex = []

#     cheapest_price_table = {}
#     cheapest_previous_table = {}

#     # the weight to get to the starting vertex is 0, as we start there
#     cheapest_price_table[start_vertex.value] = 0

#     # bookmarking variable 
#     current_vertex = start_vertex

#     while current_vertex:
#         # set the current vertex to visited 
#         visited_vertex[current_vertex.value] = True

#         # remove the current city from unvisited cities
#         # marking it as visite
#         if current_vertex in unvisited_vertex:
#             unvisited_vertex.remove(current_vertex)

#         # iterate over the current vertexes adjacent vertexes
#         # adjacent_vertices is know 
#         adjacent_vertices = current_vertex.get_adjacent_vertexes()
        
#         for vertex in adjacent_vertices:
#             pass



# atlanta = WeightedGraphVertex("Atlanta")
# boston = WeightedGraphVertex("Boston")
# chicago = WeightedGraphVertex("Chicago")
# denver = WeightedGraphVertex("Denver")
# el_paso = WeightedGraphVertex("El Paso")



# # atlanta.add_adjacent_vertex(boston, 100)
# # atlanta.add_adjacent_vertex(denver, 160)

# # boston.add_adjacent_vertex(chicago, 120)
# # boston.add_adjacent_vertex(denver, 180)

# # chicago.add_adjacent_vertex(el_paso, 80)

# # denver.add_adjacent_vertex(chicago, 40)
# # denver.add_adjacent_vertex(el_paso, 140)

# # el_paso.add_adjacent_vertex(boston, 100)

# # print(dijkstras_shortest_path(atlanta, chicago))

# # print(atlanta.is_adjacent(chicago))
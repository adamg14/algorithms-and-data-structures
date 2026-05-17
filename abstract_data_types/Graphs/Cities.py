from WeightedGraphVertex import WeightedGraphVertex
from WeightedGraph import WeightedGraph

cities = WeightedGraph()

atlanta = WeightedGraphVertex("Atlanta")
boston = WeightedGraphVertex("Boston")
chicago = WeightedGraphVertex("Chicago")
denver = WeightedGraphVertex("Denver")
el_paso = WeightedGraphVertex("El Paso")

atlanta.add_adjacent_vertex(boston, 100)
atlanta.add_adjacent_vertex(denver, 160)
boston.add_adjacent_vertex(chicago, 120)
boston.add_adjacent_vertex(denver, 180)
chicago.add_adjacent_vertex(el_paso, 80)
denver.add_adjacent_vertex(chicago, 40)
denver.add_adjacent_vertex(el_paso, 140)
el_paso.add_adjacent_vertex(boston, 100)

cities.add_vertex(atlanta)
cities.add_vertex(boston)
cities.add_vertex(chicago)
cities.add_vertex(denver)
cities.add_vertex(el_paso)


print(cities.dijkstas_shortest_path(atlanta, el_paso))
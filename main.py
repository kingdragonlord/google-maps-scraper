from src import Gmaps

queries = [
   "Car dealership in Arizona"
]

Gmaps.places(queries, max=20)
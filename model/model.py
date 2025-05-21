import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo = nx.Graph()

    def buildGraph(self, colore, anno):
        nodi = DAO.get_products_colored(colore)
        self.grafo.add_nodes_from(nodi)


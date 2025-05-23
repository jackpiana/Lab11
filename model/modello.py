from time import time

import networkx as nx
from networkx.classes import degree

from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo = nx.Graph()

    def buildGraph(self, colore, anno):
        nodi = DAO.get_products_colored(colore)
        self.grafo.add_nodes_from(nodi)
        for nodo1 in nodi:
            for nodo2 in nodi:
                if nodo1 == nodo2:
                    continue
                peso = DAO.get_peso_edge(anno, nodo1.Product_number, nodo2.Product_number)
                if peso != 0:
                    self.grafo.add_edge(nodo1, nodo2, weight=peso)

    def get_edges_ordinate(self):
        # Stampa gli archi ordinati per peso (decrescente)
        sorted_edges = sorted(self.grafo.edges(data=True), key=lambda x: x[2]['weight'], reverse=True)
        return sorted_edges
    """
        edges(data=True) restituisce una lista di tuple con i dati associati a ogni arco.
        Ogni elemento ha la forma (nodo1, nodo2, dizionario_dati)
        key=lambda x: x[2]['weight']
        Questo è un criterio di ordinamento.
        La lambda prende ogni elemento x della lista (che è una tupla come (nodo1, nodo2, dizionario_dati))
        x[2] è il dizionario dei dati dell’arco.
        x[2]['weight'] estrae il valore del peso dell’arco.
    """

    def get_top3_edges(self):
        edges = self.get_edges_ordinate()
        return edges[:3]

    def top_nodes(self):
        top_nodes = set()
        edges = self.get_top3_edges()
        sotto_grafo = nx.Graph()
        sotto_grafo.add_edges_from(edges)
        for nodo in sotto_grafo.nodes():
            if int(str(sotto_grafo.degree(nodo))) > 1:
                top_nodes.add(nodo)
        return top_nodes

    def reset(self):
        self.grafo = nx.Graph()

if __name__ == "__main__":
    m = Model()
    tic = time()
    m.buildGraph("white", 2015)
    tac = time()
    print(m.grafo)
    print(f"{tac - tic} seconds")
    for p in m.get_top3_edges():
        print(f"edge: {p[0].Product} - {p[1].Product} --- peso: {p[2]}")

    for p in m.top_nodes():
        print(p)



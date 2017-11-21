import networkx as nx


class WikipediaParser:
    """
    This class is used to parse the data from the input file to an analyzable graph using networkx.
    """
    _graph = nx.DiGraph()

    def __init__(self, filename):
        print("Wikipedia Parser initialized")
        self._graph = self._read_data(filename)
        print("Graph read - %d nodes and %d edges" % (nx.number_of_nodes(self._graph), nx.number_of_edges(self._graph)))

    def get_graph(self):
        return self._graph

    @staticmethod
    def _read_data(filename):
        g = nx.DiGraph()
        file = open(filename, "r")
        for line in file:
            # source target weight timestamp
            spl = line.split()
            if len(spl) == 4:
                g.add_edge(spl[0], spl[1], weight=spl[2], timestamp=spl[3])
        return g

    def get_first_subgraph(self):
        return self._graph

    def get_second_subgraph(self):
        return self._graph
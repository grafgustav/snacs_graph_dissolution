import networkx as nx
import _pickle as pickle


class WikipediaParser:
    """
    This class is used to parse the data from the input file to an analyzable graph using networkx. It also provides
    some functionality to split the data into separate graphs.
    """
    # the two graphs
    _graph1 = nx.DiGraph()  # training
    _graph2 = nx.DiGraph()  # ground truth

    _gt_edges = []

    # raw data
    _edges = []
    _remaining_edges = []
    _timestamps = []
    _median_timestamp = -1

    PIK_NAME = "pickle.dat"

    def __init__(self, filename, load=False):
        """
        Constructor of the WikipediaParser class. Takes a filename as input to read the dataset from.
        :param filename: input file for the dataset
        """
        print("Wikipedia Parser initialized")
        if not load:
            print("Data not persisted")
            self._edges, self._timestamps = self._read_data(filename)
            self._median_timestamp = self.get_median_timestamp()
            self._graph1, self._graph2 = self._build_graphs()
            with open(self.PIK_NAME, "wb") as f:
                data = (self._graph1, self._graph2, self._gt_edges)
                pickle.dump(data, f)
        else:
            with open(self.PIK_NAME, "rb") as f:
                self._graph1, self._graph2, self._gt_edges = pickle.load(f)

    @staticmethod
    def _read_data(filename):
        """
        Reads the data from the referenced file.
        :param filename: name of the file to read the data from
        :return: A list of 4-tuples (source, target, weight, timestamp), a list of timestamps in milliseconds
        """
        file = open(filename, "r")
        timestamps = []
        edges = []
        for line in file:
            # source target weight timestamp
            if line.startswith("%"):
                continue
            spl = line.split()
            if len(spl) == 4:
                # store that stuff in triples (source, target, weight, timestamp)
                edges.append((int(spl[0]), int(spl[1]), int(spl[2]), int(spl[3])))
                timestamps.append(int(spl[3]))
        return edges, sorted(timestamps)

    def get_first_subgraph(self):
        return self._graph1

    def get_second_subgraph(self):
        return self._graph2

    def get_first_timestamp(self):
        return min(self._timestamps)

    def get_latest_timestamp(self):
        return max(self._timestamps)

    def get_median_timestamp(self):
        median = self._timestamps[int(len(self._timestamps)*(3/4))]
        return median

    def get_gt_edges(self):
        return self._gt_edges

    def _build_graphs(self):
        """
        This method parts the data into two parts, creating two graphs. The first is the initial snapshot to a certain
        timestamp. The second is a copy of the first one, but with some edges removed.
        :return: graph1, graph2
        """
        g1 = self._build_graph1()
        g2 = self._build_graph2(g1)
        return g1, g2

    def _build_graph1(self):
        """
        This method builds the first snapshot graph of the wikipedia dataset. It takes into account all edges and nodes
        appearing from the first appearing timestamp to the median timestamp.
        :return: a directed graph
        """
        g1 = nx.DiGraph()
        for source, target, weight, timestamp in self._edges:
            if timestamp <= self._median_timestamp:
                if weight == 1:
                    g1.add_edge(source, target)
                else:
                    if g1.has_edge(source, target):
                        g1.remove_edge(source, target)
            else:
                self._remaining_edges.append((source, target, weight))
        return g1

    def _build_graph2(self, g1):
        """
        This method takes the first snapshot as input and removes all edges that are marked for removal to later
        time steps.
        :param g1: the graph from which edges will be removed
        :return: the input graph with removed edges
        """
        g2 = g1.copy()
        for source, target, weight in self._remaining_edges:
            if weight == -1:
                self._gt_edges.append((source, target))
                if g2.has_edge(source, target):
                    g2.remove_edge(source, target)
        return g2

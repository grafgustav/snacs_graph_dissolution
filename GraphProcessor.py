import networkx as nx


class GraphProcessor:

    """
    Using only static methods this class offers functionality to process a graph according to the approaches in the
    paper.
    """

    @staticmethod
    def transform_scored_edge_list_to_graph(edge_list, graph, threshold):
        """
        Helper method to transform a given edge list with scores in the form of (source, target, score) to a graph.
        The score determines whether an edge needs to be removed or not. A threshold is defined for the transformation.
        :param edge_list: The scored edge list as triple (source, target, score)
        :param graph: The input graph, whose edges will be altered
        :param threshold: The threshold used to determine whether an edge should be removed
        :return: a networkx DiGraph
        """
        result_graph = graph.copy()
        for source, target, score in edge_list:
            if score >= threshold:
                result_graph.remove_edge(source, target)
        return result_graph

    ####################################################################################################################
    # Complement score methods - Use link prediction functions on existing links and complement score
    @staticmethod
    def preferential_attachment(graph):
        """
        Using the degree of the two nodes being connected by an edge, predict the probability of this edge to be removed.
        :param graph: input graph as adjacency matrix
        :return: edge list containing probabilities (source, target, score)
        """
        # result list contains edges and their predicted scores (source, target, score)
        degrees = dict()
        for node in nx.nodes(graph):
            degrees[node] = nx.degree(graph, node)
        return GraphProcessor._preferential_attachment(graph, degrees)

    @staticmethod
    def _preferential_attachment(graph, degrees):
        result = []
        for source, target in graph.edges:
            source_degree = degrees[source]
            target_degree = degrees[target]
            score = -1 * source_degree * target_degree
            result.append((source, target, score))
        return result

    @staticmethod
    def common_neighbors(graph):
        """
        Using the neighborhood of the two nodes being connected by an edge, predict the probability of this edge to be
        removed.
        :param graph: input graph as adjacency matrix
        :return: adjacency matrix containing probabilities
        """
        neighbor_dictionary = dict()
        for node in nx.nodes(graph):
            neighbor_dictionary[node] = set(nx.neighbors(graph, node))

        result = []
        for source, target in nx.edges(graph):
            result.append((source, target,
                           (-1) * len(neighbor_dictionary[source].intersection(neighbor_dictionary[target]))))
        return result

    @staticmethod
    def cosine_similarity(graph):
        """
        Using the cosine similarity of the two nodes being connected by an edge, predict the probability of this edge
        to be removed.
        :param graph: input graph as adjacency matrix
        :return: adjacency matrix containing probabilities
        """
        result = []

        return result

    @staticmethod
    def jaccard_index(graph):
        """
        Using the jaccard index of the two nodes being connected by an edge, predict the probability of this edge to be
        removed.
        :param graph: input graph as adjacency matrix
        :return: adjacency matrix containing probabilities
        """
        result = []

        return result

    @staticmethod
    def adamic_adar(graph):
        """
        Using the methodology of Adamic and Adar predict the probability of all edges to be removed.
        :param graph: input graph as adjacency matrix
        :return: adjacency matrix containing probabilities
        """
        result = []

        return result

    ####################################################################################################################
    # Complement network - Use link prediction functions on non-existing edges in complement network and use as link
    # removal prediction

    @staticmethod
    def preferential_attachment_inv_graph(graph):
        """
        Using the degree of the two nodes being connected by an edge, predict the probability of this edge to be removed.
        :param graph: input graph as adjacency matrix
        :return: adjacency matrix containing probabilities
        """
        result = []

        return result

    @staticmethod
    def common_neighbors_inv_graph(graph):
        """
        Using the neighborhood of the two nodes being connected by an edge, predict the probability of this edge to be
        removed.
        :param graph: input graph as adjacency matrix
        :return: adjacency matrix containing probabilities
        """
        result = []

        return result

    @staticmethod
    def cosine_similarity_inv_graph(graph):
        """
        Using the cosine similarity of the two nodes being connected by an edge, predict the probability of this edge
        to be removed.
        :param graph: input graph as adjacency matrix
        :return: adjacency matrix containing probabilities
        """
        result = []

        return result

    @staticmethod
    def jaccard_index_inv_graph(graph):
        """
        Using the jaccard index of the two nodes being connected by an edge, predict the probability of this edge to be
        removed.
        :param graph: input graph as adjacency matrix
        :return: adjacency matrix containing probabilities
        """
        result = []

        return result

    @staticmethod
    def adamic_adar_inv_graph(graph):
        """
        Using the methodology of Adamic and Adar predict the probability of all edges to be removed.
        :param graph: input graph as adjacency matrix
        :return: adjacency matrix containing probabilities
        """
        result = []

        return result
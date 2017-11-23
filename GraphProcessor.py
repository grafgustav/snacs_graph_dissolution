

class GraphProcessor:

    """
    Using only static methods this class offers functionality to process a graph according to the approaches in the
    paper.
    """

    # Complement score methods - Use link prediction functions on existing links and complement score
    @staticmethod
    def preferential_attachment(graph):
        """
        Using the degree of the two nodes being connected by an edge, predict the probability of this edge to be removed.
        :param graph: input graph as adjacency matrix
        :return: adjacency matrix containing probabilities
        """
        result = []

        return result

    @staticmethod
    def common_neighbors(graph):
        """
        Using the neighborhood of the two nodes being connected by an edge, predict the probability of this edge to be
        removed.
        :param graph: input graph as adjacency matrix
        :return: adjacency matrix containing probabilities
        """
        result = []

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
import networkx as nx
import time


class GraphComparator:
    """
    This class provides static functionality to compare two graphs. One example usage is to compare a predicted graph
    to a ground truth graph.
    """

    @staticmethod
    def compare_grahs(pred_graph, gt_graph):
        """
        Compares two graphs with the first one being the predicted graph. Returns the precision and recall values of
        left over edges.
        The nodes are expected to be the same set.
        :param pred_graph: first input graph
        :param gt_graph: second input graph
        :return: Precision, Recall
        """
        # condition not satisfied
        if nx.number_of_nodes(pred_graph) != nx.number_of_nodes(gt_graph):
            return -1, -1

        # count true positives
        true_positives = 0
        for source, target in pred_graph.edges:
            if gt_graph.has_edge(source, target):
                true_positives += 1

        # true positives divided by all positives
        precision = true_positives / nx.number_of_edges(pred_graph)
        # true positives divided by all possible true positives
        recall = true_positives / nx.number_of_edges(gt_graph)

        return precision, recall

    @staticmethod
    def compare_edge_lists(pred_edge_list, gt_edge_list, threshold):
        """
        Compare two edge lists of edges to be deleted.
        :param pred_edge_list: The predicted edge list
        :param gt_edge_list: The Ground Truth edge list
        :return: precision, recall
        """
        true_positives = 0
        set_list = set(gt_edge_list)
        scored_positives = [(source, target) for source, target, score in pred_edge_list if score <= threshold]
        for source, target in scored_positives:
            if (source, target) in set_list:
                true_positives += 1

        recall = true_positives / len(set_list)
        precision = true_positives / len(scored_positives)

        return precision, recall

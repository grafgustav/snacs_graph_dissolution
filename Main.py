# main file
from snacs_2017.snacs_graph_dissolution.WikipediaParser import WikipediaParser
from snacs_2017.snacs_graph_dissolution.GraphProcessor import GraphProcessor as gp
from snacs_2017.snacs_graph_dissolution.GraphComparator import GraphComparator as gc
from operator import itemgetter
import time
import numpy as np
import networkx as nx
import sys


WIKI_NL = "out.link-dynamic-nlwiki"
WIKI_SIMPLE = "out.link-dynamic-simplewiki"


def main_function():
    print("...Entering")
    wp = WikipediaParser(WIKI_NL, load=False)
    trainings_graph = wp.get_first_subgraph()
    gt_edges = wp.get_gt_edges()
    print("Trainings graph: %s edges, %s nodes"
          % (trainings_graph.number_of_edges(), trainings_graph.number_of_nodes()))
    print("%s edges to be deleted" % len(gt_edges))
    # edges decreased, nodes constant
    print("Starting graph processing operations")

    '''
    execute_tests("Preferential attachment", trainings_graph, gt_edges, gp.preferential_attachment)
    execute_tests("Common neighbors", trainings_graph, gt_edges, gp.common_neighbors)
    execute_tests("Cosine similarity", trainings_graph, gt_edges, gp.cosine_similarity)
    execute_tests("Jaccard index", trainings_graph, gt_edges, gp.jaccard_index)
    execute_tests("Adamic-Adar", trainings_graph, gt_edges, gp.adamic_adar)

    start_time = time.time()
    trainings_graph_inv_graph = nx.DiGraph(gp.get_complement_network(trainings_graph))
    print("Size of graph: %s" % sys.getsizeof(trainings_graph_inv_graph))
    print(time.time() - start_time)
    execute_tests("Preferential attachment_inv", trainings_graph_inv_graph, gt_edges, gp.preferential_attachment_inv_graph)
    execute_tests("Common neighbors_inv", trainings_graph_inv_graph, gt_edges, gp.common_neighbors_inv_graph)
    execute_tests("Cosine similarity_inv", trainings_graph_inv_graph, gt_edges, gp.cosine_similarity_inv_graph)
    execute_tests("Jaccard index_inv", trainings_graph_inv_graph, gt_edges, gp.jaccard_index_inv_graph)
    execute_tests("Adamic-Adar_inv", trainings_graph_inv_graph, gt_edges, gp.adamic_adar_inv_graph)
    '''
    execute_and_get_average_precision("Preferential attachment", trainings_graph, gt_edges, gp.preferential_attachment)
    execute_and_get_average_precision("Common neighbors", trainings_graph, gt_edges, gp.common_neighbors)
    execute_and_get_average_precision("Cosine similarity", trainings_graph, gt_edges, gp.cosine_similarity)
    execute_and_get_average_precision("Jaccard index", trainings_graph, gt_edges, gp.jaccard_index)
    execute_and_get_average_precision("Adamic-Adar", trainings_graph, gt_edges, gp.adamic_adar)

    start_time = time.time()
    trainings_graph_inv_graph = nx.DiGraph(gp.get_complement_network(trainings_graph))
    print("Size of graph: %s" % sys.getsizeof(trainings_graph_inv_graph))
    print(time.time() - start_time)
    execute_and_get_average_precision("Preferential attachment_inv", trainings_graph_inv_graph, gt_edges, gp.preferential_attachment_inv_graph)
    execute_and_get_average_precision("Common neighbors_inv", trainings_graph_inv_graph, gt_edges, gp.common_neighbors_inv_graph)
    execute_and_get_average_precision("Cosine similarity_inv", trainings_graph_inv_graph, gt_edges, gp.cosine_similarity_inv_graph)
    execute_and_get_average_precision("Jaccard index_inv", trainings_graph_inv_graph, gt_edges, gp.jaccard_index_inv_graph)
    execute_and_get_average_precision("Adamic-Adar_inv", trainings_graph_inv_graph, gt_edges, gp.adamic_adar_inv_graph)

    print("Exiting...")


def execute_tests(name, trainings_graph, gt_edges, func):
    start_time = time.time()

    print("Calculating %s" % name)
    pred_edge_list = func(trainings_graph)
    best_threshold = -1
    best_precision = -1
    best_recall = -1
    best_f_measure = -1
    min_score = min(pred_edge_list, key=itemgetter(2))[2]
    max_score = max(pred_edge_list, key=itemgetter(2))[2]
    step = abs((min_score - max_score) / 500)
    for i in np.arange(min_score, max_score, step):
        precision, recall = gc.compare_edge_lists(pred_edge_list, gt_edges, threshold=i)
        f_measure = (2 * precision * recall) / (precision + recall)
        if (f_measure > best_f_measure) & ((precision + recall) != 0):
            best_f_measure = f_measure
            best_precision = precision
            best_recall = recall
            best_threshold = i

    print("%s scores with threshold %s: Precision: %s; Recall: %s; F-Measure: %s"
          % (name, best_threshold, best_precision, best_recall, best_f_measure))
    print("%s calculations took %s seconds" % (name, time.time() - start_time))


def execute_and_get_average_precision(name, training, gt, func):
    start_time = time.time()

    print("Calculating %s" % name)
    pred_edge_list = func(training)
    avg_precision = gc.calculate_average_precision(gt, nx.edges(training), pred_edge_list)

    print("%s scores an average precision of %s in %s seconds" % (name, avg_precision, time.time() - start_time))
    return avg_precision


if __name__ == '__main__':
    main_function()

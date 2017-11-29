# main file
from snacs_2017.snacs_graph_dissolution.WikipediaParser import WikipediaParser
from snacs_2017.snacs_graph_dissolution.GraphProcessor import GraphProcessor as gp
from snacs_2017.snacs_graph_dissolution.GraphComparator import GraphComparator as gc
from operator import itemgetter
import math
import time
import numpy as np


def main_function():
    print("...Entering")
    wp = WikipediaParser("out.link-dynamic-simplewiki", load=True)
    trainings_graph = wp.get_first_subgraph()
    gt_edges = wp.get_gt_edges()
    print("Trainings graph: %s edges, %s nodes"
          % (trainings_graph.number_of_edges(), trainings_graph.number_of_nodes()))
    print("%s edges to be deleted" % len(gt_edges))
    # edges decreased, nodes constant
    print("Starting graph processing operations")

    # execute_tests("Preferential attachment", trainings_graph, gt_edges, gp.preferential_attachment)
    # execute_tests("Common neighbors", trainings_graph, gt_edges, gp.common_neighbors)
    # execute_tests("Cosine similarity", trainings_graph, gt_edges, gp.cosine_similarity)
    # execute_tests("Jaccard index", trainings_graph, gt_edges, gp.jaccard_index)
    execute_tests()

    start_time = time.time()
    gp.get_complement_network(trainings_graph)
    print("Complementing the network took %s seconds." % (time.time() - start_time))

    print("Exiting...")


def execute_tests(name, trainings_graph, gt_edges, func):
    FALPHA = 0.5
    FBETA = 1-FALPHA

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
        f_measure = FALPHA * precision + FBETA * recall
        if (f_measure > best_f_measure) & (precision != 1):
            best_f_measure = f_measure
            best_precision = precision
            best_recall = recall
            best_threshold = i

    print("%s scores with threshold %s: Precision: %s; Recall: %s; F-Measure: %s"
          % (name, best_threshold, best_precision, best_recall, best_f_measure))
    print("%s calculations took %s seconds" % (name, time.time() - start_time))


if __name__ == '__main__':
    main_function()

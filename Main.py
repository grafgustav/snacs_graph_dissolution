# main file
from snacs_2017.snacs_graph_dissolution.WikipediaParser import WikipediaParser
from snacs_2017.snacs_graph_dissolution.GraphProcessor import GraphProcessor as gp
from snacs_2017.snacs_graph_dissolution.GraphComparator import GraphComparator as gc


def main_function():
    print("...Entering")
    wp = WikipediaParser("out.link-dynamic-simplewiki", load=True)
    trainings_graph = wp.get_first_subgraph()
    gt_edges = wp.get_gt_edges()
    print(
        "Trainings graph: %s edges, %s nodes" % (trainings_graph.number_of_edges(), trainings_graph.number_of_nodes()))
    print("%s edges to be deleted" % len(gt_edges))
    # edges decreased, nodes constant
    print("Starting graph processing operations")
    pred_edge_list = gp.preferential_attachment(trainings_graph)
    print("Calculating first score")
    for i in range(4870, 4900, 1):
        precision, recall = gc.compare_edge_lists(pred_edge_list, gt_edges, threshold=i*(-1))
        print("Preferential Attachment scores: Precision: %s; Recall: %s" % (precision, recall))
    print("Exiting...")


if __name__ == '__main__':
    main_function()

# main file
from snacs_2017.snacs_graph_dissolution.WikipediaParser import WikipediaParser
from snacs_2017.snacs_graph_dissolution.GraphProcessor import GraphProcessor as gp
from snacs_2017.snacs_graph_dissolution.GraphComparator import GraphComparator as gc


def main_function():
    print("...Entering")
    wp = WikipediaParser("out.link-dynamic-simplewiki")
    trainings_graph = wp.get_first_subgraph()
    groundtruth_graph = wp.get_second_subgraph()
    print(
        "Trainings graph: %s edges, %s nodes" % (trainings_graph.number_of_edges(), trainings_graph.number_of_nodes()))
    print(
        "GT graph: %s edges, %s nodes" % (groundtruth_graph.number_of_edges(), groundtruth_graph.number_of_nodes()))
    # edges decreased, nodes constant
    print("Starting graph processing operations")
    pred_edge_list = gp.preferential_attachment(trainings_graph)
    print(pred_edge_list)
    pred_graph = gp.transform_scored_edge_list_to_graph(pred_edge_list, trainings_graph, threshold=-1000)
    precision, recall = gc.compare_grahs(pred_graph, groundtruth_graph)
    print("Preferential Attachment scores: Precision: %s; Recall: %s" % (precision, recall))
    print("Exiting...")


if __name__ == '__main__':
    main_function()

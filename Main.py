# main file
from snacs_2017.snacs_graph_dissolution.WikipediaParser import WikipediaParser
import networkx as nx


def main_function():
    print("Begin processing")
    wp = WikipediaParser("out.link-dynamic-simplewiki")
    graph = wp.get_graph()

if __name__ == '__main__':
    main_function()
# write tests for bfs
import pytest
import networkx as nx
from search.graph import Graph

@pytest.fixture
def tiny_network():
    return nx.read_adjlist("data/tiny_network.adjlist", create_using=nx.DiGraph, delimiter=";")

def test_bfs_traversal(tiny_network):
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """

    # identify number of nodes in network
    total_nodes = tiny_network.number_of_nodes()

    # create instance of Graph using the tiny network and a version of BFS starting at Atul Butte with no end provided
    tiny_graph_instance = Graph("data/tiny_network.adjlist")
    butte_start = tiny_graph_instance.bfs('Atul Butte')
    butte_total_nodes = len(butte_start)

    # determine that the correct number of nodes are being returned
    correct_num_nodes = total_nodes==butte_total_nodes

    # determines correct order
    correct_order = butte_start == ['Atul Butte', '33765435', '33242416', '31395880', '30944313', 'Marina Sirota', 'Steven Altschuler', 'Lani Wu', 'Hani Goodarzi', 'Nevan Krogan', '31486345', '32036252', '32042149', '31806696', '30727954', '33232663', '34272374', '32353859', 'Michael Keiser', 'Luke Gilbert', 'Michael McManus', 'Charles Chiu', 'Martin Kampmann', '33483487', '31626775', '31540829', '32025019', '29700475', '32790644', 'Neil Risch']

    assert correct_num_nodes and correct_order

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    pass

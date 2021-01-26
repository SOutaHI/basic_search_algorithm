import sys

# explict "import" method
# sys.path.append('../src')
# from depth_first_search import DepthFirstSearch

# non-explict "import" method
sys.path.append('../')
from src import *


if __name__ == '__main__':

    # create graph for search 
    graph        = CreateGraph()
    search_graph = graph.get_graph()
    print(search_graph)

    # create instances of each search method
    # Depth First Search
    dfs_method = DepthFirstSearch(search_graph)
    dfs_method.exploration()
    print(dfs_method.get_closed_list())
    
    # Breadth First Search
    # bfs_method  = BreadthFirstSearch()
    # bfs_method.exploration()
    # print(bfs_method.get_closed_list) 
    
    # os_method   = OptimalSearch()
    # befs_method = BestFirstSearch()
    # assa_method = AStarSearchAlgorithm()
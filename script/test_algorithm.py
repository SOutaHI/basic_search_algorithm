import math
import sys

# explict "import" method
# sys.path.append('../src')
# from depth_first_search import DepthFirstSearch

# non-explict "import" method
sys.path.append('../')
from src import *


if __name__ == '__main__':

    # create graph for search 
    graph = CreateGraph()

    # create instances of each search method
    dfs_method  = DepthFirstSearch()
    bfs_method  = BreadthFirstSearch()
    os_method   = OptimalSearch()
    befs_method = BestFirstSearch()
    assa_method = AStarSearchAlgorithm()
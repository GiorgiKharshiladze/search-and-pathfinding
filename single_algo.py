from implement import *

def dfs_paths(graph, start, goal, path = None):
    
    if path is None:

        path = [start]

    if start == goal:

        return path

    for next in graph[start] - set(path):
    	
        yield from dfs_paths(graph, next, goal, path + [next])
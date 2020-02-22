'''
    Graphs module:
            1. Graph calculator
            2.
        By : Sina Honarvar
            ''' 


from collections import deque
from matrix import Matrix


#_________________________________________________
'''
def is_simple_graph(adj_matrix):
    'Returns True if the given matrix can be adjacency matrix of a simple graph'
    mat = adj_matrix.matrix
    for i in range(len(mat)):
        if mat[i][i] == 1:
            return False
        for j in range(i+1,len(mat)):
            if mat[i][j] not in {0,1} or mat[i][j] != mat[j][i]:
                return False
    return True
'''
#_________________________________________________
def havel(series):
    'returns degree list of vertices after perofrming Havel alghorithm'
    delta = series.pop(0)
    for i in range(delta):
        series[i] -= 1
    return series
#_________________________________________________

    
        
                
class Graph:
    '''
    simple tool for graph theory calculations
    '''
    #_________________________________________________
    def __init__(self, graph):
        '''
        Base constructor for Graph class
        We assume that given matrix belongs to a simple graph
        '''
        assert len(graph.matrix) == len(graph.matrix[0]), (print("Input data is not a square matrix"))
        if not isinstance(graph, Matrix) and isinstance(graph , list):
            graph = Matrix (graph)
            self.graph = graph
        elif isinstance(graph, Matrix):
            self.graph = graph
        else:
            assert 0 , print("input data is not list or matrix")

        self.max_deg = max(self.series())
        self.min_deg = min(self.series())
        self.q = sum(self.series())//2

    #_________________________________________________  
    def series(self):
        'Retruns the series of vertices degree in a descending sort'
        return [(self.graph * self.graph)[i][i] for i in range(len(self.graph.matrix))]
    #_________________________________________________  
    def distance(self, v, t):
        'Returns distance between two vertices'
        q = deque([v])
        d = [-1] * len(self.graph.matrix)
        d[v] = 0
        while q:
            u = q.popleft()
            for i in range(len(self.graph.matrix)):
                if self.graph.matrix[u][i] and d[i] == -1:
                    d[i] = d[u] + 1
                    q.append(i)
        return d[t]
    #_________________________________________________
      

    

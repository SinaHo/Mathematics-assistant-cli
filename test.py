''' 
    Matrix fast calculator ///////////////////////////////////////////
         Current facilities:
              1. Matrix addition
              2. Matrix multiplacation
              3. Inverse matrix  -2*2 matrix is supported only-
              4. Matrix transpose
              5. Adjacency matrix  -Graph theory-
        'CREATED BY :
                    SINA HONARVAR   September 2017'
                    
                    '''



import json
import math 
from matrix import Matrix
from graph import Graph
# import all local mudoles

lis1=[[1,2,3],
     [2,4,5],
     [1,4,5]]

lis2=[[0,7,3],
     [2,9,4],
     [1,0,5]]

mat1=Matrix(lis1)
mat2=Matrix(lis2)


lis3=[
    [0,1,1,1],
    [1,0,0,1],
    [1,0,0,1],
    [1,1,1,0]
]
mat3=Matrix(lis3)

g1=Graph(mat3)

print(g1.series())
print(g1.distance(1,2))








'''Matrix Module :
            base Matrix Class and basic matrix operations
            '''

# import math


class Matrix:
    '''Matrix Creation and basic operation Class'''
#---------------------------------------------------
    def __init__(self, listed_matrix):
        '''Class constructor : Creates a matrix object'''
        assert (isinstance(listed_matrix, list)), (
            'Given parameter must be List , got {}'.format(type(listed_matrix)))
        try:
            for i in range(len(listed_matrix)-1):
                assert (len(listed_matrix[i]) == len(listed_matrix[i+1])), (
                    ("Length Error: \n length of rows in given list-matrix- are not same \n index of row with Error: {} 0-based".format(str(i+1)))
                )
        except TypeError:
            print("Given parameter is not a two dimensional list ")
            raise TypeError
        self.matrix = listed_matrix

#---------------------------------------------------
    def __repr__(self):
        object_data = ''
        for row in self.matrix:
            object_data += str(row)+'\n'
        return object_data

#---------------------------------------------------   
    def columns(self):
        '''returns columns of matrix in a list object
                NOTE: equals with matrix TRANSPOSE'''
        cols = []
        for i in range(len(self.matrix[0])):
            col = []
            for elem in self.matrix:
                col.append(elem[i])
            cols.append(col)
        return cols

#--------------------------------------------------
    def add(self, mat):
        '''Add function :
                Adds given matrix elements to corresponding elements in self
                Raises IndexError if matrix dimensions are not same'''
        if not isinstance(mat, Matrix):
            mat = Matrix(mat)
        assert (
            len(self.matrix) == len(mat.matrix) and len(self.matrix[0]) == len(mat.matrix[0]) 
        ), (
            ('''Matrix dimensions are not same
                     base matrix :[{0}][{1}]
                     additional matrix :[{2}][{3}]'''.format(len(self.matrix), 
                     len(self.matrix[0]), len(mat.matrix), len(mat.matrix[0])))
        )
        
        #temp = [[0]*len(self.matrix[0])]*len(self.matrix)
        temp = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] + mat.matrix[i][j])
            temp.append(row)
        return temp
#---------------------------------------------------
## overloading add maethod in __add__ for '+' operator
# 
    def __add__(self, second):
        'same as .add() function executed when "+" operator is used'
        # Some Exception Handlings Needed
        return self.add(second)

#---------------------------------------------------
    def product(self, mat):
        '''Multiplies two given matrices:
                    'self' in left and 'mat' in right 
                    'self'*'mat'
                    '''
        if not isinstance(mat, Matrix):
            mat = Matrix(mat)
        assert (len(self.matrix[0]) == len(mat.matrix)), (
            ('Length Error : \n number of columns in first matrix -got {}- must be equal with number of rows in second -got {}-'.format(len(self.matrix[0]), len(mat.matrix)) )
        )
        l = len(mat.matrix)
        #prod = [[0]*len(mat.matrix)]*len(self.matrix)
        prod = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(mat.matrix[0])):
                elem = 0
                for k in range(l):
                    elem += (self.matrix[i][k] * mat.matrix[k][j])
                row.append(elem)
            prod.append(row)
        return prod
#---------------------------------------------------
## overloading multiply maethod in __mul__ for '*' operator
#
    def __mul__(self, second):
        'same as .product() function executed when "*" operator is used'
        return self.product(second)

#---------------------------------------------------
    def det_twobytwo(self):
        'returns the determinan of a 2*2 matrix'
        assert (len(self.matrix) == 2 and len(self.matrix[0]) == 2), (
            ("This Function can only calculate inverse of 2*2 matrices ")
        )
        return self.matrix[0][0]*self.matrix[1][1] - self.matrix[1][0]*self.matrix[0][1]
#---------------------------------------------------

    def multiply_by(self, num):
        'Multiplies a number in all elements in matrix and returns new matrix'
        temp_mat = []
        for row in self.matrix:
            temp_row = []
            for elem in row:
                temp_row.append(num * elem)
            temp_mat.append(temp_row)
        return temp_mat
#---------------------------------------------------

    def inverse_two_by_two(self):
        'Returns Matrix inverse for 2*2 matrices'
        assert (len(self.matrix) == 2 and len(self.matrix[0]) == 2), (
            ("This Function can only calculate inverse of 2*2 matrices ")
        )
        if self.det_twobytwo() == 0:
            print('Matrix is not inversable')
            return 0
        temp = [
            [self.matrix[1][1], -self.matrix[0][1]],
            [-self.matrix[1][0], self.matrix[0][0]]
        ]

        return Matrix(temp).multiply_by(1/(self.det_twobytwo()))
#---------------------------------------------------

''' Matrix assistant Interface //// 
NOTE: Only CommandLine Interface supported , NO GUI!!
'''

# _______________________________
import os
import time
import sys

from matrix import Matrix
from graph import Graph
# _______________________________
BASE_COMMANDS = [
    "new", "help", "quit", "again", "prev",
    "matrix", "graph",
    "operation"
]



# _______________________________
class Use:
    '''
    Use Class :
    creates an object with every user and saves history
    '''
    # _______________________________
    def __init__(self):
        '''
        initializes CLI for user
        ''' 
        self.START_TIME = time.ctime(time.time()).replace(":","-")
        
        os.chdir("history")
        os.mkdir("{}".format(self.START_TIME))
        os.chdir("..")
        self.history_path = "history/{}/".format(self.START_TIME)
        
        self.commands = []
        self.step = None
        self.data = {} 
    # _______________________________
    def get_command(self, text):
        'Gets user command with given text as command line input '
        command = input(text).lower()
        self.commands.append(command)
        with open(self.history_path+"Commands.log",'a+') as com_log:
            com_log.write(command+"\n")
            com_log.close()
        if command == "quit":
            print("Goodbye..")
            sys.exit()
        return command
    # _______________________________
    def interpret(self, command):
        'interprets every command'
        if command == "new":
            self.step = None 
            self.start_new()
        elif command == "operation":
            self.step = "operation"
            print("Available variables :...\n\n\n\n")
            print(self.data)
            stat = self.eval_operation()
            while stat == "again":
                stat = self.eval_operation()
        elif command == "data":
            self.print_data()
            
    # _______________________________
    def get_matrix(self):
        'Gets user matrix element by element'
        name = self.get_command("Enter a name for Matrix like 'mat1'\n")
        input_data = self.get_command("Enter number of 'rows','columns'\n")
        row, col = int(input_data.split(",")[0]), int(input_data.split(",")[1])
        lis = []
        for i in range(row):
            temp = [0] * col
            j = 0
            while j < col:
                command = self.get_command(
                    "Enter element in {}th row , {}th column\n".format(str(i+1), str(j+1)))

                while command == "prev":
                    j -= 1
                    command = self.get_command(
                        "Enter element in {}th row , {}th column\n".format(str(i+1), str(j+1)))

                if command == "again":
                    return "again" 
                temp[j] = command
                j += 1
            lis.append(temp)
        matrix = Matrix(lis)
        self.data.update({name:matrix})
        return "done"
    # _______________________________
    def get_graph(self):
        'Gets user graph with same approach as matrix'
        name = self.get_command("Enter a name for Graph like 'g1'\n")
        vers = self.get_command("Enter number of 'vertices'\n") # number of vertices
        lis = []
        for i in range(vers):
            temp = [0] * vers
            for j in range(vers):
                command = self.get_command(
                    "Enter element in {}th row , {}th column\n".format(str(i+1), str(j+1)))
                if command == "prev":
                    j -= 1
                elif command == "again":
                    return "again" 
                temp[j] = command
            lis.append(temp)
        graph = Graph(Matrix(lis))
        self.data.update({name:graph})
        return "done"
    # _______________________________
    def start_new(self):
        'Starts new session'
        print("New session started:...\n\n")
        data_type = self.get_command("Enter 'matrix' or 'graph' to determine a new one\n")
        while data_type not in {"matrix", "graph"}:
            data_type = self.get_command("Wrong input !..\nEnter 'matrix' or 'graph'\n")
        if data_type == "matrix":
            self.step = "matrix"
            stat = self.get_matrix()
            while stat == "again":
                stat = self.get_matrix()
        elif data_type == "graph":
            self.step = "graph"
            stat = self.get_graph()
            while stat == "again":
                stat = self.get_graph()
    # _______________________________
    def eval_operation(self):
        'Evaluates user operations'
        print("""You can use these operations:
            A. Matrix:
                 1. 'mat1' + 'mat2' - Adds two matrices 
                 2. 'mat1' * 'mat2' - Multiplies two matrices
                 3. 'mat1'.T        - Prints Matrix Transpose
                 4. 'mat1'.R        - Prints Reversed Matrix 
            B. Graph:
            """)
    # _______________________________
    def print_data(self):
        'Prints user defined data in a human readable form'
        print("\n--------------------------------------\n---->{")
        for item in self.data.keys():
            print(item+" :")
            print(repr(self.data[item])+"-------")
        print("}<----\n--------------------------------------")
    # _______________________________



def use():
    'Controls whole interaction with user'
    this = Use()
    print("Hello...\nWelcome to school assistant graph calculator. \n  Enter 'help' to get more information\n")
    while True:
        try:
            data = this.get_command("Enter new or data or operation \n\n")
            this.interpret(data)
        except KeyboardInterrupt as ki_e:
            print("Goodbye...")
            sys.exit()
            raise ki_e
        except Exception as exeption:
            print(exeption)
        else:
            print("Session completed without problem!\nStarting a new one")

            
            
    

if __name__ == '__main__':
    use()

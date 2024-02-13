""" DFS by danhs V.0
"""
import sys

sys.setrecursionlimit(10 ** 6) # Changing recursivity in Python, Python default value (10**4)

numberNodes = 2500

fileNodes="sample.txt"

def null(nNodes):

    zeros = []

    for i in range (nNodes):

        zeros.append(float(0))

    return zeros

class node:
    def __init__(self, id, posx, posy):

        self.id = id
        self.posx = posx
        self.posy = posy
        self.distanceVector = null(numberNodes)
        self.neighbor = {}
        self.order = []
        self.children = []

    def distance(self, xAnotherNode, yAnotherNode , id):

        x = (xAnotherNode - self.posx) ** 2
        y = (yAnotherNode - self.posy) ** 2
        distance = (x + y) ** .5

        if id == self.id:

            self.distanceVector[id - 1] = -1000

        else:

            self.distanceVector[id - 1] = distance

            if distance < 100:

                self.neighbor.update({str(id):distance})

    def info(self):

        print("Number of node: ", self.id)

        print("x position: ", self.posx)

        print("y position: ", self.posy)

        print("Distance Vector: ", self.distanceVector)

        print("Neighbor vector: ", self.neighbor)

    def sortFunction(self,choice):
        
        sortVector=[]

        if choice == '1':

            aux = list(self.neighbor.items())
            
            for i in self.neighbor:

                sortVector.append(self.neighbor[i])

            sortVector.sort()

            for j in range(0,len(sortVector)):

                for k in range(0, len(aux)):

                    if sortVector[j] == aux[k][1]:

                        self.order.append(aux[k][0])

        if choice == '2':

            self.order = list(self.neighbor.keys())

        if choice == '3':

            aux = list(self.neighbor.keys())

            aux.reverse()

            self.order=aux

        if choice == '4':

            aux = list(self.neighbor.items())

            for i in self.neighbor:

                sortVector.append(self.neighbor[i])

            sortVector.sort()

            sortVector.reverse()

            for j in range(0, len(sortVector)):

                for i in range(0, len(aux), 1):

                    if sortVector[j] == aux[i][1]:

                        self.order.append(aux[i][0])

class description:
    def __init__(self):

        self.route = []
        self.branch = []
        self.leaves = []
        self.count = 0
        self.previous = 0

    def start(self):
        for i in range(0,numberNodes):

            self.branch.append([])
    



'''___________________________________Handled data from TXT file_________________________________________
'''
files = open(fileNodes, "r") 

vectorNode = []                     

for line in files.readlines():

    cleanLine = line.replace(":(",",")

    secondCleanLine = cleanLine.replace(")",",")

    valuesList = secondCleanLine.split(",")

    vectorNode.append(node(int(valuesList[0]),float(valuesList[1]),float(valuesList[2])))

files.close()  

'''__________________________________________Develop Graph______________________________________________________
'''

Graph = {}

print("\n\n DFS Algorithm")
print("\n \n \t Order \n")
print("1. Minimum Euclidean distance")
print("2. Minimum identifier")
print("3. Maximum identifier")
print("4. Maximum Euclidean distance")
print("5. Exit")
print("\n\nChoice:")

option = input()

while True:
    if abs(int(option)) > 5 or abs(int(option)) == 0:
        print("\n \t Wrong option, please chose again. \n")
        print("Choice:")
        option = input()
    else:
        if int(option) == 5:
            sys.exit()
        break


for i in range(0, len(vectorNode)):

    for j in range(0, len(vectorNode)):

        vectorNode[i].distance(vectorNode[j].posx, vectorNode[j].posy, vectorNode[j].id)
        
    vectorNode[i].sortFunction(option)

    Graph.update({str(i + 1): vectorNode[i].order})

print(Graph)


'''___________________________________________Develop DFS ____________________________________________
'''


graphDescription = description()

conditionalList = []


for i in range(0,numberNodes):

    conditionalList.append(False)


def dfs(rootNode):

    if conditionalList[int(rootNode)- 1 ] == True:

        return
    

    else:

        graphDescription.route.append(rootNode)

        graphDescription.branch[graphDescription.count].append(rootNode)

        conditionalList[int(rootNode) - 1] = True

        neighborsNodes = Graph[rootNode]

        graphDescription.previous=rootNode


        for nextNode in neighborsNodes:

            if conditionalList[int(nextNode) - 1] == False:

                vectorNode[int(rootNode) - 1].children.append(int(nextNode))

            dfs(nextNode)


        if len(graphDescription.branch[graphDescription.count]) > 0:

            graphDescription.leaves.append(int(rootNode))

            graphDescription.count = graphDescription.count+1



print("\n\nInitial Node (root)")
print("\n\nChoice:")
startNode = input()

while True:
    if abs(int(startNode)) > numberNodes or abs(int(startNode)) == 0:
        print("\n \t Wrong option, please chose again. \n")
        print("Choice:")
        startNode = input()
    else:
        break

graphDescription.start()

dfs(startNode) #Starting DFS


print("\nRoute: ",graphDescription.route)
print("\nLeaves: ",graphDescription.leaves)

orderLeaves=graphDescription.leaves
orderLeaves.sort()

print("Order Leaves: ",orderLeaves)
print("Number of leaves: ",len(graphDescription.leaves))

print("Choice for Node with more children\n 1. Minimum identifier o 2. Maximum identifier ")
print("\nChose 1 or 2 :")

selector = input()

while True:
    if abs(int(selector)) > 3 or abs(int(selector)) == 0:
        print("\n \t Wrong option, please chose again. \n")
        print("Choice:")
        selector = input()
    else:
        break


ChildrenListValue = []
NodeMoreChildren = 0

for x in range(0,len(vectorNode)):

    ChildrenListValue.append(len(vectorNode[x].children))

    if len(vectorNode[x].children) > 1:

        NodeMoreChildren = NodeMoreChildren + 1


maximumValue = max(ChildrenListValue)

idNodeList = []

for x in range(0, len(vectorNode)):

    if len(vectorNode[x].children) == maximumValue:

        idNodeList.append(vectorNode[x].id)

if selector == '1':

    valueOption = min(idNodeList)

if selector == '2':

    valueOption = max(idNodeList)


print("Node with more children: ",valueOption)
print("Nodes with more than 1 child: ",NodeMoreChildren)

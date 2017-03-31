import AstarTest
from AstarTest import UnitTest
class Node(object):
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.gscore = 0
        self.hscore = 0
        self.fscore = 0
        self.parent = None

    def CalGscore(self, node):
        tentativeg = 0
        if(node.xpos == self.xpos or node.ypos == self.ypos):
            tentativeg = 10
        else: 
            tentativeg = 14
        if self.parent is None:
            self.gscore = tentativeg
            self.parent = node
        else:
            if tentativeg < self.gscore:
                self.gscore = tentativeg
                self.parent = node
                
    def calhscore(self, goal):
        xdif = abs(goal.xpos - self.xpos)
        ydif = abs(goal.ypos - self.ypos)
        self.hscore = 10 * (xdif + ydif)

    def calfscore(self):
        self.fscore = self.gscore + self.hscore

    def GetNeighbors(self, graph):
        neighbors = []
        right = [1, 0]
        topright = [1, 1]
        top = [0, 1]
        topleft = [-1, 1]
        left = [-1, 0]
        bottomleft = [-1, -1]
        bottom = [0, -1]
        bottomright = [1, -1]
        dirs = [right, topright, top, topleft,
                left, bottomleft, bottom, bottomright]
        for node in graph.nodes:
            for i in dirs:
                if node.xpos == self.xpos + i[0] and node.ypos == self.ypos + i[1]:
                    neighbors.append(node)
        return neighbors

    @staticmethod
    def compare(rhs, lhs):
        return rhs.xpos == lhs.xpos and rhs.ypos == lhs.ypos

class Graph(object):
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.nodes = []
        

    def gengraph(self):
        for row in range(0, self.width):
            for col in range(0, self.height):
                self.nodes.append(Node(row, col))

    def printnodes(self):
        for i in range(0, len(self.nodes)):
            print self.nodes[i]
            if i % self.width == 0:
                print "\n"

    def getnode(self, node):
        for graphnode in self.nodes:
            if Node.compare(node, graphnode):
                return graphnode

    def Retrace(self, end):
        retraced = []
        currentNode = end
        while currentNode.parent is not None:
            retraced.append(currentNode)
            currentNode = currentNode.parent
        return retraced


class Astar(object):
    def __init__(self, start, goal, graph):
        self.openList = []  
        self.closedList = []
        self.startNode = start
        self.goalNode = goal
        self.graph = graph

    def algorithm(self, start, goal, environment):
        currentNode = start
        self.openList.append(currentNode)
        while currentNode is not goal:
            self.openList.sort(key=lambda x: x.fscore)
            currentNode = self.openList[0]
            if currentNode is goal:
                environment.Retrace(goal)
            self.openList.remove(currentNode)
            self.closedList.append(currentNode)
            for node in currentNode.GetNeighbors(environment):
                if node in self.closedList:
                    continue
                if node not in self.openList:
                    self.openList.append(node)

            for node in self.openList:
                node.CalGscore(currentNode)
                node.calhscore(goal)
                node.calfscore()

           
           
    def SortList(self):
        for i in range(0, len(graph.nodes)):
            for j in range(0, len(graph.nodes)):
                if graph.nodes[i].fscore < graph.nodes[j].fscore:
                    temp = graph.nodes[j]
                    graph.nodes[j] = graph.nodes[i]
                    graph.nodes[i] = temp
                    

    
        
graph = Graph(5, 5)
graph.gengraph()
temp = graph.getnode(Node(0,0))
algo = Astar(graph.nodes[0], graph.nodes[24], graph)
algo.algorithm(0,0,0)
test = UnitTest("test.txt")
test.gentestcases()
a = test.testastar(algo.algorithm)

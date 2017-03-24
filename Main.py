class Node(object):
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.gscore = 0
        self.hscore = 0
        self.fscore = 0
    def CalGscore(self, node):
        if(node.xpos == self.xpos or node.ypos == self.ypos):
            self.gscore = 10
        else: 
            self.gscore = 14
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


graph = Graph(5, 5)
graph.gengraph()
temp = graph.getnode(Node(0,0))


print str(temp.xpos) + "," + str(temp.ypos)
for node in temp.GetNeighbors(graph):
    print node.xpos, node.ypos

class Astar(object):
    def __init__(self, start, goal, graph):
        self.openList = []  
        self.closedList = []
        self.startNode = start
        self.goalNode = goal
        self.graph = graph

    def algorithm(self):
        currentNode = startNode
        self.openList.append(self.startNode)
        while self.goalNode not in self.closedList:
            self.openList.remove(currentNode)
            self.closedList.append(currentNode)
    
    def SortList(self):
        for i in range(0, len(graph.nodes)):
            for j in range(0, len(graph.nodes)):
                if(graph.nodes[i].fscore <= graph.nodes[j].fscore):
                    temp = graph.nodes[i]
                    graph.nodes[i] = graph.nodes[j]
                    graph.nodes[j] = temp
                    

        
        

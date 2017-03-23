class Node(object):
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
    
    def GetNeighbors(self, graph):
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
          for i in dirs:
            for node in graph.nodes:
                if node.xpos[0] == self.xpos[0] + i[0] and node.ypos[1] == self.ypos[1] + i[1]:
                    self.GetNeighbors.append(Node)

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
        
        

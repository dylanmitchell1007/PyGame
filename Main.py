import AstarTest
from AstarTest import UnitTest

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


    def Retrace(self, end):
        retraced = []
        currentNode = end
        while currentNode.parent is not None:
            retraced.append(currentNode)
            currentNode = currentNode.parent
        return retraced
    def SortList(self):
        for i in range(0, len(graph.nodes)):
            for j in range(0, len(graph.nodes)):
                if graph.nodes[i].f < graph.nodes[j].f:
                    temp = graph.nodes[j]
                    graph.nodes[j] = graph.nodes[i]
                    graph.nodes[i] = temp
def algorithm(start, goal, environment):
        openList = []
        closedList = []
        startNode = start
        goalNode = goal
        currentNode = start
        openList.append(currentNode)
        while currentNode is not goal:
            openList.sort(key=lambda x: x.f)
            currentNode = openList[0]
            if currentNode is goal:
                environment.Retrace(goal)
            openList.remove(currentNode)
            closedList.append(currentNode)
            for node in GetNeighbors(environment):
                if node in closedList:
                    continue
                if node not in openList:
                    openList.append(node)

            for node in openList:
                node.CalGscore(currentNode)
                node.calhscore(goal)
                node.calfscore()
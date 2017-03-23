class Node(object):
    def __init__(self, value, identifier, pos):
        self.__value = value
        self.__identifier = identifier
        self.visited = False
        self.neighbors = []
        self.pos = pos
        

    def set_neighbors(self, graph):
        '''set neighbors for a node'''
        right = [1, 0]
        top_right = [1, 1]
        top = [0, 1]
        top_left = [-1, 1]
        left = [-1, 0]
        bottom_left = [-1, -1]
        bottom = [0, -1]
        bottom_right = [1, -1]
        dirs = [right, top_right, top, top_left,
                left, bottom_left, bottom, bottom_right]
        for i in dirs:
            for node in graph.nodes:
                if node.pos[0] == self.pos[0] + i[0] and node.pos[1] == self.pos[1] + i[1]:
                    self.neighbors.append(node)

    def neighbors(self):
        return self.neighbors

    @property
    def value(self):
        return self.__value

    @property
    def identifier(self):
        '''id'''
        return self.__identifier


class Graph(object):
    def __init__(self, height, width):
        self.nodes = []
        self.nodelist = []
        self.height = height
        self.width = width
        self.rows = 5
        self.cols = 5
        for i in range(0, height):
            for j in range(0, width):
                self.nodelist.append(Node([i, j]))
        for node in self.nodelist:
            node.graph_index = self.nodelist.index(node)
            node.set_neighbors(self)


def test_nodes(self):
    '''test the nodes'''
    graph = Graph([5, 5])
    node = get_node(2, graph)
    node.print_info()
    neighbors = get_neighbors(node, graph)
    for nod in neighbors:
        nod.print_info()


if __name__ == '__main__':
    test_nodes()


def start_game():
    '''init game'''
    pygame.init()
    pygame.display.set_mode((500, 500))
    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.Running = False
                if event.type == pygame.QUIT:
                    self.Running = False
    pygame.quit()

import pygame
from Main import Node
from Main import Graph


class Aapp:

    def __init__(self):
        self.Pygame = pygame
        self.graph = Graph(15, 15)

    def run(self):
        while not False:
            for event in self.Pygame.event.get():
                if event.type == self.Pygame.QUIT:
                    return False

            # Draw here
            self.draw()
            # Update
            self.Pygame.display.flip()
        self.Pygame.quit()

    def start(self, x, y):
        self.screen = self.Pygame.display.set_mode((x, y))
        self.XYBounds = (x, y)
        self.graph.gengraph()

    def draw(self):
        BLACK = (0,   0,   0)
        WHITE = (255, 255, 255)
        BLUE = (0,   0, 255)
        GREEN = (0, 255,   0)
        RED = (255,   0,   0)
        self.screen.fill(BLACK)
        offset = 35
        self.ScreenEnd = offset + (self.graph.width * offset)
        x = offset
        y = self.XYBounds[1] - offset
        

        # Nodea = self.graph.nodes[0]
        # apos = (Nodea.xpos, Nodea.ypos)
        # print apos
        for node in self.graph.nodes:
            pygame.draw.circle(self.screen, BLUE, [x,y], 10)
            x += offset
            if x == self.ScreenEnd:
                x = offset
                y -= offset
            self.graph.getnode(0, 0); 
app = Aapp()
app.start(600, 600)
app.run()

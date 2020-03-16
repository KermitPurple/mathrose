import pygame
from numpy import sin, cos

class Rose:
    
    def __init__(self, screen, size):
        self.screen = screen
        self.size = size
        self.pos = int(size[0]/2),int(size[1]/2)
        self.n = 5
        self.d = 8
        self.scale = size[0]/2 - 20
        self.mode = 'n'

    def k(self):
        return self.n/self.d

    def draw(self):
        points = []
        for i in range(2000):
            theta = i / 1000 * 3.14159265 * self.d
            r = cos(self.k() * theta)
            x = self.scale * r * cos(theta) + self.pos[0]
            y = self.scale * r * sin(theta) + self.pos[0]
            points.append((x,y))
        pygame.draw.aalines(self.screen, (255,255,255), True, points)

    def kbin(self, event):
        if event.unicode == 'n' or event.unicode == 'd':
            self.mode = str(event.unicode)
        elif event.unicode >= '1' and event.unicode <= '9':
            if self.mode == 'n':
                self.n = int(event.unicode)
            else:
                self.d = int(event.unicode)

    def printcontrols(self):
        print("=" * 75)
        print("n = select the numerator")
        print("d = select the denominator")
        print("1-9 = choose value for selected variable")
        print("=" * 75)

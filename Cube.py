import pygame
import math


class Cube(pygame.sprite.Sprite):
    def __init__(self, points, length):
        pygame.sprite.Sprite.__init__(self)
        self.x = points[0]
        self.y = points[1]
        self.length = length
        self.pt1 = [self.x,self.y]
        self.pt2 = [self.x + length, self.y]
        self.pt3 = [self.x, self.y + length]
        self.pt4 = [self.x + length, self.y + length]

        vertLen = int(length / 2)

        self.pt5 = [self.pt1[0] + vertLen, self.pt1[1] - vertLen]
        self.pt6 = [self.pt2[0] + vertLen, self.pt2[1] - vertLen]
        self.pt7 = [self.pt3[0] + vertLen, self.pt3[1] - vertLen]
        self.pt8 = [self.pt4[0] + vertLen, self.pt4[1] - vertLen]

        #self.rect = self.image.get_rect()
        #self.updateRect()

    def updateRect(self):
        # update the object's rect attribute with the new x,y coordinates
        #w, h = self.image.get_size()
        #self.width, self.height = w, h
        self.rect = pygame.Rect(self.x - w / 2, self.y - h / 2, w, h)

    def myUpdateRect(self):
        self.pt1 = [self.x,self.y]
        self.pt2 = [self.x + self.length, self.y]
        self.pt3 = [self.x, self.y + self.length]
        self.pt4 = [self.x + self.length, self.y + self.length]

        vertLen = int(self.length / 2)

        self.pt5 = [self.pt1[0] + vertLen, self.pt1[1] - vertLen]
        self.pt6 = [self.pt2[0] + vertLen, self.pt2[1] - vertLen]
        self.pt7 = [self.pt3[0] + vertLen, self.pt3[1] - vertLen]
        self.pt8 = [self.pt4[0] + vertLen, self.pt4[1] - vertLen]

    def update(self, keysDown, screenWidth, screenHeight):
        if keysDown(pygame.K_DOWN):
            self.y += 20
            if self.y > self.height:
                self.y = -10

        

    
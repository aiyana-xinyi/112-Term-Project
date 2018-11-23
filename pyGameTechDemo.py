import pygame
import MovingNotes 


#frame work from Luke Peraza
class PygameGame(object):

    def init(self):
        pygame.font.init()
        self.background = pygame.image.load("cover(1).png")

        self.screen = pygame.display.set_mode((700, 700))
        self.screen.blit(self.background,[0,0]) 
        pygame.mixer.music.load("River Flows in You.wav")
        pygame.mixer.music.play(-1)
        self.myFont = pygame.font.Font("freesansbold.ttf",20)

        self.screen.blit(self.background,[-150,0])


    def mousePressed(self, x, y):
        pass

    def mouseReleased(self, x, y):
        pass

    def mouseMotion(self, x, y):
        pass

    def mouseDrag(self, x, y):
        pass

    def keyPressed(self, keyCode, modifier):
        pass

    def keyReleased(self, keyCode, modifier):
        pass

    def timerFired(self, dt):
        pass

    def redrawAll(self, screen):
        screen.blit(self.background,[-150,0])
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed() 

        if 540 > self.mouse[0] > 390 and 640 > self.mouse[1] > 580:
            pygame.draw.rect(self.screen,(153,153,255),(390,580,150,60))
            if self.click[0] == 1:
                print("i clicked")
                MovingNotes.MovingNotes().redrawAll(self.screen)
        else:
            pygame.draw.rect(self.screen,(0,102,204),(390,580,150,60))

        #hover over instruction
        if 320>self.mouse[0]>190 and 640>self.mouse[1]>580:
            pygame.draw.rect(self.screen,(153,153,255),(190,580,130,60))
        else:
            pygame.draw.rect(self.screen,(0,102,204),(190,580,130,60))

        self.buttonFont = pygame.font.Font("freesansbold.ttf",20)
        self.buttonText = self.buttonFont.render("Choose Level",True,(0,0,255))
        self.screen.blit(self.buttonText,(400,600))

        self.instruction = self.buttonFont.render("Instruction",True,(0,0,255))
        self.screen.blit(self.instruction,(200,600))

    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)




########################################
#DO NOT TOUCH
########################################

    def __init__(self, width=700, height=700, fps=50, title="112 Pygame Game"):
       #pygame.mixer.music.load("River Flows in You.wav")
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.background = pygame.image.load("introBackground.png")
        self.bgColor = (0,0,0)
        pygame.init()

    def run(self):
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        self.init()
        playing = True
        while playing:
            time = clock.tick(self.fps)
            self.timerFired(time)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons[0] == 1):
                    self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    playing = False
            screen.fill(self.bgColor)
            
            self.redrawAll(screen)
            pygame.display.flip()

        pygame.quit()


def main():
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()
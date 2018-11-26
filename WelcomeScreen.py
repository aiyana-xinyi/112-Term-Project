import pygame
from pyGameTechDemo import PygameGame
from Instructions import Instructions
from Level import Level

class WelcomeScreen(PygameGame):
	def init(self):
		pygame.font.init()
		self.background = pygame.image.load("cover(1).png")

		self.screen = pygame.display.set_mode((700, 700))

		pygame.mixer.music.load("River Flows in You.wav")
		pygame.mixer.music.play(-1)
		self.myFont = pygame.font.Font("freesansbold.ttf",20)

		self.screen.blit(self.background,[-150,0])

	def redrawAll(self, screen):
		screen.blit(self.background,[-150,0])
		self.mouse = pygame.mouse.get_pos()
		self.click = pygame.mouse.get_pressed() 

		if 540 > self.mouse[0] > 390 and 640 > self.mouse[1] > 580:
			pygame.draw.rect(self.screen,(153,153,255),(390,580,150,60))
			if self.click[0] == 1:
				Level().run()

		else:
			pygame.draw.rect(self.screen,(0,102,204),(390,580,150,60))

		#hover over instruction
		if 320>self.mouse[0]>190 and 640>self.mouse[1]>580:
			pygame.draw.rect(self.screen,(153,153,255),(190,580,130,60))
			if self.click[0] == 1:
				Instructions().run()
		else:
			pygame.draw.rect(self.screen,(0,102,204),(190,580,130,60))

		self.buttonFont = pygame.font.Font("freesansbold.ttf",20)
		self.buttonText = self.buttonFont.render("Choose Level",True,(0,0,255))
		self.screen.blit(self.buttonText,(400,600))

		self.instruction = self.buttonFont.render("Instruction",True,(0,0,255))
		self.screen.blit(self.instruction,(200,600))
    

WelcomeScreen().run()
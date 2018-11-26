import pygame
from pyGameTechDemo import PygameGame

class Instructions(PygameGame):
	def init(self):
		pygame.font.init()
		self.background = pygame.image.load("cover(1).png")

		self.screen = pygame.display.set_mode((700, 700))

		self.screen.blit(self.background,[-150,0])
		self.buttonFont = pygame.font.Font("freesansbold.ttf",20)


	def redrawAll(self,screen):
		screen.blit(self.background,[-150,0])

		pygame.draw.rect(self.screen,(204,229,255),(self.width/2-250,self.height/2-20,500,200))
		
		self.firstLine = self.buttonFont.render("Use 'a' 's' 'd' 'f' keys to play the piano",True,(0,0,255))
		self.secondLine = self.buttonFont.render("If you make a mistake, you lose a life",True,(0,0,255))
		self.thirdLine = self.buttonFont.render("Try to make it to the end of the song",True,(0,0,255))
		self.fourthLine = self.buttonFont.render("Good Luck!",True,(0,0,255))


		self.screen.blit(self.firstLine,(self.width/2-200,self.height/2))
		self.screen.blit(self.secondLine,(self.width/2-200,self.height/2+50))
		self.screen.blit(self.thirdLine,(self.width/2-200,self.height/2+100))
		self.screen.blit(self.fourthLine,(self.width/2-100,self.height/2+150))
		


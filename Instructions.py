import pygame
from pyGameTechDemo import PygameGame
import Level 

class Instructions(PygameGame):
	def init(self):
		pygame.font.init()
		self.background = pygame.image.load("cover(1).png")

		self.screen = pygame.display.set_mode((700, 700))

		self.screen.blit(self.background,[-150,0])
		self.buttonFont = pygame.font.Font("freesansbold.ttf",20)


	def redrawAll(self,screen):
		self.mouse = pygame.mouse.get_pos()
		self.click = pygame.mouse.get_pressed()
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

		#CITATION: the following if-statement code from Youtube Channel sentdex
		if 210>self.mouse[0]>140 and 600>self.mouse[1]>560:
			#pygame.draw.rect(self.screen,(153,153,255),(90,580,190,60))
			self.big = pygame.font.Font("PG_Roof Runners_active_bold-it.ttf",40)
			self.quit = self.big.render("Quit",True,(127,0,255))
			self.screen.blit(self.quit,(140,570))
			pygame.draw.ellipse(self.screen,(96,96,96),(140,600,80,10))
			if self.click[0] == 1:
				pygame.display.quit()
		else:
			self.big = pygame.font.Font("PG_Roof Runners_active_bold-it.ttf",30)
			self.quit = self.big.render("Quit",True,(0,102,204))
			self.screen.blit(self.quit,(140,570))


		if 540>self.mouse[0]>390 and 600>self.mouse[1]>560:
			#pygame.draw.rect(self.screen,(153,153,255),(90,580,190,60))
			self.big = pygame.font.Font("PG_Roof Runners_active_bold-it.ttf",40)
			self.level = self.big.render("Choose Level",True,(127,0,255))
			self.screen.blit(self.level,(360,570))
			pygame.draw.ellipse(self.screen,(96,96,96),(360,600,250,10))
			if self.click[0] == 1:
				Level.Levels().run()
		else:
			self.big = pygame.font.Font("PG_Roof Runners_active_bold-it.ttf",30)
			self.level = self.big.render("Choose Level",True,(0,102,204))
			self.screen.blit(self.level,(390,570))

		

#Instructions().run()	


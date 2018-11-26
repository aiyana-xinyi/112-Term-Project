import pygame
from pyGameTechDemo import PygameGame
from MovingNotes import MovingNotes


class Level(PygameGame):
	def init(self):
		pygame.font.init()
		self.background = pygame.image.load("cover(1).png")

		self.screen = pygame.display.set_mode((700, 700))

		self.screen.blit(self.background,[-150,0])
		self.buttonFont = pygame.font.Font("freesansbold.ttf",50)
		self.subTitleFont = pygame.font.Font("freesansbold.ttf",30)
		self.songTitleFont = pygame.font.Font("freesansbold.ttf",20)


	def redrawAll(self,screen):
		screen.blit(self.background,[-150,0])
		self.mouse = pygame.mouse.get_pos()
		self.click = pygame.mouse.get_pressed()

		self.choose = self.buttonFont.render("Choose Your Level",True,(0,0,0))
		self.screen.blit(self.choose,(110,30))

		self.easy = self.subTitleFont.render("Easy:",True,(0,0,0))
		self.screen.blit(self.easy,(50,90))

		if 270>self.mouse[0]>70 and 170>self.mouse[1]>130:
			pygame.draw.rect(self.screen,(153,153,255),(70,130,200,40))
			if self.click[0] == 1:
				self.song = "River Flows in You"
				self.life = 3
				print(self.song)
				MovingNotes(self.song,self.life).run()
		else:
			pygame.draw.rect(self.screen,(0,102,204),(70,130,200,40))

		self.riverFlows = self.songTitleFont.render("River Flows in You",True,(0,0,0))
		self.screen.blit(self.riverFlows,(80,140))

		if 180>self.mouse[0]>70 and 230>self.mouse[1]>190:
			pygame.draw.rect(self.screen,(153,153,255),(70,190,110,40))
			if self.click[0] == 1:
				MovingNotes("Minuet 1",3).run()
		else:
			pygame.draw.rect(self.screen,(0,102,204),(70,190,110,40))

		self.minuet = self.songTitleFont.render("Minuet 1",True,(0,0,0))
		self.screen.blit(self.minuet,(80,200))

		self.mid = self.subTitleFont.render("Medium:",True,(0,0,0))
		self.screen.blit(self.mid,(50,250))

		if 180>self.mouse[0]>70 and 330>self.mouse[1]>290:
			pygame.draw.rect(self.screen,(153,153,255),(70,290,110,40))
			if self.click[0] == 1:
				MovingNotes("Paradise",2).run()
		else:
			pygame.draw.rect(self.screen,(0,102,204),(70,290,110,40))

		self.paradi = self.songTitleFont.render("Paradise",True,(0,0,0))
		self.screen.blit(self.paradi,(80,300))

		if 230>self.mouse[0]>70 and 380>self.mouse[1]>350:
			pygame.draw.rect(self.screen,(153,153,255),(70,350,160,40))
			if self.click[0] == 1:
				MovingNotes("One Call Away",2).run()
		else:
			pygame.draw.rect(self.screen,(0,102,204),(70,350,160,40))

		self.onecall = self.songTitleFont.render("One Call Away",True,(0,0,0))
		self.screen.blit(self.onecall,(80,360))

		self.hard = self.subTitleFont.render("Hard:",True,(0,0,0))
		self.screen.blit(self.hard,(50,410))


		if 220>self.mouse[0]>70 and 490>self.mouse[1]>450:
			pygame.draw.rect(self.screen,(153,153,255),(70,450,150,40))
			if self.click[0] == 1:
				MovingNotes("Clair de Lune",1).run()
		else:
			pygame.draw.rect(self.screen,(0,102,204),(70,450,150,40))

		self.clair = self.songTitleFont.render("Clair de Lune",True,(0,0,0))
		self.screen.blit(self.clair,(80,460))

		if 180>self.mouse[0]>70 and 540>self.mouse[1]>500:
			pygame.draw.rect(self.screen,(153,153,255),(70,500,110,40))
			if self.click[0] == 1:
				MovingNotes("Nocturne",1).run()
		else:
			pygame.draw.rect(self.screen,(0,102,204),(70,500,110,40))

		self.chopin = self.songTitleFont.render("Nocturne",True,(0,0,0))
		self.screen.blit(self.chopin,(80,510))



import pygame
from pyGameTechDemo import PygameGame
from Struct import Struct
import Level 


class Win(PygameGame):
	def init(self):
		pygame.mixer.music.stop()
		pygame.font.init()
		self.background = pygame.image.load("cover(1).png")

		self.screen = pygame.display.set_mode((700, 700))

		self.screen.blit(self.background,[-150,0])
		self.buttonFont = pygame.font.SysFont("comicsansms",70)
		self.smallFont = pygame.font.Font("freesansbold.ttf",20)
		self.mouse = pygame.mouse.get_pos()
		self.click = pygame.mouse.get_pressed()
		self.score = Struct.score

		self.mixer = pygame.mixer
		self.mixer.init()
		self.playing = self.mixer.Sound("Win.wav")
		self.channel = self.playing.play()

		self.starNum = 0
		self.getStars()
		self.star = pygame.image.load("star3.png")
		self.starOutline = pygame.image.load("starOutline2.png")

		self.myFont = pygame.font.Font("PG_Roof Runners_active_bold-it.ttf",70)
		self.myFont2 = pygame.font.Font("PG_Roof Runners_active_bold-it.ttf",60)

	def getStars(self):
		if self.score <= 50:
			self.starNum = 1
		elif 50 < self.score <= 90:
			self.starNum = 2
		else:
			self.starNum = 3

	def redrawAll(self,screen):
		#congrats, stars, score, buttons
		screen.blit(self.background,[-150,0])
		self.mouse = pygame.mouse.get_pos()
		self.click = pygame.mouse.get_pressed()

		self.congrat = self.myFont.render("Congratulations!",True,(255,204,102))
		self.screen.blit(self.congrat,(50,100))

		if self.starNum == 1:
			screen.blit(self.star,[100,200])
			screen.blit(self.starOutline,[240,180])
			screen.blit(self.starOutline,[400,180])
		elif self.starNum == 2:
			screen.blit(self.star,[100,200])
			screen.blit(self.star,[260,200])
			screen.blit(self.starOutline,[400,180])
		else:
			screen.blit(self.star,[100,200])
			screen.blit(self.star,[260,200])
			screen.blit(self.star,[420,200])


		self.scoreStr = self.myFont2.render("Score:",True,(255,204,102))
		self.scoreNum = self.myFont2.render(str(self.score),True,(255,204,102))
		self.screen.blit(self.scoreStr,(200,380))
		self.screen.blit(self.scoreNum,(420,380))

		if 265>self.mouse[0]>140 and 580>self.mouse[1]>540:
			#pygame.draw.rect(self.screen,(153,153,255),(90,580,190,60))
			self.big = pygame.font.Font("PG_Roof Runners_active_bold-it.ttf",40)
			self.quit = self.big.render("Quit",True,(255,204,102))
			self.screen.blit(self.quit,(130,550))
			if self.click[0] == 1:
				pygame.display.quit()
		else:
			#pygame.draw.rect(self.screen,(0,102,204),(90,580,190,60))
			self.big = pygame.font.Font("PG_Roof Runners_active_bold-it.ttf",30)
			self.quit = self.big.render("Quit",True,(255,204,102))
			self.screen.blit(self.quit,(140,550))

		if 600>self.mouse[0]>390 and 580>self.mouse[1]>540:
			#pygame.draw.rect(self.screen,(153,153,255),(90,580,190,60))
			self.big = pygame.font.Font("PG_Roof Runners_active_bold-it.ttf",40)
			self.again = self.big.render("Play Again",True,(255,204,102))
			self.screen.blit(self.again,(400,550))
			if self.click[0] == 1:
				Level.Levels().run()
		else:
			#pygame.draw.rect(self.screen,(0,102,204),(90,580,190,60))
			self.big = pygame.font.Font("PG_Roof Runners_active_bold-it.ttf",30)
			self.again = self.big.render("Play Again",True,(255,204,102))
			self.screen.blit(self.again,(410,550))

		Struct.score = 0


#Win().run()
import pygame
from pyGameTechDemo import PygameGame
from Struct import Struct
import Level 

class Lost(PygameGame):
	def init(self):
		pygame.mixer.music.stop()

		pygame.font.init()
		self.background = pygame.image.load("plain-black-background.png")

		self.screen = pygame.display.set_mode((700, 700))

		self.screen.blit(self.background,[-150,0])
		self.buttonFont = pygame.font.SysFont("comicsansms",70)
		self.smallFont = pygame.font.Font("freesansbold.ttf",20)
		self.mouse = pygame.mouse.get_pos()
		self.click = pygame.mouse.get_pressed()
		self.score = Struct.score

		self.mixer = pygame.mixer
		self.mixer.init()
		self.playing = self.mixer.Sound("Lose.wav")
		self.channel = self.playing.play()

		self.myFont = pygame.font.Font("PG_Roof Runners_active_bold-it.ttf",80)
		self.myFont2 = pygame.font.Font("PG_Roof Runners_active_bold-it.ttf",60)


	def redrawAll(self,screen):
		self.mouse = pygame.mouse.get_pos()
		self.click = pygame.mouse.get_pressed()
		screen.blit(self.background,[-150,0])


		self.gameOver = self.myFont.render("Game Over!",True,(255,255,255))
		self.screen.blit(self.gameOver,(150,250))

		self.scoreStr = self.myFont2.render("Score:",True,(255,255,255))
		self.scoreNum = self.myFont2.render(str(self.score),True,(255,255,255))
		self.screen.blit(self.scoreStr,(200,380))
		self.screen.blit(self.scoreNum,(420,380))

		if 200>self.mouse[0]>130 and 580>self.mouse[1]>540:
			#pygame.draw.rect(self.screen,(153,153,255),(90,580,190,60))
			self.big = pygame.font.Font("PG_Roof Runners_active_bold-it.ttf",40)
			self.quit = self.big.render("Quit",True,(255,255,255))
			self.screen.blit(self.quit,(130,550))
			if self.click[0] == 1:
				pygame.display.quit()
		else:
			#pygame.draw.rect(self.screen,(0,102,204),(90,580,190,60))
			self.big = pygame.font.Font("PG_Roof Runners_active_bold-it.ttf",30)
			self.quit = self.big.render("Quit",True,(255,255,255))
			self.screen.blit(self.quit,(140,550))

		if 450>self.mouse[0]>380 and 580>self.mouse[1]>540:
			#pygame.draw.rect(self.screen,(153,153,255),(90,580,190,60))
			self.big = pygame.font.Font("PG_Roof Runners_active_bold-it.ttf",40)
			self.play = self.big.render("Play Again",True,(255,255,255))
			self.screen.blit(self.play,(390,550))
			if self.click[0] == 1:
				Level.Levels().run()
		else:
			#pygame.draw.rect(self.screen,(0,102,204),(90,580,190,60))
			self.big = pygame.font.Font("PG_Roof Runners_active_bold-it.ttf",30)
			self.play = self.big.render("Play Again",True,(255,255,255))
			self.screen.blit(self.play,(400,550))

		


		# pygame.draw.rect(self.screen,(0,0,0),(180,240,340,200))
		# self.message = self.buttonFont.render("You Lost!",True,(255,255,255))
		# self.lost = self.buttonFont.render("Sorry",True,(255,255,255))
		# self.screen.blit(self.lost,(280,250))
		# self.screen.blit(self.message,(250,300))

		# self.scoreStr = self.buttonFont.render("Score:",True,(255,255,255))
		# self.scoreNum = self.buttonFont.render(str(self.score),True,(255,255,255))
		# self.screen.blit(self.scoreStr,(240,380))
		# self.screen.blit(self.scoreNum,(420,380))

		# #CITATION: The following if-statement code is from Youtube Channel sentdex
		# if 265>self.mouse[0]>140 and 580>self.mouse[1]>540:
		# 	pygame.draw.rect(self.screen,(153,153,255),(140,540,125,40))
		# 	if self.click[0] == 1:
		# 		Level.Levels().run()
		# else:
		# 	pygame.draw.rect(self.screen,(0,102,204),(140,540,125,40))

		# self.playAgain = self.smallFont.render("Play Again",True,(0,0,0))
		# self.screen.blit(self.playAgain,(150,550))

		# if 505>self.mouse[0]>440 and 580>self.mouse[1]>540:
		# 	pygame.draw.rect(self.screen,(153,153,255),(440,540,65,40))
		# 	if self.click[0] == 1:
		# 		pygame.quit()
		# else:
		# 	pygame.draw.rect(self.screen,(0,102,204),(440,540,65,40))

		# self.quit = self.smallFont.render("Quit",True,(0,0,0))
		# self.screen.blit(self.quit,(450,550))
		Struct.score = 0


#Lost().run()
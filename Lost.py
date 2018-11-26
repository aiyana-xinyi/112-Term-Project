import pygame
from pyGameTechDemo import PygameGame


class Lost(PygameGame):
	def init(self):
		pygame.font.init()
		self.background = pygame.image.load("cover(1).png")

		self.screen = pygame.display.set_mode((700, 700))

		self.screen.blit(self.background,[-150,0])
		self.buttonFont = pygame.font.SysFont("comicsansms",70)
		self.smallFont = pygame.font.Font("freesansbold.ttf",20)
		self.mouse = pygame.mouse.get_pos()
		self.click = pygame.mouse.get_pressed()

	def redrawAll(self,screen):
		self.mouse = pygame.mouse.get_pos()
		self.click = pygame.mouse.get_pressed()
		screen.blit(self.background,[-150,0])
		pygame.draw.rect(self.screen,(0,0,0),(180,240,340,200))
		self.message = self.buttonFont.render("You Lost!",True,(255,255,255))
		self.lost = self.buttonFont.render("Sorry",True,(255,255,255))
		self.screen.blit(self.lost,(280,250))
		self.screen.blit(self.message,(250,300))

		self.scoreStr = self.buttonFont.render("Score:",True,(255,255,255))
		self.scoreNum = self.buttonFont.render(str(self.score),True,(255,255,255))
		self.screen.blit(self.scoreStr,(240,380))
		self.screen.blit(self.scoreNum,(420,380))

		if 265>self.mouse[0]>140 and 580>self.mouse[1]>540:
			pygame.draw.rect(self.screen,(153,153,255),(140,540,125,40))
			if self.click[0] == 1:
				pass
		else:
			pygame.draw.rect(self.screen,(0,102,204),(140,540,125,40))

		self.playAgain = self.smallFont.render("Play Again",True,(0,0,0))
		self.screen.blit(self.playAgain,(150,550))

		if 505>self.mouse[0]>440 and 580>self.mouse[1]>540:
			pygame.draw.rect(self.screen,(153,153,255),(440,540,65,40))
			if self.click[0] == 1:
				pass
		else:
			pygame.draw.rect(self.screen,(0,102,204),(440,540,65,40))

		self.quit = self.smallFont.render("Quit",True,(0,0,0))
		self.screen.blit(self.quit,(450,550))




#Lost().run()
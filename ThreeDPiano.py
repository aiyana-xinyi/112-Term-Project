import pygame
from pyGameTechDemo import PygameGame
from Struct import Struct
import random
from Lost import Lost
from Struct import Struct
from win import Win
import pyaudio
import threading

class ThreeDPiano(PygameGame):
	#CITATION: following code from 112 website
	def gameDimensions(self):
		rows = 10
		cols = 4
		margin = 1
		return (rows,cols,margin)

	#set values to variables
	def init(self,song,life):
		pygame.mixer.music.stop()
		#CITATION: the next line of code is from 112 website
		(self.rows,self.cols,self.margin) = self.gameDimensions()

		self.selected = [[0,0]]
		self.timerCalls = 0
		self.timerDelay = 100

		self.buttonFont = pygame.font.Font("freesansbold.ttf",20)
		self.life = life
		self.originalLife = life
		self.song = song+".wav"
		self.win = False

		self.mixer = pygame.mixer
		self.mixer.init()
		self.playing = self.mixer.Sound(self.song)
		self.channel = self.playing.play()
		

		self.points = []
		self.getCoordinates()
		self.twoDPoints = []
		self.getAdjacentPoints()
		self.allSelectBlock = []


	def getRandomCell(self):
		randCol = random.randint(0,3)
		self.allSelectBlock.append(randCol)

	def getCoordinates(self):
		for row in range(self.rows+1):
			for col in range (self.cols+1):
				if col == 0:
					l0 = ((0,self.height),(200,0))
					b = self.findYIntercept((0,self.height),(200,0))[0]
					m = self.findYIntercept((0,self.height),(200,0))[1]
					x,y = self.findIntersection(m,b,row*70)
					self.points.append((x,y))
				elif col == 1:
					l1 = ((1*(self.width//4)),(1*((300//4)+200)))
					b1 = self.findYIntercept((1*(self.width//4),self.height),(1*((300//4)+200),0))[0]
					m1 = self.findYIntercept((1*(self.width//4),self.height),(1*((300//4)+200),0))[1]
					x1,y1 = self.findIntersection(m1,b1,row*70)
					self.points.append((x1,y1))
				elif col == 2:
					self.points.append((self.width//2,row*70))
				elif col == 3:
					l3 = ((self.width-(1*(self.width//4))),(self.width - (1*((300//4)+200))))
					b3 = self.findYIntercept(((self.width-(1*(self.width//4))),self.height),((self.width - (1*((300//4)+200))),0))[0]
					m3 = self.findYIntercept(((self.width-(1*(self.width//4))),self.height),((self.width - (1*((300//4)+200))),0))[1]
					x3,y3 = self.findIntersection(m3,b3,row*70)
					self.points.append((x3,y3))
				elif col == 4:
					l4 = (self.width,500)
					b4 = self.findYIntercept((self.width,self.height),(500,0))[0]
					m4 = self.findYIntercept((self.width,self.height),(500,0))[1]
					x4,y4 = self.findIntersection(m4,b4,row*70)
					self.points.append((x4,y4))

	def getAdjacentPoints(self):
		#50 points total
		count = 0
		for i in range(len(self.points)):
			subList = []
			if i%(self.cols + 1) != self.cols and i//(self.cols +1) <= self.rows -1:
				subList.append(self.points[i])
				subList.append(self.points[i+1])
				subList.append(self.points[i+self.cols+1])
				subList.append(self.points[i+self.cols+2])
			self.twoDPoints.append(subList)
		
		self.twoDPoints = [x for x in self.twoDPoints if x != []]

	def timerFired(self,dt):
		self.fallingTime = 1
		if self.originalLife == 3:
			self.fallingTime = 8
		elif self.originalLife == 2:
			self.fallingTime = 4
		elif self.originalLife == 1:
			self.fallingTime == 2

		self.timerCalls += 1
		if self.life != 0 and self.channel.get_busy() == 1:
			for item in (self.allSelectBlock):
				if item > 39:
					self.life -= 1
					self.allSelectBlock.remove(item)
			if self.timerCalls % 9 == 0:
				self.getRandomCell()
			if self.timerCalls % self.fallingTime == 0:
				for i in range(len(self.allSelectBlock)):
					block = self.allSelectBlock[i]
					self.allSelectBlock[i] = block+4
		#win
		elif self.channel.get_busy() == 0 and self.life != 0:
			pygame.mixer.music.stop()
			self.channel = self.playing.set_volume(0)
			Win().run()
		#lost
		elif self.life == 0:
			pygame.mixer.music.stop()
			self.channel = self.playing.set_volume(0)
			Lost().run()

	def playDing(self):
		pygame.mixer.music.load('Ding.wav')
		pygame.mixer.music.play(0)

	def playWrong(self):
		pygame.mixer.music.load('Wrong.wav')
		pygame.mixer.music.play(0)
		

	def keyPressed(self,keycode,mod):
		#if it's still in game
		if self.life != 0 and self.channel.get_busy() == 1:
			# if keycode == pygame.K_SPACE:
			# 	threading.Thread(target = self.playMusic,args = ("River Flows in You.wav",44100)).start()
			# if keycode == pygame.K_RIGHT:
			# 	threading.Thread(target = self.playMusic,args = ("River Flows in You.wav",80000)).start()
			# if keycode == pygame.K_LEFT:
			# 	threading.Thread(target = self.playMusic,args = ("River Flows in You.wav",30000)).start()
			if keycode == pygame.K_a:
				contain = False
				for block in self.allSelectBlock:
					if block % 4 ==  0:
						contain = True
						break
				if contain == False:
					threading.Thread(target = self.playWrong,args=()).start()
					self.life -= 1
				for i in range (len(self.allSelectBlock)):
					if self.allSelectBlock[i] % 4 == 0:
						threading.Thread(target = self.playDing,args=()).start()
						self.allSelectBlock.pop(i)
						Struct.score += 1
						break
		
			if keycode == pygame.K_s:
				contain = False
				for block in self.allSelectBlock:
					if (block-1) % 4 ==  0:
						contain = True
						break
				if contain == False:
					threading.Thread(target = self.playWrong,args=()).start()
					self.life -= 1
				for i in range (len(self.allSelectBlock)):
					if (self.allSelectBlock[i]-1) % 4 == 0:
						threading.Thread(target = self.playDing,args=()).start()
						self.allSelectBlock.pop(i)
						Struct.score += 1
						break
				
			if keycode == pygame.K_d:
				contain = False
				for block in self.allSelectBlock:
					if (block-2) % 4 ==  0:
						contain = True
						break
				if contain == False:
					threading.Thread(target = self.playWrong,args=()).start()
					self.life -= 1
				for i in range (len(self.allSelectBlock)):
					if (self.allSelectBlock[i]-2) % 4 == 0:
						threading.Thread(target = self.playDing,args=()).start()
						self.allSelectBlock.pop(i)
						Struct.score += 1
						break

			if keycode == pygame.K_f:
				contain = False
				for block in self.allSelectBlock:
					if (block-3) % 4 ==  0:
						contain = True
						break
				if contain == False:
					threading.Thread(target = self.playWrong,args=()).start()
					self.life -= 1
				for i in range (len(self.allSelectBlock)):
					if (self.allSelectBlock[i]-3) % 4 == 0:
						threading.Thread(target = self.playDing,args=()).start()
						self.allSelectBlock.pop(i)
						Struct.score += 1
						break


		elif self.life <= 0 or self.channel.get_busy() == 0:
			Lost().run()

	def findIntersection(self,l1Slope,l1Intercept,l2Intercept):
		x,y = 0,0
		x = (l2Intercept-(l1Intercept))//l1Slope
		y = l2Intercept
		return (x,y)

	def findYIntercept(self,pt1,pt2):
		x1,y1 = pt1
		x2,y2 = pt2
		slope = (y1-y2)/(x1-x2)
		return ((y1)-(slope*x1),slope)


	def redrawAll(self,screen):
		#two side vertical line
		pygame.draw.line(self.screen,(255,255,255),(0,self.height),(200,0))
		pygame.draw.line(self.screen,(255,255,255),(self.width,self.height),(500,0))

		#horizontal lines
		for row in range(self.rows):
			pygame.draw.line(self.screen,(255,255,255),(200*((10-row)/10),row*70),((700-(200*((10-row)/10))),row*70))

		#vertical lines
		for col in range(self.cols):
			if col == 0:
				pygame.draw.line(self.screen,(255,255,255),(1*(self.width//4),self.height),(1*((300//4)+200),0))
			elif col == 1:
				pygame.draw.line(self.screen,(255,255,255),(self.width//2,self.height),((self.width/2,0)))
			elif col == 2:
				pygame.draw.line(self.screen,(255,255,255),((self.width-(1*(self.width//4))),self.height),((self.width - (1*((300//4)+200))),0))

		for i in range (len(self.twoDPoints)):
			for block in self.allSelectBlock:
				if block == i:
					[pt2,pt1,pt3,pt4] = self.twoDPoints[i]
					pygame.draw.polygon(self.screen,(232,229,229),[pt1,pt2,pt3,pt4])
					(c2,c1,c3,c4) = (pt2,pt1,pt3,pt4)
					upperShape = [(c2[0]+15,c2[1]),c1,c3,c4]
					pygame.draw.polygon(self.screen,(87,85,85),upperShape)


		self.scoreText = self.buttonFont.render("Score:",True,(255,255,255))
		self.scoreNum = self.buttonFont.render(str(Struct.score),True,(255,255,255))
		screen.blit(self.scoreText,(20,10))
		screen.blit(self.scoreNum,(90,10))
		self.lifeText = self.buttonFont.render("Life:",True,(255,255,255))
		self.lifeNum = self.buttonFont.render(str(self.life),True,(255,255,255))
		screen.blit(self.lifeText,(20,30))
		screen.blit(self.lifeNum,(90,30))


	def run(self):
			clock = pygame.time.Clock()
			self.screen = pygame.display.set_mode((700, 700))
			# set the title of the window
			pygame.display.set_caption("Falling Piano Tiles")

			# stores all the keys currently being held down
			self._keys = dict()

			# call game-specific initialization
			
			self.init(Struct.song,Struct.life)
			#self.init("Nocturne",3)

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
				self.screen.fill(self.bgColor)

				self.redrawAll(self.screen)
				pygame.display.flip()

			pygame.display.quit()

#ThreeDPiano().run()

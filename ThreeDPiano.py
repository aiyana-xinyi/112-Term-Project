import pygame
from pyGameTechDemo import PygameGame
from Struct import Struct
import random
#from Lost import Lost
from Struct import Struct
#from win import Win
import pyaudio
import threading

class ThreeDPiano(PygameGame):
	def gameDimensions(self):
		rows = 10
		cols = 4
		margin = 1
		return (rows,cols,margin)

	#set values to variables
	def init(self,song,life):
		pygame.mixer.music.stop()
		(self.rows,self.cols,self.margin) = self.gameDimensions()
		self.emptyColor = "white"
		self.board = []

		for i in range (self.rows):
			self.board += [[self.emptyColor]*self.cols]

		# self.firstFallingPiece = newFallingPiece(self)
		self.cellWidth = self.width//len(self.board[0])
		self.cellHeight = self.height//len(self.board)
		self.cellSize = min(self.cellWidth,self.cellHeight)
		self.selected = [[0,0]]
		self.timerCalls = 0
		self.timerDelay = 100

		self.curTime = 0
		self.endTime = 0
		self.buttonFont = pygame.font.Font("freesansbold.ttf",20)
		self.life = life
		self.originalLife = life
		self.song = song+".wav"
		self.win = False

		self.mixer = pygame.mixer
		self.mixer.init()
		self.playing = self.mixer.Sound(self.song)
		self.channel = self.playing.play()
		pygame.mixer.music.set_volume(0.3)


		self.points = []
		self.getCoordinates()
		self.twoDPoints = []
		self.getAdjacentPoints()
		# for i in range(self.rows):
		# 	self.points += [[]*self.cols]

	def getRandomCell(self):
		randCol = random.randint(0,3)
		self.selected.append([0,randCol])

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
		#print(self.points)

	def getAdjacentPoints(self):
		#50 points total
		count = 0
		for i in range(len(self.points)):
			subList = []
			print('bey', i)
			if i%(self.cols + 1) != self.cols and i//(self.cols +1) <= self.cols +1:
				subList.append(self.points[i])
				subList.append(self.points[i+1])
				subList.append(self.points[i+self.cols+1])
				subList.append(self.points[i+self.cols+2])
				print(i)
			else:
				print(i,"height")
			self.twoDPoints.append(subList)

		for l in self.twoDPoints:
			if len(l) == 0:
				self.twoDPoints.remove(l)
		print(self.twoDPoints)
		




		# for row in range(self.rows):
		# 	line1 = ((200*((10-row)/10),row*70),((700-(200*((10-row)/10))),row*70)) #row end coord
		# 	for col in range(self.cols+1):
		# 		if col == 0:
		# 			l0 = ((0,self.height),(200,0))
		# 			b = findYIntercept((0,self.height),(200,0))[0]
		# 			m = findYIntercept((0,self.height),(200,0))[1]
		# 			x,y = findIntersection(m,b,row*70)
		# 		if col == 1:
		# 			l1 = ((1*(self.width//4)),(1*((300//4)+200)))
		# 			b1 = findYIntercept((0,self.height),(200,0))[0]
		# 			m1 = findYIntercept((0,self.height),(200,0))[1]
		# 			x1,y1 = findIntersection(m1,b1,row*70)
		# 		elif col == 2:
		# 			pygame.draw.line(self.screen,(0,255,0),(self.width//2,self.height),((self.width/2,0)))
		# 		elif col == 3:
		# 			pygame.draw.line(self.screen,(0,0,255),((self.width-(1*(self.width//4))),self.height),((self.width - (1*((300//4)+200))),0))
		# 		elif col == 4:
		# 			pygame.draw.line(self.screen,(255,255,255),(self.width,self.height),(500,0))


	#taken from course notes
	def getCell(self,x, y):
	    gridWidth  = self.width - 2*self.margin
	    gridHeight = self.height - 2*self.margin
	    cellWidth  = gridWidth / self.cols
	    cellHeight = gridHeight / self.rows
	    row = (y - self.margin) // cellHeight
	    col = (x - self.margin) // cellWidth
	    # triple-check that we are in bounds
	    row = min(self.rows-1, max(0, row))
	    col = min(self.cols-1, max(0, col))
	    return (row, col)

	#taken from course notes
	def getCellBounds(self,row, col):
	    gridWidth  = self.width - 2*self.margin
	    gridHeight = self.height - 2*self.margin
	    columnWidth = gridWidth / self.cols
	    rowHeight = gridHeight / self.rows
	    x0 = self.margin + col * columnWidth
	    x1 = self.margin + (col+1) * columnWidth
	    y0 = self.margin + row * rowHeight
	    y1 = self.margin + (row+1) * rowHeight
	    return (x0, y0, x1, y1)

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
			for item in (self.selected):
				[row,col] = item
				if row > self.rows:
					self.life -= 1
					self.selected.remove(item)
			if self.timerCalls % 9 == 0:
				self.getRandomCell()
			if self.timerCalls % self.fallingTime == 0:
				for i in range (len(self.selected)):
					[row,col] = self.selected[i]
					self.selected[i] = [row+1,col]
		#win
		elif self.channel.get_busy() == 0 and self.life != 0:
			pygame.mixer.music.stop()
			Win().run()
		#lost
		elif self.life == 0:
			pygame.mixer.music.stop()
			Lost().run()

	def playDing(self):
		pygame.mixer.music.load('Ding.wav')
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
			try:
				if keycode == pygame.K_a:
					contain = False
					self.curTime = self.timerCalls
					self.endTime = self.curTime + 5
					for [row,col] in self.selected:
						if col == 0:
							contain = True
							break
					if contain == False:
						self.life -= 1
					for i in range (len(self.selected)):
						#if none of the col equal to 0, then life subtracts 1
						if self.selected[i][1] == 0:
							threading.Thread(target = self.playDing,args=()).start()
							self.selected.pop(i)
							Struct.score += 1
							break
			
				if keycode == pygame.K_s:
					contain = False
					self.curTime = self.timerCalls
					self.endTime = self.curTime + 5
					for [row,col] in self.selected:
						if col == 1:
							contain = True
							break
					if contain == False:
						self.life -= 1
					for i in range (len(self.selected)):
						if self.selected[i][1] == 1:
							threading.Thread(target = self.playDing,args=()).start()
							self.selected.pop(i)
							Struct.score += 1
							break
					
				if keycode == pygame.K_d:
					contain = False
					self.curTime = self.timerCalls
					self.endTime = self.curTime + 5
					for [row,col] in self.selected:
						if col == 2:
							contain = True
							break
					if contain == False:
						self.life -= 1
					for i in range (len(self.selected)):
						if self.selected[i][1] == 2:
							threading.Thread(target = self.playDing,args=()).start()
							self.selected.pop(i)
							Struct.score += 1
							break

				if keycode == pygame.K_f:
					contain = False
					self.curTime = self.timerCalls
					self.endTime = self.curTime + 5
					for [row,col] in self.selected:
						if col == 3:
							contain = True
							break
					if contain == False:
						self.life -= 1
					for i in range (len(self.selected)):
						if self.selected[i][1] == 3:
							threading.Thread(target = self.playDing,args=()).start()
							self.selected.pop(i)
							Struct.score += 1
							break
					
			except:
				self.life -= 1

		elif self.life <= 0 or self.channel.get_busy() == 0:
			Lost().run()

	def findIntersection(self,l1Slope,l1Intercept,l2Intercept):
		x,y = 0,0
		x = (l2Intercept-(l1Intercept))//l1Slope
		y = l2Intercept
		#pygame.draw.circle(self.screen,(255,0,0),(-1*x,y),4)
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
				pygame.draw.line(self.screen,(255,0,0),(1*(self.width//4),self.height),(1*((300//4)+200),0))
			elif col == 1:
				pygame.draw.line(self.screen,(0,255,0),(self.width//2,self.height),((self.width/2,0)))
			elif col == 2:
				pygame.draw.line(self.screen,(0,0,255),((self.width-(1*(self.width//4))),self.height),((self.width - (1*((300//4)+200))),0))
		
		# for i in range(len(self.points)):
		# 	x,y = self.points[i]
		# 	pygame.draw.circle(self.screen,(255,0,0),(int(x),int(y)),4)
		# 	self.songTitleFont = pygame.font.Font("freesansbold.ttf",20)
		# 	self.num = self.songTitleFont.render(str(i),True,(255,255,255))
		# 	self.screen.blit(self.num,(int(x),int(y)))

		for i in range (len(self.twoDPoints)):
			for (x,y) in self.twoDPoints[i]:
				pygame.draw.circle(self.screen,(255,0,0),(int(x),int(y)),4)

		
		   

	# def redrawAll(self,screen):
	# 	constant = 5
	# 	for row in range(self.rows):
	# 		for col in range(self.cols):
	# 			(x0, y0, x1, y1) = self.getCellBounds(row,col)
	# 			pygame.draw.rect(self.screen,(255,255,255),(x0, y0,x1-x0,y1-y0)) #background white tiles
	# 			pygame.draw.rect(self.screen,(0,0,0),(x0, y0,x1-x0,y1-y0),1)
	# 			for (selectedRow,selectedCol) in self.selected:
	# 				if (selectedRow,selectedCol) == (row,col):
	# 					pygame.draw.rect(self.screen,(107,103,103),(x0, y0, x1-x0, y1-y0)) #the actual black falling tile
	# 					#canvas.create_rectangle(x0,y0,x1,y1,fill = "red3")
	# 					pygame.draw.rect(self.screen,(41,41,41),(x0+5, y0+5, x1-x0-5, y1-y0-5))
	# 					#canvas.create_rectangle(x0+5,y0+5,x1-5,y1-5, fill = "red4")
	# 					pygame.draw.line(self.screen,(0,0,0),(x0,y0),(x0+5,y0+5))
	# 					pygame.draw.line(self.screen,(0,0,0),(x0,y0),(x0+5,y0+5))
	# 					pygame.draw.line(self.screen,(0,0,0),(x1,y0),(x1-5,y0+5))
	# 					pygame.draw.line(self.screen,(0,0,0),(x0,y1),(x0+5,y1-5))
	# 	self.scoreText = self.buttonFont.render("Score:",True,(0,0,0))
	# 	self.scoreNum = self.buttonFont.render(str(Struct.score),True,(0,0,0))
	# 	screen.blit(self.scoreText,(20,10))
	# 	screen.blit(self.scoreNum,(90,10))
	# 	self.lifeText = self.buttonFont.render("Life:",True,(0,0,0))
	# 	self.lifeNum = self.buttonFont.render(str(self.life),True,(0,0,0))
	# 	screen.blit(self.lifeText,(20,30))
	# 	screen.blit(self.lifeNum,(90,30))



	def run(self):
			clock = pygame.time.Clock()
			self.screen = pygame.display.set_mode((700, 700))
			# set the title of the window
			pygame.display.set_caption("Falling Piano Tiles")

			# stores all the keys currently being held down
			self._keys = dict()

			# call game-specific initialization
			
			#self.init(Struct.song,Struct.life)
			self.init("Nocturne",3)

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

ThreeDPiano().run()

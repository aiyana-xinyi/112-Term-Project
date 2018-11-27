import pygame
from pyGameTechDemo import PygameGame
from Struct import Struct
import random

class ThreeDPiano(PygameGame):
	def gameDimensions(self):
		rows = 10
		cols = 4
		margin = 1
		return (rows,cols,margin)

	#set values to variables
	def init(self,song,life):
		(self.rows,self.cols,self.margin) = self.gameDimensions()
		self.emptyColor = "white"
		self.board = []
		# self.isGameOver = False
		# self.score = 0
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
		self.song = song+".wav"
		self.win = False
		pygame.mixer.music.load(self.song)
		pygame.mixer.music.play(0)

		self.mixer = pygame.mixer
		self.mixer.init()
		self.playing = self.mixer.Sound(self.song)
		self.channel = self.playing.play()



	def getRandomCell(self):
		randCol = random.randint(0,5)
		self.selected.append([0,randCol])


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
	    self.timerCalls += 1
	    if self.timerCalls % 9 == 0:
	    	self.getRandomCell()

	    if self.timerCalls % 5 == 0:
	    	for i in range (len(self.selected)):
		        [row,col] = self.selected[i]
		        self.selected[i] = [row+1,col]

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
					print("ha")
					self.curTime = self.timerCalls
					self.endTime = self.curTime + 5
					Struct.score += 1
					print("la")
					for i in range (len(self.selected)):
						print(self.selected[i])
						if self.selected[i][1] == 0:
							print("im here")
							self.selected.pop(i)
							break
			
				if keycode == pygame.K_s:
					self.curTime = self.timerCalls
					self.endTime = self.curTime + 5
					Struct.score += 1
					for i in range (len(self.selected)):
						if self.selected[i][1] == 1:
							self.selected.pop(i)
							break
					
				if keycode == pygame.K_d:
					self.curTime = self.timerCalls
					self.endTime = self.curTime + 5
					Struct.score += 1
					for i in range (len(self.selected)):
						if self.selected[i][1] == 2:
							self.selected.pop(i)
							break
					
				if keycode == pygame.K_f:
					self.curTime = self.timerCalls
					self.endTime = self.curTime + 5
					Struct.score += 1
					for i in range (len(self.selected)):
						if self.selected[i][1] == 3:
							self.selected.pop(i)
							break

			except:
				self.life -= 1
		elif self.life == 0 or self.channel.get_busy() == 0:
			pass

		   

	def redrawAll(self,screen):
		for row in range(self.rows):
			for col in range(self.cols):
				(x0, y0, x1, y1) = self.getCellBounds(row,col)
				pygame.draw.rect(self.screen,(255,255,255),(x0, y0,x1-x0,y1-y0))
				pygame.draw.rect(self.screen,(0,0,0),(x0, y0,x1-x0,y1-y0),1)
				for (selectedRow,selectedCol) in self.selected:
					if (selectedRow,selectedCol) == (row,col):
						pygame.draw.rect(self.screen,(107,103,103),(x0, y0, x1-x0, y1-y0))
						#canvas.create_rectangle(x0,y0,x1,y1,fill = "red3")
						pygame.draw.rect(self.screen,(41,41,41),(x0+5, y0+5, x1-x0-5, y1-y0-5))
						#canvas.create_rectangle(x0+5,y0+5,x1-5,y1-5, fill = "red4")
						pygame.draw.line(self.screen,(0,0,0),(x0,y0),(x0+5,y0+5))
						pygame.draw.line(self.screen,(0,0,0),(x0,y0),(x0+5,y0+5))
						pygame.draw.line(self.screen,(0,0,0),(x1,y0),(x1-5,y0+5))
						pygame.draw.line(self.screen,(0,0,0),(x0,y1),(x0+5,y1-5))
		self.scoreText = self.buttonFont.render("Score:",True,(0,0,0))
		self.scoreNum = self.buttonFont.render(str(Struct.score),True,(0,0,0))
		screen.blit(self.scoreText,(20,10))
		screen.blit(self.scoreNum,(90,10))



	def run(self):
			clock = pygame.time.Clock()
			self.screen = pygame.display.set_mode((700, 700))
			# set the title of the window
			pygame.display.set_caption("Falling Piano Tiles")

			# stores all the keys currently being held down
			self._keys = dict()

			# call game-specific initialization
			# print("3")
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

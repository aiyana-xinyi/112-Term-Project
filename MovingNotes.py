import pygame
from pyGameTechDemo import PygameGame
from Notes import Notes
from Cube import Cube
import pyaudio
import wave
from array import array
from struct import pack
import threading
import random
import audioop
from Lost import Lost

class MovingNotes(PygameGame):
	def init(self,song,life):
		pygame.mixer.music.set_volume(0.5)
		self.notes = pygame.sprite.Group()
		self.background = pygame.image.load("piano(1).png")
		self.cube1Lst = []
		self.cube2Lst = []
		self.cube3Lst = []
		self.cube4Lst = []
		self.allCubesLst = [[]]
		self.cubeGroup = pygame.sprite.Group(self.cube1Lst,self.cube2Lst,self.cube3Lst,self.cube4Lst)
		self.timeCount = 0
		self.randRow = 0
		self.timerDelay = 100
		self.pause = False
		self.curTime = 0
		self.endTime = 0
		self.buttonFont = pygame.font.Font("freesansbold.ttf",20)
		print("1")
		print(self.song)
		
		pygame.mixer.music.load(self.song+".wav")
		pygame.mixer.music.play(0)
		

	def generateRandomCube(self):
		margin = 30
		self.gap = self.width / 4
		self.x1 = self.randRow*self.gap+margin
		self.y1 = 50
		return Cube([self.x1,self.y1],50)


	#taken from pyaudio demo code
	def playMusic(self,file,rate):
		CHUNK = 1024 #measured in bytes
		RECORD_SECONDS = 5
		#the next one line is from stackOverflow
		self.RATE = rate
		wf = wave.open(file, 'rb')

		p = pyaudio.PyAudio()

		stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
			channels=wf.getnchannels(),
			rate=self.RATE,
			output=True)

		#play file
		self.data = wf.readframes(CHUNK)
		while len(self.data) > 0:
			stream.write(self.data)
			self.data = wf.readframes(CHUNK)

		stream.stop_stream()
		stream.close()

		p.terminate()

	def determineWin(self):
		mixer = pygame.mixer
		mixer.init()
		song = mixer.Sound(self.song)
		channel = song.play()
		while channel.get_busy():
			print ("Playing...")
		print ("Finished.")
		

	def keyPressed(self,keycode,mod):
		if self.life != 0:
			# if keycode == pygame.K_SPACE:
			# 	threading.Thread(target = self.playMusic,args = ("River Flows in You.wav",44100)).start()
			# if keycode == pygame.K_RIGHT:
			# 	threading.Thread(target = self.playMusic,args = ("River Flows in You.wav",80000)).start()
			# if keycode == pygame.K_LEFT:
			# 	threading.Thread(target = self.playMusic,args = ("River Flows in You.wav",30000)).start()
			try:
				if keycode == pygame.K_a:
					self.cube1Lst.pop(0)
					self.curTime = self.timeCount
					self.endTime = self.curTime + 5
					self.score += 1
			
				if keycode == pygame.K_s:
					self.cube2Lst.pop(0)
					self.curTime = self.timeCount
					self.endTime = self.curTime + 5
					self.score += 1
					
				if keycode == pygame.K_d:
					self.cube3Lst.pop(0)
					self.curTime = self.timeCount
					self.endTime = self.curTime + 5
					self.score += 1
					
				if keycode == pygame.K_f:
					self.cube4Lst.pop(0)
					self.curTime = self.timeCount
					self.endTime = self.curTime + 5
					self.score += 1

			except:
				self.life -= 1
		else:
			pass

	def timerFired(self,dt):
		if self.life != 0:
			self.timeCount += 1
			if self.timeCount <= self.endTime:
				pygame.mixer.music.set_volume(0.8)
			else:
				pygame.mixer.music.set_volume(0.5)


			#get random falling time
			randTime = random.randint(5,20)
			if self.timeCount % 10 == 0:
				for cube in self.cube1Lst:
					cube.y += 10
					cube.myUpdateRect()
					if cube.y > self.height:
						print("You Lost")
				for cube in self.cube2Lst:
					cube.y += 10
					cube.myUpdateRect()
					if cube.y > self.height:
						print("You Lost")
				for cube in self.cube3Lst:
					cube.y += 10
					cube.myUpdateRect()
					if cube.y > self.height:
						print("You Lost")
				for cube in self.cube4Lst:
					cube.y += 10
					cube.myUpdateRect()
					if cube.y > self.height:
						print("You Lost")

			if self.timeCount % randTime == 0:
				self.randRow = random.randint(0,4)
				if self.randRow == 0:
					self.cube1Lst.append(self.generateRandomCube())
				elif self.randRow == 1:
					self.cube2Lst.append(self.generateRandomCube())
				elif self.randRow == 2:
					self.cube3Lst.append(self.generateRandomCube())
				elif self.randRow == 3:
					self.cube4Lst.append(self.generateRandomCube())
		else:
			pygame.mixer.music.stop()
			#goes to lose screen
			#Lost().run()


	def drawCubes(self,screen,Cube,color):
		#draw square 1
		pygame.draw.line(screen,color,(Cube.pt1),(Cube.pt2),4)
		pygame.draw.line(screen,color,(Cube.pt3),(Cube.pt4),4)
		pygame.draw.line(screen,color,(Cube.pt1),(Cube.pt3),4)
		pygame.draw.line(screen,color,(Cube.pt2),(Cube.pt4),4)
		#draw square 2
		pygame.draw.line(screen,color,(Cube.pt5),(Cube.pt6),4)
		pygame.draw.line(screen,color,(Cube.pt7),(Cube.pt8),4)
		pygame.draw.line(screen,color,(Cube.pt5),(Cube.pt7),4)
		pygame.draw.line(screen,color,(Cube.pt6),(Cube.pt8),4)
		#draw lines
		pygame.draw.line(screen,color,(Cube.pt1),(Cube.pt5),4)
		pygame.draw.line(screen,color,(Cube.pt2),(Cube.pt6),4)
		pygame.draw.line(screen,color,(Cube.pt3),(Cube.pt7),4)
		pygame.draw.line(screen,color,(Cube.pt4),(Cube.pt8),4)


	def redrawAll(self, screen):
		screen.blit(self.background,[0,0])
		#self.noteGroup.draw(screen)

		for cube in self.cube1Lst:
			self.drawCubes(screen,cube,(255,255,255))
		for cube in self.cube2Lst:
			self.drawCubes(screen,cube,(255,0,0)) #red
		for cube in self.cube3Lst:
			self.drawCubes(screen,cube,(0,255,0)) #green
		for cube in self.cube4Lst:
			self.drawCubes(screen,cube,(0,0,255)) #blue

		self.scoreText = self.buttonFont.render("Score:",True,(0,0,0))
		self.scoreNum = self.buttonFont.render(str(self.score),True,(0,0,0))
		screen.blit(self.scoreText,(20,10))
		screen.blit(self.scoreNum,(90,10))

	def run(self):
		clock = pygame.time.Clock()
		screen = pygame.display.set_mode((700, 700))
		# set the title of the window
		pygame.display.set_caption("Falling Piano Tiles")

		# stores all the keys currently being held down
		self._keys = dict()

		# call game-specific initialization
		# print("3")
		# print(self.song)
		self.init(self.song,self.life)

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
			screen.fill(self.bgColor)

			self.redrawAll(screen)
			pygame.display.flip()

		pygame.quit()

#MovingNotes("Nocturne",3).run()

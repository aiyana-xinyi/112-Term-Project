import pygame
from pyGameTechDemo import PygameGame
from Notes import Notes
from Cube import Cube
#from Ike's pyaudio demo
import pyaudio
import wave
from array import array
from struct import pack
import threading

class MovingNotes(PygameGame):
	def init(self):
		self.notes = pygame.sprite.Group()
		self.cube1Lst = []
		self.cube2Lst = []
		self.cube3Lst = []
		self.cube4Lst = []
		self.allCubesLst = [[]]
		self.cubeGroup = pygame.sprite.Group(self.cube1Lst,self.cube2Lst,self.cube3Lst,self.cube4Lst)
		self.timeCount = 0

	def generateRandomCube(self):
		margin = 30
		self.gap = self.width / 4
		self.x1 = 0*self.gap+margin
		self.y1 = 50
		self.cube1 = Cube([self.x1,self.y1],50)
		self.x2 = 1*self.gap+margin
		self.y2 = 50
		self.cube2 = Cube([self.x2,self.y2],50)
		self.x3 = 2*self.gap+margin
		self.y3 = 50
		self.cube3 = Cube([self.x3,self.y3],50)
		self.x4 = 3*self.gap+margin
		self.y4 = 50
		self.cube4 = Cube([self.x4,self.y4],50)


	#taken from pyaudio code
	def playMusic(self,file,rate):
			CHUNK = 1024 #measured in bytes
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
		

	def keyPressed(self,keycode,mod):
		if keycode == pygame.K_SPACE:
			threading.Thread(target = self.playMusic,args = ("River Flows in You.wav",44100)).start()
		if keycode == pygame.K_RIGHT:
			threading.Thread(target = self.playMusic,args = ("River Flows in You.wav",80000)).start()
		if keycode == pygame.K_LEFT:
			threading.Thread(target = self.playMusic,args = ("River Flows in You.wav",30000)).start()
		if keycode == pygame.K_DOWN:
			self.y1 += 20
		if keycode == pygame.K_a:
			Sprite.kill(self.cube1)



	def timerFired(self, dt):
		self.timeCount += 1
		if self.timeCount % 10 == 0:
			for cube in self.cube1Lst:
				

				
			# self.cube1.y += 10
			# self.cube2.y += 10
			# self.cube3.y += 10
			# self.cube4.y += 10
			# self.cube2.myUpdateRect()
			# self.cube1.myUpdateRect()
			# self.cube3.myUpdateRect()
			# self.cube4.myUpdateRect()

			# if self.cube1.y > self.height or self.cube2.y > self.height or\
			# 	self.cube3.y > self.height or self.cube4.y > self.height:
			# 	print("You Lost")

		if self.timeCount % 20 == 0:
			self.cube1Lst.append(self.generateRandomCube())
			self.cube2Lst.append(self.generateRandomCube())
			self.cube3Lst.append(self.generateRandomCube())
			self.cube4Lst.append(self.generateRandomCube())


	def drawCubes(self,screen,Cube,color):
		#draw square 1
		pygame.draw.line(screen,color,(Cube.pt1),(Cube.pt2))
		pygame.draw.line(screen,color,(Cube.pt3),(Cube.pt4))
		pygame.draw.line(screen,color,(Cube.pt1),(Cube.pt3))
		pygame.draw.line(screen,color,(Cube.pt2),(Cube.pt4))
		#draw square 2
		pygame.draw.line(screen,color,(Cube.pt5),(Cube.pt6))
		pygame.draw.line(screen,color,(Cube.pt7),(Cube.pt8))
		pygame.draw.line(screen,color,(Cube.pt5),(Cube.pt7))
		pygame.draw.line(screen,color,(Cube.pt6),(Cube.pt8))
		#draw lines
		pygame.draw.line(screen,color,(Cube.pt1),(Cube.pt5))
		pygame.draw.line(screen,color,(Cube.pt2),(Cube.pt6))
		pygame.draw.line(screen,color,(Cube.pt3),(Cube.pt7))
		pygame.draw.line(screen,color,(Cube.pt4),(Cube.pt8))


	def redrawAll(self, screen):
		#self.noteGroup.draw(screen)
		#screen.blit(self.note1.image, (self.note1.x, self.note1.y))
		#screen.blit(self.note2.image,(self.note2.x,self.note2.y))

		self.drawCubes(screen,self.cube1,(255,0,0))
		self.drawCubes(screen,self.cube2,(0,255,0))
		self.drawCubes(screen,self.cube3,(0,0,255))
		self.drawCubes(screen,self.cube4,(255,255,255))



game = MovingNotes()
game.run()
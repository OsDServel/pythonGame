#Pygame development 1
#Start the basic game set up
#Set up the display

#Pygame development 2
#Set up the game loop
#Use game loop render graphics

#Pygame development 3
#Draw objects to the screen
#Load images into objects

#pygame development 4
#Focus on making code object oriented
#Introduce classes and objects into our code

#Pygame development 5
#Implement game classes
#Implement generic game object class

#Pygame development 6
#Implement game classes
#Implament player character class and movement

#Pygame development 7
#Implement game classes
#Implement enemy character class and bounds checking



#Gain access to the pygame library
import pygame

#size of the screen
SCREEN_TITLE= 'Crossy RPG'
SCREEN_WIDTH= 800
SCREEN_HEIGHT= 800

#colors according to RGB codes
WHITE_COLOR= (255, 255, 255)
BLACK_COLOR= (0, 0, 0)
clock= pygame.time.Clock()

class Game:

	#Typical rate of 60, equivalent to FPS
	TICK_RATE= 60

	def __init__(self, title, width, height):
		self.title= title
		self.width= width
		self.height= height

		#Create the window of specified size in white to display the game
		self.game_screen= pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		#Set the game window color to white
		self.game_screen.fill(WHITE_COLOR)
		pygame.display.set_caption(SCREEN_TITLE)

	def run_game_loop(self):
		is_game_over= False
		direction= 0

		player_character= PlayerCharacter('img/player.png', 375, 700, 50, 50)
		enemy_0=  NonPlayerCharacter('img/enemy.png', 20, 400, 50, 50)

		#Main game loop, used to update all gameplay such as movement, checks, and graphics
		#Runs until is_game_over= True
		while not is_game_over:

			#A loop to get all of the events occuring at any given time
			#events are most often mouse movement, mouse and button clicks, or exit events
			for event in pygame.event.get():
				#If we have a quit type event (exit out) then exit out of the game loop
				if event.type== pygame.QUIT:
					is_game_over= True
				#Detect when key is pressed down
				elif event.type== pygame.KEYDOWN:
					#Move up if up key pressed
					if event.key== pygame.K_UP:
						direction= 1
					#Move down if down key pressed
					elif event.type== pygame.K_DOWN:
						direction= -1
				#Detect when key is released
				elif event.type== pygame.KEYUP:
					#Stop movement when key is no longer pressed
					if event.key== pygame.K_UP or event.key== pygame.K_DOWN:
						direction= 0

				print(event)

			#Redraw the screen to be a blank white window
			self.game_screen.fill(WHITE_COLOR)
			#Update the player position
			player_character.move(direction)
			#Draw the player at the new  position
			player_character.draw(self.game_screen)

			#Update all game graphics
			pygame.display.update()
			#Tick the clock to update everything within the game
			clock.tick(self.TICK_RATE)

#Generic game object class to be subclassed by other objects in the game 
class GameObject:

	def __init__(self, image_path, x, y, width, height):
		#NOTE: make sure to place all image files for PYTHON, within the python folder, ALWAYS	
		# #load player image from the file directory
		object_image= pygame.image.load(image_path)
		# #Scale the image up
		self.image= pygame.transform.scale(object_image, (width, height))

		self.x_pos= x
		self.y_pos= y

		self.width= width
		self.height= height

	#Draw the object by blitting it into the background (game screen)
	def draw(self, background):
			background.blit(self.image, (self.x_pos, self.y_pos))
#Class to represent the character controlled by the player
class PlayerCharacter(GameObject):

	#how many tiles the character moves per second
	SPEED= 10

	def __init__(self, image_path, x, y, width, height):
		#NOTE: when PYTHON's error says "expected an indeted block" just indent the line
		super().__init__(image_path, x, y, width, height)

	#Move function will move character up if direction> 0 and down if< 0
	def move(self, direction):
		# self.y_pos+= direction* SPEED
		if direction> 0:
			self.y_pos-= self.SPEED
		elif direction< 0:
			self.y_pos+= self.SPEED


#Class to represent the enemies moving left and right
class NonPlayerCharacter(GameObject):

	#how many tiles the character moves per second
	SPEED= 10

	def __init__(self, image_path, x, y, width, height):
		#NOTE: when PYTHON's error says "expected an indeted block" just indent the line
		super().__init__(image_path, x, y, width, height)

	#Move function will move enemy left and right
	def move(self, game_screen):
		if self.x_pos<= 20:
			self.SPEED= abs(self.SPEED)
		elif self.x_pos>= game_screen.width- 20:
			self.SPEED= -abs(self.SPEED)
		self.x_pos+= self.SPEED

pygame.init()

new_game= Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()

#Quit pygame and the program
pygame.quit()
quit()



#NOTE: make sure to place all image files for PYTHON, within the python folder, ALWAYS	
# #load player image from the file directory
# player_image= pygame.image.load('player.png')
# #Scale the image up
# player_image= pygame.transform.scale(player_image, (50, 50))
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

#Pygame Development 8
#Implement collision detection
#Detect collions with treasure and enemies

#Pygame development 9
#Add true end game conditions
#Implement specific win and lose conditions

#Pygame development 10
#Make the game more interesting
#Add more enemies and make them move faster

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
pygame.font.init()
font= pygame.font.SysFont('comicsans', 75)

class Game:

	#Typical rate of 60, equivalent to FPS
	TICK_RATE= 60

	#Initializer for the game class to set up the width, height, and title 
	def __init__(self, image_path, title, width, height):
		self.title= title
		self.width= width
		self.height= height

		#Create the window of specified size in white to display the game
		self.game_screen= pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		#Set the game window color to white
		self.game_screen.fill(WHITE_COLOR)
		pygame.display.set_caption(title)

		#background image loading
		background_image= pygame.image.load(image_path)
		#background image Scaling
		self.image= pygame.transform.scale(background_image, (width, height))

	def run_game_loop(self, level_speed):
		is_game_over= False
		did_win= False
		direction= 0

		player_character= PlayerCharacter('img/player.png', 375, 700, 50, 50)
		
		enemy_0=  NonPlayerCharacter('img/enemy.png', 20, 600, 50, 50)
		enemy_0.SPEED*= level_speed

		enemy_1=  NonPlayerCharacter('img/enemy.png', 20, 400, 50, 50)
		enemy_1.SPEED*= level_speed

		enemy_2=  NonPlayerCharacter('img/enemy.png', 20, 200, 50, 50)
		enemy_2.SPEED*= level_speed


		treasure= GameObject('img/treasure.png', 375, 50, 50, 50)

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
					elif event.key== pygame.K_DOWN:
						direction= -1
				#Detect when key is released
				elif event.type== pygame.KEYUP:
					#Stop movement when key is no longer pressed
					if event.key== pygame.K_UP or event.key== pygame.K_DOWN:
						direction= 0

				print(event)

#DRAW section
			#Redraw the screen to be a blank white window
			self.game_screen.fill(WHITE_COLOR)
			#Draw the image onto the background
			self.game_screen.blit(self.image, (0, 0))

			#draw treasure
			treasure.draw(self.game_screen)

			#Update the player position
			player_character.move(direction, self.height)
			#Draw the player at the new  position
			player_character.draw(self.game_screen)
			# Move and draw the enemy character
			enemy_0.move(self.width)
			enemy_0.draw(self.game_screen)



	#DRAWING in more enemies
			if level_speed> 2:
			 enemy_1.move(self.width)
			 enemy_1.draw(self.game_screen)
			if level_speed> 4:
			 enemy_2.move(self.width)
			 enemy_2.draw(self.game_screen)

#COLLISION Detection section, for enemy, and treasure
	#End game if collision between enemy and treasure
	#Close game if we lose
	#Restart gaem loop if we win
			#collision detection for enemy_0
			if player_character.detect_collision(enemy_0):
				is_game_over= True
				did_win= False
				text= font.render('You lose! :(', True, BLACK_COLOR)
				self.game_screen.blit(text, (300, 350))
				pygame.display.update()
				clock.tick(1)
				break

			#collision detection with treasure
			elif player_character.detect_collision(treasure):
				is_game_over= True
				did_win= True
				text= font.render('You win! :)', True, BLACK_COLOR)
				self.game_screen.blit(text, (300, 350))
				pygame.display.update()
				clock.tick(1)
				break


			#Update all game graphics
			pygame.display.update()
			#Tick the clock to update everything within the game
			clock.tick(self.TICK_RATE)

		#Restart game loop if we won
		#Break out of game loop and quit if we lose
		if did_win:
			self.run_game_loop(level_speed+ 0.5)
		else:
			return

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
	def move(self, direction, max_height):
		# self.y_pos+= direction* SPEED
		if direction> 0:
			self.y_pos-= self.SPEED
		elif direction< 0:
			self.y_pos+= self.SPEED
		# # this makes sure that the character does not go past the top of the screen
		if self.y_pos>= max_height -40:
			self.y_pos= max_height -40

#collision code area
	#Retun False (no collision) if Y positions and X positions do not overlap
	#Return Tru X and Y positions overlap
	def detect_collision(self, other_body):
		#if the character position is above the (other_body), no collision
		if self.y_pos> other_body.y_pos+ other_body.height:
			return False
		#if the character position is below the (other_body), no collision
		elif self.y_pos+ self.height< other_body.y_pos:
			return False

		#if the character is to the RIGHT of the (other_body), no collision
		if self.x_pos> other_body.x_pos+ other_body.width:
			return False
		#if the character us to the LEFT of the (other_body), no collision
		elif self.x_pos+ self.width< other_body.x_pos:
			return False
		#if all ELSE FAILS, return TRUE, there IS COLLISION
		return True


#Class to represent the enemies moving left and right
class NonPlayerCharacter(GameObject):

	#how many tiles the character moves per second
	SPEED= 5

	def __init__(self, image_path, x, y, width, height):
		#NOTE: when PYTHON's error says "expected an indeted block" just indent the line
		super().__init__(image_path, x, y, width, height)

	#Move function will move enemy left once it collides with the right side of the screen
	# and move right, once it hits the left side of the screen
	def move(self, max_width):
		if self.x_pos<= 20:
			self.SPEED= abs(self.SPEED)
		elif self.x_pos>= max_width - 40:
			self.SPEED= -abs(self.SPEED)
		self.x_pos+= self.SPEED

pygame.init()

new_game= Game('img/background.png', SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop(1)


#NOTE: make sure to place all image files for PYTHON, within the python folder, ALWAYS	
# #load player image from the file directory
# player_image= pygame.image.load('player.png')
# #Scale the image up
# player_image= pygame.transform.scale(player_image, (50, 50))

#Quit pygame and the program
pygame.quit()
quit()
import xbox
import maestro
import pygame
import random
import drive

# CONSTANTS
# Channels for Servo Controller #1
CH_LEFT_MOTOR  = 1
CH_RIGHT_MOTOR = 0
# Channels for Servo Controller #2
CH_BROW  = 1
CH_YAW   = 1
CH_PITCH = 2


#
# FUNCTIONS
#
def playSnd(file) :
	global channel
	file = "/home/pi/walle/Sounds/" + file
	if file[-3:] == "wav":
		channel.play(pygame.mixer.Sound(file))
	else:
		pygame.mixer.music.load(file)
		pygame.mixer.music.play()

#
# INITIALIZATION
#

# Joystick
j = xbox.Joystick()
# Maestro Controllers
servo = maestro.Controller()
#servo2 = maestro.Controller(2) #serial port 2 for 2nd Maestro unit
# DriveTrain
drivetrain = drive.DriveTrain(servo,CH_RIGHT_MOTOR,CH_LEFT_MOTOR)
# Sound
pygame.mixer.init(22050, -16, 1, 1024)
channel = pygame.mixer.Channel(1)
sounds = [
	"Chatter 2.mp3",
	"Chatter.mp3",
	"Click and squeak.mp3",
	"Hiccup whir.mp3",
	"Walle Name.mp3",
	"Jitters.mp3",
	"Motor whir 2.mp3",
	"Motor whir 3.mp3",
	"Motor whir 4.mp3",
	"Ohhhh.mp3",
	"Oooh 2.mp3",
	"Oooh.mp3"
]


#
# MAIN LOOP
#
try: 
	while True :
		# Drive
		if j.connected():
			drivetrain.drive(j.leftX(), j.leftY())
		else:
			drivetrain.stop()
		# Play Sounds
		if j.B():
			playSnd(sounds[random.randint(0, 11)])
		# Print test results if A button is pressed
		if j.A():
			print(servo.isMoving(0),servo.isMoving(1))
except:
	drivetrain.close()
	servo.close()
	#servo2.close()
	j.close()
	raise

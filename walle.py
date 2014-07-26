import xbox
import maestro
import pygame
import random
import drive
import head
import time
import emotions

# CONSTANTS


# Channels for Servo Controller #1
CH_LEFT_MOTOR  = 1
CH_RIGHT_MOTOR = 0


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
# DriveTrain
drivetrain = drive.DriveTrain(servo,CH_RIGHT_MOTOR,CH_LEFT_MOTOR)
speedtoggle = True # false = slow, true = normal
# Head servo
head = head.Head(servo)
# Emotions
emotion = emotions.Emotions(head)
# Sound
pygame.mixer.init(22050, -16, 1, 1024)
channel = pygame.mixer.Channel(1)
sounds = [
        "Chatter 2.mp3",
	"Motor whir 3.mp3",
	"Jitters.mp3",
	"Motor whir 4.mp3",
	"Ohhhh.mp3",
        "Oooh.mp3",
        "Shakey shakey.mp3",
        "Whir Click.mp3",
        "Whoa 2.mp3"
]


#
# MAIN LOOP
#
print ("Robot Online")
try:
        idleTimer = time.time()  # Timer to determine if we should switch to Idle mode
        idleWait = 0   # Timer value for next idle event occurence
        mode = "manual"
	while True :
		# Drive
		if j.connected():
                        if speedtoggle == True:
                                drivetrain.drive(j.leftX() * .5, -(j.leftY()))
                        else:
                                drivetrain.drive(j.leftX() * .40, -(j.leftY() * .5))
			
		else:
			drivetrain.stop()
                # Head
                
                # if the joystick is centered for 5 seconds, change to idle mode
                #print mode,j.rightX(),j.rightY()
                if abs(j.rightX()) <.1 and abs(j.rightY()) < .1 and abs(j.leftTrigger()) < .1 and abs(j.rightTrigger()) < .1:
                        if time.time() - idleTimer >= 12:
                                mode = "idle"
                else:
                        mode = "manual"
                        idleTimer = time.time()
                # Interactive control
                if mode == "manual":
                        head.moveAbs(j.rightX(), j.rightY())
                        if j.dpadUp():
                                head.lookUp(1)
                                idleTimer = time.time()
                        elif j.dpadDown():
                                head.lookDown(1)
                                idleTimer = time.time()
                        elif j.dpadRight():
                                head.lookRight(1)
                                idleTimer = time.time()
                        elif j.dpadLeft():
                                head.lookLeft(1)
                                idleTimer = time.time()
                        if j.rightTrigger() > .5:
                                head.browUp()
                                idleTimer = time.time()
                        elif j.leftTrigger() > .5:
                                head.browDown()
                                idleTimer = time.time()
                        else:
                                head.browCenter()
                if mode == "idle":
                        # Is it time to start an idle move?
                        if time.time() > idleWait:  
                                idleWait = time.time() + random.randint(2,10) #Next idle event wait time
                                #
                                look = random.randint(1, 17)
                                if look == 1:
                                        head.lookUp()
                                elif look == 2:
                                        head.lookDown()
                                elif look == 3:
                                        head.lookLeft()
                                elif look == 4:
                                        head.lookRight()
                                elif look >=5 and look <= 6:
                                        brow =random.randint(1,3)
                                        if brow == 1:
                                                head.browUp()
                                        if brow == 2:
                                                head.browCenter()
                                        if brow == 3:
                                                head.browDown()
                                elif look >= 7 and look <= 8:
                                        emotion.Outburst()
                                else:
                                        head.lookCentered(0.5)
                #speed Toggle
                if j.Back():
                        speedtoggle = False
                if j.Start():
                        speedtoggle = True
		# Play Sounds
		if j.B():
			playSnd(sounds[random.randint(0, 8)])
		# Print test results if A button is pressed
		if j.Y():
                        idleWait = time.time() + random.randint(2,10) #Next idle event wait time
                        mode = "idle"      
                        if j.leftBumper():
                                if j.rightBumper():
                                        emotion.easterEgg()
                                else:
                                        emotion.intro()
                        else:
                                emotion.intro()
                                
		# Print test results if A button is pressed
		if j.A():
			print(servo.isMoving(0),servo.isMoving(1))
		if j.X():
                        idleWait = time.time() + random.randint(2,10) #Next idle event wait time
                        mode = "idle"
                        emotion.Outburst()
                        
except:
	drivetrain.close()
	servo.close()
	j.close()
	raise

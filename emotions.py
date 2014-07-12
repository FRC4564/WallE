import head
import random
import pygame
import maestro
import xbox
import drive
import time

#VARIABLES


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

class Emotions:
        def __init__(self, head):
                self.head = head

        #
        # EMOTION OPTIONS
        #:
        def happy(self):
            playSnd("Chatter 2.mp3")
            self.head.browCenter()
            self.head.lookCentered()


        def curious(self):
            self.head.lookCentered()
            self.head.browCenter()


        def sad(self):
            playSnd("Ohhhh.mp3")
            self.head.browUp()
            self.head.lookDown()
            self.head.lookLeft()


        def pissed(self):
            playSnd("Motor whir.mp3")
            self.head.browDown()
            self.head.lookCentered()
            playSnd("Jitters.mp3")


        def startled(self):
            playSnd("Whoohoo.mp3")
            self.head.lookCentered()
            self.head.browCenter()

        def intro(self):
            self.head.browDown()
            self.head.lookUp()
            playSnd("Walle Name.mp3")

        # function to select an emotion
        def Outburst(self):
                selectEm = random.randint(0,5)
                if selectEm == 0:
                        self.happy()
                elif selectEm == 1:
                        self.curious()
                elif selectEm == 2:
                        self.sad()
                elif selectEm == 3:
                        self.pissed()
                elif selectEm == 4:
                        self.startled()
                else:
                        self.intro()
                print selectEm

        # BAD WOLF
        def easterEgg(self, egg):
                #if egg == 0:
                
                self.head.lookCentered()
                self.head.browUp()
                playSnd("Shakey shakey.mp3")
                self.head.lookLeft()
                self.head.lookRight()
                self.head.lookLeft()
                self.head.lookRight()
                self.head.lookLeft()
                #Drive in circles, maybe?
                #playSnd("Whoa 2.mp3")
                egg = 1
                #else:
                #        self.intro()

                    
        #Additional Thoughts
                """
                Play the Sad emotion if Wall-E receives no input in a 20 second interval
                play the happy emotion the first time someone moves the left joystick
                play the easterEgg emotion the first time the Y Button is pressed
                        (Preferably pressed after someone says "Alex is driving")
                        easterEgg will cause walle to scream and drive in circles
                        while shaking his head no
                        This emotion will be set to only activate once using a boolean ADR
                
                """

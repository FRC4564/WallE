import maestro

# Servo channels
CH_YAW = 0
CH_PITCH = 1
CH_BROW = 2
# Left/Right yaw constants
YAW_SPEED = 30
YAW_L = 3000
YAW_CL = 5500
YAW_C = 6000
YAW_CR = 6500
YAW_R = 9000
# Up/Down pitch constants
PITCH_SPEED = 20
PITCH_U = 3000
PITCH_CU = 5500
PITCH_C = 6000
PITCH_CD = 6500
PITCH_D = 9000
# Brow Up/Down constants
BROW_SPEED = 60
BROW_U = 7000
BROW_C = 6500
BROW_D = 5500

#
# FUNCTIONS
#


# Test if x is within or on two points of a range
function between(x,limit1,limit2)
        if limit1 < limit2:
                return x >= limit1 and x <= limit2
        else:
                return x >= limit2 and x <= limit1

#
# HEAD CLASS
#

class Head():
        # Provide maestro controller obj
	def __init__(self, maestro):
		self.maestro = maestro

	def isUp(self):
		return between(self.maestro.getPosition(CH_PITCH),PITCH_CU,PITCH_U)

	def isDown(self):

	def isPitchCentered(self):

	def isLeft(self):

	def isRight(self):

	def isYawCentered(self):

	def isBrowUp(self):

	def isBrowDown(self):

	def isBrowCentered(self):

	def isPitchMoving(self):

	def isYawMoving(self):

	def isBrowMoving(self):

	def isHeadMoving(self):

	def movePitch(self, position, speed):

	def moveYaw(self, position, speed):

	def moveBrow(self, position, speed):

	def lookUp(self, speed):

	def lookDown(self, speed):

	def lookLeft(self, speed):
	
	def lookRight(self, speed):

	def lookCentered(self, speed):

	def lookSad(self, speed):

	def lookSurprised(self, speed):
	
	def moveAbs(self, x, y):
		if x >= 0:
			mx = int(x * (YAW_U - YAW_C) + YAW_C)
			maestro.setTarget(CH_YAW, mx)
		else:
			mx = int(YAW_C - x * (YAW_C - YAW_D))
			maestro.setTarget(CH_YAW, mx)
		if y >= 0:
			my = int(y * (PITCH_U - PITCH_C) + PITCH_C)
			maestro.setTarget(CH_PITCH, my)
		else:
			my = int(PITCH_C - y * (PITCH_C - PITCH_D))
			maestro.setTarget(CH_PITCH, my)

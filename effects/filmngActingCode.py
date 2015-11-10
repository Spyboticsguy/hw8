from Myro import *
import effectsCode

init()

def moveCapture():
	motionPicture = []
	while not testForObs(6400):
		#do movement here
		motionPicture.append(takePicture())
	
	#turn 90 degrees (either direction) slowly while capturing pictures
	fps = 10
	frames = fps * 
	for i in range(frames)
def splitCap(seconds, fps):
    frameNum = seconds * fps
	scene1 = []
	scene2 = []
	
    for i in range(frameNum):
        turnLeft(0.25, 0.25)
        scene1.append(takePicture()) 
    for i in range(frameNum):
        turnRight(0.25, 0.25)
        scene2.append(takePicture())
		
	return [scene1, scene2]
	
def testForObs(threshold):
    obs = getObstacle()
    #check each entry in obs
    if (obs[0] >= threshold or obs[1] >= threshold or obs[2] >= threshold):
        return True
    else:
        return False
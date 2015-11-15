###Tristen Allen
###tristen.allen@gatech.edu
###Rasheed Lewis
###rlewis67@gatech.edu
###CS1301 C04
###We worked on this assignment alone,
###using only this semester's course materials.

from Myro import *

#init()

#runs acting and filming 'script' and saves images to multiple files
def main():
    
    #initial picture for fading in
    fadePic = takePicture()
    savePicture(fadePic, "fade.png")
    
    #moves forwards and captures a gif of length 10 seconds
    forwardPic = moveCapture(10, 5, 5)
    savePicture(forwardPic, "forward.gif")
    
    #turns left 90 degrees and captures a gif of length 4 seconds
    turnPic = turnCapture(4, 4)
    savePicture(turnPic, "turn.gif")
    
    #turns left for 50 frames, reverses gif, combines into a 5 second gif
    splitCaps = splitCap(5, 10)
    savePicture(splitCaps[0], "split1.gif")
    savePicture(splitCaps[1], "split2.gif")
    
    #final picture for flashing red
    finalPic = takePicture()
    savePicture(finalPic, "flash.png")
    
def moveCapture(seconds, fps, distTime):
    motionPicture = []
    frames = seconds * fps
    for i in range(frames):
        moveTime = distTime / frames
        forward(0.5, moveTime)
        motionPicture.append(takePicture())
    
    return motionPicture
def turnCapture(seconds, fps):
    motionPicture = []
    frames = seconds * fps
    moveTime = 0.1
    for i in range(frames):
        turnLeft(0.1, moveTime)
        motionPicture.append(takePicture())
        
    return motionPicture
    
def splitCap(seconds, fps):
    frameNum = seconds * fps
    scene1 = []
    scene2 = []
	
    for i in range(frameNum):
        turnLeft(0.25, 0.25)
        scene1.append(takePicture())
    
    scene2 = scene1[::-1]
		
    return [scene1, scene2]

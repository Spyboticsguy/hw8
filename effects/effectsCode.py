#Tristen Allen
#tristen.allen@gatech.edu 903035156
#Rasheed Lewis
#rlewis67@gatech.edu 903138303
#We worked on this homework assignment alone,
#using only this semester's course materials.
from Myro import *

#function that applies effects. Requires filmingCode.main() to have been run already.
#or for its generated files to be present in the "filming" directory
def main():
    fadeOrig = makePicture("../filming/fade.png")
    splitOrig = [loadPictures("../filming/split1.gif"), loadPictures("../filming/split2.gif")]
    flashOrig = makePicture("../filming/flash.png")
    
    fadePic = fadeTrans(fadeOrig, True)
    splitPic = splitTrans(splitOrig[0], splitOrig[1])
    flashPic = redTrans(flashOrig)
    
    savePicture(fadePic, "processed/fade.gif")
    savePicture(splitPic, "processed/split.gif")
    savePicture(flashPic, "processed/flash2.png")
    
def fadeTrans(p, reverse):
    fadeGif = [copyPicture(p)]
    
    for i in range(19):
        newPic = copyPicture(fadeGif[i])
        for pixel in getPixels(newPic):
            r,g,b = getRGB(pixel)
            r -= 13
            g -= 13
            b -= 13
            
            if r < 0:
                r = 0
            if g < 0:
                g = 0
            if b < 0:
                b = 0
            
            setColor(pixel, makeColor(r,g,b))
        fadeGif.append(newPic)
        
    if reverse == True:
        reversedGif = fadeGif[::-1]
        return reversedGif
    else:
        return fadeGif

def splitTrans(scene1, scene2):
    splitScene = [] 
    picHalf = getWidth(scene1[0]) // 2

    for i in range(len(scene1)):
        rightSide = copyPicture(scene2[i])
        
        for pixel in getPixels(scene1[i]):
            if getX(pixel) <= picHalf:
                r,g,b = getRGB(pixel)
                oldPixel = getPixel(rightSide, getX(pixel), getY(pixel))
                
                setRed(oldPixel, r)
                setGreen(oldPixel, g)
                setBlue(oldPixel, b)
        splitScene.append(rightSide)
        
    return splitScene

def redTrans(p):
    for pixel in getPixels(p):
        setRed(pixel, getRed(pixel) + 50)

    return p

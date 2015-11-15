#Tristen Allen
#tristen.allen@gatech.edu 903035156
#Rasheed Lewis
#add yourself
#We completed this homework assignment alone, using only
#this semester's course materials.

from Myro import *
#function that displays the movie - RUN THIS to check homework,
#Takes optional parameter 'music' - set to False to turn off music
def perform(music=True):
    #LIST FORMAT: tuple (filename, frame length, gif)
    movieClips = []
    name = "Survey and Capture"
    #initialize some variables for order of pictures, length, gif, etc
    movieClips.append(("effects/processed/fade.gif", 0.1, True))
    movieClips.append(("filming/forward.gif", 0.2, True))
    movieClips.append(("filming/turn.gif", 0.2, True))
    movieClips.append(("effects/processed/split.gif", 0.1, True))
    for i in range(3):
        movieClips.append(("effects/processed/flash2.png", 1, False))
        movieClips.append(("filming/flash.png", 1, False))
    if music:
        play("performance/music.wav")
    
    for picture in movieClips:
        delay = picture[1]
        
        if picture[2]:
            clip = loadPictures(picture[0])
        else:
            clip = [makePicture(picture[0])]
        
        for i in clip:
            show(i, name)
            wait(delay)
        
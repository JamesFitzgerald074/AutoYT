import getMaterials
import render
import os
from moviepy.editor import VideoFileClip

os.chdir('sample') #for testing

def makeVideo(vidName, vidFileList): #method for making final video from enriched clips
    vidList = []
    for vid in vidFileList:
        vidList.append(VideoFileClip(vid))
    render.combineClips(vidList, vidName)
    return vidList

def enrichClipSet(clipDict): #passed a dictionary with the title as the key and the clip as the value
    for clipName, clipFile in clipDict.items():
        getMaterials.makeAudio(clipName, clipName+'.mp3')
        render.enrichClip(clipName, clipName + '.mp3', clipFile, 'ENR'+clipFile)

#example of
#testVidList = ['ENRThor.mp4', 'ENRmoviepy_sample.mp4', 'Thor.mp4']
#makeVideo('makevideoTest.mp4', testVidList)

#testDict = {'OHHHH my, it works':'initial_test.mp4'} #Exxample dict for endrichClipSet
#enrichClipSet(testDict)

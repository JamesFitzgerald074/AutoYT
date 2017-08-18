import getMaterials
import render
import os
from moviepy.editor import VideoFileClip

def makeVideo(vidName, vidFileDict): #method for making final video from enriched clips
    vidList = []
    for vidName, vid in vidFileDict.items:
        vidList.append(VideoFileClip(vid))
    render.combineClips(vidList, vidName)

#makeVideo test
#testVidList = ['ENRThor.mp4', 'ENRmoviepy_sample.mp4', 'Thor.mp4']
#makeVideo('makevideoTest.mp4', testVidList)

def enrichClipSet(clipDict): #passed a dictionary with the title as the key and the clip as the value
    posNum = len(clipDict)
    for clipName, clipFile in clipDict.items():
        getMaterials.makeAudio(clipName, clipName+'.mp3')
        render.enrichClip(clipName, clipName + '.mp3', clipFile, 'ENR' + clipFile, clipNum=posNum)
        posNum -= 1
        clipDict[clipName] = 'ENR' + clipFile
    return clipDict

#testDict = {'WOW':'initial_test.mp4'} #Exxample dict for endrichClipSet
#enrichClipSet(testDict)

def makeDict(listSrc):
    outDict = {}
    for s in listSrc:
        outDict[s] = ''
    return outDict

#print(makeDict(testVidList))

def getContent(searchDict):
    for peice in searchDict:
        links = getMaterials.getYT(peice + ' clip')#TODO remove temporary clip search modifier
        searchDict[peice] = peice + '.mp4'
        for link in links:
            if getMaterials.downloadVid(link, searchDict[peice]):
                break
    return searchDict

os.chdir('sample') #for testing
test = {'Iron Man':'Iron Man.mp4',
        'Thor':'Thor.mp4',
        'Dr Strange': 'Dr Strange.mp4'}
testDict = enrichClipSet(test)
print(testDict)
makeVideo("top3Marvel.mp4",testdict)

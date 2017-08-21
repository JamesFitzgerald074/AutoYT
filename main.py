import getMaterials
import render
import os
from moviepy.editor import VideoFileClip

def makeVideo(outVidName, vidFileDict): #method for making final video from enriched clips
    vidList = []
    for vidName, vid in vidFileDict.items():
        vidList.append(VideoFileClip(vid))
    return render.combineClips(vidList, outVidName)

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
    for s in reversed(listSrc):
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

def makeCompleteVideo(videoList, vidTitle, vidDir):
    os.chdir(vidDir)
    videoDict = makeDict(videoList)
    videoDict = getContent(videoDict)
    videoDict = enrichClipSet(videoDict)
    return makeVideo(vidTitle + '.mp4', videoDict)

#test = ['Iron Man','Thor','Dr Strange']
#testDict = makeDict(test)
#os.chdir('sample') #for testing
#print(testDict)
#testDict = getContent(testDict)
#print(testDict)
#testDict = enrichClipSet(testDict)
#print(testDict)
#print(makeVideo("top3Marvel.mp4",testDict))

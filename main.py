import getMaterials
import render
import os
import collections #for OrderedDict
from moviepy.editor import VideoFileClip

def makeFinalVideo(outVidName, vidFileDict): #method for making final video from enriched clips
    vidList = []
    for vidName, vid in vidFileDict.items():
        vidList.append(VideoFileClip(vid))
    return render.combineClips(vidList, outVidName)


def enrichClipSet(clipDict): #passed a dictionary with the title as the key and the clip as the value
    posNum = len(clipDict) - 1
    for clipName, clipFile in clipDict.items():
        if clipName[0] == '.':
            pass
        getMaterials.makeAudio(clipName, clipName+'.mp3')
        render.enrichClip(clipName, clipName + '.mp3', clipFile, 'ENR' + clipFile, clipNum=posNum)
        posNum -= 1
        clipDict[clipName] = 'ENR' + clipFile
    return clipDict

def makeDict(listSrc):
    outDict = collections.OrderedDict()
    for s in listSrc:
        if s[0] == '#':
            outDict[s] = s[1:]
        outDict[s] = ''
    return outDict

def getContent(searchDict):
    for peice in searchDict:
        if peice[0] == '.':
            render.makeTitle(peice[1:])
            searchDict[peice] = peice[1:] + 'mp4'
            pass
        links = getMaterials.getYT(peice + ' trailer')#TODO remove temporary clip search modifier
        searchDict[peice] = peice + '.mp4'
        for link in links:
            if getMaterials.downloadVid(link, searchDict[peice]):
                print('downloading ' + searchDict[peice])
                break
    return searchDict

def makeVideo(videoDict, vidTitle):
    videoDict = getContent(videoDict)
    videoDict = enrichClipSet(videoDict)
    makeFinalVideo(vidTitle + '.mp4', videoDict)

def makeList(inFile):
    with open(inFile) as f:
        return f.read().splitlines()

def listVideo(listVidFolder):
    os.chdir(listVidFolder)
    listFile = '#list'
    videoList = makeList(listFile)
    videoDict = makeDict(videoList)
    print(videoDict)
    videoTitle = list(videoDict.items())[0][0][1:] #messy way to get title from ordered dict
    makeVideo(videoDict, videoTitle)

listVideo('#0TEST')

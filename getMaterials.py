import requests
import lxml
from bs4 import BeautifulSoup
import urllib

from pytube import YouTube #Youtube download

from gtts import gTTS #TTS(Text To Speech)
import os

import json
import isodate #converting iso durations to seconds

import apiKeys

def getYT(search):
    #Returns a list with all youtbe video links
    url = 'http://www.youtube.com/results?search_query='
    YTwatchURL = 'http://www.youtube.com'
    links = []
    r = requests.get(url + search)
    soup = BeautifulSoup(r.text,'lxml')
    try:
        #all links in the youtube search
        souplinks = soup.findAll(attrs={'class':'yt-uix-tile-link'})
    except:
        #in case its empty
        return []
    for vid in souplinks:
        vidLink = vid['href']
        #have to remove user profiles and playlists from results
        if '/user/' not in vidLink and 'list=' not in vidLink:
            #testing for
            maxLength = 360 #6min video
            YTvidLength = getYTLength(vidLink)
            if YTvidLength < maxLength:
                links.append(YTwatchURL + vidLink)
            else:
                print('[*]video too long')
    return links

def getYTLength(vidCode):
    searchUrl = "https://www.googleapis.com/youtube/v3/videos?id="+vidCode+"&key="+api_key+"&part=contentDetails"
    response = urllib.request.urlopen(searchUrl).read()
    data = json.loads(response.decode('utf-8'))
    all_data = data['items']
    contentDetails = all_data[0]['contentDetails']
    duration = contentDetails['duration']
    parseDur = isodate.parse_duration(duration)
    return int(parseDur.total_seconds())

def downloadVid(videoLink, filename):#saves video to CWD
    YT = YouTube(videoLink)
    YT.set_filename(filename)
    try:
        video = YT.get('mp4','720p')
        video.download(filename)
        return True
    except:
        return False

def makeAudio(speechText, filename):
    try:
        tts = gTTS(text=speechText, lang='en')
        tts.save(filename)
        return True
    except:
        return False


#earch = input('> ')
#print(getYTlink(search))
#stuff = makeAudio('this works welcome to vid salsa', 'vidsalsa.mp3','/home/aimless/Top10/test')
#print(stuff)
#downloadVid(['http://www.youtube.com/watch?v=X4j-MUZRq0g'],'bleh','/home/aimless/Top10')

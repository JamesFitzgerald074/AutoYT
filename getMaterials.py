import requests, lxml, urllib
from bs4 import BeautifulSoup


from pytube import YouTube #Youtube download

from gtts import gTTS #TTS(Text To Speech)
import os

import json, isodate #converting iso durations to seconds

import apiKeys #.py file with apikeys as variables

def getYT(search):
    """Returns a list with all youtube video links related to search parameter"""
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
            try:
                YTvidLength = getYTLength(vidLink)
            except: YTvidLength = 100
            if YTvidLength < maxLength:
                links.append(YTwatchURL + vidLink)
            else:
                print('[*]video too long')
    return links

def getYTLength(vidCode):
    """request video for data for video total length"""
    searchUrl = "https://www.googleapis.com/youtube/v3/videos?id="+vidCode+"&key="+ apiKeys.api_key +"&part=contentDetails"
    response = urllib.request.urlopen(searchUrl).read()
    #parse response
    data = json.loads(response.decode('utf-8'))
    all_data = data['items']
    contentDetails = all_data[0]['contentDetails']
    #find and parse duration
    duration = contentDetails['duration']
    parseDur = isodate.parse_duration(duration)
    return int(parseDur.total_seconds())

def downloadVid(videoLink, filename):#saves video to CWD
    """Downlaods youtube video from link and filename"""
    YT = YouTube(videoLink)
    YT.set_filename(filename)
    try:
        video = YT.get('mp4','720p')
        video.download(filename)
        return True
    except:
        return False

def makeAudio(speechText, filename):
    """makes TTS audio from a string and then sves the output as an mp3 to a given filename"""
    try:
        tts = gTTS(text=speechText, lang='en')
        tts.save(filename)
        return True
    except:
        return False

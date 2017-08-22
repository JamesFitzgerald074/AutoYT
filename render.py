from moviepy.editor import * 

def cutClip(outClip):#Takes source clip and cuts it to a usable size EG 1 min
    if outClip.duration > 80:
        outClip = outClip.subclip(t_start=10,t_end=30)
    return outClip


def enrichClip(overlayText, audioClipPath, inputClipPath, outputClipName, clipNum=0):
    vClip = VideoFileClip(inputClipPath, audio=False)
    aClip = AudioFileClip(audioClipPath)
    vClip = cutClip(vClip)

    w,h = moviesize = vClip.size#vclips dimensions w, hs
    vClip = (vClip.set_audio(aClip))#Brings together the video and audio clips
    #create text clip
    txt = TextClip(overlayText, font='Amiri-regular',
    	               color='white',fontsize= 70).set_duration(23)
    #puts text clip on and object
    #makes a colour shape to place the text on
    #color is a RGB
    txt_col = txt.on_color(size=(vClip.w + txt.w,txt.h-10),
                      color=(0,0,0), pos=(6,'center'), col_opacity=0.6)
    #lamda calculation frame by frame for the position of the text on the screen
    txt_mov = txt_col.set_pos( lambda t: (max(w/30,int(w-0.5*w*t)),
                                      max(5*h/6,int(100*t))) )

    clipFinal = CompositeVideoClip([vClip, txt_mov])# Composite clips
    #if clipNum is at its default it will not add a numbered clip before it
    if clipNum:
        num_clip = TextClip(str(clipNum), fontsize=100, color='green').set_duration(3)
        clipFinal = concatenate_videoclips([num_clip, clipFinal], method='compose')
    clipFinal.write_videofile(outputClipName, fps=30, codec='libx264')
    #remove uneeded video objects from memory
    del vClip, aClip, txt, txt_col, txt_mov, clipFinal
    return True

def combineClips(vidList, outputClipName):#Concatrates list of videoObjects in CWD
    outputClip = concatenate_videoclips(vidList, method='compose')
    outputClip.write_videofile(outputClipName, fps=30, codec='libx264')
    return True

def makeTitle(text):
    txt = TextClip(str(text), fontsize=60, color='green').set_duration(3)
    txt.write_videofile(text + '.mp4', fps=5, codec='libx264')

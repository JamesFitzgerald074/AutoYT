from moviepy.editor import *   #TODO only import things in use

def cutClip(outClip):#Takes source clip and cuts it to a usable size EG 1 min
    #clip = VideoFileClip(clipName)
    if outClip.duration > 80:
        outClip = outClip.subclip(t_start=10,t_end=30)
    return outClip


def enrichClip(overlayText, audioClipPath, inputClipPath, outputClipName, clipNum=0):
    nclip = VideoFileClip(inputClipPath, audio=False)
    aclip = AudioFileClip(audioClipPath)
    vclip = cutClip(nclip)
    #print(vclip.duration)
    #vclips dimensions w, hs
    w,h = moviesize = vclip.size
    #creates text clip
    #Brings together the video and audio clips
    vaclip = (vclip.set_audio(aclip))

    txt = TextClip( overlayText, font='Amiri-regular',
    	               color='white',fontsize= 70).set_duration(23)
    #puts text clip on and object
    #makes a colour shape to place the text on
    #color is a RGB numpy array
    txt_col = txt.on_color(size=(vclip.w + txt.w,txt.h-10),
                      color=(0,0,0), pos=(6,'center'), col_opacity=0.6)
    #???
    txt_mov = txt_col.set_pos( lambda t: (max(w/30,int(w-0.5*w*t)),
                                      max(5*h/6,int(100*t))) )
    # Composite clips
    clipFinal = CompositeVideoClip([vaclip, txt_mov])
    if clipNum:
        num_clip = TextClip(str(clipNum), fontsize=60, color='green').set_duration(2)
        final = concatenate_videoclips([num_clip, clipFinal], method='compose')
    final.write_videofile(outputClipName, fps=30, codec='libx264')
    return True

def combineClips(vidList, outputClipName):#Concatrates list of videoObjects in CWD
    #try:
    print(vidList)
    outputClip = concatenate_videoclips(vidList, method='compose')
    #except:
        #return 'failed concatenate_videoclips'
    #try:
    outputClip.write_videofile(outputClipName, fps=30, codec='libx264')
    #except:
    return True

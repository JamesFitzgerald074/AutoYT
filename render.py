from moviepy.editor import *

def cutClip(inClip):#Takes source clip and cuts it to a usable size EG 1 min
    #clip = VideoFileClip(clipName)
    if inClip.duration > 80:
        outClip = inClip.subclip(t_start=10,t_end=80)
    return outClip


def enrichClip(overlayText, audioClipPath, inputClipPath, outputClipName):
    nclip = VideoFileClip(inputClipPath, audio=False)
    aclip = AudioFileClip(audioClipPath)
    vclip = cutClip(nclip)
    print(vclip.duration)
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
    final = CompositeVideoClip([vaclip, txt_mov])
    final.write_videofile(outputClipName, fps=30, codec='libx264')
    return True

def stitchClips(vidList, outputClipName):#Concatrates list of videoObjects in CWD
    try:
        outputClip = concatenate_videoclips(vidList)
        outputClip.write_videofile(outputClipName)
        return True
    except:
        return False

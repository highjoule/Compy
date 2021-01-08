#!/usr/bin/env python
# coding: utf-8

# 
# # submysrs
# 
# ## This code makes a black video with large subtitles from a chosen folder
# 
# ### Files localization
# 
# This code is designed to make work with a `for` cycle in a folder with more that one `.srt` extension.
# 
# The next block uses Tkinter to pop up the explorer window to choose the folder.
# 
# 
# 
#     

# In[ ]:


try:
    import Tkinter as tk#this error detection is uses this error detector because sometimes Tkinter is used instead of tkinter
except:
    import tkinter as tk
import glob
from tkinter.filedialog import askdirectory

def fileloc():    
    tk.Tk().withdraw()#with this we close the GUI window from this function
    path=askdirectory()#ask for the folder location
    lista = glob.glob1(path,'*.srt')#a file with a .srt are stored in this variable
    listasub = []#store all the subtitles files in this list
    listavid = []#create the name and path for the subtitles videos
    for x in lista:#cycle that stored every sub file and creates its video file name
        listasub.append(path + '/'+x)
        listavid.append(path+'/'+x[:-4]+'.mp4')
    return listasub,listavid,path#return the file names and the path of the folder


# In[ ]:


lista = fileloc()#run fileloc
subloc = lista[0]#store the subtitles filenames in lista with subindex 0
vidloc = lista[1]#store the video filenames in lista with subindex 1


# ### Longest video
# 
# Since this is aimed for a folder with videos of more or less similar length, this function will determinate the longest video to create the background video in a later code. This function will return the longest second count plus 60 seconds just for the fun of it.
# 
# **NOTE:** The font choosen is Goergia Regular, although some characters from other languages may not be supported under this font so some cities or last names may display weirdly. 

# In[ ]:


from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip


def longestvideo(subloc):
    lsaux = []#auxiliar variable to store one videolegth at a time
    for x in subloc:#cycle that will compare all the videos
        generator = lambda txt: TextClip(txt, font='Georgia-Regular', fontsize=27, color='white')#properties of the text
        sub = SubtitlesClip(x,generator)# makes the sub readable
        last=sub[-1]# reads the last time interval
        tint=last[0]# takes the last time from the previous interval
        lsaux.append(tint[1])#stores the time count in a list
    return max(lsaux)+60#returns the highest number in the list


# ### Background video creation
# 
# The creation of one video background takes the path of the folder and will generate a video with black background and the length of the longest video taken from the subtitles.
# 
# **Size:** Depending on the screen of the resolution of the monitor one can change the size of the pixels, however change of the subtitles properties should be adjusted as well.
# 
# **Color:** Same case with color, one can change the background to any color however the subtitles text properties should be change.

# In[ ]:


size = (600, 300)
duration=longestvideo(subloc)
bckloc = lista[2]+'/background.mp4'

def background(size, duration, fps=25, color=(0,0,0),output=bckloc):
    ColorClip(size, color, duration=duration).write_videofile(output, fps=fps)

background(size,duration)


# ### Merging of background video and subtitles text
# 
# Next function takes the black background video and generates the text on it with the properties defined.

# In[ ]:


from moviepy.video.io.VideoFileClip import VideoFileClip

def makevideo(subloc,vidloc,bckloc):
    generator = lambda txt: TextClip(txt, font='Georgia-Regular', fontsize=27, color='white')
    sub = SubtitlesClip(subloc,generator)
    vid = VideoFileClip(bckloc)
    final = CompositeVideoClip([vid,sub.set_pos(('center','center'))])
    final.write_videofile(vidloc,fps=vid.fps)


# ### Production of all videos
# 
# With the code below is possible to make all the video included in the folder selected.

# In[ ]:


i=0
for x in lista[0]:
    makevideo(lista[0][i],lista[1][i],bckloc)
    i+=1
    


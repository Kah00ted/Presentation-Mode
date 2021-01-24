# get status: defaults read com.apple.finder CreateDesktop
# set status: defaults write com.apple.finder CreateDesktop -bool TRUE; killall Finder
import os
import tkinter
from tkinter import messagebox

def setPresentationMode(torf):
    if (torf == True):
        # This code is to hide the main tkinter window
        root = tkinter.Tk()
        root.withdraw()

        # Message Box
        finderAsk = messagebox.askokcancel("Warning", "All finder windows will be closed and some unsaved files may be deleted.", default="cancel", icon='warning')
        if finderAsk == True:
            print ("ok")
        

def setDesktopIcons(value):
    if (value == False):
        os.system('defaults write com.apple.finder CreateDesktop -bool FALSE; killall Finder')
    if (value == True):
        os.system('defaults write com.apple.finder CreateDesktop -bool True; killall Finder')

setDesktopIcons(True)

def closeApps():
    print("closing apps")
    #os.kill("brave")
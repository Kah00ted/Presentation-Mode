# get status: defaults read com.apple.finder CreateDesktop
# set status: defaults write com.apple.finder CreateDesktop -bool TRUE; killall Finder
import os
import tkinter
from tkinter import messagebox

def setPresentationMode(torf):
    if (torf == True): #setPresentationMode(True)
        setDesktopIcons(False)

    elif (torf == False):
        setDesktopIcons(True)
        

def setDesktopIcons(value):
    if (value == False):
        os.system('defaults write com.apple.finder CreateDesktop -bool FALSE; killall Finder')
    if (value == True):
        os.system('defaults write com.apple.finder CreateDesktop -bool True; killall Finder')

def closeApps():
    print("closing apps")
    #os.kill("brave")

#setPresentationMode(True)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.3),
    on octubre 11, 2022, at 22:03
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.3'
expName = 'BananaMonkey'  # from the Builder filename that created this script
expInfo = {'Participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['Participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\David\\Documents\\GitHub\\OpenBrains\\Monkey_game\\task\\BananaMonkey.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1366, 768], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1.000,-1.000,-1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='norm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "title"
titleClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='imagenes/Title.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
Bienvenida = visual.TextStim(win=win, name='Bienvenida',
    text='Bienvenido a nuestro experimento!\n\nPulsa start para empezar',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "Game"
GameClock = core.Clock()
spin = 0
TitleW = 0
TitleH = 0
xpos = 0
ypos = -0.5
Bhoz = 0
Bver = 1.5
splatpos = 2
SadFace = 0
HappyFace = 0
munch = 0
splat = 0
count = 0

MonkeyMouse = event.Mouse(win=win)
x, y = [None, None]
MonkeyMouse.mouseClock = core.Clock()
Banana = visual.ImageStim(
    win=win,
    name='Banana', units='norm', 
    image='banana.png', mask=None,
    ori=0, pos=[0,0], size=(0.15, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
SplatBanana = visual.ImageStim(
    win=win,
    name='SplatBanana', units='norm', 
    image='bansplat.png', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
Munch = sound.Sound('munch.wav', secs=-1, stereo=True, hamming=True,
    name='Munch')
Munch.setVolume(1)
Splat = sound.Sound('splat.wav', secs=-1, stereo=True, hamming=True,
    name='Splat')
Splat.setVolume(1)
MonkeyMouth = visual.ImageStim(
    win=win,
    name='MonkeyMouth', units='norm', 
    image='monkey.png', mask=None,
    ori=0, pos=[0,0], size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
MonkeyHappy = visual.ImageStim(
    win=win,
    name='MonkeyHappy', units='norm', 
    image='monkeymunch.png', mask=None,
    ori=0, pos=[0,0], size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
MonkeySad = visual.ImageStim(
    win=win,
    name='MonkeySad', units='norm', 
    image='monkeyno.png', mask=None,
    ori=0, pos=[0,0], size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)

# Initialize components for Routine "End"
EndClock = core.Clock()
Adios = visual.TextStim(win=win, name='Adios',
    text='Muchas gracias por participar',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "title"-------
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
titleComponents = [image]
for thisComponent in titleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
titleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "title"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = titleClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=titleClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    if image.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            image.tStop = t  # not accounting for scr refresh
            image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
            image.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in titleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "title"-------
for thisComponent in titleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)

# ------Prepare to start Routine "Instructions"-------
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
# keep track of which components have finished
InstructionsComponents = [Bienvenida, key_resp]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Bienvenida* updates
    if Bienvenida.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Bienvenida.frameNStart = frameN  # exact frame index
        Bienvenida.tStart = t  # local t and not account for scr refresh
        Bienvenida.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Bienvenida, 'tStartRefresh')  # time at next scr refresh
        Bienvenida.setAutoDraw(True)
    if Bienvenida.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Bienvenida.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            Bienvenida.tStop = t  # not accounting for scr refresh
            Bienvenida.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Bienvenida, 'tStopRefresh')  # time at next scr refresh
            Bienvenida.setAutoDraw(False)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp.keys = theseKeys.name  # just the last key pressed
            key_resp.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Bienvenida.started', Bienvenida.tStartRefresh)
thisExp.addData('Bienvenida.stopped', Bienvenida.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Game"-------
# update component parameters for each repeat
timer = core.Clock()

# setup some python lists for storing info about the MonkeyMouse
gotValidClick = False  # until a click is received
Munch.setSound('munch.wav', hamming=True)
Munch.setVolume(1, log=False)
Splat.setSound('splat.wav', hamming=True)
Splat.setVolume(1, log=False)
# keep track of which components have finished
GameComponents = [MonkeyMouse, Banana, SplatBanana, Munch, Splat, MonkeyMouth, MonkeyHappy, MonkeySad]
for thisComponent in GameComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
GameClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Game"-------
while continueRoutine:
    # get current time
    t = GameClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=GameClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    #spin the title 360 degrees at a rate of 4 unite per frame#
    if spin < 360:
        spin = spin + 4
    else:
        spin = 360
    
    #increase the width of the title by 0.05 units per frame until it reaches 1.5#
    if TitleW < 1.5: 
        TitleW = TitleW + 0.05 
    else:
        TitleW = 1.5 
    
    #increase the height of the title by 0.02 units per frame until it reaches 0.6#
    if TitleH < 0.6: 
        TitleH = TitleH+ 0.02 
    else: 
        TitleH = 0.6  
        
    #set the monkey to move with the mouse#
    xpos = (MonkeyMouse.getPos()[0]) 
    
    #tell the banana to drop at a rate on 0.02 units between 7 and 25 secs#
    if (0.1 < timer.getTime() < 60): 
        Bver = Bver - 0.02 
    else:
        Bver = 1.5 
    
    
    #what to do if the banana overlaps the monkey#
    if ((Bver < -0.5) and ((xpos-0.2) <= Bhoz <= (xpos+0.2))): 
        HappyFace = 1 
        munch = 1
        Bver = 1.4
        Bhoz = 0.1*(randint(-8,9))
    
    if Bver < -0.5: 
         splatpos = Bhoz
         splat =  1
         SadFace = 1
         Bver = 1.4
         Bhoz = 0.1*(randint(-8,9))  
    
    
    
    if Bver < 0.4:
        splatpos = 2 
     
    if Bver < 1: 
        HappyFace = 0
        SadFace = 0
        
        
    if 0.5 < Bver < 1:
        splat =  0
        munch = 0
    
    
    
    #set final chat #
    FinalChat = f'Well done! \n You helped the monkey eat \n {munch} bananas!'
    
    if (timer.getTime()>=60):
        continueRoutine = False
    # *MonkeyMouse* updates
    if MonkeyMouse.status == NOT_STARTED and t >= 0-frameTolerance:
        # keep track of start time/frame for later
        MonkeyMouse.frameNStart = frameN  # exact frame index
        MonkeyMouse.tStart = t  # local t and not account for scr refresh
        MonkeyMouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MonkeyMouse, 'tStartRefresh')  # time at next scr refresh
        MonkeyMouse.status = STARTED
        MonkeyMouse.mouseClock.reset()
        prevButtonState = MonkeyMouse.getPressed()  # if button is down already this ISN'T a new click
    if MonkeyMouse.status == STARTED:  # only update if started and not finished!
        buttons = MonkeyMouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *Banana* updates
    if Banana.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Banana.frameNStart = frameN  # exact frame index
        Banana.tStart = t  # local t and not account for scr refresh
        Banana.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Banana, 'tStartRefresh')  # time at next scr refresh
        Banana.setAutoDraw(True)
    if Banana.status == STARTED:  # only update if drawing
        Banana.setPos((Bhoz,Bver), log=False)
    
    # *SplatBanana* updates
    if SplatBanana.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        SplatBanana.frameNStart = frameN  # exact frame index
        SplatBanana.tStart = t  # local t and not account for scr refresh
        SplatBanana.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(SplatBanana, 'tStartRefresh')  # time at next scr refresh
        SplatBanana.setAutoDraw(True)
    if SplatBanana.status == STARTED:  # only update if drawing
        SplatBanana.setPos((splatpos,-0.5), log=False)
    # start/stop Munch
    if Munch.status == NOT_STARTED and munch == 1:
        # keep track of start time/frame for later
        Munch.frameNStart = frameN  # exact frame index
        Munch.tStart = t  # local t and not account for scr refresh
        Munch.tStartRefresh = tThisFlipGlobal  # on global time
        Munch.play(when=win)  # sync with win flip
    # start/stop Splat
    if Splat.status == NOT_STARTED and splat == 1:
        # keep track of start time/frame for later
        Splat.frameNStart = frameN  # exact frame index
        Splat.tStart = t  # local t and not account for scr refresh
        Splat.tStartRefresh = tThisFlipGlobal  # on global time
        Splat.play(when=win)  # sync with win flip
    
    # *MonkeyMouth* updates
    if MonkeyMouth.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        MonkeyMouth.frameNStart = frameN  # exact frame index
        MonkeyMouth.tStart = t  # local t and not account for scr refresh
        MonkeyMouth.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MonkeyMouth, 'tStartRefresh')  # time at next scr refresh
        MonkeyMouth.setAutoDraw(True)
    if MonkeyMouth.status == STARTED:  # only update if drawing
        MonkeyMouth.setPos((xpos,ypos), log=False)
    
    # *MonkeyHappy* updates
    if MonkeyHappy.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        MonkeyHappy.frameNStart = frameN  # exact frame index
        MonkeyHappy.tStart = t  # local t and not account for scr refresh
        MonkeyHappy.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MonkeyHappy, 'tStartRefresh')  # time at next scr refresh
        MonkeyHappy.setAutoDraw(True)
    if MonkeyHappy.status == STARTED:  # only update if drawing
        MonkeyHappy.setOpacity(HappyFace, log=False)
        MonkeyHappy.setPos((xpos,ypos), log=False)
    
    # *MonkeySad* updates
    if MonkeySad.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        MonkeySad.frameNStart = frameN  # exact frame index
        MonkeySad.tStart = t  # local t and not account for scr refresh
        MonkeySad.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MonkeySad, 'tStartRefresh')  # time at next scr refresh
        MonkeySad.setAutoDraw(True)
    if MonkeySad.status == STARTED:  # only update if drawing
        MonkeySad.setOpacity(SadFace, log=False)
        MonkeySad.setPos((xpos,ypos), log=False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GameComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Game"-------
for thisComponent in GameComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
Munch.stop()  # ensure sound has stopped at end of routine
Splat.stop()  # ensure sound has stopped at end of routine
# the Routine "Game" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "End"-------
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndComponents = [Adios]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "End"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Adios* updates
    if Adios.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Adios.frameNStart = frameN  # exact frame index
        Adios.tStart = t  # local t and not account for scr refresh
        Adios.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Adios, 'tStartRefresh')  # time at next scr refresh
        Adios.setAutoDraw(True)
    if Adios.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Adios.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            Adios.tStop = t  # not accounting for scr refresh
            Adios.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Adios, 'tStopRefresh')  # time at next scr refresh
            Adios.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Adios.started', Adios.tStartRefresh)
thisExp.addData('Adios.stopped', Adios.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.3),
    on octubre 19, 2022, at 09:01
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
    originPath='C:\\Users\\David\\Documents\\GitHub\\OpenBrains\\Square_game2_new\\task\\SquareDot2.py',
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

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
Bienvenida = visual.TextStim(win=win, name='Bienvenida',
    text='        ¡Bienvenido a nuestro juego!\n\nMueve al cuadrado con el "mouse" para coger los triángulos.\n\n      Pulsa "space" para iniciar el juego',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()
logo_OB_intro = visual.ImageStim(
    win=win,
    name='logo_OB_intro', 
    image='logo_OB.png', mask=None,
    ori=0, pos=(0.6, 0.6), size=(0.2, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

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
banana_op =1
splat_op = 0
lim_inf = -1.6
SPEED = 0.015 ##0.02 #monkey
number_corrects = 0
plus_ = 0  ##0.0025 #monkey
penalty_ = 0  ##0.01 #monkey

speeds_ = []
trials_done = []
MonkeyMouse = event.Mouse(win=win)
x, y = [None, None]
MonkeyMouse.mouseClock = core.Clock()
rectangle = visual.Rect(
    win=win, name='rectangle',
    width=(0.25, 0.45)[0], height=(0.25, 0.45)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
circle_falling = visual.ShapeStim(
    win=win, name='circle_falling',
    vertices=[[-(0.15, 0.25)[0]/2.0,-(0.15, 0.25)[1]/2.0], [+(0.15, 0.25)[0]/2.0,-(0.15, 0.25)[1]/2.0], [0,(0.15, 0.25)[1]/2.0]],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1.0, depth=-3.0, interpolate=True)

# Initialize components for Routine "repeat_"
repeat_Clock = core.Clock()
text_repeat = visual.TextStim(win=win, name='text_repeat',
    text='¿Quieres continuar?\n\n        SÍ: pulsa "S"\n\n        NO: pulsa "N"',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
si = keyboard.Keyboard()
no = keyboard.Keyboard()

# Initialize components for Routine "valoracion"
valoracionClock = core.Clock()
text_valoracion = visual.TextStim(win=win, name='text_valoracion',
    text='¿Te ha parecido un juego divertido?\n\n        Puntúalo del 0 al 5 \n\n        0: muy aburrido\n        5: muy divertido\n\nPulsa en el teclado ese número para terminar',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "End"
EndClock = core.Clock()
Adios = visual.TextStim(win=win, name='Adios',
    text='¡Muchas gracias por participar!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
logo_ob_fin = visual.ImageStim(
    win=win,
    name='logo_ob_fin', 
    image='logo_OB.png', mask=None,
    ori=0, pos=(0.6, 0.6), size=(0.2, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
# keep track of which components have finished
InstructionsComponents = [Bienvenida, key_resp, logo_OB_intro]
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
    
    # *logo_OB_intro* updates
    if logo_OB_intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        logo_OB_intro.frameNStart = frameN  # exact frame index
        logo_OB_intro.tStart = t  # local t and not account for scr refresh
        logo_OB_intro.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(logo_OB_intro, 'tStartRefresh')  # time at next scr refresh
        logo_OB_intro.setAutoDraw(True)
    
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
thisExp.addData('logo_OB_intro.started', logo_OB_intro.tStartRefresh)
thisExp.addData('logo_OB_intro.stopped', logo_OB_intro.tStopRefresh)
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
repeat = data.TrialHandler(nReps=10, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='repeat')
thisExp.addLoop(repeat)  # add the loop to the experiment
thisRepeat = repeat.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRepeat.rgb)
if thisRepeat != None:
    for paramName in thisRepeat:
        exec('{} = thisRepeat[paramName]'.format(paramName))

for thisRepeat in repeat:
    currentLoop = repeat
    # abbreviate parameter names if possible (e.g. rgb = thisRepeat.rgb)
    if thisRepeat != None:
        for paramName in thisRepeat:
            exec('{} = thisRepeat[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=15, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Game"-------
        # update component parameters for each repeat
        timer = core.Clock()
        xpos = 0
        ypos = -0.5
        Bhoz = 0.1*(randint(-8,9))
        Bver = 1.5
        splatpos = 2
        SadFace = 0
        HappyFace = 0
        munch = 0
        splat = 0
        count = 0
        banana_op = 1
        splat_op = 0
        correct_trial = 0
        
        
        
        # setup some python lists for storing info about the MonkeyMouse
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        GameComponents = [MonkeyMouse, rectangle, circle_falling]
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
            #set the monkey to move with the mouse#
            xpos = (MonkeyMouse.getPos()[0]) 
            
            #tell the banana to drop at a rate on 0.02 units between 7 and 25 secs#
            if (0.1 < timer.getTime() < 60): 
                Bver = Bver - SPEED
            else:
                Bver = 1.5 
            
            
            
            #what to do if the banana overlaps the monkey#
            if (( -0.6 < Bver < -0.5) and ((xpos-0.2) <= Bhoz <= (xpos+0.2))): 
                #HappyFace = 1 
                #munch =  1
                #SPEED = SPEED + 0.01
                #Bver = 1.4
                #Bhoz = 0.1*(randint(-8,9))
                banana_op = 0
                correct_trial=1
                
                
                
                
            
            if ((-0.6< Bver < -0.5) and ( Bhoz>(xpos+0.2))): 
                 #splatpos = Bhoz
                 #splat_op = 1
                 #splat =  1
                 #SadFace = 1
                 #Bver = 1.4
                 #Bhoz = 0.1*(randint(-8,9))
                 banana_op = 0
                  
            
            if ((-0.6 < Bver < -0.5) and ( Bhoz < (xpos-0.2))): 
                 #splatpos = Bhoz
                 #splat_op = 1
                 #splat =  1
                 #SadFace = 1
                 banana_op = 0
                  
            
            
            if Bver < -0.6:
                #splat_op = 0
                banana_op = 0
                
                
            
            if Bver <lim_inf:
                continueRoutine = False
            
            
            
            #set final chat #
            #FinalChat = f'Well done! \n You helped the monkey eat \n {munch} bananas!'
            
            #if (timer.getTime()>=60):
            #    continueRoutine = False
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
            
            # *rectangle* updates
            if rectangle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rectangle.frameNStart = frameN  # exact frame index
                rectangle.tStart = t  # local t and not account for scr refresh
                rectangle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rectangle, 'tStartRefresh')  # time at next scr refresh
                rectangle.setAutoDraw(True)
            if rectangle.status == STARTED:  # only update if drawing
                rectangle.setPos((xpos,ypos), log=False)
            
            # *circle_falling* updates
            if circle_falling.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle_falling.frameNStart = frameN  # exact frame index
                circle_falling.tStart = t  # local t and not account for scr refresh
                circle_falling.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle_falling, 'tStartRefresh')  # time at next scr refresh
                circle_falling.setAutoDraw(True)
            if circle_falling.status == STARTED:  # only update if drawing
                circle_falling.setOpacity(banana_op, log=False)
                circle_falling.setPos((Bhoz,Bver), log=False)
            
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
        
        speeds_.append(SPEED)
        
        
        trials_done.append(correct_trial)
        
        if correct_trial == 1:
            
            number_corrects=number_corrects + 1
            
            
            
            
        ##Feedback 
        import numpy as np
        SPEED_SHOW = np.round(np.mean(speeds_),3)*1000
        
        
        if len(trials_done)>14:
            SPEED = 0.1
            penalty = 0
        # store data for trials (TrialHandler)
        trials.addData('rectangle.started', rectangle.tStartRefresh)
        trials.addData('rectangle.stopped', rectangle.tStopRefresh)
        trials.addData('circle_falling.started', circle_falling.tStartRefresh)
        trials.addData('circle_falling.stopped', circle_falling.tStopRefresh)
        # the Routine "Game" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 15 repeats of 'trials'
    
    
    # ------Prepare to start Routine "repeat_"-------
    # update component parameters for each repeat
    si.keys = []
    si.rt = []
    no.keys = []
    no.rt = []
    # keep track of which components have finished
    repeat_Components = [text_repeat, si, no]
    for thisComponent in repeat_Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    repeat_Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "repeat_"-------
    while continueRoutine:
        # get current time
        t = repeat_Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=repeat_Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_repeat* updates
        if text_repeat.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_repeat.frameNStart = frameN  # exact frame index
            text_repeat.tStart = t  # local t and not account for scr refresh
            text_repeat.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_repeat, 'tStartRefresh')  # time at next scr refresh
            text_repeat.setAutoDraw(True)
        
        # *si* updates
        waitOnFlip = False
        if si.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            si.frameNStart = frameN  # exact frame index
            si.tStart = t  # local t and not account for scr refresh
            si.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(si, 'tStartRefresh')  # time at next scr refresh
            si.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(si.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(si.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if si.status == STARTED and not waitOnFlip:
            theseKeys = si.getKeys(keyList=['s'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                si.keys = theseKeys.name  # just the last key pressed
                si.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # *no* updates
        waitOnFlip = False
        if no.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            no.frameNStart = frameN  # exact frame index
            no.tStart = t  # local t and not account for scr refresh
            no.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(no, 'tStartRefresh')  # time at next scr refresh
            no.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(no.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(no.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if no.status == STARTED and not waitOnFlip:
            theseKeys = no.getKeys(keyList=['n'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                no.keys = theseKeys.name  # just the last key pressed
                no.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        if no.keys == "n": 
            repeat.finished = True    
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in repeat_Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "repeat_"-------
    for thisComponent in repeat_Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    repeat.addData('text_repeat.started', text_repeat.tStartRefresh)
    repeat.addData('text_repeat.stopped', text_repeat.tStopRefresh)
    # check responses
    if si.keys in ['', [], None]:  # No response was made
        si.keys = None
    repeat.addData('si.keys',si.keys)
    if si.keys != None:  # we had a response
        repeat.addData('si.rt', si.rt)
    repeat.addData('si.started', si.tStartRefresh)
    repeat.addData('si.stopped', si.tStopRefresh)
    # check responses
    if no.keys in ['', [], None]:  # No response was made
        no.keys = None
    repeat.addData('no.keys',no.keys)
    if no.keys != None:  # we had a response
        repeat.addData('no.rt', no.rt)
    repeat.addData('no.started', no.tStartRefresh)
    repeat.addData('no.stopped', no.tStopRefresh)
    # the Routine "repeat_" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 10 repeats of 'repeat'


# ------Prepare to start Routine "valoracion"-------
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
# keep track of which components have finished
valoracionComponents = [text_valoracion, key_resp_2]
for thisComponent in valoracionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
valoracionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "valoracion"-------
while continueRoutine:
    # get current time
    t = valoracionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=valoracionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_valoracion* updates
    if text_valoracion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_valoracion.frameNStart = frameN  # exact frame index
        text_valoracion.tStart = t  # local t and not account for scr refresh
        text_valoracion.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_valoracion, 'tStartRefresh')  # time at next scr refresh
        text_valoracion.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['0', '1', '2', '3', '4', '5'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            if key_resp_2.keys == []:  # then this was the first keypress
                key_resp_2.keys = theseKeys.name  # just the first key pressed
                key_resp_2.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in valoracionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "valoracion"-------
for thisComponent in valoracionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_valoracion.started', text_valoracion.tStartRefresh)
thisExp.addData('text_valoracion.stopped', text_valoracion.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "valoracion" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "End"-------
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndComponents = [Adios, logo_ob_fin]
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
    
    # *logo_ob_fin* updates
    if logo_ob_fin.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        logo_ob_fin.frameNStart = frameN  # exact frame index
        logo_ob_fin.tStart = t  # local t and not account for scr refresh
        logo_ob_fin.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(logo_ob_fin, 'tStartRefresh')  # time at next scr refresh
        logo_ob_fin.setAutoDraw(True)
    if logo_ob_fin.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > logo_ob_fin.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            logo_ob_fin.tStop = t  # not accounting for scr refresh
            logo_ob_fin.frameNStop = frameN  # exact frame index
            win.timeOnFlip(logo_ob_fin, 'tStopRefresh')  # time at next scr refresh
            logo_ob_fin.setAutoDraw(False)
    
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
import numpy as np

mean_speed = np.mean(speeds_) ##mean speed -->the larger the better
max_speed = np.max(speeds_)
number_trials_done = len(trials_done) ##number of trials
number_trials_correct = np.sum(trials_done)  ##number corrects

thisExp.addData('mean_speed', mean_speed)
thisExp.addData('max_speed', max_speed)
thisExp.addData('number_trials', number_trials_done)
thisExp.addData('number_trials_correct', number_trials_correct)
thisExp.addData('logo_ob_fin.started', logo_ob_fin.tStartRefresh)
thisExp.addData('logo_ob_fin.stopped', logo_ob_fin.tStopRefresh)

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

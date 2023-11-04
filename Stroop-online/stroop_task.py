#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.3),
    on November 04, 2023, at 11:57
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
expName = 'stroop_task'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\David\\Documents\\GitHub\\OpenBrains\\Stroop-online\\stroop_task.py',
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
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instrucciones"
InstruccionesClock = core.Clock()
Instrucciones_texto = visual.TextStim(win=win, name='Instrucciones_texto',
    text='En esta tarea, tendrás que responder lo más rápido que puedas.\n\nPresiona "a" si la palabra es "azul"\nPresiona "v" si la palabra es "verde"\nPresiona "n" si la palabra es "naranja"\nPresiona "l" si la palabra es "lila"\n\n\nPara hacerlo la más rápido posible, mantén siempre un dedo encima de cada letra.\n\nCuando quieras, presiona "space"',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "color_negro"
color_negroClock = core.Clock()
colores1 = visual.TextStim(win=win, name='colores1',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
respuesta = keyboard.Keyboard()

# Initialize components for Routine "instrucciones_2"
instrucciones_2Clock = core.Clock()
text_intructionses2 = visual.TextStim(win=win, name='text_intructionses2',
    text='Ahora tendrás que indicar el color del cuadrado.\n\nPresiona "a" si es de color "azul"\nPresiona "v" si es de color "verde"\nPresiona "n" si es de color "naranja"\nPresiona "l" si es de color "lila"\n\n\nPara hacerlo la más rápido posible, mantén siempre un dedo encima de cada letra.\n\nCuando estés listo, presiona "space"',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "color_rectangulo"
color_rectanguloClock = core.Clock()
rectangulo = visual.Rect(
    win=win, name='rectangulo',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
respuesta_rect = keyboard.Keyboard()

# Initialize components for Routine "instrucciones_3"
instrucciones_3Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Finalmente,\n\ntendrás que indicar de qué color está escrita la palabra.\n\nPresiona "a" si la palabra está escrita en color "azul"\nPresiona "v" si la palabra está escrita en color "verde"\nPresiona "n" si la palabra está escrita en color "naranja"\nPresiona "l" si la palabra está escrita en color "lila"\n\n\nPara hacerlo la más rápido posible, mantén siempre un dedo encima de cada letra.\n\nCuando estés listo, presiona "space"',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "color_variado"
color_variadoClock = core.Clock()
colores2 = visual.TextStim(win=win, name='colores2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
respuesta_mix = keyboard.Keyboard()

# Initialize components for Routine "gracias"
graciasClock = core.Clock()
despedida = visual.TextStim(win=win, name='despedida',
    text='¡Muchas gracias por participar!',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instrucciones"-------
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
# keep track of which components have finished
InstruccionesComponents = [Instrucciones_texto, key_resp]
for thisComponent in InstruccionesComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstruccionesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Instrucciones"-------
while continueRoutine:
    # get current time
    t = InstruccionesClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstruccionesClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instrucciones_texto* updates
    if Instrucciones_texto.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instrucciones_texto.frameNStart = frameN  # exact frame index
        Instrucciones_texto.tStart = t  # local t and not account for scr refresh
        Instrucciones_texto.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instrucciones_texto, 'tStartRefresh')  # time at next scr refresh
        Instrucciones_texto.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
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
    for thisComponent in InstruccionesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instrucciones"-------
for thisComponent in InstruccionesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instrucciones_texto.started', Instrucciones_texto.tStartRefresh)
thisExp.addData('Instrucciones_texto.stopped', Instrucciones_texto.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instrucciones" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('colores1_negro.xlsx', selection='1:38'),
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
    
    # ------Prepare to start Routine "color_negro"-------
    # update component parameters for each repeat
    colores1.setText(texto)
    respuesta.keys = []
    respuesta.rt = []
    # keep track of which components have finished
    color_negroComponents = [colores1, respuesta]
    for thisComponent in color_negroComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    color_negroClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "color_negro"-------
    while continueRoutine:
        # get current time
        t = color_negroClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=color_negroClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *colores1* updates
        if colores1.status == NOT_STARTED and tThisFlip >= 0.05-frameTolerance:
            # keep track of start time/frame for later
            colores1.frameNStart = frameN  # exact frame index
            colores1.tStart = t  # local t and not account for scr refresh
            colores1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(colores1, 'tStartRefresh')  # time at next scr refresh
            colores1.setAutoDraw(True)
        
        # *respuesta* updates
        waitOnFlip = False
        if respuesta.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            respuesta.frameNStart = frameN  # exact frame index
            respuesta.tStart = t  # local t and not account for scr refresh
            respuesta.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(respuesta, 'tStartRefresh')  # time at next scr refresh
            respuesta.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(respuesta.clock.reset)  # t=0 on next screen flip
        if respuesta.status == STARTED and not waitOnFlip:
            theseKeys = respuesta.getKeys(keyList=['a', 'v', 'n', 'l'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                respuesta.keys.append(theseKeys.name)  # storing all keys
                respuesta.rt.append(theseKeys.rt)
                # was this 'correct'?
                if (respuesta.keys == str(answer)) or (respuesta.keys == answer):
                    respuesta.corr = 1
                else:
                    respuesta.corr = 0
        if respuesta.keys: # ie if the list isn't empty:
            if respuesta.keys[-1] != answer: # check the latest response
                continueRoutine = True 
            elif respuesta.keys[-1] == answer: # check the latest response
                continueRoutine = False #"
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in color_negroComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "color_negro"-------
    for thisComponent in color_negroComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('colores1.started', colores1.tStartRefresh)
    trials.addData('colores1.stopped', colores1.tStopRefresh)
    # check responses
    if respuesta.keys in ['', [], None]:  # No response was made
        respuesta.keys = None
        # was no response the correct answer?!
        if str(answer).lower() == 'none':
           respuesta.corr = 1;  # correct non-response
        else:
           respuesta.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('respuesta.keys',respuesta.keys)
    trials.addData('respuesta.corr', respuesta.corr)
    if respuesta.keys != None:  # we had a response
        trials.addData('respuesta.rt', respuesta.rt)
    trials.addData('respuesta.started', respuesta.tStartRefresh)
    trials.addData('respuesta.stopped', respuesta.tStopRefresh)
    # the Routine "color_negro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "instrucciones_2"-------
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
# keep track of which components have finished
instrucciones_2Components = [text_intructionses2, key_resp_2]
for thisComponent in instrucciones_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrucciones_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instrucciones_2"-------
while continueRoutine:
    # get current time
    t = instrucciones_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrucciones_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_intructionses2* updates
    if text_intructionses2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_intructionses2.frameNStart = frameN  # exact frame index
        text_intructionses2.tStart = t  # local t and not account for scr refresh
        text_intructionses2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_intructionses2, 'tStartRefresh')  # time at next scr refresh
        text_intructionses2.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
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
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_2.keys = theseKeys.name  # just the last key pressed
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
    for thisComponent in instrucciones_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instrucciones_2"-------
for thisComponent in instrucciones_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_intructionses2.started', text_intructionses2.tStartRefresh)
thisExp.addData('text_intructionses2.stopped', text_intructionses2.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "instrucciones_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('colores2_rectangulos.xlsx', selection='1:38'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "color_rectangulo"-------
    # update component parameters for each repeat
    rectangulo.setFillColor([farber, farbeg, farbeb])
    rectangulo.setLineColor([farber, farbeg, farbeb])
    respuesta_rect.keys = []
    respuesta_rect.rt = []
    # keep track of which components have finished
    color_rectanguloComponents = [rectangulo, respuesta_rect]
    for thisComponent in color_rectanguloComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    color_rectanguloClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "color_rectangulo"-------
    while continueRoutine:
        # get current time
        t = color_rectanguloClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=color_rectanguloClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rectangulo* updates
        if rectangulo.status == NOT_STARTED and tThisFlip >= 0.05-frameTolerance:
            # keep track of start time/frame for later
            rectangulo.frameNStart = frameN  # exact frame index
            rectangulo.tStart = t  # local t and not account for scr refresh
            rectangulo.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rectangulo, 'tStartRefresh')  # time at next scr refresh
            rectangulo.setAutoDraw(True)
        
        # *respuesta_rect* updates
        waitOnFlip = False
        if respuesta_rect.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            respuesta_rect.frameNStart = frameN  # exact frame index
            respuesta_rect.tStart = t  # local t and not account for scr refresh
            respuesta_rect.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(respuesta_rect, 'tStartRefresh')  # time at next scr refresh
            respuesta_rect.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(respuesta_rect.clock.reset)  # t=0 on next screen flip
        if respuesta_rect.status == STARTED and not waitOnFlip:
            theseKeys = respuesta_rect.getKeys(keyList=['a', 'v', 'n', 'l'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                respuesta_rect.keys.append(theseKeys.name)  # storing all keys
                respuesta_rect.rt.append(theseKeys.rt)
                # was this 'correct'?
                if (respuesta_rect.keys == str(answer)) or (respuesta_rect.keys == answer):
                    respuesta_rect.corr = 1
                else:
                    respuesta_rect.corr = 0
        if respuesta_rect.keys: # ie if the list isn't empty:
            if respuesta_rect.keys[-1] != answer: # check the latest response
                continueRoutine = True 
            elif respuesta_rect.keys[-1] == answer: # check the latest response
                continueRoutine = False #"
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in color_rectanguloComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "color_rectangulo"-------
    for thisComponent in color_rectanguloComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('rectangulo.started', rectangulo.tStartRefresh)
    trials_2.addData('rectangulo.stopped', rectangulo.tStopRefresh)
    # check responses
    if respuesta_rect.keys in ['', [], None]:  # No response was made
        respuesta_rect.keys = None
        # was no response the correct answer?!
        if str(answer).lower() == 'none':
           respuesta_rect.corr = 1;  # correct non-response
        else:
           respuesta_rect.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('respuesta_rect.keys',respuesta_rect.keys)
    trials_2.addData('respuesta_rect.corr', respuesta_rect.corr)
    if respuesta_rect.keys != None:  # we had a response
        trials_2.addData('respuesta_rect.rt', respuesta_rect.rt)
    trials_2.addData('respuesta_rect.started', respuesta_rect.tStartRefresh)
    trials_2.addData('respuesta_rect.stopped', respuesta_rect.tStopRefresh)
    # the Routine "color_rectangulo" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'


# ------Prepare to start Routine "instrucciones_3"-------
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
# keep track of which components have finished
instrucciones_3Components = [text, key_resp_3]
for thisComponent in instrucciones_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrucciones_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instrucciones_3"-------
while continueRoutine:
    # get current time
    t = instrucciones_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrucciones_3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_3.keys = theseKeys.name  # just the last key pressed
            key_resp_3.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrucciones_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instrucciones_3"-------
for thisComponent in instrucciones_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "instrucciones_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('colores3_mix.xlsx', selection='1:38'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "color_variado"-------
    # update component parameters for each repeat
    colores2.setColor([farber, farbeg, farbeb], colorSpace='rgb')
    colores2.setText(texto
)
    respuesta_mix.keys = []
    respuesta_mix.rt = []
    # keep track of which components have finished
    color_variadoComponents = [colores2, respuesta_mix]
    for thisComponent in color_variadoComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    color_variadoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "color_variado"-------
    while continueRoutine:
        # get current time
        t = color_variadoClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=color_variadoClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *colores2* updates
        if colores2.status == NOT_STARTED and tThisFlip >= 0.05-frameTolerance:
            # keep track of start time/frame for later
            colores2.frameNStart = frameN  # exact frame index
            colores2.tStart = t  # local t and not account for scr refresh
            colores2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(colores2, 'tStartRefresh')  # time at next scr refresh
            colores2.setAutoDraw(True)
        
        # *respuesta_mix* updates
        waitOnFlip = False
        if respuesta_mix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            respuesta_mix.frameNStart = frameN  # exact frame index
            respuesta_mix.tStart = t  # local t and not account for scr refresh
            respuesta_mix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(respuesta_mix, 'tStartRefresh')  # time at next scr refresh
            respuesta_mix.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(respuesta_mix.clock.reset)  # t=0 on next screen flip
        if respuesta_mix.status == STARTED and not waitOnFlip:
            theseKeys = respuesta_mix.getKeys(keyList=['a', 'v', 'n', 'l'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                respuesta_mix.keys.append(theseKeys.name)  # storing all keys
                respuesta_mix.rt.append(theseKeys.rt)
                # was this 'correct'?
                if (respuesta_mix.keys == str(answer)) or (respuesta_mix.keys == answer):
                    respuesta_mix.corr = 1
                else:
                    respuesta_mix.corr = 0
        if respuesta_mix.keys: # ie if the list isn't empty:
            if respuesta_mix.keys[-1] != answer: # check the latest response
                continueRoutine = True 
            elif respuesta_mix.keys[-1] == answer: # check the latest response
                continueRoutine = False #"
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in color_variadoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "color_variado"-------
    for thisComponent in color_variadoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('colores2.started', colores2.tStartRefresh)
    trials_3.addData('colores2.stopped', colores2.tStopRefresh)
    # check responses
    if respuesta_mix.keys in ['', [], None]:  # No response was made
        respuesta_mix.keys = None
        # was no response the correct answer?!
        if str(answer).lower() == 'none':
           respuesta_mix.corr = 1;  # correct non-response
        else:
           respuesta_mix.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_3 (TrialHandler)
    trials_3.addData('respuesta_mix.keys',respuesta_mix.keys)
    trials_3.addData('respuesta_mix.corr', respuesta_mix.corr)
    if respuesta_mix.keys != None:  # we had a response
        trials_3.addData('respuesta_mix.rt', respuesta_mix.rt)
    trials_3.addData('respuesta_mix.started', respuesta_mix.tStartRefresh)
    trials_3.addData('respuesta_mix.stopped', respuesta_mix.tStopRefresh)
    # the Routine "color_variado" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_3'


# ------Prepare to start Routine "gracias"-------
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
graciasComponents = [despedida]
for thisComponent in graciasComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
graciasClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "gracias"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = graciasClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=graciasClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *despedida* updates
    if despedida.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        despedida.frameNStart = frameN  # exact frame index
        despedida.tStart = t  # local t and not account for scr refresh
        despedida.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(despedida, 'tStartRefresh')  # time at next scr refresh
        despedida.setAutoDraw(True)
    if despedida.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > despedida.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            despedida.tStop = t  # not accounting for scr refresh
            despedida.frameNStop = frameN  # exact frame index
            win.timeOnFlip(despedida, 'tStopRefresh')  # time at next scr refresh
            despedida.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in graciasComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "gracias"-------
for thisComponent in graciasComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('despedida.started', despedida.tStartRefresh)
thisExp.addData('despedida.stopped', despedida.tStopRefresh)

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

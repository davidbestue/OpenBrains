#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on February 04, 2024, at 20:04
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'bart'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'age': '',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = 'data' + os.sep + '%s_%s' % (expInfo['participant'], expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\david\\OneDrive\\Documentos\\GitHub\\OpenBrains\\pumps\\pumps\\bart_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.WARNING)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.WARNING)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1440, 900], fullscr=True, screen=0,
            winType='pyglet', allowStencil=True,
            monitor='testMonitor', color=[-1.0000, 0.6157, 0.6392], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units=None
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [-1.0000, 0.6157, 0.6392]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = None
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='iohub')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='ioHub')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "instructions" ---
    background = visual.ImageStim(
        win=win,
        name='background', 
        image='assets/background.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(2.2, 1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    resp = keyboard.Keyboard()
    instrtxt = visual.TextBox2(
         win, text='Aquest és un joc on has d\'optimitzar els teus guanys en una competició d\'inflar globus.\n\nRebreu un premi en diners per cada globus que infleu segons la seva mida. Però si l\'infleu massa (bombant el globus), el globus esclatarà i no obtindreu diners.\n\nEls globus es diferencien en la seva mida màxima: de vegades poden arribar a gairebé la mida de la pantalla, però la majoria explotarà molt abans.\n\nPremeu\n    ESPAI per inflar el globus\n    ENTER per posar al banc l\'efectiu d\'aquest globus i passar al següent\n\nPer començar l\'experiement, premeu "ESPAI"', placeholder='Type here...', font='Arial',
         pos=(0, 0),     letterHeight=0.04,
         size=(1, 0.7), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=0.8,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor='white', borderColor='black',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='instrtxt',
         depth=-2, autoLog=True,
    )
    pop_sound = sound.Sound('assets/bang.wav', secs=1.0, stereo=True, hamming=True,
        name='pop_sound')
    pop_sound.setVolume(0.0)
    
    # --- Initialize components for Routine "reset_balloon" ---
    
    # --- Initialize components for Routine "trial" ---
    background_2 = visual.ImageStim(
        win=win,
        name='background_2', 
        image='assets/background.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(2.2, 1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    bankButton = keyboard.Keyboard()
    # Run 'Begin Experiment' code from updateEarnings
    bankedEarnings=0.0
    totalPumps=0.0
    balloonEarnings = ''
    bankedText = ''
    lastBalloonEarnings=0.0
    thisBalloonEarnings=0.0
    reminder = visual.TextBox2(
         win, text="Premeu ESPAI per bombar el globus\nPremeu ENTER per posar al banc l'efectiu d'aquest globus i passar al següent", placeholder='Type here...', font='Arial',
         pos=(-0.4, -0.3),     letterHeight=0.03,
         size=(0.5, 0.2), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=0.8,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor='white', borderColor='black',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='reminder',
         depth=-3, autoLog=True,
    )
    balloonValTxt = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         pos=(-0.4, 0.4),     letterHeight=0.03,
         size=(0.5, 0.2), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=0.8,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor='white', borderColor='black',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='balloonValTxt',
         depth=-4, autoLog=True,
    )
    bankedTxt = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         pos=(0.4, 0.4),     letterHeight=0.03,
         size=(0.5, 0.2), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=0.8,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor='white', borderColor='black',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='bankedTxt',
         depth=-5, autoLog=True,
    )
    # Run 'Begin Experiment' code from setBalloonSize
    balloonSize=0.08
    balloonMsgHeight=0.01
    balloonBody = visual.ImageStim(
        win=win,
        name='balloonBody', units='height', 
        image='assets/redBalloon.png', mask=None, anchor='center',
        ori=-90, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-7.0)
    trialcount = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         pos=(0.4, -0.3),     letterHeight=0.03,
         size=(0.5, 0.2), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=0.8,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor='white', borderColor='black',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='trialcount',
         depth=-8, autoLog=True,
    )
    
    # --- Initialize components for Routine "feedback" ---
    background_3 = visual.ImageStim(
        win=win,
        name='background_3', 
        image='assets/background.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(2.2, 1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    # Run 'Begin Experiment' code from checkPopped
    feedbackText=""
    
    feedbacktxt = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         pos=(0,0),     letterHeight=0.05,
         size=(0.4, 0.2), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='feedbacktxt',
         depth=-2, autoLog=True,
    )
    bankedTxt_2 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         pos=(0.4, 0.4),     letterHeight=0.03,
         size=(0.5, 0.2), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=0.8,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor='white', borderColor='black',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='bankedTxt_2',
         depth=-3, autoLog=True,
    )
    balloonValTxt_2 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         pos=(-0.4, 0.4),     letterHeight=0.03,
         size=(0.5, 0.2), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=0.8,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor='white', borderColor='black',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='balloonValTxt_2',
         depth=-4, autoLog=True,
    )
    reminder_2 = visual.TextBox2(
         win, text="Premeu ESPAI per bombar el globus\nPremeu ENTER per posar al banc l'efectiu d'aquest globus i passar al següent", placeholder='Type here...', font='Arial',
         pos=(-0.4, -0.3),     letterHeight=0.03,
         size=(0.5, 0.2), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=0.8,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor='white', borderColor='black',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='reminder_2',
         depth=-5, autoLog=True,
    )
    trialcount_2 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         pos=(0.4, -0.3),     letterHeight=0.03,
         size=(0.5, 0.2), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=0.8,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor='white', borderColor='black',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='trialcount_2',
         depth=-6, autoLog=True,
    )
    
    # --- Initialize components for Routine "finalScore" ---
    background_4 = visual.ImageStim(
        win=win,
        name='background_4', 
        image='assets/background.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(2.2, 1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    scoremsg = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         pos=(0, 0.25),     letterHeight=0.04,
         size=(1, 0.3), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=0.8,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor='white', borderColor='black',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='scoremsg',
         depth=-2, autoLog=True,
    )
    scoremsg_2 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         pos=(0, -0.25),     letterHeight=0.04,
         size=(1, 0.3), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=0.8,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor='white', borderColor='black',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='scoremsg_2',
         depth=-3, autoLog=True,
    )
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "instructions" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('instructions.started', globalClock.getTime())
    resp.keys = []
    resp.rt = []
    _resp_allKeys = []
    instrtxt.reset()
    pop_sound.setSound('assets/bang.wav', secs=1.0, hamming=True)
    pop_sound.setVolume(0.0, log=False)
    pop_sound.seek(0)
    # keep track of which components have finished
    instructionsComponents = [background, resp, instrtxt, pop_sound]
    for thisComponent in instructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instructions" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *background* updates
        
        # if background is starting this frame...
        if background.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            background.frameNStart = frameN  # exact frame index
            background.tStart = t  # local t and not account for scr refresh
            background.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(background, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'background.started')
            # update status
            background.status = STARTED
            background.setAutoDraw(True)
        
        # if background is active this frame...
        if background.status == STARTED:
            # update params
            pass
        
        # *resp* updates
        waitOnFlip = False
        
        # if resp is starting this frame...
        if resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resp.frameNStart = frameN  # exact frame index
            resp.tStart = t  # local t and not account for scr refresh
            resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'resp.started')
            # update status
            resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp.status == STARTED and not waitOnFlip:
            theseKeys = resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _resp_allKeys.extend(theseKeys)
            if len(_resp_allKeys):
                resp.keys = _resp_allKeys[-1].name  # just the last key pressed
                resp.rt = _resp_allKeys[-1].rt
                resp.duration = _resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *instrtxt* updates
        
        # if instrtxt is starting this frame...
        if instrtxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instrtxt.frameNStart = frameN  # exact frame index
            instrtxt.tStart = t  # local t and not account for scr refresh
            instrtxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instrtxt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instrtxt.started')
            # update status
            instrtxt.status = STARTED
            instrtxt.setAutoDraw(True)
        
        # if instrtxt is active this frame...
        if instrtxt.status == STARTED:
            # update params
            pass
        
        # if pop_sound is starting this frame...
        if pop_sound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pop_sound.frameNStart = frameN  # exact frame index
            pop_sound.tStart = t  # local t and not account for scr refresh
            pop_sound.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('pop_sound.started', tThisFlipGlobal)
            # update status
            pop_sound.status = STARTED
            pop_sound.play(when=win)  # sync with win flip
        
        # if pop_sound is stopping this frame...
        if pop_sound.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pop_sound.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                pop_sound.tStop = t  # not accounting for scr refresh
                pop_sound.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pop_sound.stopped')
                # update status
                pop_sound.status = FINISHED
                pop_sound.stop()
        # update pop_sound status according to whether it's playing
        if pop_sound.isPlaying:
            pop_sound.status = STARTED
        elif pop_sound.isFinished:
            pop_sound.status = FINISHED
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions" ---
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('instructions.stopped', globalClock.getTime())
    pop_sound.pause()  # ensure sound has stopped at end of Routine
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('spreadsheets/conditions.xlsx'),
        seed=1832, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    
    for thisTrial in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "reset_balloon" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('reset_balloon.started', globalClock.getTime())
        # Run 'Begin Routine' code from code
        balloonSize=0.08
        popped=False
        nPumps=0
        # keep track of which components have finished
        reset_balloonComponents = []
        for thisComponent in reset_balloonComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "reset_balloon" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in reset_balloonComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "reset_balloon" ---
        for thisComponent in reset_balloonComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('reset_balloon.stopped', globalClock.getTime())
        # the Routine "reset_balloon" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        pump = data.TrialHandler(nReps=maxPumps, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='pump')
        thisExp.addLoop(pump)  # add the loop to the experiment
        thisPump = pump.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisPump.rgb)
        if thisPump != None:
            for paramName in thisPump:
                globals()[paramName] = thisPump[paramName]
        
        for thisPump in pump:
            currentLoop = pump
            thisExp.timestampOnFlip(win, 'thisRow.t')
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    inputs=inputs, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisPump.rgb)
            if thisPump != None:
                for paramName in thisPump:
                    globals()[paramName] = thisPump[paramName]
            
            # --- Prepare to start Routine "trial" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('trial.started', globalClock.getTime())
            bankButton.keys = []
            bankButton.rt = []
            _bankButton_allKeys = []
            # Run 'Begin Routine' code from updateEarnings
            thisBalloonEarnings=(pump.thisN)*0.05
            balloonEarnings = "Valor d'aquest globus:\n€" + str(round(thisBalloonEarnings, 2))
            bankedText = "Has guanyat:\n€" + str(round(bankedEarnings, 2))
            reminder.reset()
            balloonValTxt.reset()
            bankedTxt.reset()
            # Run 'Begin Routine' code from setBalloonSize
            balloonBody.setPos([0, balloonSize/2-.5])
            balloonBody.setSize(balloonSize)
            trialcount.reset()
            trialcount.setText('Globus número: ' + str(trials.thisN+1) +'/' + str(trials.nTotal))
            # keep track of which components have finished
            trialComponents = [background_2, bankButton, reminder, balloonValTxt, bankedTxt, balloonBody, trialcount]
            for thisComponent in trialComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "trial" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *background_2* updates
                
                # if background_2 is starting this frame...
                if background_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    background_2.frameNStart = frameN  # exact frame index
                    background_2.tStart = t  # local t and not account for scr refresh
                    background_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(background_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'background_2.started')
                    # update status
                    background_2.status = STARTED
                    background_2.setAutoDraw(True)
                
                # if background_2 is active this frame...
                if background_2.status == STARTED:
                    # update params
                    pass
                
                # *bankButton* updates
                waitOnFlip = False
                
                # if bankButton is starting this frame...
                if bankButton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    bankButton.frameNStart = frameN  # exact frame index
                    bankButton.tStart = t  # local t and not account for scr refresh
                    bankButton.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(bankButton, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'bankButton.started')
                    # update status
                    bankButton.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(bankButton.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(bankButton.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if bankButton.status == STARTED and not waitOnFlip:
                    theseKeys = bankButton.getKeys(keyList=['return', 'space'], ignoreKeys=["escape"], waitRelease=False)
                    _bankButton_allKeys.extend(theseKeys)
                    if len(_bankButton_allKeys):
                        bankButton.keys = _bankButton_allKeys[-1].name  # just the last key pressed
                        bankButton.rt = _bankButton_allKeys[-1].rt
                        bankButton.duration = _bankButton_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # *reminder* updates
                
                # if reminder is starting this frame...
                if reminder.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    reminder.frameNStart = frameN  # exact frame index
                    reminder.tStart = t  # local t and not account for scr refresh
                    reminder.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(reminder, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'reminder.started')
                    # update status
                    reminder.status = STARTED
                    reminder.setAutoDraw(True)
                
                # if reminder is active this frame...
                if reminder.status == STARTED:
                    # update params
                    pass
                
                # *balloonValTxt* updates
                
                # if balloonValTxt is starting this frame...
                if balloonValTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    balloonValTxt.frameNStart = frameN  # exact frame index
                    balloonValTxt.tStart = t  # local t and not account for scr refresh
                    balloonValTxt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(balloonValTxt, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'balloonValTxt.started')
                    # update status
                    balloonValTxt.status = STARTED
                    balloonValTxt.setAutoDraw(True)
                
                # if balloonValTxt is active this frame...
                if balloonValTxt.status == STARTED:
                    # update params
                    balloonValTxt.setText(balloonEarnings, log=False)
                
                # *bankedTxt* updates
                
                # if bankedTxt is starting this frame...
                if bankedTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    bankedTxt.frameNStart = frameN  # exact frame index
                    bankedTxt.tStart = t  # local t and not account for scr refresh
                    bankedTxt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(bankedTxt, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'bankedTxt.started')
                    # update status
                    bankedTxt.status = STARTED
                    bankedTxt.setAutoDraw(True)
                
                # if bankedTxt is active this frame...
                if bankedTxt.status == STARTED:
                    # update params
                    bankedTxt.setText(bankedText, log=False)
                # Run 'Each Frame' code from setBalloonSize
                balloonSize=0.1+(pump.thisN+1)*0.015
                
                # *balloonBody* updates
                
                # if balloonBody is starting this frame...
                if balloonBody.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    balloonBody.frameNStart = frameN  # exact frame index
                    balloonBody.tStart = t  # local t and not account for scr refresh
                    balloonBody.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(balloonBody, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'balloonBody.started')
                    # update status
                    balloonBody.status = STARTED
                    balloonBody.setAutoDraw(True)
                
                # if balloonBody is active this frame...
                if balloonBody.status == STARTED:
                    # update params
                    balloonBody.setPos([0, balloonSize/2-.5], log=False)
                    balloonBody.setSize(balloonSize, log=False)
                
                # *trialcount* updates
                
                # if trialcount is starting this frame...
                if trialcount.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    trialcount.frameNStart = frameN  # exact frame index
                    trialcount.tStart = t  # local t and not account for scr refresh
                    trialcount.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(trialcount, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'trialcount.started')
                    # update status
                    trialcount.status = STARTED
                    trialcount.setAutoDraw(True)
                
                # if trialcount is active this frame...
                if trialcount.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial" ---
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('trial.stopped', globalClock.getTime())
            # Run 'End Routine' code from updateEarnings
            #calculate cash 'earned'
            if pump.thisN + 1 == maxPumps:
                popped = True
            else:
                popped = False
            
            # if balloon popped reset the earnings
            if popped:
              thisBalloonEarnings=0.0
              lastBalloonEarnings=0.0
            else:
                lastBalloonEarnings=thisBalloonEarnings
            
            if 'return' in bankButton.keys:
                pump.finished = True
            
            
            # Run 'End Routine' code from setBalloonSize
            #save data
            trials.addData('nPumps', pump.thisN)
            trials.addData('size', balloonSize)
            trials.addData('earnings', thisBalloonEarnings)
            trials.addData('popped', popped)
            
            
            # the Routine "trial" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
        # completed maxPumps repeats of 'pump'
        
        
        # --- Prepare to start Routine "feedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('feedback.started', globalClock.getTime())
        # Run 'Begin Routine' code from checkPopped
        # track the banked earnings
        bankedEarnings = bankedEarnings+lastBalloonEarnings
        
        # track the total amount of pumps
        totalPumps = totalPumps+(pump.thisN-1)
        
        
        #update the text 
        balloonEarnings = "Valor d'aquest globus:\n€" + str(round(thisBalloonEarnings, 2))
        bankedText = "Has guanyat:\n€" + str(round(bankedEarnings, 2))
        
        pop_sound.setVolume(1)
        
        # play the pop sound
        if popped==True:
          feedbackText="Ooooh! Has perdut aquest globus!"
          pop_sound.play()
        else:
          feedbackText="Has guanyat €" + str(round(lastBalloonEarnings, 2))
          
        feedbacktxt.reset()
        feedbacktxt.setText(feedbackText)
        bankedTxt_2.reset()
        balloonValTxt_2.reset()
        reminder_2.reset()
        trialcount_2.reset()
        trialcount_2.setText('Globus número: ' + str(trials.thisN+1) +'/' + str(trials.nTotal))
        # keep track of which components have finished
        feedbackComponents = [background_3, feedbacktxt, bankedTxt_2, balloonValTxt_2, reminder_2, trialcount_2]
        for thisComponent in feedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "feedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *background_3* updates
            
            # if background_3 is starting this frame...
            if background_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                background_3.frameNStart = frameN  # exact frame index
                background_3.tStart = t  # local t and not account for scr refresh
                background_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(background_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'background_3.started')
                # update status
                background_3.status = STARTED
                background_3.setAutoDraw(True)
            
            # if background_3 is active this frame...
            if background_3.status == STARTED:
                # update params
                pass
            
            # if background_3 is stopping this frame...
            if background_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > background_3.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    background_3.tStop = t  # not accounting for scr refresh
                    background_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'background_3.stopped')
                    # update status
                    background_3.status = FINISHED
                    background_3.setAutoDraw(False)
            
            # *feedbacktxt* updates
            
            # if feedbacktxt is starting this frame...
            if feedbacktxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedbacktxt.frameNStart = frameN  # exact frame index
                feedbacktxt.tStart = t  # local t and not account for scr refresh
                feedbacktxt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedbacktxt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedbacktxt.started')
                # update status
                feedbacktxt.status = STARTED
                feedbacktxt.setAutoDraw(True)
            
            # if feedbacktxt is active this frame...
            if feedbacktxt.status == STARTED:
                # update params
                pass
            
            # if feedbacktxt is stopping this frame...
            if feedbacktxt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedbacktxt.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    feedbacktxt.tStop = t  # not accounting for scr refresh
                    feedbacktxt.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedbacktxt.stopped')
                    # update status
                    feedbacktxt.status = FINISHED
                    feedbacktxt.setAutoDraw(False)
            
            # *bankedTxt_2* updates
            
            # if bankedTxt_2 is starting this frame...
            if bankedTxt_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                bankedTxt_2.frameNStart = frameN  # exact frame index
                bankedTxt_2.tStart = t  # local t and not account for scr refresh
                bankedTxt_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(bankedTxt_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'bankedTxt_2.started')
                # update status
                bankedTxt_2.status = STARTED
                bankedTxt_2.setAutoDraw(True)
            
            # if bankedTxt_2 is active this frame...
            if bankedTxt_2.status == STARTED:
                # update params
                bankedTxt_2.setText(bankedText, log=False)
            
            # if bankedTxt_2 is stopping this frame...
            if bankedTxt_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > bankedTxt_2.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    bankedTxt_2.tStop = t  # not accounting for scr refresh
                    bankedTxt_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'bankedTxt_2.stopped')
                    # update status
                    bankedTxt_2.status = FINISHED
                    bankedTxt_2.setAutoDraw(False)
            
            # *balloonValTxt_2* updates
            
            # if balloonValTxt_2 is starting this frame...
            if balloonValTxt_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                balloonValTxt_2.frameNStart = frameN  # exact frame index
                balloonValTxt_2.tStart = t  # local t and not account for scr refresh
                balloonValTxt_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(balloonValTxt_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'balloonValTxt_2.started')
                # update status
                balloonValTxt_2.status = STARTED
                balloonValTxt_2.setAutoDraw(True)
            
            # if balloonValTxt_2 is active this frame...
            if balloonValTxt_2.status == STARTED:
                # update params
                balloonValTxt_2.setText(balloonEarnings, log=False)
            
            # if balloonValTxt_2 is stopping this frame...
            if balloonValTxt_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > balloonValTxt_2.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    balloonValTxt_2.tStop = t  # not accounting for scr refresh
                    balloonValTxt_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'balloonValTxt_2.stopped')
                    # update status
                    balloonValTxt_2.status = FINISHED
                    balloonValTxt_2.setAutoDraw(False)
            
            # *reminder_2* updates
            
            # if reminder_2 is starting this frame...
            if reminder_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                reminder_2.frameNStart = frameN  # exact frame index
                reminder_2.tStart = t  # local t and not account for scr refresh
                reminder_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(reminder_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'reminder_2.started')
                # update status
                reminder_2.status = STARTED
                reminder_2.setAutoDraw(True)
            
            # if reminder_2 is active this frame...
            if reminder_2.status == STARTED:
                # update params
                pass
            
            # if reminder_2 is stopping this frame...
            if reminder_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > reminder_2.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    reminder_2.tStop = t  # not accounting for scr refresh
                    reminder_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'reminder_2.stopped')
                    # update status
                    reminder_2.status = FINISHED
                    reminder_2.setAutoDraw(False)
            
            # *trialcount_2* updates
            
            # if trialcount_2 is starting this frame...
            if trialcount_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialcount_2.frameNStart = frameN  # exact frame index
                trialcount_2.tStart = t  # local t and not account for scr refresh
                trialcount_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialcount_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trialcount_2.started')
                # update status
                trialcount_2.status = STARTED
                trialcount_2.setAutoDraw(True)
            
            # if trialcount_2 is active this frame...
            if trialcount_2.status == STARTED:
                # update params
                pass
            
            # if trialcount_2 is stopping this frame...
            if trialcount_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trialcount_2.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    trialcount_2.tStop = t  # not accounting for scr refresh
                    trialcount_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'trialcount_2.stopped')
                    # update status
                    trialcount_2.status = FINISHED
                    trialcount_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback" ---
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('feedback.stopped', globalClock.getTime())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.500000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials'
    
    # get names of stimulus parameters
    if trials.trialList in ([], [None], None):
        params = []
    else:
        params = trials.trialList[0].keys()
    # save data for this loop
    trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "finalScore" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('finalScore.started', globalClock.getTime())
    # Run 'Begin Routine' code from finalScoreCode
    scoreText="Has guanyat un total de\n" + str(round(bankedEarnings,2)) + "€";
    #balloonEarnings = "Valor d'aquest globus:\n€" + str(round(thisBalloonEarnings, 2))
    scoreText2="Has fet un total de\n" + str(int(totalPumps)) + " bombeigs";
    
    totalPumps
    scoremsg.reset()
    scoremsg.setText(scoreText
    )
    scoremsg_2.reset()
    scoremsg_2.setText(scoreText2
    )
    # keep track of which components have finished
    finalScoreComponents = [background_4, scoremsg, scoremsg_2]
    for thisComponent in finalScoreComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "finalScore" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *background_4* updates
        
        # if background_4 is starting this frame...
        if background_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            background_4.frameNStart = frameN  # exact frame index
            background_4.tStart = t  # local t and not account for scr refresh
            background_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(background_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'background_4.started')
            # update status
            background_4.status = STARTED
            background_4.setAutoDraw(True)
        
        # if background_4 is active this frame...
        if background_4.status == STARTED:
            # update params
            pass
        
        # *scoremsg* updates
        
        # if scoremsg is starting this frame...
        if scoremsg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            scoremsg.frameNStart = frameN  # exact frame index
            scoremsg.tStart = t  # local t and not account for scr refresh
            scoremsg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(scoremsg, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'scoremsg.started')
            # update status
            scoremsg.status = STARTED
            scoremsg.setAutoDraw(True)
        
        # if scoremsg is active this frame...
        if scoremsg.status == STARTED:
            # update params
            pass
        
        # *scoremsg_2* updates
        
        # if scoremsg_2 is starting this frame...
        if scoremsg_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            scoremsg_2.frameNStart = frameN  # exact frame index
            scoremsg_2.tStart = t  # local t and not account for scr refresh
            scoremsg_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(scoremsg_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'scoremsg_2.started')
            # update status
            scoremsg_2.status = STARTED
            scoremsg_2.setAutoDraw(True)
        
        # if scoremsg_2 is active this frame...
        if scoremsg_2.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in finalScoreComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "finalScore" ---
    for thisComponent in finalScoreComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('finalScore.stopped', globalClock.getTime())
    # the Routine "finalScore" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)

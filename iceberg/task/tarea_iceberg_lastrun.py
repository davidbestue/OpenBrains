#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on September 18, 2024, at 14:21
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
prefs.hardware['audioLatencyMode'] = '3'
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

# Run 'Before Experiment' code from code_5
path_videomar = 'imgs/video_mar_luis.mp4' #'imgs/marluis.mp4' #'imgs/video_mar.mp4'
path_musicafondo = 'imgs/song_titanic.mp4'
path_musicaletra = 'imgs/titanic_spanish.mp4'
path_pelicula = 'imgs/titanic.mp4'

nRows = 3
# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'tarea_iceberg'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'Edad': f"{randint(0, 999999):06.0f}",
    'Sexo': ['Hombre', 'Mujer', 'Otro'],
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
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\david\\OneDrive\\Documentos\\GitHub\\OpenBrains\\iceberg\\task\\tarea_iceberg_lastrun.py',
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
    logging.console.setLevel(logging.EXP)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    
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
            size=[1536, 864], fullscr=True, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
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
    
    # --- Initialize components for Routine "portada" ---
    image_5 = visual.ImageStim(
        win=win,
        name='image_5', 
        image='imgs/logo_OB.jpeg', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.6, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    text_6 = visual.TextStim(win=win, name='text_6',
        text='¡Bienvenido a un experimento de Open Brains!',
        font='Open Sans',
        pos=(0, -0.35), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "instructions" ---
    text_5 = visual.TextStim(win=win, name='text_5',
        text='En este experiemento te verás navegando por el mar...\n\n¡Pero hay icebergs que aparcerán de repente en pantalla!\n\nCuando veas uno, debes pulsar "SPACE" lo más rápido posible.\n\nHay 4 rondas.\n\nCuando estés listo, aprieta "SPACE" para empezar.',
        font='Open Sans',
        pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_5 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Ronda_1" ---
    text_7 = visual.TextStim(win=win, name='text_7',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from code_5
    import random 
    # Lista de nombres de rutinas
    rutinas = ["control", "music", "music_words", "music_video"]
    # Barajar el orden de las rutinas
    random.shuffle(rutinas)
    print(rutinas)
    
    # Un índice para seguir qué rutina ejecutar
    ronda1=rutinas[0]
    ronda2=rutinas[1]
    ronda3=rutinas[2]
    ronda4=rutinas[3]
    
    ronda1="music_video"
    
    
    # --- Initialize components for Routine "control" ---
    image = visual.ImageStim(
        win=win,
        name='image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.35, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    key_resp = keyboard.Keyboard()
    # Run 'Begin Experiment' code from mar1
    mar_movie = visual.MovieStim3(
        win=win,                        # Ventana en la que se va a mostrar el video
        filename=path_videomar, # Ruta al archivo de video
        size=(1900,1200),               # Tamaño del video (opcional)
        pos=(0,0),
        flipVert=False,                 # Si se debe voltear verticalmente
        flipHoriz=False,                # Si se debe voltear horizontalmente
        loop=True                      # Si el video debe repetirse
    )
    
    
    # --- Initialize components for Routine "music" ---
    image_2 = visual.ImageStim(
        win=win,
        name='image_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.35, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    key_resp_2 = keyboard.Keyboard()
    # Run 'Begin Experiment' code from code
    background_sound = visual.MovieStim3(
        win=win,                        # Ventana en la que se va a mostrar el video
        filename=path_musicafondo, # Ruta al archivo de video
        size=(20, 20),               # Tamaño del video (opcional)
        pos=(0,0),
        flipVert=False,                 # Si se debe voltear verticalmente
        flipHoriz=False,                # Si se debe voltear horizontalmente
        loop=False                      # Si el video debe repetirse
    )
    
    
    # --- Initialize components for Routine "music_words" ---
    # Run 'Begin Experiment' code from code_2
    background_movie = visual.MovieStim3(
        win=win,                        # Ventana en la que se va a mostrar el video
        filename=path_musicaletra , # Ruta al archivo de video
        size=(10,10),               # Tamaño del video (opcional)
        pos=(0,0),
        flipVert=False,                 # Si se debe voltear verticalmente
        flipHoriz=False,                # Si se debe voltear horizontalmente
        loop=False                      # Si el video debe repetirse
    )
    
    
    image_3 = visual.ImageStim(
        win=win,
        name='image_3', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.35, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    key_resp_3 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "music_video" ---
    # Run 'Begin Experiment' code from code_2_2
    background_movie2 = visual.MovieStim3(
        win=win,                        # Ventana en la que se va a mostrar el video
        filename=path_musicaletra , # Ruta al archivo de video
        size=(10,10),               # Tamaño del video (opcional)
        pos=(0,0),
        flipVert=False,                 # Si se debe voltear verticalmente
        flipHoriz=False,                # Si se debe voltear horizontalmente
        loop=False                      # Si el video debe repetirse
    )
    
    # Run 'Begin Experiment' code from code_3
    displayed_movie = visual.MovieStim3(
        win=win,                        # Ventana en la que se va a mostrar el video
        filename=path_pelicula, # Ruta al archivo de video
        size=(500,350),               # Tamaño del video (opcional)
        pos=(0,-350),
        flipVert=False,                 # Si se debe voltear verticalmente
        flipHoriz=False,                # Si se debe voltear horizontalmente
        loop=False                      # Si el video debe repetirse
    )
    
    image_4 = visual.ImageStim(
        win=win,
        name='image_4', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.35, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    Key_resp_4 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Ronda_2" ---
    text_8 = visual.TextStim(win=win, name='text_8',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "control2" ---
    image_6 = visual.ImageStim(
        win=win,
        name='image_6', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.35, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    key_resp_6 = keyboard.Keyboard()
    # Run 'Begin Experiment' code from mar_1_2
    mar_movie = visual.MovieStim3(
        win=win,                        # Ventana en la que se va a mostrar el video
        filename=path_videomar, # Ruta al archivo de video
        size=(1900,1200),               # Tamaño del video (opcional)
        pos=(0,0),
        flipVert=False,                 # Si se debe voltear verticalmente
        flipHoriz=False,                # Si se debe voltear horizontalmente
        loop=True                      # Si el video debe repetirse
    )
    
    
    # --- Initialize components for Routine "music2" ---
    image_7 = visual.ImageStim(
        win=win,
        name='image_7', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.35, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    key_resp_7 = keyboard.Keyboard()
    # Run 'Begin Experiment' code from code_6
    background_sound_r2 = visual.MovieStim3(
        win=win,                        # Ventana en la que se va a mostrar el video
        filename=path_musicafondo, # Ruta al archivo de video
        size=(20, 20),               # Tamaño del video (opcional)
        pos=(0,0),
        flipVert=False,                 # Si se debe voltear verticalmente
        flipHoriz=False,                # Si se debe voltear horizontalmente
        loop=False                      # Si el video debe repetirse
    )
    
    
    # --- Initialize components for Routine "music_words2" ---
    # Run 'Begin Experiment' code from code_7
    background_movie_r2 = visual.MovieStim3(
        win=win,                        # Ventana en la que se va a mostrar el video
        filename=path_musicaletra , # Ruta al archivo de video
        size=(10,10),               # Tamaño del video (opcional)
        pos=(0,0),
        flipVert=False,                 # Si se debe voltear verticalmente
        flipHoriz=False,                # Si se debe voltear horizontalmente
        loop=False                      # Si el video debe repetirse
    )
    
    
    image_8 = visual.ImageStim(
        win=win,
        name='image_8', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.35, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    key_resp_8 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "music_video2" ---
    # Run 'Begin Experiment' code from code_2_3
    backgroung_movie2_r2 = visual.MovieStim3(
        win=win,                        # Ventana en la que se va a mostrar el video
        filename=path_musicaletra , # Ruta al archivo de video
        size=(10,10),               # Tamaño del video (opcional)
        pos=(0,0),
        flipVert=False,                 # Si se debe voltear verticalmente
        flipHoriz=False,                # Si se debe voltear horizontalmente
        loop=False                      # Si el video debe repetirse
    )
    
    # Run 'Begin Experiment' code from code_8
    displayed_movie_r2 = visual.MovieStim3(
        win=win,                        # Ventana en la que se va a mostrar el video
        filename=path_pelicula, # Ruta al archivo de video
        size=(500,400),               # Tamaño del video (opcional)
        pos=(0,100),
        flipVert=False,                 # Si se debe voltear verticalmente
        flipHoriz=False,                # Si se debe voltear horizontalmente
        loop=False                      # Si el video debe repetirse
    )
    
    image_9 = visual.ImageStim(
        win=win,
        name='image_9', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.35, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    Key_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Ronda_3" ---
    text_9 = visual.TextStim(win=win, name='text_9',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "control3" ---
    image_10 = visual.ImageStim(
        win=win,
        name='image_10', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.35, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    key_resp_9 = keyboard.Keyboard()
    # Run 'Begin Experiment' code from mar_1_3
    mar_movie = visual.MovieStim3(
        win=win,                        # Ventana en la que se va a mostrar el video
        filename=path_videomar, # Ruta al archivo de video
        size=(1900,1200),               # Tamaño del video (opcional)
        pos=(0,0),
        flipVert=False,                 # Si se debe voltear verticalmente
        flipHoriz=False,                # Si se debe voltear horizontalmente
        loop=True                      # Si el video debe repetirse
    )
    
    
    # --- Initialize components for Routine "music3" ---
    image_11 = visual.ImageStim(
        win=win,
        name='image_11', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.35, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    key_resp_10 = keyboard.Keyboard()
    # Run 'Begin Experiment' code from code_9
    background_sound_r3 = visual.MovieStim3(
        win=win,                        # Ventana en la que se va a mostrar el video
        filename=path_musicafondo, # Ruta al archivo de video
        size=(20, 20),               # Tamaño del video (opcional)
        pos=(0,0),
        flipVert=False,                 # Si se debe voltear verticalmente
        flipHoriz=False,                # Si se debe voltear horizontalmente
        loop=False                      # Si el video debe repetirse
    )
    
    
    # --- Initialize components for Routine "music_words3" ---
    # Run 'Begin Experiment' code from code_10
    background_movie_r3 = visual.MovieStim3(
        win=win,                        # Ventana en la que se va a mostrar el video
        filename=path_musicaletra , # Ruta al archivo de video
        size=(10,10),               # Tamaño del video (opcional)
        pos=(0,0),
        flipVert=False,                 # Si se debe voltear verticalmente
        flipHoriz=False,                # Si se debe voltear horizontalmente
        loop=False                      # Si el video debe repetirse
    )
    
    
    image_12 = visual.ImageStim(
        win=win,
        name='image_12', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.35, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    key_resp_11 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "music_video3" ---
    # Run 'Begin Experiment' code from code_2_4
    backgroung_movie2_r3 = visual.MovieStim3(
        win=win,                        # Ventana en la que se va a mostrar el video
        filename=path_musicaletra , # Ruta al archivo de video
        size=(10,10),               # Tamaño del video (opcional)
        pos=(0,0),
        flipVert=False,                 # Si se debe voltear verticalmente
        flipHoriz=False,                # Si se debe voltear horizontalmente
        loop=False                      # Si el video debe repetirse
    )
    
    # Run 'Begin Experiment' code from code_11
    displayed_movie_r3 = visual.MovieStim3(
        win=win,                        # Ventana en la que se va a mostrar el video
        filename=path_pelicula, # Ruta al archivo de video
        size=(500,400),               # Tamaño del video (opcional)
        pos=(0,100),
        flipVert=False,                 # Si se debe voltear verticalmente
        flipHoriz=False,                # Si se debe voltear horizontalmente
        loop=False                      # Si el video debe repetirse
    )
    
    image_13 = visual.ImageStim(
        win=win,
        name='image_13', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.35, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    Key_resp_2 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Ronda_4" ---
    text_10 = visual.TextStim(win=win, name='text_10',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "control4" ---
    image_14 = visual.ImageStim(
        win=win,
        name='image_14', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.35, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    key_resp_12 = keyboard.Keyboard()
    # Run 'Begin Experiment' code from mar_1_4
    mar_movie = visual.MovieStim3(
        win=win,                        # Ventana en la que se va a mostrar el video
        filename=path_videomar, # Ruta al archivo de video
        size=(1900,1200),               # Tamaño del video (opcional)
        pos=(0,0),
        flipVert=False,                 # Si se debe voltear verticalmente
        flipHoriz=False,                # Si se debe voltear horizontalmente
        loop=True                      # Si el video debe repetirse
    )
    
    
    # --- Initialize components for Routine "music4" ---
    image_15 = visual.ImageStim(
        win=win,
        name='image_15', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.35, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    key_resp_13 = keyboard.Keyboard()
    # Run 'Begin Experiment' code from code_12
    background_sound_r4 = visual.MovieStim3(
        win=win,                        # Ventana en la que se va a mostrar el video
        filename=path_musicafondo, # Ruta al archivo de video
        size=(20, 20),               # Tamaño del video (opcional)
        pos=(0,0),
        flipVert=False,                 # Si se debe voltear verticalmente
        flipHoriz=False,                # Si se debe voltear horizontalmente
        loop=False                      # Si el video debe repetirse
    )
    
    
    # --- Initialize components for Routine "music_words4" ---
    # Run 'Begin Experiment' code from code_13
    background_movie_r4 = visual.MovieStim3(
        win=win,                        # Ventana en la que se va a mostrar el video
        filename=path_musicaletra , # Ruta al archivo de video
        size=(10,10),               # Tamaño del video (opcional)
        pos=(0,0),
        flipVert=False,                 # Si se debe voltear verticalmente
        flipHoriz=False,                # Si se debe voltear horizontalmente
        loop=False                      # Si el video debe repetirse
    )
    
    
    image_16 = visual.ImageStim(
        win=win,
        name='image_16', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.35, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    key_resp_14 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "music_video4" ---
    # Run 'Begin Experiment' code from code_2_5
    backgroung_movie2_r4 = visual.MovieStim3(
        win=win,                        # Ventana en la que se va a mostrar el video
        filename=path_musicaletra , # Ruta al archivo de video
        size=(10,10),               # Tamaño del video (opcional)
        pos=(0,0),
        flipVert=False,                 # Si se debe voltear verticalmente
        flipHoriz=False,                # Si se debe voltear horizontalmente
        loop=False                      # Si el video debe repetirse
    )
    
    # Run 'Begin Experiment' code from code_14
    displayed_movie_r4 = visual.MovieStim3(
        win=win,                        # Ventana en la que se va a mostrar el video
        filename=path_pelicula, # Ruta al archivo de video
        size=(500,400),               # Tamaño del video (opcional)
        pos=(0,100),
        flipVert=False,                 # Si se debe voltear verticalmente
        flipHoriz=False,                # Si se debe voltear horizontalmente
        loop=False                      # Si el video debe repetirse
    )
    
    image_17 = visual.ImageStim(
        win=win,
        name='image_17', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.35, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    Key_resp_3 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "final" ---
    text_4 = visual.TextStim(win=win, name='text_4',
        text='¡Muchas gracias por participar!',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
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
    
    # --- Prepare to start Routine "portada" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('portada.started', globalClock.getTime())
    # keep track of which components have finished
    portadaComponents = [image_5, text_6]
    for thisComponent in portadaComponents:
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
    
    # --- Run Routine "portada" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_5* updates
        
        # if image_5 is starting this frame...
        if image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_5.frameNStart = frameN  # exact frame index
            image_5.tStart = t  # local t and not account for scr refresh
            image_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_5.started')
            # update status
            image_5.status = STARTED
            image_5.setAutoDraw(True)
        
        # if image_5 is active this frame...
        if image_5.status == STARTED:
            # update params
            pass
        
        # if image_5 is stopping this frame...
        if image_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_5.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                image_5.tStop = t  # not accounting for scr refresh
                image_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_5.stopped')
                # update status
                image_5.status = FINISHED
                image_5.setAutoDraw(False)
        
        # *text_6* updates
        
        # if text_6 is starting this frame...
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_6.started')
            # update status
            text_6.status = STARTED
            text_6.setAutoDraw(True)
        
        # if text_6 is active this frame...
        if text_6.status == STARTED:
            # update params
            pass
        
        # if text_6 is stopping this frame...
        if text_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_6.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                text_6.tStop = t  # not accounting for scr refresh
                text_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_6.stopped')
                # update status
                text_6.status = FINISHED
                text_6.setAutoDraw(False)
        
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
        for thisComponent in portadaComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "portada" ---
    for thisComponent in portadaComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('portada.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    
    # --- Prepare to start Routine "instructions" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('instructions.started', globalClock.getTime())
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    # keep track of which components have finished
    instructionsComponents = [text_5, key_resp_5]
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
        
        # *text_5* updates
        
        # if text_5 is starting this frame...
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_5.started')
            # update status
            text_5.status = STARTED
            text_5.setAutoDraw(True)
        
        # if text_5 is active this frame...
        if text_5.status == STARTED:
            # update params
            pass
        
        # *key_resp_5* updates
        waitOnFlip = False
        
        # if key_resp_5 is starting this frame...
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_5.started')
            # update status
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                key_resp_5.duration = _key_resp_5_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
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
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
    thisExp.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        thisExp.addData('key_resp_5.rt', key_resp_5.rt)
        thisExp.addData('key_resp_5.duration', key_resp_5.duration)
    thisExp.nextEntry()
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Ronda_1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Ronda_1.started', globalClock.getTime())
    text_7.setText('Ronda 1/4')
    # Run 'Begin Routine' code from code_5
    totalRows = 118  # Replace with the total number of rows in your Excel file
    selectedRows = random.sample(range(totalRows), nRows)
    selectedRowsStr = [i for i in selectedRows]
    # keep track of which components have finished
    Ronda_1Components = [text_7]
    for thisComponent in Ronda_1Components:
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
    
    # --- Run Routine "Ronda_1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_7* updates
        
        # if text_7 is starting this frame...
        if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_7.started')
            # update status
            text_7.status = STARTED
            text_7.setAutoDraw(True)
        
        # if text_7 is active this frame...
        if text_7.status == STARTED:
            # update params
            pass
        
        # if text_7 is stopping this frame...
        if text_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_7.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_7.tStop = t  # not accounting for scr refresh
                text_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_7.stopped')
                # update status
                text_7.status = FINISHED
                text_7.setAutoDraw(False)
        
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
        for thisComponent in Ronda_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Ronda_1" ---
    for thisComponent in Ronda_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Ronda_1.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('imgs/iceberg_times.xlsx', selection=selectedRowsStr),
        seed=None, name='trials')
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
        
        # --- Prepare to start Routine "control" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('control.started', globalClock.getTime())
        # Run 'Begin Routine' code from control_r1
        if ronda1=="control":
            continueRoutine = True
        else:
            continueRoutine = False
        image.setPos([posx, posy])
        image.setImage('imgs/iceberg.png')
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # Run 'Begin Routine' code from mar1
        mar_movie.play()  
        
        # keep track of which components have finished
        controlComponents = [image, key_resp]
        for thisComponent in controlComponents:
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
        
        # --- Run Routine "control" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image* updates
            
            # if image is starting this frame...
            if image.status == NOT_STARTED and tThisFlip >= timepresentation-frameTolerance:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image.started')
                # update status
                image.status = STARTED
                image.setAutoDraw(True)
            
            # if image is active this frame...
            if image.status == STARTED:
                # update params
                pass
            
            # if image is stopping this frame...
            if image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    image.tStop = t  # not accounting for scr refresh
                    image.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image.stopped')
                    # update status
                    image.status = FINISHED
                    image.setAutoDraw(False)
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= timepresentation-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                # update status
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp is stopping this frame...
            if key_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp.tStop = t  # not accounting for scr refresh
                    key_resp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp.stopped')
                    # update status
                    key_resp.status = FINISHED
                    key_resp.status = FINISHED
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    key_resp.duration = _key_resp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            # Run 'Each Frame' code from mar1
            mar_movie.draw()
            
            
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
            for thisComponent in controlComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "control" ---
        for thisComponent in controlComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('control.stopped', globalClock.getTime())
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        trials.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            trials.addData('key_resp.rt', key_resp.rt)
            trials.addData('key_resp.duration', key_resp.duration)
        # the Routine "control" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('imgs/iceberg_times.xlsx', selection=selectedRowsStr),
        seed=None, name='trials_2')
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            globals()[paramName] = thisTrial_2[paramName]
    
    for thisTrial_2 in trials_2:
        currentLoop = trials_2
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
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                globals()[paramName] = thisTrial_2[paramName]
        
        # --- Prepare to start Routine "music" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('music.started', globalClock.getTime())
        # Run 'Begin Routine' code from music_r1
        if ronda1=="music":
            continueRoutine = True
        else:
            continueRoutine = False
        image_2.setPos([posx, posy])
        image_2.setImage('imgs/iceberg.png')
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        # Run 'Begin Routine' code from code
        if trials_2.thisN == 0:
            background_sound.play()        
        # Run 'Begin Routine' code from mar2
        mar_movie.play()  
        
        # keep track of which components have finished
        musicComponents = [image_2, key_resp_2]
        for thisComponent in musicComponents:
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
        
        # --- Run Routine "music" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_2* updates
            
            # if image_2 is starting this frame...
            if image_2.status == NOT_STARTED and tThisFlip >= timepresentation-frameTolerance:
                # keep track of start time/frame for later
                image_2.frameNStart = frameN  # exact frame index
                image_2.tStart = t  # local t and not account for scr refresh
                image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_2.started')
                # update status
                image_2.status = STARTED
                image_2.setAutoDraw(True)
            
            # if image_2 is active this frame...
            if image_2.status == STARTED:
                # update params
                pass
            
            # if image_2 is stopping this frame...
            if image_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_2.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    image_2.tStop = t  # not accounting for scr refresh
                    image_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_2.stopped')
                    # update status
                    image_2.status = FINISHED
                    image_2.setAutoDraw(False)
            
            # *key_resp_2* updates
            waitOnFlip = False
            
            # if key_resp_2 is starting this frame...
            if key_resp_2.status == NOT_STARTED and tThisFlip >= timepresentation-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_2.started')
                # update status
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp_2 is stopping this frame...
            if key_resp_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_2.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_2.tStop = t  # not accounting for scr refresh
                    key_resp_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_2.stopped')
                    # update status
                    key_resp_2.status = FINISHED
                    key_resp_2.status = FINISHED
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    key_resp_2.duration = _key_resp_2_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            # Run 'Each Frame' code from code
            background_sound.draw()
            # Run 'Each Frame' code from mar2
            mar_movie.draw()
            
            
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
            for thisComponent in musicComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "music" ---
        for thisComponent in musicComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('music.stopped', globalClock.getTime())
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
        trials_2.addData('key_resp_2.keys',key_resp_2.keys)
        if key_resp_2.keys != None:  # we had a response
            trials_2.addData('key_resp_2.rt', key_resp_2.rt)
            trials_2.addData('key_resp_2.duration', key_resp_2.duration)
        # Run 'End Routine' code from code
        if trials_2.thisN == nRows-1:
            background_sound.stop()
        # the Routine "music" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials_2'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_3 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('imgs/iceberg_times.xlsx', selection=selectedRowsStr),
        seed=None, name='trials_3')
    thisExp.addLoop(trials_3)  # add the loop to the experiment
    thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            globals()[paramName] = thisTrial_3[paramName]
    
    for thisTrial_3 in trials_3:
        currentLoop = trials_3
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
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
        if thisTrial_3 != None:
            for paramName in thisTrial_3:
                globals()[paramName] = thisTrial_3[paramName]
        
        # --- Prepare to start Routine "music_words" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('music_words.started', globalClock.getTime())
        # Run 'Begin Routine' code from musicw_r1
        if ronda1=="music_words":
            continueRoutine = True
        else:
            continueRoutine = False
        # Run 'Begin Routine' code from code_2
        if trials_3.thisN == 0:
            background_movie.play()
            background_movie.draw()    
        # Run 'Begin Routine' code from mar3
        mar_movie.play()  
        
        image_3.setPos([posx, posy])
        image_3.setImage('imgs/iceberg.png')
        key_resp_3.keys = []
        key_resp_3.rt = []
        _key_resp_3_allKeys = []
        # keep track of which components have finished
        music_wordsComponents = [image_3, key_resp_3]
        for thisComponent in music_wordsComponents:
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
        
        # --- Run Routine "music_words" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_2
            background_movie.draw()
            # Run 'Each Frame' code from mar3
            mar_movie.draw()
            
            
            # *image_3* updates
            
            # if image_3 is starting this frame...
            if image_3.status == NOT_STARTED and tThisFlip >= timepresentation-frameTolerance:
                # keep track of start time/frame for later
                image_3.frameNStart = frameN  # exact frame index
                image_3.tStart = t  # local t and not account for scr refresh
                image_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_3.started')
                # update status
                image_3.status = STARTED
                image_3.setAutoDraw(True)
            
            # if image_3 is active this frame...
            if image_3.status == STARTED:
                # update params
                pass
            
            # if image_3 is stopping this frame...
            if image_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_3.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    image_3.tStop = t  # not accounting for scr refresh
                    image_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_3.stopped')
                    # update status
                    image_3.status = FINISHED
                    image_3.setAutoDraw(False)
            
            # *key_resp_3* updates
            waitOnFlip = False
            
            # if key_resp_3 is starting this frame...
            if key_resp_3.status == NOT_STARTED and tThisFlip >= timepresentation-frameTolerance:
                # keep track of start time/frame for later
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.tStart = t  # local t and not account for scr refresh
                key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_3.started')
                # update status
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp_3 is stopping this frame...
            if key_resp_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_3.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_3.tStop = t  # not accounting for scr refresh
                    key_resp_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_3.stopped')
                    # update status
                    key_resp_3.status = FINISHED
                    key_resp_3.status = FINISHED
            if key_resp_3.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_3.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_3_allKeys.extend(theseKeys)
                if len(_key_resp_3_allKeys):
                    key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                    key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                    key_resp_3.duration = _key_resp_3_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
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
            for thisComponent in music_wordsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "music_words" ---
        for thisComponent in music_wordsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('music_words.stopped', globalClock.getTime())
        # Run 'End Routine' code from code_2
        if trials_3.thisN == nRows-1:
            background_movie.stop()
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
            key_resp_3.keys = None
        trials_3.addData('key_resp_3.keys',key_resp_3.keys)
        if key_resp_3.keys != None:  # we had a response
            trials_3.addData('key_resp_3.rt', key_resp_3.rt)
            trials_3.addData('key_resp_3.duration', key_resp_3.duration)
        # the Routine "music_words" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials_3'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_4 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('imgs/iceberg_times.xlsx', selection=selectedRowsStr),
        seed=None, name='trials_4')
    thisExp.addLoop(trials_4)  # add the loop to the experiment
    thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            globals()[paramName] = thisTrial_4[paramName]
    
    for thisTrial_4 in trials_4:
        currentLoop = trials_4
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
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
        if thisTrial_4 != None:
            for paramName in thisTrial_4:
                globals()[paramName] = thisTrial_4[paramName]
        
        # --- Prepare to start Routine "music_video" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('music_video.started', globalClock.getTime())
        # Run 'Begin Routine' code from musicv_r1
        if ronda1=="music_video":
            continueRoutine = True
        else:
            continueRoutine = False
        # Run 'Begin Routine' code from code_2_2
        if trials_4.thisN == 0:
            background_movie2.play()
            background_movie2.draw()    
        # Run 'Begin Routine' code from mar4
        mar_movie.play()  
        
        # Run 'Begin Routine' code from code_3
        if trials_4.thisN == 0:
            displayed_movie.play()
            displayed_movie.draw()    
        image_4.setPos([posx, posy])
        image_4.setImage('imgs/iceberg.png')
        Key_resp_4.keys = []
        Key_resp_4.rt = []
        _Key_resp_4_allKeys = []
        # keep track of which components have finished
        music_videoComponents = [image_4, Key_resp_4]
        for thisComponent in music_videoComponents:
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
        
        # --- Run Routine "music_video" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_2_2
            background_movie2.draw()
            # Run 'Each Frame' code from mar4
            mar_movie.draw()
            
            # Run 'Each Frame' code from code_3
            displayed_movie.draw()
            
            
            # *image_4* updates
            
            # if image_4 is starting this frame...
            if image_4.status == NOT_STARTED and tThisFlip >= timepresentation-frameTolerance:
                # keep track of start time/frame for later
                image_4.frameNStart = frameN  # exact frame index
                image_4.tStart = t  # local t and not account for scr refresh
                image_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_4.started')
                # update status
                image_4.status = STARTED
                image_4.setAutoDraw(True)
            
            # if image_4 is active this frame...
            if image_4.status == STARTED:
                # update params
                pass
            
            # if image_4 is stopping this frame...
            if image_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_4.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    image_4.tStop = t  # not accounting for scr refresh
                    image_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_4.stopped')
                    # update status
                    image_4.status = FINISHED
                    image_4.setAutoDraw(False)
            
            # *Key_resp_4* updates
            waitOnFlip = False
            
            # if Key_resp_4 is starting this frame...
            if Key_resp_4.status == NOT_STARTED and tThisFlip >= timepresentation-frameTolerance:
                # keep track of start time/frame for later
                Key_resp_4.frameNStart = frameN  # exact frame index
                Key_resp_4.tStart = t  # local t and not account for scr refresh
                Key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Key_resp_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Key_resp_4.started')
                # update status
                Key_resp_4.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(Key_resp_4.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(Key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if Key_resp_4 is stopping this frame...
            if Key_resp_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Key_resp_4.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    Key_resp_4.tStop = t  # not accounting for scr refresh
                    Key_resp_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Key_resp_4.stopped')
                    # update status
                    Key_resp_4.status = FINISHED
                    Key_resp_4.status = FINISHED
            if Key_resp_4.status == STARTED and not waitOnFlip:
                theseKeys = Key_resp_4.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _Key_resp_4_allKeys.extend(theseKeys)
                if len(_Key_resp_4_allKeys):
                    Key_resp_4.keys = _Key_resp_4_allKeys[-1].name  # just the last key pressed
                    Key_resp_4.rt = _Key_resp_4_allKeys[-1].rt
                    Key_resp_4.duration = _Key_resp_4_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
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
            for thisComponent in music_videoComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "music_video" ---
        for thisComponent in music_videoComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('music_video.stopped', globalClock.getTime())
        # Run 'End Routine' code from code_2_2
        if trials_4.thisN == nRows-1:
            background_movie2.stop()
        # Run 'End Routine' code from code_3
        if trials_4.thisN == nRows-1:
            displayed_movie.stop()
        # check responses
        if Key_resp_4.keys in ['', [], None]:  # No response was made
            Key_resp_4.keys = None
        trials_4.addData('Key_resp_4.keys',Key_resp_4.keys)
        if Key_resp_4.keys != None:  # we had a response
            trials_4.addData('Key_resp_4.rt', Key_resp_4.rt)
            trials_4.addData('Key_resp_4.duration', Key_resp_4.duration)
        # the Routine "music_video" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials_4'
    
    
    # --- Prepare to start Routine "Ronda_2" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Ronda_2.started', globalClock.getTime())
    text_8.setText('Ronda 2/4')
    # Run 'Begin Routine' code from code_15
    totalRows = 118  # Replace with the total number of rows in your Excel file
    selectedRows = random.sample(range(totalRows), nRows)
    selectedRowsStr = [i for i in selectedRows]
    # keep track of which components have finished
    Ronda_2Components = [text_8]
    for thisComponent in Ronda_2Components:
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
    
    # --- Run Routine "Ronda_2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_8* updates
        
        # if text_8 is starting this frame...
        if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_8.frameNStart = frameN  # exact frame index
            text_8.tStart = t  # local t and not account for scr refresh
            text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_8.started')
            # update status
            text_8.status = STARTED
            text_8.setAutoDraw(True)
        
        # if text_8 is active this frame...
        if text_8.status == STARTED:
            # update params
            pass
        
        # if text_8 is stopping this frame...
        if text_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_8.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_8.tStop = t  # not accounting for scr refresh
                text_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_8.stopped')
                # update status
                text_8.status = FINISHED
                text_8.setAutoDraw(False)
        
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
        for thisComponent in Ronda_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Ronda_2" ---
    for thisComponent in Ronda_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Ronda_2.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    
    # set up handler to look after randomisation of conditions etc
    trials_5 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('imgs/iceberg_times.xlsx', selection=selectedRowsStr),
        seed=None, name='trials_5')
    thisExp.addLoop(trials_5)  # add the loop to the experiment
    thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
    if thisTrial_5 != None:
        for paramName in thisTrial_5:
            globals()[paramName] = thisTrial_5[paramName]
    
    for thisTrial_5 in trials_5:
        currentLoop = trials_5
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
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
        if thisTrial_5 != None:
            for paramName in thisTrial_5:
                globals()[paramName] = thisTrial_5[paramName]
        
        # --- Prepare to start Routine "control2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('control2.started', globalClock.getTime())
        # Run 'Begin Routine' code from control_r2
        if ronda2=="control":
            continueRoutine = True
        else:
            continueRoutine = False
        image_6.setPos([posx, posy])
        image_6.setImage('imgs/iceberg.png')
        key_resp_6.keys = []
        key_resp_6.rt = []
        _key_resp_6_allKeys = []
        # Run 'Begin Routine' code from mar_1_2
        mar_movie.play()  
        
        # keep track of which components have finished
        control2Components = [image_6, key_resp_6]
        for thisComponent in control2Components:
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
        
        # --- Run Routine "control2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_6* updates
            
            # if image_6 is starting this frame...
            if image_6.status == NOT_STARTED and tThisFlip >= timepresentation-frameTolerance:
                # keep track of start time/frame for later
                image_6.frameNStart = frameN  # exact frame index
                image_6.tStart = t  # local t and not account for scr refresh
                image_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_6.started')
                # update status
                image_6.status = STARTED
                image_6.setAutoDraw(True)
            
            # if image_6 is active this frame...
            if image_6.status == STARTED:
                # update params
                pass
            
            # if image_6 is stopping this frame...
            if image_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_6.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    image_6.tStop = t  # not accounting for scr refresh
                    image_6.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_6.stopped')
                    # update status
                    image_6.status = FINISHED
                    image_6.setAutoDraw(False)
            
            # *key_resp_6* updates
            waitOnFlip = False
            
            # if key_resp_6 is starting this frame...
            if key_resp_6.status == NOT_STARTED and tThisFlip >= timepresentation-frameTolerance:
                # keep track of start time/frame for later
                key_resp_6.frameNStart = frameN  # exact frame index
                key_resp_6.tStart = t  # local t and not account for scr refresh
                key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_6.started')
                # update status
                key_resp_6.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp_6 is stopping this frame...
            if key_resp_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_6.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_6.tStop = t  # not accounting for scr refresh
                    key_resp_6.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_6.stopped')
                    # update status
                    key_resp_6.status = FINISHED
                    key_resp_6.status = FINISHED
            if key_resp_6.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_6.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_6_allKeys.extend(theseKeys)
                if len(_key_resp_6_allKeys):
                    key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                    key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                    key_resp_6.duration = _key_resp_6_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            # Run 'Each Frame' code from mar_1_2
            mar_movie.draw()
            
            
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
            for thisComponent in control2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "control2" ---
        for thisComponent in control2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('control2.stopped', globalClock.getTime())
        # check responses
        if key_resp_6.keys in ['', [], None]:  # No response was made
            key_resp_6.keys = None
        trials_5.addData('key_resp_6.keys',key_resp_6.keys)
        if key_resp_6.keys != None:  # we had a response
            trials_5.addData('key_resp_6.rt', key_resp_6.rt)
            trials_5.addData('key_resp_6.duration', key_resp_6.duration)
        # the Routine "control2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials_5'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_6 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('imgs/iceberg_times.xlsx', selection=selectedRowsStr),
        seed=None, name='trials_6')
    thisExp.addLoop(trials_6)  # add the loop to the experiment
    thisTrial_6 = trials_6.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
    if thisTrial_6 != None:
        for paramName in thisTrial_6:
            globals()[paramName] = thisTrial_6[paramName]
    
    for thisTrial_6 in trials_6:
        currentLoop = trials_6
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
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
        if thisTrial_6 != None:
            for paramName in thisTrial_6:
                globals()[paramName] = thisTrial_6[paramName]
        
        # --- Prepare to start Routine "music2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('music2.started', globalClock.getTime())
        # Run 'Begin Routine' code from music_r2
        if ronda2=="music":
            continueRoutine = True
        else:
            continueRoutine = False
        image_7.setPos([posx, posy])
        image_7.setImage('imgs/iceberg.png')
        key_resp_7.keys = []
        key_resp_7.rt = []
        _key_resp_7_allKeys = []
        # Run 'Begin Routine' code from code_6
        if trials_6.thisN == 0:
            background_sound_r2.play()        
        # Run 'Begin Routine' code from mar2_2
        mar_movie.play()  
        
        # keep track of which components have finished
        music2Components = [image_7, key_resp_7]
        for thisComponent in music2Components:
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
        
        # --- Run Routine "music2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_7* updates
            
            # if image_7 is starting this frame...
            if image_7.status == NOT_STARTED and tThisFlip >= timepresentation-frameTolerance:
                # keep track of start time/frame for later
                image_7.frameNStart = frameN  # exact frame index
                image_7.tStart = t  # local t and not account for scr refresh
                image_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_7.started')
                # update status
                image_7.status = STARTED
                image_7.setAutoDraw(True)
            
            # if image_7 is active this frame...
            if image_7.status == STARTED:
                # update params
                pass
            
            # if image_7 is stopping this frame...
            if image_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_7.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    image_7.tStop = t  # not accounting for scr refresh
                    image_7.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_7.stopped')
                    # update status
                    image_7.status = FINISHED
                    image_7.setAutoDraw(False)
            
            # *key_resp_7* updates
            waitOnFlip = False
            
            # if key_resp_7 is starting this frame...
            if key_resp_7.status == NOT_STARTED and tThisFlip >= timepresentation-frameTolerance:
                # keep track of start time/frame for later
                key_resp_7.frameNStart = frameN  # exact frame index
                key_resp_7.tStart = t  # local t and not account for scr refresh
                key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_7.started')
                # update status
                key_resp_7.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp_7 is stopping this frame...
            if key_resp_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_7.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_7.tStop = t  # not accounting for scr refresh
                    key_resp_7.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_7.stopped')
                    # update status
                    key_resp_7.status = FINISHED
                    key_resp_7.status = FINISHED
            if key_resp_7.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_7.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_7_allKeys.extend(theseKeys)
                if len(_key_resp_7_allKeys):
                    key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                    key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                    key_resp_7.duration = _key_resp_7_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            # Run 'Each Frame' code from code_6
            background_sound_r2.draw()
            # Run 'Each Frame' code from mar2_2
            mar_movie.draw()
            
            
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
            for thisComponent in music2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "music2" ---
        for thisComponent in music2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('music2.stopped', globalClock.getTime())
        # check responses
        if key_resp_7.keys in ['', [], None]:  # No response was made
            key_resp_7.keys = None
        trials_6.addData('key_resp_7.keys',key_resp_7.keys)
        if key_resp_7.keys != None:  # we had a response
            trials_6.addData('key_resp_7.rt', key_resp_7.rt)
            trials_6.addData('key_resp_7.duration', key_resp_7.duration)
        # Run 'End Routine' code from code_6
        if trials_6.thisN == nRows-1:
            background_sound_r2.stop()
        # the Routine "music2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials_6'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_7 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('imgs/iceberg_times.xlsx', selection=selectedRowsStr),
        seed=None, name='trials_7')
    thisExp.addLoop(trials_7)  # add the loop to the experiment
    thisTrial_7 = trials_7.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_7.rgb)
    if thisTrial_7 != None:
        for paramName in thisTrial_7:
            globals()[paramName] = thisTrial_7[paramName]
    
    for thisTrial_7 in trials_7:
        currentLoop = trials_7
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
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_7.rgb)
        if thisTrial_7 != None:
            for paramName in thisTrial_7:
                globals()[paramName] = thisTrial_7[paramName]
        
        # --- Prepare to start Routine "music_words2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('music_words2.started', globalClock.getTime())
        # Run 'Begin Routine' code from musicw_r2
        if ronda2=="music_words":
            continueRoutine = True
        else:
            continueRoutine = False
        # Run 'Begin Routine' code from code_7
        if trials_7.thisN == 0:
            background_movie_r2.play()
            background_movie_r2.draw()    
        # Run 'Begin Routine' code from mar3_2
        mar_movie.play()  
        
        image_8.setPos([posx, posy])
        image_8.setImage('imgs/iceberg.png')
        key_resp_8.keys = []
        key_resp_8.rt = []
        _key_resp_8_allKeys = []
        # keep track of which components have finished
        music_words2Components = [image_8, key_resp_8]
        for thisComponent in music_words2Components:
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
        
        # --- Run Routine "music_words2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_7
            background_movie_r2.draw()
            # Run 'Each Frame' code from mar3_2
            mar_movie.draw()
            
            
            # *image_8* updates
            
            # if image_8 is starting this frame...
            if image_8.status == NOT_STARTED and tThisFlip >= timepresentation-frameTolerance:
                # keep track of start time/frame for later
                image_8.frameNStart = frameN  # exact frame index
                image_8.tStart = t  # local t and not account for scr refresh
                image_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_8.started')
                # update status
                image_8.status = STARTED
                image_8.setAutoDraw(True)
            
            # if image_8 is active this frame...
            if image_8.status == STARTED:
                # update params
                pass
            
            # if image_8 is stopping this frame...
            if image_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_8.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    image_8.tStop = t  # not accounting for scr refresh
                    image_8.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_8.stopped')
                    # update status
                    image_8.status = FINISHED
                    image_8.setAutoDraw(False)
            
            # *key_resp_8* updates
            waitOnFlip = False
            
            # if key_resp_8 is starting this frame...
            if key_resp_8.status == NOT_STARTED and tThisFlip >= timepresentation-frameTolerance:
                # keep track of start time/frame for later
                key_resp_8.frameNStart = frameN  # exact frame index
                key_resp_8.tStart = t  # local t and not account for scr refresh
                key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_8.started')
                # update status
                key_resp_8.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp_8 is stopping this frame...
            if key_resp_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_8.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_8.tStop = t  # not accounting for scr refresh
                    key_resp_8.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_8.stopped')
                    # update status
                    key_resp_8.status = FINISHED
                    key_resp_8.status = FINISHED
            if key_resp_8.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_8.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_8_allKeys.extend(theseKeys)
                if len(_key_resp_8_allKeys):
                    key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
                    key_resp_8.rt = _key_resp_8_allKeys[-1].rt
                    key_resp_8.duration = _key_resp_8_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
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
            for thisComponent in music_words2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "music_words2" ---
        for thisComponent in music_words2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('music_words2.stopped', globalClock.getTime())
        # Run 'End Routine' code from code_7
        if trials_7.thisN == nRows-1:
            background_movie_r2.stop()
        # check responses
        if key_resp_8.keys in ['', [], None]:  # No response was made
            key_resp_8.keys = None
        trials_7.addData('key_resp_8.keys',key_resp_8.keys)
        if key_resp_8.keys != None:  # we had a response
            trials_7.addData('key_resp_8.rt', key_resp_8.rt)
            trials_7.addData('key_resp_8.duration', key_resp_8.duration)
        # the Routine "music_words2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials_7'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_8 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('imgs/iceberg_times.xlsx', selection=selectedRowsStr),
        seed=None, name='trials_8')
    thisExp.addLoop(trials_8)  # add the loop to the experiment
    thisTrial_8 = trials_8.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_8.rgb)
    if thisTrial_8 != None:
        for paramName in thisTrial_8:
            globals()[paramName] = thisTrial_8[paramName]
    
    for thisTrial_8 in trials_8:
        currentLoop = trials_8
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
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_8.rgb)
        if thisTrial_8 != None:
            for paramName in thisTrial_8:
                globals()[paramName] = thisTrial_8[paramName]
        
        # --- Prepare to start Routine "music_video2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('music_video2.started', globalClock.getTime())
        # Run 'Begin Routine' code from musicv_r2
        if ronda2=="music_video":
            continueRoutine = True
        else:
            continueRoutine = False
        # Run 'Begin Routine' code from code_2_3
        if trials_8.thisN == 0:
            backgroung_movie2_r2.play()
            backgroung_movie2_r2.draw()    
        # Run 'Begin Routine' code from mar4_2
        mar_movie.play()  
        
        # Run 'Begin Routine' code from code_8
        if trials_8.thisN == 0:
            displayed_movie_r2.play()
            displayed_movie_r2.draw()    
        image_9.setPos([posx, posy])
        image_9.setImage('imgs/iceberg.png')
        Key_resp.keys = []
        Key_resp.rt = []
        _Key_resp_allKeys = []
        # keep track of which components have finished
        music_video2Components = [image_9, Key_resp]
        for thisComponent in music_video2Components:
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
        
        # --- Run Routine "music_video2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_2_3
            backgroung_movie2_r2.draw()
            # Run 'Each Frame' code from mar4_2
            mar_movie.draw()
            
            # Run 'Each Frame' code from code_8
            displayed_movie_r2.draw()
            
            
            # *image_9* updates
            
            # if image_9 is starting this frame...
            if image_9.status == NOT_STARTED and tThisFlip >= timepresentation-frameTolerance:
                # keep track of start time/frame for later
                image_9.frameNStart = frameN  # exact frame index
                image_9.tStart = t  # local t and not account for scr refresh
                image_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_9, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_9.started')
                # update status
                image_9.status = STARTED
                image_9.setAutoDraw(True)
            
            # if image_9 is active this frame...
            if image_9.status == STARTED:
                # update params
                pass
            
            # if image_9 is stopping this frame...
            if image_9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_9.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    image_9.tStop = t  # not accounting for scr refresh
                    image_9.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_9.stopped')
                    # update status
                    image_9.status = FINISHED
                    image_9.setAutoDraw(False)
            
            # *Key_resp* updates
            waitOnFlip = False
            
            # if Key_resp is starting this frame...
            if Key_resp.status == NOT_STARTED and tThisFlip >= timepresentation-frameTolerance:
                # keep track of start time/frame for later
                Key_resp.frameNStart = frameN  # exact frame index
                Key_resp.tStart = t  # local t and not account for scr refresh
                Key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Key_resp.started')
                # update status
                Key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(Key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(Key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if Key_resp is stopping this frame...
            if Key_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Key_resp.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    Key_resp.tStop = t  # not accounting for scr refresh
                    Key_resp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Key_resp.stopped')
                    # update status
                    Key_resp.status = FINISHED
                    Key_resp.status = FINISHED
            if Key_resp.status == STARTED and not waitOnFlip:
                theseKeys = Key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _Key_resp_allKeys.extend(theseKeys)
                if len(_Key_resp_allKeys):
                    Key_resp.keys = _Key_resp_allKeys[-1].name  # just the last key pressed
                    Key_resp.rt = _Key_resp_allKeys[-1].rt
                    Key_resp.duration = _Key_resp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
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
            for thisComponent in music_video2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "music_video2" ---
        for thisComponent in music_video2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('music_video2.stopped', globalClock.getTime())
        # Run 'End Routine' code from code_2_3
        if trials_8.thisN == nRows-1:
            backgroung_movie2_r2.stop()
        # Run 'End Routine' code from code_8
        if trials_8.thisN == nRows-1:
            displayed_movie_r2.stop()
        # check responses
        if Key_resp.keys in ['', [], None]:  # No response was made
            Key_resp.keys = None
        trials_8.addData('Key_resp.keys',Key_resp.keys)
        if Key_resp.keys != None:  # we had a response
            trials_8.addData('Key_resp.rt', Key_resp.rt)
            trials_8.addData('Key_resp.duration', Key_resp.duration)
        # the Routine "music_video2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials_8'
    
    
    # --- Prepare to start Routine "Ronda_3" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Ronda_3.started', globalClock.getTime())
    text_9.setText('Ronda 3/4')
    # Run 'Begin Routine' code from code_16
    totalRows = 118  # Replace with the total number of rows in your Excel file
    selectedRows = random.sample(range(totalRows), nRows)
    selectedRowsStr = [i for i in selectedRows]
    # keep track of which components have finished
    Ronda_3Components = [text_9]
    for thisComponent in Ronda_3Components:
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
    
    # --- Run Routine "Ronda_3" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_9* updates
        
        # if text_9 is starting this frame...
        if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_9.frameNStart = frameN  # exact frame index
            text_9.tStart = t  # local t and not account for scr refresh
            text_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_9.started')
            # update status
            text_9.status = STARTED
            text_9.setAutoDraw(True)
        
        # if text_9 is active this frame...
        if text_9.status == STARTED:
            # update params
            pass
        
        # if text_9 is stopping this frame...
        if text_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_9.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_9.tStop = t  # not accounting for scr refresh
                text_9.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_9.stopped')
                # update status
                text_9.status = FINISHED
                text_9.setAutoDraw(False)
        
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
        for thisComponent in Ronda_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Ronda_3" ---
    for thisComponent in Ronda_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Ronda_3.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    
    # set up handler to look after randomisation of conditions etc
    trials_9 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('imgs/iceberg_times.xlsx', selection=selectedRowsStr),
        seed=None, name='trials_9')
    thisExp.addLoop(trials_9)  # add the loop to the experiment
    thisTrial_9 = trials_9.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_9.rgb)
    if thisTrial_9 != None:
        for paramName in thisTrial_9:
            globals()[paramName] = thisTrial_9[paramName]
    
    for thisTrial_9 in trials_9:
        currentLoop = trials_9
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
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_9.rgb)
        if thisTrial_9 != None:
            for paramName in thisTrial_9:
                globals()[paramName] = thisTrial_9[paramName]
        
        # --- Prepare to start Routine "control3" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('control3.started', globalClock.getTime())
        # Run 'Begin Routine' code from control_r3
        if ronda3=="control":
            continueRoutine = True
        else:
            continueRoutine = False
        image_10.setPos([posx, posy])
        image_10.setImage('imgs/iceberg.png')
        key_resp_9.keys = []
        key_resp_9.rt = []
        _key_resp_9_allKeys = []
        # Run 'Begin Routine' code from mar_1_3
        mar_movie.play()  
        
        # keep track of which components have finished
        control3Components = [image_10, key_resp_9]
        for thisComponent in control3Components:
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
        
        # --- Run Routine "control3" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_10* updates
            
            # if image_10 is starting this frame...
            if image_10.status == NOT_STARTED and tThisFlip >= timepresentation-frameTolerance:
                # keep track of start time/frame for later
                image_10.frameNStart = frameN  # exact frame index
                image_10.tStart = t  # local t and not account for scr refresh
                image_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_10, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_10.started')
                # update status
                image_10.status = STARTED
                image_10.setAutoDraw(True)
            
            # if image_10 is active this frame...
            if image_10.status == STARTED:
                # update params
                pass
            
            # if image_10 is stopping this frame...
            if image_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_10.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    image_10.tStop = t  # not accounting for scr refresh
                    image_10.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_10.stopped')
                    # update status
                    image_10.status = FINISHED
                    image_10.setAutoDraw(False)
            
            # *key_resp_9* updates
            waitOnFlip = False
            
            # if key_resp_9 is starting this frame...
            if key_resp_9.status == NOT_STARTED and tThisFlip >= timepresentation-frameTolerance:
                # keep track of start time/frame for later
                key_resp_9.frameNStart = frameN  # exact frame index
                key_resp_9.tStart = t  # local t and not account for scr refresh
                key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_9.started')
                # update status
                key_resp_9.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp_9 is stopping this frame...
            if key_resp_9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_9.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_9.tStop = t  # not accounting for scr refresh
                    key_resp_9.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_9.stopped')
                    # update status
                    key_resp_9.status = FINISHED
                    key_resp_9.status = FINISHED
            if key_resp_9.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_9.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_9_allKeys.extend(theseKeys)
                if len(_key_resp_9_allKeys):
                    key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
                    key_resp_9.rt = _key_resp_9_allKeys[-1].rt
                    key_resp_9.duration = _key_resp_9_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            # Run 'Each Frame' code from mar_1_3
            mar_movie.draw()
            
            
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
            for thisComponent in control3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "control3" ---
        for thisComponent in control3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('control3.stopped', globalClock.getTime())
        # check responses
        if key_resp_9.keys in ['', [], None]:  # No response was made
            key_resp_9.keys = None
        trials_9.addData('key_resp_9.keys',key_resp_9.keys)
        if key_resp_9.keys != None:  # we had a response
            trials_9.addData('key_resp_9.rt', key_resp_9.rt)
            trials_9.addData('key_resp_9.duration', key_resp_9.duration)
        # the Routine "control3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials_9'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_10 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('imgs/iceberg_times.xlsx', selection=selectedRowsStr),
        seed=None, name='trials_10')
    thisExp.addLoop(trials_10)  # add the loop to the experiment
    thisTrial_10 = trials_10.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_10.rgb)
    if thisTrial_10 != None:
        for paramName in thisTrial_10:
            globals()[paramName] = thisTrial_10[paramName]
    
    for thisTrial_10 in trials_10:
        currentLoop = trials_10
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
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_10.rgb)
        if thisTrial_10 != None:
            for paramName in thisTrial_10:
                globals()[paramName] = thisTrial_10[paramName]
        
        # --- Prepare to start Routine "music3" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('music3.started', globalClock.getTime())
        # Run 'Begin Routine' code from music_r3
        if ronda3=="music":
            continueRoutine = True
        else:
            continueRoutine = False
        image_11.setPos([posx, posy])
        image_11.setImage('imgs/iceberg.png')
        key_resp_10.keys = []
        key_resp_10.rt = []
        _key_resp_10_allKeys = []
        # Run 'Begin Routine' code from code_9
        if trials_10.thisN == 0:
            background_sound_r3.play()        
        # Run 'Begin Routine' code from mar2_3
        mar_movie.play()  
        
        # keep track of which components have finished
        music3Components = [image_11, key_resp_10]
        for thisComponent in music3Components:
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
        
        # --- Run Routine "music3" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_11* updates
            
            # if image_11 is starting this frame...
            if image_11.status == NOT_STARTED and tThisFlip >= timepresentation-frameTolerance:
                # keep track of start time/frame for later
                image_11.frameNStart = frameN  # exact frame index
                image_11.tStart = t  # local t and not account for scr refresh
                image_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_11, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_11.started')
                # update status
                image_11.status = STARTED
                image_11.setAutoDraw(True)
            
            # if image_11 is active this frame...
            if image_11.status == STARTED:
                # update params
                pass
            
            # if image_11 is stopping this frame...
            if image_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_11.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    image_11.tStop = t  # not accounting for scr refresh
                    image_11.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_11.stopped')
                    # update status
                    image_11.status = FINISHED
                    image_11.setAutoDraw(False)
            
            # *key_resp_10* updates
            waitOnFlip = False
            
            # if key_resp_10 is starting this frame...
            if key_resp_10.status == NOT_STARTED and tThisFlip >= timepresentation-frameTolerance:
                # keep track of start time/frame for later
                key_resp_10.frameNStart = frameN  # exact frame index
                key_resp_10.tStart = t  # local t and not account for scr refresh
                key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_10.started')
                # update status
                key_resp_10.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp_10 is stopping this frame...
            if key_resp_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_10.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_10.tStop = t  # not accounting for scr refresh
                    key_resp_10.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_10.stopped')
                    # update status
                    key_resp_10.status = FINISHED
                    key_resp_10.status = FINISHED
            if key_resp_10.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_10.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_10_allKeys.extend(theseKeys)
                if len(_key_resp_10_allKeys):
                    key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
                    key_resp_10.rt = _key_resp_10_allKeys[-1].rt
                    key_resp_10.duration = _key_resp_10_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            # Run 'Each Frame' code from code_9
            background_sound_r3.draw()
            # Run 'Each Frame' code from mar2_3
            mar_movie.draw()
            
            
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
            for thisComponent in music3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "music3" ---
        for thisComponent in music3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('music3.stopped', globalClock.getTime())
        # check responses
        if key_resp_10.keys in ['', [], None]:  # No response was made
            key_resp_10.keys = None
        trials_10.addData('key_resp_10.keys',key_resp_10.keys)
        if key_resp_10.keys != None:  # we had a response
            trials_10.addData('key_resp_10.rt', key_resp_10.rt)
            trials_10.addData('key_resp_10.duration', key_resp_10.duration)
        # Run 'End Routine' code from code_9
        if trials_10.thisN == nRows-1:
            background_sound_r3.stop()
        # the Routine "music3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials_10'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_11 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('imgs/iceberg_times.xlsx', selection=selectedRowsStr),
        seed=None, name='trials_11')
    thisExp.addLoop(trials_11)  # add the loop to the experiment
    thisTrial_11 = trials_11.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_11.rgb)
    if thisTrial_11 != None:
        for paramName in thisTrial_11:
            globals()[paramName] = thisTrial_11[paramName]
    
    for thisTrial_11 in trials_11:
        currentLoop = trials_11
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
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_11.rgb)
        if thisTrial_11 != None:
            for paramName in thisTrial_11:
                globals()[paramName] = thisTrial_11[paramName]
        
        # --- Prepare to start Routine "music_words3" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('music_words3.started', globalClock.getTime())
        # Run 'Begin Routine' code from musicw_r3
        if ronda3=="music_words":
            continueRoutine = True
        else:
            continueRoutine = False
        # Run 'Begin Routine' code from code_10
        if trials_11.thisN == 0:
            background_movie_r3.play()
            background_movie_r3.draw()    
        # Run 'Begin Routine' code from mar3_3
        mar_movie.play()  
        
        image_12.setPos([posx, posy])
        image_12.setImage('imgs/iceberg.png')
        key_resp_11.keys = []
        key_resp_11.rt = []
        _key_resp_11_allKeys = []
        # keep track of which components have finished
        music_words3Components = [image_12, key_resp_11]
        for thisComponent in music_words3Components:
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
        
        # --- Run Routine "music_words3" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_10
            background_movie_r3.draw()
            # Run 'Each Frame' code from mar3_3
            mar_movie.draw()
            
            
            # *image_12* updates
            
            # if image_12 is starting this frame...
            if image_12.status == NOT_STARTED and tThisFlip >= timepresentation-frameTolerance:
                # keep track of start time/frame for later
                image_12.frameNStart = frameN  # exact frame index
                image_12.tStart = t  # local t and not account for scr refresh
                image_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_12, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_12.started')
                # update status
                image_12.status = STARTED
                image_12.setAutoDraw(True)
            
            # if image_12 is active this frame...
            if image_12.status == STARTED:
                # update params
                pass
            
            # if image_12 is stopping this frame...
            if image_12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_12.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    image_12.tStop = t  # not accounting for scr refresh
                    image_12.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_12.stopped')
                    # update status
                    image_12.status = FINISHED
                    image_12.setAutoDraw(False)
            
            # *key_resp_11* updates
            waitOnFlip = False
            
            # if key_resp_11 is starting this frame...
            if key_resp_11.status == NOT_STARTED and tThisFlip >= timepresentation-frameTolerance:
                # keep track of start time/frame for later
                key_resp_11.frameNStart = frameN  # exact frame index
                key_resp_11.tStart = t  # local t and not account for scr refresh
                key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_11.started')
                # update status
                key_resp_11.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp_11 is stopping this frame...
            if key_resp_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_11.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_11.tStop = t  # not accounting for scr refresh
                    key_resp_11.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_11.stopped')
                    # update status
                    key_resp_11.status = FINISHED
                    key_resp_11.status = FINISHED
            if key_resp_11.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_11.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_11_allKeys.extend(theseKeys)
                if len(_key_resp_11_allKeys):
                    key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
                    key_resp_11.rt = _key_resp_11_allKeys[-1].rt
                    key_resp_11.duration = _key_resp_11_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
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
            for thisComponent in music_words3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "music_words3" ---
        for thisComponent in music_words3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('music_words3.stopped', globalClock.getTime())
        # Run 'End Routine' code from code_10
        if trials_11.thisN == nRows-1:
            background_movie_r3.stop()
        # check responses
        if key_resp_11.keys in ['', [], None]:  # No response was made
            key_resp_11.keys = None
        trials_11.addData('key_resp_11.keys',key_resp_11.keys)
        if key_resp_11.keys != None:  # we had a response
            trials_11.addData('key_resp_11.rt', key_resp_11.rt)
            trials_11.addData('key_resp_11.duration', key_resp_11.duration)
        # the Routine "music_words3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials_11'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_12 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('imgs/iceberg_times.xlsx', selection=selectedRowsStr),
        seed=None, name='trials_12')
    thisExp.addLoop(trials_12)  # add the loop to the experiment
    thisTrial_12 = trials_12.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_12.rgb)
    if thisTrial_12 != None:
        for paramName in thisTrial_12:
            globals()[paramName] = thisTrial_12[paramName]
    
    for thisTrial_12 in trials_12:
        currentLoop = trials_12
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
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_12.rgb)
        if thisTrial_12 != None:
            for paramName in thisTrial_12:
                globals()[paramName] = thisTrial_12[paramName]
        
        # --- Prepare to start Routine "music_video3" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('music_video3.started', globalClock.getTime())
        # Run 'Begin Routine' code from musicv_r3
        if ronda3=="music_video":
            continueRoutine = True
        else:
            continueRoutine = False
        # Run 'Begin Routine' code from code_2_4
        if trials_12.thisN == 0:
            backgroung_movie2_r3.play()
            backgroung_movie2_r3.draw()    
        # Run 'Begin Routine' code from mar4_3
        mar_movie.play()  
        
        # Run 'Begin Routine' code from code_11
        if trials_12.thisN == 0:
            displayed_movie_r3.play()
            displayed_movie_r3.draw()    
        image_13.setPos([posx, posy])
        image_13.setImage('imgs/iceberg.png')
        Key_resp_2.keys = []
        Key_resp_2.rt = []
        _Key_resp_2_allKeys = []
        # keep track of which components have finished
        music_video3Components = [image_13, Key_resp_2]
        for thisComponent in music_video3Components:
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
        
        # --- Run Routine "music_video3" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_2_4
            backgroung_movie2_r3.draw()
            # Run 'Each Frame' code from mar4_3
            mar_movie.draw()
            
            # Run 'Each Frame' code from code_11
            displayed_movie_r3.draw()
            
            
            # *image_13* updates
            
            # if image_13 is starting this frame...
            if image_13.status == NOT_STARTED and tThisFlip >= timepresentation-frameTolerance:
                # keep track of start time/frame for later
                image_13.frameNStart = frameN  # exact frame index
                image_13.tStart = t  # local t and not account for scr refresh
                image_13.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_13, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_13.started')
                # update status
                image_13.status = STARTED
                image_13.setAutoDraw(True)
            
            # if image_13 is active this frame...
            if image_13.status == STARTED:
                # update params
                pass
            
            # if image_13 is stopping this frame...
            if image_13.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_13.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    image_13.tStop = t  # not accounting for scr refresh
                    image_13.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_13.stopped')
                    # update status
                    image_13.status = FINISHED
                    image_13.setAutoDraw(False)
            
            # *Key_resp_2* updates
            waitOnFlip = False
            
            # if Key_resp_2 is starting this frame...
            if Key_resp_2.status == NOT_STARTED and tThisFlip >= timepresentation-frameTolerance:
                # keep track of start time/frame for later
                Key_resp_2.frameNStart = frameN  # exact frame index
                Key_resp_2.tStart = t  # local t and not account for scr refresh
                Key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Key_resp_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Key_resp_2.started')
                # update status
                Key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(Key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(Key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if Key_resp_2 is stopping this frame...
            if Key_resp_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Key_resp_2.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    Key_resp_2.tStop = t  # not accounting for scr refresh
                    Key_resp_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Key_resp_2.stopped')
                    # update status
                    Key_resp_2.status = FINISHED
                    Key_resp_2.status = FINISHED
            if Key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = Key_resp_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _Key_resp_2_allKeys.extend(theseKeys)
                if len(_Key_resp_2_allKeys):
                    Key_resp_2.keys = _Key_resp_2_allKeys[-1].name  # just the last key pressed
                    Key_resp_2.rt = _Key_resp_2_allKeys[-1].rt
                    Key_resp_2.duration = _Key_resp_2_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
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
            for thisComponent in music_video3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "music_video3" ---
        for thisComponent in music_video3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('music_video3.stopped', globalClock.getTime())
        # Run 'End Routine' code from code_2_4
        if trials_12.thisN == nRows-1:
            backgroung_movie2_r3.stop()
        # Run 'End Routine' code from code_11
        if trials_12.thisN == nRows-1:
            displayed_movie_r3.stop()
        # check responses
        if Key_resp_2.keys in ['', [], None]:  # No response was made
            Key_resp_2.keys = None
        trials_12.addData('Key_resp_2.keys',Key_resp_2.keys)
        if Key_resp_2.keys != None:  # we had a response
            trials_12.addData('Key_resp_2.rt', Key_resp_2.rt)
            trials_12.addData('Key_resp_2.duration', Key_resp_2.duration)
        # the Routine "music_video3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials_12'
    
    
    # --- Prepare to start Routine "Ronda_4" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Ronda_4.started', globalClock.getTime())
    text_10.setText('Ronda 4/4')
    # Run 'Begin Routine' code from code_17
    totalRows = 118  # Replace with the total number of rows in your Excel file
    selectedRows = random.sample(range(totalRows), nRows)
    selectedRowsStr = [i for i in selectedRows]
    # keep track of which components have finished
    Ronda_4Components = [text_10]
    for thisComponent in Ronda_4Components:
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
    
    # --- Run Routine "Ronda_4" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_10* updates
        
        # if text_10 is starting this frame...
        if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_10.frameNStart = frameN  # exact frame index
            text_10.tStart = t  # local t and not account for scr refresh
            text_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_10.started')
            # update status
            text_10.status = STARTED
            text_10.setAutoDraw(True)
        
        # if text_10 is active this frame...
        if text_10.status == STARTED:
            # update params
            pass
        
        # if text_10 is stopping this frame...
        if text_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_10.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_10.tStop = t  # not accounting for scr refresh
                text_10.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_10.stopped')
                # update status
                text_10.status = FINISHED
                text_10.setAutoDraw(False)
        
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
        for thisComponent in Ronda_4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Ronda_4" ---
    for thisComponent in Ronda_4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Ronda_4.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    
    # set up handler to look after randomisation of conditions etc
    trials_13 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('imgs/iceberg_times.xlsx', selection=selectedRowsStr),
        seed=None, name='trials_13')
    thisExp.addLoop(trials_13)  # add the loop to the experiment
    thisTrial_13 = trials_13.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_13.rgb)
    if thisTrial_13 != None:
        for paramName in thisTrial_13:
            globals()[paramName] = thisTrial_13[paramName]
    
    for thisTrial_13 in trials_13:
        currentLoop = trials_13
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
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_13.rgb)
        if thisTrial_13 != None:
            for paramName in thisTrial_13:
                globals()[paramName] = thisTrial_13[paramName]
        
        # --- Prepare to start Routine "control4" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('control4.started', globalClock.getTime())
        # Run 'Begin Routine' code from control_r4
        if ronda4=="control":
            continueRoutine = True
        else:
            continueRoutine = False
        image_14.setPos([posx, posy])
        image_14.setImage('imgs/iceberg.png')
        key_resp_12.keys = []
        key_resp_12.rt = []
        _key_resp_12_allKeys = []
        # Run 'Begin Routine' code from mar_1_4
        mar_movie.play()  
        
        # keep track of which components have finished
        control4Components = [image_14, key_resp_12]
        for thisComponent in control4Components:
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
        
        # --- Run Routine "control4" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_14* updates
            
            # if image_14 is starting this frame...
            if image_14.status == NOT_STARTED and tThisFlip >= timepresentation-frameTolerance:
                # keep track of start time/frame for later
                image_14.frameNStart = frameN  # exact frame index
                image_14.tStart = t  # local t and not account for scr refresh
                image_14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_14, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_14.started')
                # update status
                image_14.status = STARTED
                image_14.setAutoDraw(True)
            
            # if image_14 is active this frame...
            if image_14.status == STARTED:
                # update params
                pass
            
            # if image_14 is stopping this frame...
            if image_14.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_14.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    image_14.tStop = t  # not accounting for scr refresh
                    image_14.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_14.stopped')
                    # update status
                    image_14.status = FINISHED
                    image_14.setAutoDraw(False)
            
            # *key_resp_12* updates
            waitOnFlip = False
            
            # if key_resp_12 is starting this frame...
            if key_resp_12.status == NOT_STARTED and tThisFlip >= timepresentation-frameTolerance:
                # keep track of start time/frame for later
                key_resp_12.frameNStart = frameN  # exact frame index
                key_resp_12.tStart = t  # local t and not account for scr refresh
                key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_12.started')
                # update status
                key_resp_12.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp_12 is stopping this frame...
            if key_resp_12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_12.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_12.tStop = t  # not accounting for scr refresh
                    key_resp_12.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_12.stopped')
                    # update status
                    key_resp_12.status = FINISHED
                    key_resp_12.status = FINISHED
            if key_resp_12.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_12.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_12_allKeys.extend(theseKeys)
                if len(_key_resp_12_allKeys):
                    key_resp_12.keys = _key_resp_12_allKeys[-1].name  # just the last key pressed
                    key_resp_12.rt = _key_resp_12_allKeys[-1].rt
                    key_resp_12.duration = _key_resp_12_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            # Run 'Each Frame' code from mar_1_4
            mar_movie.draw()
            
            
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
            for thisComponent in control4Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "control4" ---
        for thisComponent in control4Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('control4.stopped', globalClock.getTime())
        # check responses
        if key_resp_12.keys in ['', [], None]:  # No response was made
            key_resp_12.keys = None
        trials_13.addData('key_resp_12.keys',key_resp_12.keys)
        if key_resp_12.keys != None:  # we had a response
            trials_13.addData('key_resp_12.rt', key_resp_12.rt)
            trials_13.addData('key_resp_12.duration', key_resp_12.duration)
        # the Routine "control4" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials_13'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_14 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('imgs/iceberg_times.xlsx', selection=selectedRowsStr),
        seed=None, name='trials_14')
    thisExp.addLoop(trials_14)  # add the loop to the experiment
    thisTrial_14 = trials_14.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_14.rgb)
    if thisTrial_14 != None:
        for paramName in thisTrial_14:
            globals()[paramName] = thisTrial_14[paramName]
    
    for thisTrial_14 in trials_14:
        currentLoop = trials_14
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
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_14.rgb)
        if thisTrial_14 != None:
            for paramName in thisTrial_14:
                globals()[paramName] = thisTrial_14[paramName]
        
        # --- Prepare to start Routine "music4" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('music4.started', globalClock.getTime())
        # Run 'Begin Routine' code from music_r4
        if ronda4=="music":
            continueRoutine = True
        else:
            continueRoutine = False
        image_15.setPos([posx, posy])
        image_15.setImage('imgs/iceberg.png')
        key_resp_13.keys = []
        key_resp_13.rt = []
        _key_resp_13_allKeys = []
        # Run 'Begin Routine' code from code_12
        if trials_14.thisN == 0:
            background_sound_r4.play()        
        # Run 'Begin Routine' code from mar2_4
        mar_movie.play()  
        
        # keep track of which components have finished
        music4Components = [image_15, key_resp_13]
        for thisComponent in music4Components:
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
        
        # --- Run Routine "music4" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_15* updates
            
            # if image_15 is starting this frame...
            if image_15.status == NOT_STARTED and tThisFlip >= timepresentation-frameTolerance:
                # keep track of start time/frame for later
                image_15.frameNStart = frameN  # exact frame index
                image_15.tStart = t  # local t and not account for scr refresh
                image_15.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_15, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_15.started')
                # update status
                image_15.status = STARTED
                image_15.setAutoDraw(True)
            
            # if image_15 is active this frame...
            if image_15.status == STARTED:
                # update params
                pass
            
            # if image_15 is stopping this frame...
            if image_15.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_15.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    image_15.tStop = t  # not accounting for scr refresh
                    image_15.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_15.stopped')
                    # update status
                    image_15.status = FINISHED
                    image_15.setAutoDraw(False)
            
            # *key_resp_13* updates
            waitOnFlip = False
            
            # if key_resp_13 is starting this frame...
            if key_resp_13.status == NOT_STARTED and tThisFlip >= timepresentation-frameTolerance:
                # keep track of start time/frame for later
                key_resp_13.frameNStart = frameN  # exact frame index
                key_resp_13.tStart = t  # local t and not account for scr refresh
                key_resp_13.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_13, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_13.started')
                # update status
                key_resp_13.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_13.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp_13 is stopping this frame...
            if key_resp_13.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_13.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_13.tStop = t  # not accounting for scr refresh
                    key_resp_13.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_13.stopped')
                    # update status
                    key_resp_13.status = FINISHED
                    key_resp_13.status = FINISHED
            if key_resp_13.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_13.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_13_allKeys.extend(theseKeys)
                if len(_key_resp_13_allKeys):
                    key_resp_13.keys = _key_resp_13_allKeys[-1].name  # just the last key pressed
                    key_resp_13.rt = _key_resp_13_allKeys[-1].rt
                    key_resp_13.duration = _key_resp_13_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            # Run 'Each Frame' code from code_12
            background_sound_r4.draw()
            # Run 'Each Frame' code from mar2_4
            mar_movie.draw()
            
            
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
            for thisComponent in music4Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "music4" ---
        for thisComponent in music4Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('music4.stopped', globalClock.getTime())
        # check responses
        if key_resp_13.keys in ['', [], None]:  # No response was made
            key_resp_13.keys = None
        trials_14.addData('key_resp_13.keys',key_resp_13.keys)
        if key_resp_13.keys != None:  # we had a response
            trials_14.addData('key_resp_13.rt', key_resp_13.rt)
            trials_14.addData('key_resp_13.duration', key_resp_13.duration)
        # Run 'End Routine' code from code_12
        if trials_14.thisN == nRows-1:
            background_sound_r4.stop()
        # the Routine "music4" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials_14'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_15 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('imgs/iceberg_times.xlsx', selection=selectedRowsStr),
        seed=None, name='trials_15')
    thisExp.addLoop(trials_15)  # add the loop to the experiment
    thisTrial_15 = trials_15.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_15.rgb)
    if thisTrial_15 != None:
        for paramName in thisTrial_15:
            globals()[paramName] = thisTrial_15[paramName]
    
    for thisTrial_15 in trials_15:
        currentLoop = trials_15
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
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_15.rgb)
        if thisTrial_15 != None:
            for paramName in thisTrial_15:
                globals()[paramName] = thisTrial_15[paramName]
        
        # --- Prepare to start Routine "music_words4" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('music_words4.started', globalClock.getTime())
        # Run 'Begin Routine' code from musicw_r4
        if ronda4=="music_words":
            continueRoutine = True
        else:
            continueRoutine = False
        # Run 'Begin Routine' code from code_13
        if trials_15.thisN == 0:
            background_movie_r4.play()
            background_movie_r4.draw()    
        # Run 'Begin Routine' code from mar_3_4
        mar_movie.play()  
        
        image_16.setPos([posx, posy])
        image_16.setImage('imgs/iceberg.png')
        key_resp_14.keys = []
        key_resp_14.rt = []
        _key_resp_14_allKeys = []
        # keep track of which components have finished
        music_words4Components = [image_16, key_resp_14]
        for thisComponent in music_words4Components:
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
        
        # --- Run Routine "music_words4" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_13
            background_movie_r4.draw()
            # Run 'Each Frame' code from mar_3_4
            mar_movie.draw()
            
            
            # *image_16* updates
            
            # if image_16 is starting this frame...
            if image_16.status == NOT_STARTED and tThisFlip >= timepresentation-frameTolerance:
                # keep track of start time/frame for later
                image_16.frameNStart = frameN  # exact frame index
                image_16.tStart = t  # local t and not account for scr refresh
                image_16.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_16, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_16.started')
                # update status
                image_16.status = STARTED
                image_16.setAutoDraw(True)
            
            # if image_16 is active this frame...
            if image_16.status == STARTED:
                # update params
                pass
            
            # if image_16 is stopping this frame...
            if image_16.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_16.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    image_16.tStop = t  # not accounting for scr refresh
                    image_16.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_16.stopped')
                    # update status
                    image_16.status = FINISHED
                    image_16.setAutoDraw(False)
            
            # *key_resp_14* updates
            waitOnFlip = False
            
            # if key_resp_14 is starting this frame...
            if key_resp_14.status == NOT_STARTED and tThisFlip >= timepresentation-frameTolerance:
                # keep track of start time/frame for later
                key_resp_14.frameNStart = frameN  # exact frame index
                key_resp_14.tStart = t  # local t and not account for scr refresh
                key_resp_14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_14, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_14.started')
                # update status
                key_resp_14.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_14.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp_14 is stopping this frame...
            if key_resp_14.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_14.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_14.tStop = t  # not accounting for scr refresh
                    key_resp_14.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_14.stopped')
                    # update status
                    key_resp_14.status = FINISHED
                    key_resp_14.status = FINISHED
            if key_resp_14.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_14.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_14_allKeys.extend(theseKeys)
                if len(_key_resp_14_allKeys):
                    key_resp_14.keys = _key_resp_14_allKeys[-1].name  # just the last key pressed
                    key_resp_14.rt = _key_resp_14_allKeys[-1].rt
                    key_resp_14.duration = _key_resp_14_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
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
            for thisComponent in music_words4Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "music_words4" ---
        for thisComponent in music_words4Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('music_words4.stopped', globalClock.getTime())
        # Run 'End Routine' code from code_13
        if trials_15.thisN == nRows-1:
            background_movie_r4.stop()
        # check responses
        if key_resp_14.keys in ['', [], None]:  # No response was made
            key_resp_14.keys = None
        trials_15.addData('key_resp_14.keys',key_resp_14.keys)
        if key_resp_14.keys != None:  # we had a response
            trials_15.addData('key_resp_14.rt', key_resp_14.rt)
            trials_15.addData('key_resp_14.duration', key_resp_14.duration)
        # the Routine "music_words4" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials_15'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_16 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('imgs/iceberg_times.xlsx', selection=selectedRowsStr),
        seed=None, name='trials_16')
    thisExp.addLoop(trials_16)  # add the loop to the experiment
    thisTrial_16 = trials_16.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_16.rgb)
    if thisTrial_16 != None:
        for paramName in thisTrial_16:
            globals()[paramName] = thisTrial_16[paramName]
    
    for thisTrial_16 in trials_16:
        currentLoop = trials_16
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
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_16.rgb)
        if thisTrial_16 != None:
            for paramName in thisTrial_16:
                globals()[paramName] = thisTrial_16[paramName]
        
        # --- Prepare to start Routine "music_video4" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('music_video4.started', globalClock.getTime())
        # Run 'Begin Routine' code from musicv_r4
        if ronda4=="music_video":
            continueRoutine = True
        else:
            continueRoutine = False
        # Run 'Begin Routine' code from code_2_5
        if trials_16.thisN == 0:
            backgroung_movie2_r4.play()
            backgroung_movie2_r4.draw()    
        # Run 'Begin Routine' code from mar4_4
        mar_movie.play()  
        
        # Run 'Begin Routine' code from code_14
        if trials_16.thisN == 0:
            displayed_movie_r4.play()
            displayed_movie_r4.draw()    
        image_17.setPos([posx, posy])
        image_17.setImage('imgs/iceberg.png')
        Key_resp_3.keys = []
        Key_resp_3.rt = []
        _Key_resp_3_allKeys = []
        # keep track of which components have finished
        music_video4Components = [image_17, Key_resp_3]
        for thisComponent in music_video4Components:
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
        
        # --- Run Routine "music_video4" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_2_5
            backgroung_movie2_r4.draw()
            # Run 'Each Frame' code from mar4_4
            mar_movie.draw()
            
            # Run 'Each Frame' code from code_14
            displayed_movie_r4.draw()
            
            
            # *image_17* updates
            
            # if image_17 is starting this frame...
            if image_17.status == NOT_STARTED and tThisFlip >= timepresentation-frameTolerance:
                # keep track of start time/frame for later
                image_17.frameNStart = frameN  # exact frame index
                image_17.tStart = t  # local t and not account for scr refresh
                image_17.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_17, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_17.started')
                # update status
                image_17.status = STARTED
                image_17.setAutoDraw(True)
            
            # if image_17 is active this frame...
            if image_17.status == STARTED:
                # update params
                pass
            
            # if image_17 is stopping this frame...
            if image_17.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_17.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    image_17.tStop = t  # not accounting for scr refresh
                    image_17.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_17.stopped')
                    # update status
                    image_17.status = FINISHED
                    image_17.setAutoDraw(False)
            
            # *Key_resp_3* updates
            waitOnFlip = False
            
            # if Key_resp_3 is starting this frame...
            if Key_resp_3.status == NOT_STARTED and tThisFlip >= timepresentation-frameTolerance:
                # keep track of start time/frame for later
                Key_resp_3.frameNStart = frameN  # exact frame index
                Key_resp_3.tStart = t  # local t and not account for scr refresh
                Key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Key_resp_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Key_resp_3.started')
                # update status
                Key_resp_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(Key_resp_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(Key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if Key_resp_3 is stopping this frame...
            if Key_resp_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Key_resp_3.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    Key_resp_3.tStop = t  # not accounting for scr refresh
                    Key_resp_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Key_resp_3.stopped')
                    # update status
                    Key_resp_3.status = FINISHED
                    Key_resp_3.status = FINISHED
            if Key_resp_3.status == STARTED and not waitOnFlip:
                theseKeys = Key_resp_3.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _Key_resp_3_allKeys.extend(theseKeys)
                if len(_Key_resp_3_allKeys):
                    Key_resp_3.keys = _Key_resp_3_allKeys[-1].name  # just the last key pressed
                    Key_resp_3.rt = _Key_resp_3_allKeys[-1].rt
                    Key_resp_3.duration = _Key_resp_3_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
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
            for thisComponent in music_video4Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "music_video4" ---
        for thisComponent in music_video4Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('music_video4.stopped', globalClock.getTime())
        # Run 'End Routine' code from code_2_5
        if trials_16.thisN == nRows-1:
            backgroung_movie2_r4.stop()
        # Run 'End Routine' code from code_14
        if trials_16.thisN == nRows-1:
            displayed_movie_r4.stop()
        # check responses
        if Key_resp_3.keys in ['', [], None]:  # No response was made
            Key_resp_3.keys = None
        trials_16.addData('Key_resp_3.keys',Key_resp_3.keys)
        if Key_resp_3.keys != None:  # we had a response
            trials_16.addData('Key_resp_3.rt', Key_resp_3.rt)
            trials_16.addData('Key_resp_3.duration', Key_resp_3.duration)
        # the Routine "music_video4" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials_16'
    
    
    # --- Prepare to start Routine "final" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('final.started', globalClock.getTime())
    # keep track of which components have finished
    finalComponents = [text_4]
    for thisComponent in finalComponents:
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
    
    # --- Run Routine "final" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        
        # if text_4 is starting this frame...
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_4.started')
            # update status
            text_4.status = STARTED
            text_4.setAutoDraw(True)
        
        # if text_4 is active this frame...
        if text_4.status == STARTED:
            # update params
            pass
        
        # if text_4 is stopping this frame...
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_4.stopped')
                # update status
                text_4.status = FINISHED
                text_4.setAutoDraw(False)
        
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
        for thisComponent in finalComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "final" ---
    for thisComponent in finalComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('final.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    
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

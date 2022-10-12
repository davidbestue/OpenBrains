/********************* 
 * Bananamonkey Test *
 *********************/

import { PsychoJS } from 'https://pavlovia.org/lib/core.js';
import * as core from 'https://pavlovia.org/lib/core.js';
import { TrialHandler } from 'https://pavlovia.org/lib/data.js';
import { Scheduler } from 'https://pavlovia.org/lib/util.js';
import * as util from 'https://pavlovia.org/lib/util.js';
import * as visual from 'https://pavlovia.org/lib/visual.js';
import { Sound } from 'https://pavlovia.org/lib/sound.js';

// init psychoJS:
var psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
  units: 'norm',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'BananaMonkey';  // from the Builder filename that created this script
let expInfo = {'Participant': ''};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(TranslationsRoutineBegin);
flowScheduler.add(TranslationsRoutineEachFrame);
flowScheduler.add(TranslationsRoutineEnd);
flowScheduler.add(InstructionsRoutineBegin);
flowScheduler.add(InstructionsRoutineEachFrame);
flowScheduler.add(InstructionsRoutineEnd);
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin, trialsLoopScheduler);
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(EndRoutineBegin);
flowScheduler.add(EndRoutineEachFrame);
flowScheduler.add(EndRoutineEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({expName, expInfo});

var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '3.2.3';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0/Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0/60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}

var TranslationsClock;
var randint;
var InstructionsClock;
var GameClock;
var spin;
var TitleW;
var TitleH;
var xpos;
var ypos;
var Bhoz;
var Bver;
var splatpos;
var SadFace;
var HappyFace;
var munch;
var splat;
var count;
var MonkeyMouse;
var Banana;
var SplatBanana;
var Munch;
var Splat;
var MonkeyMouth;
var MonkeyHappy;
var MonkeySad;
var EndClock;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "Translations"
  TranslationsClock = new util.Clock();
  randint = function(min, maxplusone) {
    return Math.floor(Math.random() * (maxplusone - min) ) + min;
  }
  
  
  // Initialize components for Routine "Instructions"
  InstructionsClock = new util.Clock();
  // Initialize components for Routine "Game"
  GameClock = new util.Clock();
  spin = 0;
  TitleW = 0;
  TitleH = 0;
  xpos = 0;
  ypos = (- 0.5);
  Bhoz = 0;
  Bver = 1.5;
  splatpos = 2;
  SadFace = 0;
  HappyFace = 0;
  munch = 0;
  splat = 0;
  count = 0;
  
  MonkeyMouse = new core.Mouse({
    win: psychoJS.window,
  });
  MonkeyMouse.mouseClock = new util.Clock();
  Banana = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Banana', units : 'norm', 
    image : 'imgenes/banana.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.15, 0.4],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  SplatBanana = new visual.ImageStim({
    win : psychoJS.window,
    name : 'SplatBanana', units : 'norm', 
    image : 'imgenes/bansplat.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.4],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  Munch = new Sound({
    win: psychoJS.window,
    value: 'sonidos/munch.wav',
    secs: (- 1),
    });
  Munch.setVolume(1);
  Splat = new Sound({
    win: psychoJS.window,
    value: 'sonidos/splat.wav',
    secs: (- 1),
    });
  Splat.setVolume(1);
  MonkeyMouth = new visual.ImageStim({
    win : psychoJS.window,
    name : 'MonkeyMouth', units : 'norm', 
    image : 'imgenes/monkey.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -6.0 
  });
  MonkeyHappy = new visual.ImageStim({
    win : psychoJS.window,
    name : 'MonkeyHappy', units : 'norm', 
    image : 'imgenes/monkeymunch.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -7.0 
  });
  MonkeySad = new visual.ImageStim({
    win : psychoJS.window,
    name : 'MonkeySad', units : 'norm', 
    image : 'imgenes/monkeyno.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -8.0 
  });
  // Initialize components for Routine "End"
  EndClock = new util.Clock();
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

var t;
var frameN;
var TranslationsComponents;
function TranslationsRoutineBegin() {
  //------Prepare to start Routine 'Translations'-------
  t = 0;
  TranslationsClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // keep track of which components have finished
  TranslationsComponents = [];
  
  for (const thisComponent of TranslationsComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var continueRoutine;
function TranslationsRoutineEachFrame() {
  //------Loop for each frame of Routine 'Translations'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = TranslationsClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of TranslationsComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function TranslationsRoutineEnd() {
  //------Ending Routine 'Translations'-------
  for (const thisComponent of TranslationsComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "Translations" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var InstructionsComponents;
function InstructionsRoutineBegin() {
  //------Prepare to start Routine 'Instructions'-------
  t = 0;
  InstructionsClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // keep track of which components have finished
  InstructionsComponents = [];
  
  for (const thisComponent of InstructionsComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function InstructionsRoutineEachFrame() {
  //------Loop for each frame of Routine 'Instructions'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = InstructionsClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of InstructionsComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function InstructionsRoutineEnd() {
  //------Ending Routine 'Instructions'-------
  for (const thisComponent of InstructionsComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var trials;
var currentLoop;
function trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 10, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials'});
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrial of trials) {
    thisScheduler.add(importConditions(trials));
    thisScheduler.add(GameRoutineBegin);
    thisScheduler.add(GameRoutineEachFrame);
    thisScheduler.add(GameRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}

var timer;
var gotValidClick;
var GameComponents;
function GameRoutineBegin() {
  //------Prepare to start Routine 'Game'-------
  t = 0;
  GameClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  timer = new util.Clock();
  
  // setup some python lists for storing info about the MonkeyMouse
  gotValidClick = false; // until a click is received
  Munch.setVolume(1);
  Splat.setVolume(1);
  // keep track of which components have finished
  GameComponents = [];
  GameComponents.push(MonkeyMouse);
  GameComponents.push(Banana);
  GameComponents.push(SplatBanana);
  GameComponents.push(Munch);
  GameComponents.push(Splat);
  GameComponents.push(MonkeyMouth);
  GameComponents.push(MonkeyHappy);
  GameComponents.push(MonkeySad);
  
  for (const thisComponent of GameComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var FinalChat;
var prevButtonState;
var frameRemains;
function GameRoutineEachFrame() {
  //------Loop for each frame of Routine 'Game'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = GameClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  if ((spin < 360)) {
      spin = (spin + 4);
  } else {
      spin = 360;
  }
  if ((TitleW < 1.5)) {
      TitleW = (TitleW + 0.05);
  } else {
      TitleW = 1.5;
  }
  if ((TitleH < 0.6)) {
      TitleH = (TitleH + 0.02);
  } else {
      TitleH = 0.6;
  }
  xpos = MonkeyMouse.getPos()[0];
  if (((7 < timer.getTime()) && (timer.getTime() < 25))) {
      Bver = (Bver - 0.02);
  } else {
      Bver = 1.5;
  }
  if (((Bver < (- 0.5)) && (((xpos - 0.2) <= Bhoz) && (Bhoz <= (xpos + 0.2))))) {
      HappyFace = 1;
      munch = (munch + 1);
      Bver = 1.4;
      Bhoz = (0.1 * randint((- 8), 9));
  }
  if ((Bver < (- 0.5))) {
      splatpos = Bhoz;
      splat = (splat + 1);
      SadFace = 1;
      Bver = 1.4;
      Bhoz = (0.1 * randint((- 8), 9));
  }
  if ((Bver < 0.4)) {
      splatpos = 2;
  }
  if ((Bver < 1)) {
      HappyFace = 0;
      SadFace = 0;
  }
  FinalChat = `Well done!
  You helped the monkey eat
  ${munch} bananas!`
  ;
  if ((timer.getTime() >= 30)) {
      continueRoutine = false;
  }
  
  // *MonkeyMouse* updates
  if (t >= 0 && MonkeyMouse.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    MonkeyMouse.tStart = t;  // (not accounting for frame time here)
    MonkeyMouse.frameNStart = frameN;  // exact frame index
    MonkeyMouse.status = PsychoJS.Status.STARTED;
    MonkeyMouse.mouseClock.reset();
    prevButtonState = MonkeyMouse.getPressed();  // if button is down already this ISN'T a new click
    }
  frameRemains = 0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (MonkeyMouse.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    MonkeyMouse.status = PsychoJS.Status.FINISHED;
  }
  if (MonkeyMouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
    let buttons = MonkeyMouse.getPressed();
    if (!buttons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
      prevButtonState = buttons;
      if (buttons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
        if (gotValidClick === true) { // abort routine on response
          continueRoutine = false;
        }
      }
    }
  }
  
  // *Banana* updates
  if (t >= 0 && Banana.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Banana.tStart = t;  // (not accounting for frame time here)
    Banana.frameNStart = frameN;  // exact frame index
    Banana.setAutoDraw(true);
  }

  frameRemains = 0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (Banana.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    Banana.setAutoDraw(false);
  }
  
  if (Banana.status === PsychoJS.Status.STARTED){ // only update if being drawn
    Banana.setPos([Bhoz, Bver]);
  }
  
  // *SplatBanana* updates
  if (t >= 0 && SplatBanana.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    SplatBanana.tStart = t;  // (not accounting for frame time here)
    SplatBanana.frameNStart = frameN;  // exact frame index
    SplatBanana.setAutoDraw(true);
  }

  frameRemains = 0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (SplatBanana.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    SplatBanana.setAutoDraw(false);
  }
  
  if (SplatBanana.status === PsychoJS.Status.STARTED){ // only update if being drawn
    SplatBanana.setPos([splatpos, (- 0.5)]);
  }
  // start/stop Munch
  if (((munch == 1)) && Munch.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Munch.tStart = t;  // (not accounting for frame time here)
    Munch.frameNStart = frameN;  // exact frame index
    psychoJS.window.callOnFlip(function(){ Munch.play(); });  // screen flip
    Munch.status = PsychoJS.Status.STARTED;
  }
  if (t >= (Munch.getDuration() + Munch.tStart)     && Munch.status === PsychoJS.Status.STARTED) {
    Munch.stop();  // stop the sound (if longer than duration)
    Munch.status = PsychoJS.Status.FINISHED;
  }
  // start/stop Splat
  if (((splat == 1)) && Splat.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Splat.tStart = t;  // (not accounting for frame time here)
    Splat.frameNStart = frameN;  // exact frame index
    psychoJS.window.callOnFlip(function(){ Splat.play(); });  // screen flip
    Splat.status = PsychoJS.Status.STARTED;
  }
  if (t >= (Splat.getDuration() + Splat.tStart)     && Splat.status === PsychoJS.Status.STARTED) {
    Splat.stop();  // stop the sound (if longer than duration)
    Splat.status = PsychoJS.Status.FINISHED;
  }
  
  // *MonkeyMouth* updates
  if (t >= 0 && MonkeyMouth.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    MonkeyMouth.tStart = t;  // (not accounting for frame time here)
    MonkeyMouth.frameNStart = frameN;  // exact frame index
    MonkeyMouth.setAutoDraw(true);
  }

  frameRemains = 0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (MonkeyMouth.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    MonkeyMouth.setAutoDraw(false);
  }
  
  if (MonkeyMouth.status === PsychoJS.Status.STARTED){ // only update if being drawn
    MonkeyMouth.setPos([xpos, ypos]);
  }
  
  // *MonkeyHappy* updates
  if (t >= 0 && MonkeyHappy.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    MonkeyHappy.tStart = t;  // (not accounting for frame time here)
    MonkeyHappy.frameNStart = frameN;  // exact frame index
    MonkeyHappy.setAutoDraw(true);
  }

  frameRemains = 0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (MonkeyHappy.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    MonkeyHappy.setAutoDraw(false);
  }
  
  if (MonkeyHappy.status === PsychoJS.Status.STARTED){ // only update if being drawn
    MonkeyHappy.setOpacity(HappyFace);
    MonkeyHappy.setPos([xpos, ypos]);
  }
  
  // *MonkeySad* updates
  if (t >= 0 && MonkeySad.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    MonkeySad.tStart = t;  // (not accounting for frame time here)
    MonkeySad.frameNStart = frameN;  // exact frame index
    MonkeySad.setAutoDraw(true);
  }

  frameRemains = 0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (MonkeySad.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    MonkeySad.setAutoDraw(false);
  }
  
  if (MonkeySad.status === PsychoJS.Status.STARTED){ // only update if being drawn
    MonkeySad.setOpacity(SadFace);
    MonkeySad.setPos([xpos, ypos]);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of GameComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function GameRoutineEnd() {
  //------Ending Routine 'Game'-------
  for (const thisComponent of GameComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // store data for thisExp (ExperimentHandler)
  Munch.stop();  // ensure sound has stopped at end of routine
  Splat.stop();  // ensure sound has stopped at end of routine
  // the Routine "Game" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var EndComponents;
function EndRoutineBegin() {
  //------Prepare to start Routine 'End'-------
  t = 0;
  EndClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // keep track of which components have finished
  EndComponents = [];
  
  for (const thisComponent of EndComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function EndRoutineEachFrame() {
  //------Loop for each frame of Routine 'End'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = EndClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of EndComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function EndRoutineEnd() {
  //------Ending Routine 'End'-------
  for (const thisComponent of EndComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "End" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}


function endLoopIteration({thisScheduler, isTrials=true}) {
  // ------Prepare for next entry------
  return function () {
    // ------Check if user ended loop early------
    if (currentLoop.finished) {
      // Check for and save orphaned data
      if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
        psychoJS.experiment.nextEntry();
      }
      thisScheduler.stop();
    } else if (isTrials) {
      psychoJS.experiment.nextEntry();
    }
  return Scheduler.Event.NEXT;
  };
}


function importConditions(loop) {
  const trialIndex = loop.getTrialIndex();
  return function () {
    loop.setTrialIndex(trialIndex);
    psychoJS.importAttributes(loop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});

  return Scheduler.Event.QUIT;
}

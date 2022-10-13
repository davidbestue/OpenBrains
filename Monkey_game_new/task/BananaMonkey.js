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
flowScheduler.add(titleRoutineBegin);
flowScheduler.add(titleRoutineEachFrame);
flowScheduler.add(titleRoutineEnd);
flowScheduler.add(InstructionsRoutineBegin);
flowScheduler.add(InstructionsRoutineEachFrame);
flowScheduler.add(InstructionsRoutineEnd);
const repeatLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(repeatLoopBegin, repeatLoopScheduler);
flowScheduler.add(repeatLoopScheduler);
flowScheduler.add(repeatLoopEnd);
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

var titleClock;
var image;
var monkey_sound;
var InstructionsClock;
var Bienvenida;
var key_resp;
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
var feedback_2Clock;
var feedback_text;
var level_up_sound;
var velo;
var repeat_Clock;
var text;
var si;
var no;
var EndClock;
var Adios;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "title"
  titleClock = new util.Clock();
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : undefined, 
    image : 'imagenes/Title.png', mask : undefined,
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  monkey_sound = new Sound({
    win: psychoJS.window,
    value: 'monkeys_sound.wav',
    secs: (- 1),
    });
  monkey_sound.setVolume(1);
  // Initialize components for Routine "Instructions"
  InstructionsClock = new util.Clock();
  Bienvenida = new visual.TextStim({
    win: psychoJS.window,
    name: 'Bienvenida',
    text: 'Bienvenido a nuestro juego!\n¡Mueve el mouse para comerte las bananas!\n\n      Pulsa "space" para empezar',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
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
    image : 'banana.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.15, 0.4],
    color : new util.Color([1, 1, 1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  SplatBanana = new visual.ImageStim({
    win : psychoJS.window,
    name : 'SplatBanana', units : 'norm', 
    image : 'bansplat.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.4],
    color : new util.Color([1, 1, 1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  Munch = new Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  Munch.setVolume(1.0);
  Splat = new Sound({
    win: psychoJS.window,
    value: 'splat.wav',
    secs: (- 1),
    });
  Splat.setVolume(1);
  MonkeyMouth = new visual.ImageStim({
    win : psychoJS.window,
    name : 'MonkeyMouth', units : 'norm', 
    image : 'monkey.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -6.0 
  });
  MonkeyHappy = new visual.ImageStim({
    win : psychoJS.window,
    name : 'MonkeyHappy', units : 'norm', 
    image : 'monkeymunch.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -7.0 
  });
  MonkeySad = new visual.ImageStim({
    win : psychoJS.window,
    name : 'MonkeySad', units : 'norm', 
    image : 'monkeyno.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -8.0 
  });
  // Initialize components for Routine "feedback_2"
  feedback_2Clock = new util.Clock();
  feedback_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_text',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  level_up_sound = new Sound({
    win: psychoJS.window,
    value: 'level_up.wav',
    secs: (- 1),
    });
  level_up_sound.setVolume(1);
  velo = new visual.TextStim({
    win: psychoJS.window,
    name: 'velo',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [(- 0.1), (- 0.2)], height: 0.12,  wrapWidth: undefined, ori: 0,
    color: new util.Color('red'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "repeat_"
  repeat_Clock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: '¿quieres continuar?\n\n        sí: pulsa S\n\n        no: pulsa N',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  si = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  no = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "End"
  EndClock = new util.Clock();
  Adios = new visual.TextStim({
    win: psychoJS.window,
    name: 'Adios',
    text: '¡Muchas gracias por participar!',
    font: 'Arial',
    units : undefined, 
    pos: [(- 0.05), 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

var t;
var frameN;
var titleComponents;
function titleRoutineBegin() {
  //------Prepare to start Routine 'title'-------
  t = 0;
  titleClock.reset(); // clock
  frameN = -1;
  routineTimer.add(3.000000);
  // update component parameters for each repeat
  monkey_sound.secs=3;
  monkey_sound.setVolume(1);
  // keep track of which components have finished
  titleComponents = [];
  titleComponents.push(image);
  titleComponents.push(monkey_sound);
  
  for (const thisComponent of titleComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var frameRemains;
var continueRoutine;
function titleRoutineEachFrame() {
  //------Loop for each frame of Routine 'title'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = titleClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *image* updates
  if (t >= 0.0 && image.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image.tStart = t;  // (not accounting for frame time here)
    image.frameNStart = frameN;  // exact frame index
    image.setAutoDraw(true);
  }

  frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    image.setAutoDraw(false);
  }
  
  if (image.status === PsychoJS.Status.STARTED){ // only update if being drawn
    image.setSize([TitleW, TitleH]);
    image.setOri(spin);
  }
  // start/stop monkey_sound
  if (t >= 0.0 && monkey_sound.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    monkey_sound.tStart = t;  // (not accounting for frame time here)
    monkey_sound.frameNStart = frameN;  // exact frame index
    psychoJS.window.callOnFlip(function(){ monkey_sound.play(); });  // screen flip
    monkey_sound.status = PsychoJS.Status.STARTED;
  }
  frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (monkey_sound.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    if (3 > 0.5) {  monkey_sound.stop();  // stop the sound (if longer than duration)
      monkey_sound.status = PsychoJS.Status.FINISHED;
    }
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
  for (const thisComponent of titleComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function titleRoutineEnd() {
  //------Ending Routine 'title'-------
  for (const thisComponent of titleComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  monkey_sound.stop();  // ensure sound has stopped at end of routine
  return Scheduler.Event.NEXT;
}

var InstructionsComponents;
function InstructionsRoutineBegin() {
  //------Prepare to start Routine 'Instructions'-------
  t = 0;
  InstructionsClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  key_resp.keys = undefined;
  key_resp.rt = undefined;
  // keep track of which components have finished
  InstructionsComponents = [];
  InstructionsComponents.push(Bienvenida);
  InstructionsComponents.push(key_resp);
  
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
  
  // *Bienvenida* updates
  if (t >= 0.0 && Bienvenida.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Bienvenida.tStart = t;  // (not accounting for frame time here)
    Bienvenida.frameNStart = frameN;  // exact frame index
    Bienvenida.setAutoDraw(true);
  }

  
  // *key_resp* updates
  if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp.tStart = t;  // (not accounting for frame time here)
    key_resp.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
  }

  if (key_resp.status === PsychoJS.Status.STARTED) {
    let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      key_resp.keys = theseKeys[0].name;  // just the last key pressed
      key_resp.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
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
  psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
  if (typeof key_resp.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
      routineTimer.reset();
      }
  
  key_resp.stop();
  // the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var repeat;
var currentLoop;
function repeatLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  repeat = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 10, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'repeat'});
  psychoJS.experiment.addLoop(repeat); // add the loop to the experiment
  currentLoop = repeat;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisRepeat of repeat) {
    thisScheduler.add(importConditions(repeat));
    const trialsLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(trialsLoopBegin, trialsLoopScheduler);
    thisScheduler.add(trialsLoopScheduler);
    thisScheduler.add(trialsLoopEnd);
    thisScheduler.add(feedback_2RoutineBegin);
    thisScheduler.add(feedback_2RoutineEachFrame);
    thisScheduler.add(feedback_2RoutineEnd);
    thisScheduler.add(repeat_RoutineBegin);
    thisScheduler.add(repeat_RoutineEachFrame);
    thisScheduler.add(repeat_RoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}

var trials;
function trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 20, method: TrialHandler.Method.RANDOM,
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


function repeatLoopEnd() {
  psychoJS.experiment.removeLoop(repeat);

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
  Munch = new Sound({
    win: psychoJS.window,
    value: 'munch.wav',
    secs: -1,
    });
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

  
  if (Banana.status === PsychoJS.Status.STARTED){ // only update if being drawn
    Banana.setOpacity(banana_op);
    Banana.setPos([Bhoz, Bver]);
  }
  
  // *SplatBanana* updates
  if (t >= 0 && SplatBanana.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    SplatBanana.tStart = t;  // (not accounting for frame time here)
    SplatBanana.frameNStart = frameN;  // exact frame index
    SplatBanana.setAutoDraw(true);
  }

  
  if (SplatBanana.status === PsychoJS.Status.STARTED){ // only update if being drawn
    SplatBanana.setOpacity(splat_op);
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

var feedback_2Components;
function feedback_2RoutineBegin() {
  //------Prepare to start Routine 'feedback_2'-------
  t = 0;
  feedback_2Clock.reset(); // clock
  frameN = -1;
  routineTimer.add(3.000000);
  // update component parameters for each repeat
  level_up_sound.secs=3;
  level_up_sound.setVolume(1);
  // keep track of which components have finished
  feedback_2Components = [];
  feedback_2Components.push(feedback_text);
  feedback_2Components.push(level_up_sound);
  feedback_2Components.push(velo);
  
  for (const thisComponent of feedback_2Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function feedback_2RoutineEachFrame() {
  //------Loop for each frame of Routine 'feedback_2'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = feedback_2Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *feedback_text* updates
  if (t >= 0.0 && feedback_text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    feedback_text.tStart = t;  // (not accounting for frame time here)
    feedback_text.frameNStart = frameN;  // exact frame index
    feedback_text.setAutoDraw(true);
  }

  frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (feedback_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    feedback_text.setAutoDraw(false);
  }
  
  if (feedback_text.status === PsychoJS.Status.STARTED){ // only update if being drawn
    feedback_text.setText((('         ¡Sigue así!' + '\n') + '\n'));
  }
  // start/stop level_up_sound
  if (t >= 0 && level_up_sound.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    level_up_sound.tStart = t;  // (not accounting for frame time here)
    level_up_sound.frameNStart = frameN;  // exact frame index
    psychoJS.window.callOnFlip(function(){ level_up_sound.play(); });  // screen flip
    level_up_sound.status = PsychoJS.Status.STARTED;
  }
  frameRemains = 0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (level_up_sound.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    if (3 > 0.5) {  level_up_sound.stop();  // stop the sound (if longer than duration)
      level_up_sound.status = PsychoJS.Status.FINISHED;
    }
  }
  
  // *velo* updates
  if (t >= 0.0 && velo.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    velo.tStart = t;  // (not accounting for frame time here)
    velo.frameNStart = frameN;  // exact frame index
    velo.setAutoDraw(true);
  }

  frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (velo.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    velo.setAutoDraw(false);
  }
  
  if (velo.status === PsychoJS.Status.STARTED){ // only update if being drawn
    velo.setText(((('velocidad = ' + str(SPEED_SHOW)) + 'Km/h') + '\n'));
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
  for (const thisComponent of feedback_2Components)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function feedback_2RoutineEnd() {
  //------Ending Routine 'feedback_2'-------
  for (const thisComponent of feedback_2Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  level_up_sound.stop();  // ensure sound has stopped at end of routine
  return Scheduler.Event.NEXT;
}

var repeat_Components;
function repeat_RoutineBegin() {
  //------Prepare to start Routine 'repeat_'-------
  t = 0;
  repeat_Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  si.keys = undefined;
  si.rt = undefined;
  no.keys = undefined;
  no.rt = undefined;
  // keep track of which components have finished
  repeat_Components = [];
  repeat_Components.push(text);
  repeat_Components.push(si);
  repeat_Components.push(no);
  
  for (const thisComponent of repeat_Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function repeat_RoutineEachFrame() {
  //------Loop for each frame of Routine 'repeat_'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = repeat_Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text* updates
  if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text.tStart = t;  // (not accounting for frame time here)
    text.frameNStart = frameN;  // exact frame index
    text.setAutoDraw(true);
  }

  
  // *si* updates
  if (t >= 0.0 && si.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    si.tStart = t;  // (not accounting for frame time here)
    si.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { si.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { si.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { si.clearEvents(); });
  }

  if (si.status === PsychoJS.Status.STARTED) {
    let theseKeys = si.getKeys({keyList: ['s'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      si.keys = theseKeys[0].name;  // just the last key pressed
      si.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  
  // *no* updates
  if (t >= 0.0 && no.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    no.tStart = t;  // (not accounting for frame time here)
    no.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { no.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { no.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { no.clearEvents(); });
  }

  if (no.status === PsychoJS.Status.STARTED) {
    let theseKeys = no.getKeys({keyList: ['n'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      no.keys = theseKeys[0].name;  // just the last key pressed
      no.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
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
  for (const thisComponent of repeat_Components)
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


function repeat_RoutineEnd() {
  //------Ending Routine 'repeat_'-------
  for (const thisComponent of repeat_Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  psychoJS.experiment.addData('si.keys', si.keys);
  if (typeof si.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('si.rt', si.rt);
      routineTimer.reset();
      }
  
  si.stop();
  psychoJS.experiment.addData('no.keys', no.keys);
  if (typeof no.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('no.rt', no.rt);
      routineTimer.reset();
      }
  
  no.stop();
  // the Routine "repeat_" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var EndComponents;
function EndRoutineBegin() {
  //------Prepare to start Routine 'End'-------
  t = 0;
  EndClock.reset(); // clock
  frameN = -1;
  routineTimer.add(5.000000);
  // update component parameters for each repeat
  // keep track of which components have finished
  EndComponents = [];
  EndComponents.push(Adios);
  
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
  
  // *Adios* updates
  if (t >= 0.0 && Adios.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Adios.tStart = t;  // (not accounting for frame time here)
    Adios.frameNStart = frameN;  // exact frame index
    Adios.setAutoDraw(true);
  }

  frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (Adios.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    Adios.setAutoDraw(false);
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
  for (const thisComponent of EndComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
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

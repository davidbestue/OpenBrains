/******************* 
 * Squaredot2 Test *
 *******************/

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
let expName = 'SquareDot2';  // from the Builder filename that created this script
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
flowScheduler.add(InstructionsRoutineBegin);
flowScheduler.add(InstructionsRoutineEachFrame);
flowScheduler.add(InstructionsRoutineEnd);
const repeatLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(repeatLoopBegin, repeatLoopScheduler);
flowScheduler.add(repeatLoopScheduler);
flowScheduler.add(repeatLoopEnd);
flowScheduler.add(valoracionRoutineBegin);
flowScheduler.add(valoracionRoutineEachFrame);
flowScheduler.add(valoracionRoutineEnd);
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

var InstructionsClock;
var Bienvenida;
var key_resp;
var logo_OB_intro;
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
var banana_op;
var splat_op;
var lim_inf;
var SPEED;
var number_corrects;
var plus;
var penalty;
var speeds;
var trials_done;
var MonkeyMouse;
var rectangle;
var circle_falling;
var repeat_Clock;
var text_repeat;
var si;
var no;
var valoracionClock;
var text_valoracion;
var key_resp_2;
var EndClock;
var Adios;
var logo_ob_fin;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "Instructions"
  InstructionsClock = new util.Clock();
  Bienvenida = new visual.TextStim({
    win: psychoJS.window,
    name: 'Bienvenida',
    text: '        ¡Bienvenido a nuestro juego!\n\nMueve al cuadrado con el "mouse" para coger los triángulos.\n\n      Pulsa "space" para iniciar el juego',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  logo_OB_intro = new visual.ImageStim({
    win : psychoJS.window,
    name : 'logo_OB_intro', units : undefined, 
    image : 'logo_OB.png', mask : undefined,
    ori : 0, pos : [0.6, 0.6], size : [0.2, 0.25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
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
  banana_op = 1;
  splat_op = 0;
  lim_inf = (- 1.6);
  SPEED = 0.015;
  number_corrects = 0;
  plus = 0;
  penalty = 0;
  
  speeds = [];
  trials_done = [];
  MonkeyMouse = new core.Mouse({
    win: psychoJS.window,
  });
  MonkeyMouse.mouseClock = new util.Clock();
  rectangle = new visual.Rect ({
    win: psychoJS.window, name: 'rectangle', 
    width: [0.25, 0.45][0], height: [0.25, 0.45][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([0, 0, 0]),
    fillColor: new util.Color([0, 0, 0]),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  circle_falling = new visual.ShapeStim ({
    win: psychoJS.window, name: 'circle_falling', 
    vertices: [[-[0.15, 0.25][0]/2.0, -[0.15, 0.25][1]/2.0], [+[0.15, 0.25][0]/2.0, -[0.15, 0.25][1]/2.0], [0, [0.15, 0.25][1]/2.0]],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([0, 0, 0]),
    fillColor: new util.Color([0, 0, 0]),
    opacity: 1.0, depth: -3, interpolate: true,
  });
  
  // Initialize components for Routine "repeat_"
  repeat_Clock = new util.Clock();
  text_repeat = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_repeat',
    text: '¿Quieres continuar?\n\n        SÍ: pulsa "S"\n\n        NO: pulsa "N"',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  si = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  no = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "valoracion"
  valoracionClock = new util.Clock();
  text_valoracion = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_valoracion',
    text: '¿Te ha parecido un juego divertido?\n\n        Puntúalo del 0 al 5 \n\n        0: muy aburrido\n        5: muy divertido\n\nPulsa en el teclado ese número para terminar',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.07,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "End"
  EndClock = new util.Clock();
  Adios = new visual.TextStim({
    win: psychoJS.window,
    name: 'Adios',
    text: '¡Muchas gracias por participar!',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  logo_ob_fin = new visual.ImageStim({
    win : psychoJS.window,
    name : 'logo_ob_fin', units : undefined, 
    image : 'logo_OB.png', mask : undefined,
    ori : 0, pos : [0.6, 0.6], size : [0.2, 0.25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

var t;
var frameN;
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
  InstructionsComponents.push(logo_OB_intro);
  
  for (const thisComponent of InstructionsComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var continueRoutine;
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
  
  
  // *logo_OB_intro* updates
  if (t >= 0.0 && logo_OB_intro.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    logo_OB_intro.tStart = t;  // (not accounting for frame time here)
    logo_OB_intro.frameNStart = frameN;  // exact frame index
    logo_OB_intro.setAutoDraw(true);
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
    nReps: 15, method: TrialHandler.Method.RANDOM,
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
var correct_trial;
var gotValidClick;
var GameComponents;
function GameRoutineBegin() {
  //------Prepare to start Routine 'Game'-------
  t = 0;
  GameClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  timer = new util.Clock();
  
  
  function randomIntFromInterval(min, max) { // min and max included 
    return Math.floor(Math.random() * (max - min + 1) + min)
  }
  
  const rndInt = randomIntFromInterval((-8), 9)
  
  
  
  xpos = 0;
  ypos = -0.5;
  Bhoz = (0.1 * rndInt);
  Bver = 1.5;
  splatpos = 2;
  SadFace = 0;
  HappyFace = 0;
  munch = 0;
  splat = 0;
  count = 0;
  banana_op = 1;
  splat_op = 0;
  correct_trial = 0;
  
  
  
  // setup some python lists for storing info about the MonkeyMouse
  gotValidClick = false; // until a click is received
  // keep track of which components have finished
  GameComponents = [];
  GameComponents.push(MonkeyMouse);
  GameComponents.push(rectangle);
  GameComponents.push(circle_falling);
  
  for (const thisComponent of GameComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var prevButtonState;
function GameRoutineEachFrame() {
  //------Loop for each frame of Routine 'Game'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = GameClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  xpos = MonkeyMouse.getPos()[0];
  
  
  
  if (((0.1 < timer.getTime()) && (timer.getTime() < 60))) {
      Bver = (Bver - SPEED);
  } else {
      Bver = 1.5;
  }
  
  
  
  if (((((- 0.6) < Bver) && (Bver < (- 0.5))) && (((xpos - 0.2) <= Bhoz) && (Bhoz <= (xpos + 0.2))))) {
      banana_op = 0;
      correct_trial = 1;
  }
  
  
  if (((((- 0.6) < Bver) && (Bver < (- 0.5))) && (Bhoz > (xpos + 0.2)))) {
      banana_op = 0;
  }
  
  
  
  if (((((- 0.6) < Bver) && (Bver < (- 0.5))) && (Bhoz < (xpos - 0.2)))) {
      banana_op = 0;
  }
  
  
  
  
  if ((Bver < (- 0.6))) {
      splat_op = 0;
      banana_op = 0;
  }
  
  
  
  if ((Bver < lim_inf)) {
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
  
  // *rectangle* updates
  if (t >= 0.0 && rectangle.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    rectangle.tStart = t;  // (not accounting for frame time here)
    rectangle.frameNStart = frameN;  // exact frame index
    rectangle.setAutoDraw(true);
  }

  
  if (rectangle.status === PsychoJS.Status.STARTED){ // only update if being drawn
    rectangle.setPos([xpos, ypos]);
  }
  
  // *circle_falling* updates
  if (t >= 0.0 && circle_falling.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    circle_falling.tStart = t;  // (not accounting for frame time here)
    circle_falling.frameNStart = frameN;  // exact frame index
    circle_falling.setAutoDraw(true);
  }

  
  if (circle_falling.status === PsychoJS.Status.STARTED){ // only update if being drawn
    circle_falling.setOpacity(banana_op);
    circle_falling.setPos([Bhoz, Bver]);
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
  
  speeds.push(SPEED);
  
  trials_done.push(correct_trial);
  
  
  if ((correct_trial === 1)) {
      number_corrects = (number_corrects + 1);
  }
  
  
  if ((trials_done.length > 14)) {
      SPEED = 0.1;
      }
  
  
  
  // store data for thisExp (ExperimentHandler)
  // the Routine "Game" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
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
  repeat_Components.push(text_repeat);
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
  
  // *text_repeat* updates
  if (t >= 0.0 && text_repeat.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_repeat.tStart = t;  // (not accounting for frame time here)
    text_repeat.frameNStart = frameN;  // exact frame index
    text_repeat.setAutoDraw(true);
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
  
  if ((no.keys === 'N')) {
  currentLoop.finished = true;
  }
  
  
  if ((no.keys === 'n')) {
  currentLoop.finished = true;
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

var valoracionComponents;
function valoracionRoutineBegin() {
  //------Prepare to start Routine 'valoracion'-------
  t = 0;
  valoracionClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  key_resp_2.keys = undefined;
  key_resp_2.rt = undefined;
  // keep track of which components have finished
  valoracionComponents = [];
  valoracionComponents.push(text_valoracion);
  valoracionComponents.push(key_resp_2);
  
  for (const thisComponent of valoracionComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function valoracionRoutineEachFrame() {
  //------Loop for each frame of Routine 'valoracion'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = valoracionClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text_valoracion* updates
  if (t >= 0.0 && text_valoracion.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_valoracion.tStart = t;  // (not accounting for frame time here)
    text_valoracion.frameNStart = frameN;  // exact frame index
    text_valoracion.setAutoDraw(true);
  }

  
  // *key_resp_2* updates
  if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_2.tStart = t;  // (not accounting for frame time here)
    key_resp_2.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
  }

  if (key_resp_2.status === PsychoJS.Status.STARTED) {
    let theseKeys = key_resp_2.getKeys({keyList: ['0', '1', '2', '3', '4', '5'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      if (key_resp_2.keys === undefined) {  // then this was the first keypress
        key_resp_2.keys = theseKeys[0].name;  // just the first key pressed
        key_resp_2.rt = theseKeys[0].rt;
        // a response ends the routine
        continueRoutine = false;
      }
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
  for (const thisComponent of valoracionComponents)
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


function valoracionRoutineEnd() {
  //------Ending Routine 'valoracion'-------
  for (const thisComponent of valoracionComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
  if (typeof key_resp_2.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
      routineTimer.reset();
      }
  
  key_resp_2.stop();
  // the Routine "valoracion" was not non-slip safe, so reset the non-slip timer
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
  EndComponents.push(logo_ob_fin);
  
  for (const thisComponent of EndComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var frameRemains;
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
  
  // *logo_ob_fin* updates
  if (t >= 0.0 && logo_ob_fin.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    logo_ob_fin.tStart = t;  // (not accounting for frame time here)
    logo_ob_fin.frameNStart = frameN;  // exact frame index
    logo_ob_fin.setAutoDraw(true);
  }

  frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (logo_ob_fin.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    logo_ob_fin.setAutoDraw(false);
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

var mean_speed;
var max_speed;
var number_trials_done;
var number_trials_correct;
function EndRoutineEnd() {
  //------Ending Routine 'End'-------
  for (const thisComponent of EndComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  const average = list => list.reduce((prev, curr) => prev + curr) / list.length;
  const list = speeds
  mean_speed = average(list) 
  psychoJS.experiment.addData('mean_speed', mean_speed)
  
  
  max_speed = Math.max.apply(Math, speeds)
  psychoJS.experiment.addData('max_speed', max_speed.toString())
  
  
  number_trials_done = trials_done.length
  psychoJS.experiment.addData('number_trials', number_trials_done)
  
  
  const sumas = list2 => list2.reduce((prev, curr) => prev + curr);
  const list2 = trials_done
  number_trials_correct = sumas(list2) 
  psychoJS.experiment.addData('number_trials_correct', number_trials_correct)
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

/******************** 
 * Stroop_Task Test *
 ********************/

// init psychoJS:
var psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'stroop_task';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

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
flowScheduler.add(InstruccionesRoutineBegin);
flowScheduler.add(InstruccionesRoutineEachFrame);
flowScheduler.add(InstruccionesRoutineEnd);
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin, trialsLoopScheduler);
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(instrucciones_2RoutineBegin);
flowScheduler.add(instrucciones_2RoutineEachFrame);
flowScheduler.add(instrucciones_2RoutineEnd);
const trials_2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_2LoopBegin, trials_2LoopScheduler);
flowScheduler.add(trials_2LoopScheduler);
flowScheduler.add(trials_2LoopEnd);
flowScheduler.add(instrucciones_3RoutineBegin);
flowScheduler.add(instrucciones_3RoutineEachFrame);
flowScheduler.add(instrucciones_3RoutineEnd);
const trials_3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_3LoopBegin, trials_3LoopScheduler);
flowScheduler.add(trials_3LoopScheduler);
flowScheduler.add(trials_3LoopEnd);
flowScheduler.add(graciasRoutineBegin);
flowScheduler.add(graciasRoutineEachFrame);
flowScheduler.add(graciasRoutineEnd);
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

var InstruccionesClock;
var Instrucciones_texto;
var key_resp;
var color_negroClock;
var colores1;
var respuesta;
var instrucciones_2Clock;
var text_intructionses2;
var key_resp_2;
var color_rectanguloClock;
var rectangulo;
var respuesta_rect;
var instrucciones_3Clock;
var text;
var key_resp_3;
var color_variadoClock;
var colores2;
var respuesta_mix;
var graciasClock;
var despedida;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "Instrucciones"
  InstruccionesClock = new util.Clock();
  Instrucciones_texto = new visual.TextStim({
    win: psychoJS.window,
    name: 'Instrucciones_texto',
    text: 'En esta tarea, tendrás que responder lo más rápido que puedas.\n\nPresiona "a" si la palabra es "azul"\nPresiona "v" si la palabra es "verde"\nPresiona "n" si la palabra es "naranja"\nPresiona "l" si la palabra es "lila"\n\n\nPara hacerlo la más rápido posible, mantén siempre un dedo encima de cada letra.\n\nCuando quieras, presiona "space"',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "color_negro"
  color_negroClock = new util.Clock();
  colores1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'colores1',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  respuesta = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instrucciones_2"
  instrucciones_2Clock = new util.Clock();
  text_intructionses2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_intructionses2',
    text: 'Ahora tendrás que indicar el color del cuadrado.\n\nPresiona "a" si es de color "azul"\nPresiona "v" si es de color "verde"\nPresiona "n" si es de color "naranja"\nPresiona "l" si es de color "lila"\n\n\nPara hacerlo la más rápido posible, mantén siempre un dedo encima de cada letra.\n\nCuando estés listo, presiona "space"',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "color_rectangulo"
  color_rectanguloClock = new util.Clock();
  rectangulo = new visual.Rect ({
    win: psychoJS.window, name: 'rectangulo', 
    width: [0.5, 0.5][0], height: [0.5, 0.5][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color(1.0),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  respuesta_rect = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instrucciones_3"
  instrucciones_3Clock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Finalmente,\n\ntendrás que indicar de qué color está escrita la palabra.\n\nPresiona "a" si la palabra está escrita en color "azul"\nPresiona "v" si la palabra está escrita en color "verde"\nPresiona "n" si la palabra está escrita en color "naranja"\nPresiona "l" si la palabra está escrita en color "lila"\n\n\nPara hacerlo la más rápido posible, mantén siempre un dedo encima de cada letra.\n\nCuando estés listo, presiona "space"',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "color_variado"
  color_variadoClock = new util.Clock();
  colores2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'colores2',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  respuesta_mix = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "gracias"
  graciasClock = new util.Clock();
  despedida = new visual.TextStim({
    win: psychoJS.window,
    name: 'despedida',
    text: '¡Muchas gracias por participar!',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
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
var InstruccionesComponents;
function InstruccionesRoutineBegin() {
  //------Prepare to start Routine 'Instrucciones'-------
  t = 0;
  InstruccionesClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  key_resp.keys = undefined;
  key_resp.rt = undefined;
  // keep track of which components have finished
  InstruccionesComponents = [];
  InstruccionesComponents.push(Instrucciones_texto);
  InstruccionesComponents.push(key_resp);
  
  InstruccionesComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

var continueRoutine;
function InstruccionesRoutineEachFrame() {
  //------Loop for each frame of Routine 'Instrucciones'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = InstruccionesClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *Instrucciones_texto* updates
  if (t >= 0.0 && Instrucciones_texto.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Instrucciones_texto.tStart = t;  // (not accounting for frame time here)
    Instrucciones_texto.frameNStart = frameN;  // exact frame index
    Instrucciones_texto.setAutoDraw(true);
  }

  
  // *key_resp* updates
  if (t >= 6 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
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
  InstruccionesComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function InstruccionesRoutineEnd() {
  //------Ending Routine 'Instrucciones'-------
  InstruccionesComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
  if (typeof key_resp.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
      routineTimer.reset();
      }
  
  key_resp.stop();
  // the Routine "Instrucciones" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var trials;
var currentLoop;
var trialIterator;
function trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'colores1_negro.xlsx', '1:38'),
    seed: undefined, name: 'trials'});
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = trials[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisTrial = result.value;
    thisScheduler.add(importConditions(trials));
    thisScheduler.add(color_negroRoutineBegin);
    thisScheduler.add(color_negroRoutineEachFrame);
    thisScheduler.add(color_negroRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}

var trials_2;
function trials_2LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_2 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'colores2_rectangulos.xlsx', '1:38'),
    seed: undefined, name: 'trials_2'});
  psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
  currentLoop = trials_2;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = trials_2[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisTrial_2 = result.value;
    thisScheduler.add(importConditions(trials_2));
    thisScheduler.add(color_rectanguloRoutineBegin);
    thisScheduler.add(color_rectanguloRoutineEachFrame);
    thisScheduler.add(color_rectanguloRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}


function trials_2LoopEnd() {
  psychoJS.experiment.removeLoop(trials_2);

  return Scheduler.Event.NEXT;
}

var trials_3;
function trials_3LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_3 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'colores3_mix.xlsx', '1:38'),
    seed: undefined, name: 'trials_3'});
  psychoJS.experiment.addLoop(trials_3); // add the loop to the experiment
  currentLoop = trials_3;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = trials_3[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisTrial_3 = result.value;
    thisScheduler.add(importConditions(trials_3));
    thisScheduler.add(color_variadoRoutineBegin);
    thisScheduler.add(color_variadoRoutineEachFrame);
    thisScheduler.add(color_variadoRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}


function trials_3LoopEnd() {
  psychoJS.experiment.removeLoop(trials_3);

  return Scheduler.Event.NEXT;
}

var color_negroComponents;
function color_negroRoutineBegin() {
  //------Prepare to start Routine 'color_negro'-------
  t = 0;
  color_negroClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  colores1.setText(texto);
  respuesta.keys = undefined;
  respuesta.rt = undefined;
  // keep track of which components have finished
  color_negroComponents = [];
  color_negroComponents.push(colores1);
  color_negroComponents.push(respuesta);
  
  color_negroComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function color_negroRoutineEachFrame() {
  //------Loop for each frame of Routine 'color_negro'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = color_negroClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *colores1* updates
  if (t >= 0.05 && colores1.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    colores1.tStart = t;  // (not accounting for frame time here)
    colores1.frameNStart = frameN;  // exact frame index
    colores1.setAutoDraw(true);
  }

  
  // *respuesta* updates
  if (t >= 0.0 && respuesta.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    respuesta.tStart = t;  // (not accounting for frame time here)
    respuesta.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { respuesta.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { respuesta.start(); }); // start on screen flip
  }

  if (respuesta.status === PsychoJS.Status.STARTED) {
    let theseKeys = respuesta.getKeys({keyList: ['a', 'v', 'n', 'l'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      respuesta.keys = [].concat(respuesta.keys, theseKeys[0].name).filter((i) => i !== undefined);  // storing all keys
      respuesta.rt = [].concat(respuesta.rt, theseKeys[0].rt).filter((i) => i !== undefined);
      // was this 'correct'?
      if (respuesta.keys === answer) {
          respuesta.corr = 1;
      } else {
          respuesta.corr = 0;
      }
    }
  }
  
  if (respuesta_rect.keys) {
    if (respuesta_rect.keys.slice(-1)[0] !== answer) {
      continueRoutine = true;
    } else {
      if (respuesta_rect.keys.slice(-1)[0] === answer) {
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
  color_negroComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function color_negroRoutineEnd() {
  //------Ending Routine 'color_negro'-------
  color_negroComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // was no response the correct answer?!
  if (respuesta.keys === undefined) {
    if (['None','none',undefined].includes(answer)) {
       respuesta.corr = 1  // correct non-response
    } else {
       respuesta.corr = 0  // failed to respond (incorrectly)
    }
  }
  // store data for thisExp (ExperimentHandler)
  psychoJS.experiment.addData('respuesta.keys', respuesta.keys);
  psychoJS.experiment.addData('respuesta.corr', respuesta.corr);
  if (typeof respuesta.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('respuesta.rt', respuesta.rt);
      }
  
  respuesta.stop();
  // the Routine "color_negro" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var instrucciones_2Components;
function instrucciones_2RoutineBegin() {
  //------Prepare to start Routine 'instrucciones_2'-------
  t = 0;
  instrucciones_2Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  key_resp_2.keys = undefined;
  key_resp_2.rt = undefined;
  // keep track of which components have finished
  instrucciones_2Components = [];
  instrucciones_2Components.push(text_intructionses2);
  instrucciones_2Components.push(key_resp_2);
  
  instrucciones_2Components.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function instrucciones_2RoutineEachFrame() {
  //------Loop for each frame of Routine 'instrucciones_2'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = instrucciones_2Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text_intructionses2* updates
  if (t >= 0.0 && text_intructionses2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_intructionses2.tStart = t;  // (not accounting for frame time here)
    text_intructionses2.frameNStart = frameN;  // exact frame index
    text_intructionses2.setAutoDraw(true);
  }

  
  // *key_resp_2* updates
  if (t >= 5 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_2.tStart = t;  // (not accounting for frame time here)
    key_resp_2.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
  }

  if (key_resp_2.status === PsychoJS.Status.STARTED) {
    let theseKeys = key_resp_2.getKeys({keyList: ['space'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      key_resp_2.keys = theseKeys[0].name;  // just the last key pressed
      key_resp_2.rt = theseKeys[0].rt;
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
  instrucciones_2Components.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function instrucciones_2RoutineEnd() {
  //------Ending Routine 'instrucciones_2'-------
  instrucciones_2Components.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
  if (typeof key_resp_2.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
      routineTimer.reset();
      }
  
  key_resp_2.stop();
  // the Routine "instrucciones_2" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var color_rectanguloComponents;
function color_rectanguloRoutineBegin() {
  //------Prepare to start Routine 'color_rectangulo'-------
  t = 0;
  color_rectanguloClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  rectangulo.setFillColor(new util.Color([farber, farbeg, farbeb]));
  rectangulo.setLineColor(new util.Color([farber, farbeg, farbeb]));
  respuesta_rect.keys = undefined;
  respuesta_rect.rt = undefined;
  // keep track of which components have finished
  color_rectanguloComponents = [];
  color_rectanguloComponents.push(rectangulo);
  color_rectanguloComponents.push(respuesta_rect);
  
  color_rectanguloComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function color_rectanguloRoutineEachFrame() {
  //------Loop for each frame of Routine 'color_rectangulo'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = color_rectanguloClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *rectangulo* updates
  if (t >= 0.05 && rectangulo.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    rectangulo.tStart = t;  // (not accounting for frame time here)
    rectangulo.frameNStart = frameN;  // exact frame index
    rectangulo.setAutoDraw(true);
  }

  
  // *respuesta_rect* updates
  if (t >= 0.0 && respuesta_rect.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    respuesta_rect.tStart = t;  // (not accounting for frame time here)
    respuesta_rect.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { respuesta_rect.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { respuesta_rect.start(); }); // start on screen flip
  }

  if (respuesta_rect.status === PsychoJS.Status.STARTED) {
    let theseKeys = respuesta_rect.getKeys({keyList: ['a', 'v', 'n', 'l'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      respuesta_rect.keys = [].concat(respuesta_rect.keys, theseKeys[0].name).filter((i) => i !== undefined);  // storing all keys
      respuesta_rect.rt = [].concat(respuesta_rect.rt, theseKeys[0].rt).filter((i) => i !== undefined);
      // was this 'correct'?
      if (respuesta_rect.keys === answer) {
          respuesta_rect.corr = 1;
      } else {
          respuesta_rect.corr = 0;
      }
    }
  }
  
  if (respuesta_rect.keys) {
    if (respuesta_rect.keys.slice(-1)[0] !== answer) {
      continueRoutine = true;
    } else {
      if (respuesta_rect.keys.slice(-1)[0] === answer) {
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
  color_rectanguloComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function color_rectanguloRoutineEnd() {
  //------Ending Routine 'color_rectangulo'-------
  color_rectanguloComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // was no response the correct answer?!
  if (respuesta_rect.keys === undefined) {
    if (['None','none',undefined].includes(answer)) {
       respuesta_rect.corr = 1  // correct non-response
    } else {
       respuesta_rect.corr = 0  // failed to respond (incorrectly)
    }
  }
  // store data for thisExp (ExperimentHandler)
  psychoJS.experiment.addData('respuesta_rect.keys', respuesta_rect.keys);
  psychoJS.experiment.addData('respuesta_rect.corr', respuesta_rect.corr);
  if (typeof respuesta_rect.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('respuesta_rect.rt', respuesta_rect.rt);
      }
  
  respuesta_rect.stop();
  // the Routine "color_rectangulo" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var instrucciones_3Components;
function instrucciones_3RoutineBegin() {
  //------Prepare to start Routine 'instrucciones_3'-------
  t = 0;
  instrucciones_3Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  key_resp_3.keys = undefined;
  key_resp_3.rt = undefined;
  // keep track of which components have finished
  instrucciones_3Components = [];
  instrucciones_3Components.push(text);
  instrucciones_3Components.push(key_resp_3);
  
  instrucciones_3Components.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function instrucciones_3RoutineEachFrame() {
  //------Loop for each frame of Routine 'instrucciones_3'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = instrucciones_3Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text* updates
  if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text.tStart = t;  // (not accounting for frame time here)
    text.frameNStart = frameN;  // exact frame index
    text.setAutoDraw(true);
  }

  
  // *key_resp_3* updates
  if (t >= 5 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_3.tStart = t;  // (not accounting for frame time here)
    key_resp_3.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
  }

  if (key_resp_3.status === PsychoJS.Status.STARTED) {
    let theseKeys = key_resp_3.getKeys({keyList: ['space'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      key_resp_3.keys = theseKeys[0].name;  // just the last key pressed
      key_resp_3.rt = theseKeys[0].rt;
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
  instrucciones_3Components.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function instrucciones_3RoutineEnd() {
  //------Ending Routine 'instrucciones_3'-------
  instrucciones_3Components.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
  if (typeof key_resp_3.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
      routineTimer.reset();
      }
  
  key_resp_3.stop();
  // the Routine "instrucciones_3" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var color_variadoComponents;
function color_variadoRoutineBegin() {
  //------Prepare to start Routine 'color_variado'-------
  t = 0;
  color_variadoClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  colores2.setColor(new util.Color(color));
  colores2.setText(texto);
  respuesta_mix.keys = undefined;
  respuesta_mix.rt = undefined;
  // keep track of which components have finished
  color_variadoComponents = [];
  color_variadoComponents.push(colores2);
  color_variadoComponents.push(respuesta_mix);
  
  color_variadoComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function color_variadoRoutineEachFrame() {
  //------Loop for each frame of Routine 'color_variado'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = color_variadoClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *colores2* updates
  if (t >= 0.05 && colores2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    colores2.tStart = t;  // (not accounting for frame time here)
    colores2.frameNStart = frameN;  // exact frame index
    colores2.setAutoDraw(true);
  }

  
  // *respuesta_mix* updates
  if (t >= 0.0 && respuesta_mix.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    respuesta_mix.tStart = t;  // (not accounting for frame time here)
    respuesta_mix.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { respuesta_mix.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { respuesta_mix.start(); }); // start on screen flip
  }

  if (respuesta_mix.status === PsychoJS.Status.STARTED) {
    let theseKeys = respuesta_mix.getKeys({keyList: ['a', 'v', 'n', 'l'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      respuesta_mix.keys = [].concat(respuesta_mix.keys, theseKeys[0].name).filter((i) => i !== undefined);  // storing all keys
      respuesta_mix.rt = [].concat(respuesta_mix.rt, theseKeys[0].rt).filter((i) => i !== undefined);
      // was this 'correct'?
      if (respuesta_mix.keys === answer) {
          respuesta_mix.corr = 1;
      } else {
          respuesta_mix.corr = 0;
      }
    }
  }
  
  if (respuesta_rect.keys) {
    if (respuesta_rect.keys.slice(-1)[0] !== answer) {
      continueRoutine = true;
    } else {
      if (respuesta_rect.keys.slice(-1)[0] === answer) {
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
  color_variadoComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function color_variadoRoutineEnd() {
  //------Ending Routine 'color_variado'-------
  color_variadoComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // was no response the correct answer?!
  if (respuesta_mix.keys === undefined) {
    if (['None','none',undefined].includes(answer)) {
       respuesta_mix.corr = 1  // correct non-response
    } else {
       respuesta_mix.corr = 0  // failed to respond (incorrectly)
    }
  }
  // store data for thisExp (ExperimentHandler)
  psychoJS.experiment.addData('respuesta_mix.keys', respuesta_mix.keys);
  psychoJS.experiment.addData('respuesta_mix.corr', respuesta_mix.corr);
  if (typeof respuesta_mix.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('respuesta_mix.rt', respuesta_mix.rt);
      }
  
  respuesta_mix.stop();
  // the Routine "color_variado" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var graciasComponents;
function graciasRoutineBegin() {
  //------Prepare to start Routine 'gracias'-------
  t = 0;
  graciasClock.reset(); // clock
  frameN = -1;
  routineTimer.add(3.000000);
  // update component parameters for each repeat
  // keep track of which components have finished
  graciasComponents = [];
  graciasComponents.push(despedida);
  
  graciasComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

var frameRemains;
function graciasRoutineEachFrame() {
  //------Loop for each frame of Routine 'gracias'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = graciasClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *despedida* updates
  if (t >= 0.0 && despedida.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    despedida.tStart = t;  // (not accounting for frame time here)
    despedida.frameNStart = frameN;  // exact frame index
    despedida.setAutoDraw(true);
  }

  frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (despedida.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    despedida.setAutoDraw(false);
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
  graciasComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function graciasRoutineEnd() {
  //------Ending Routine 'gracias'-------
  graciasComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
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

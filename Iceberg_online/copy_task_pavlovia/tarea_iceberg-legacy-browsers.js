/********************** 
 * Tarea_Iceberg *
 **********************/


// store info about the experiment session:
let expName = 'tarea_iceberg';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'Edad': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'Sexo': ["Hombre", "Mujer", "Otro"],
};

// Start code blocks for 'Before Experiment'
// Run 'Before Experiment' code from codigos_generales
let nRows = 10;
let totalRows = 195;


function sample(array, n) {
    let shuffled = array.slice();
    for (let i = shuffled.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
    }
    return shuffled.slice(0, n);
}

// Crear un array de 0 a totalRows - 1
let allRows = [];
for (let i = 0; i < totalRows; i++) {
    allRows.push(i);
}


// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
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
flowScheduler.add(portadaRoutineBegin());
flowScheduler.add(portadaRoutineEachFrame());
flowScheduler.add(portadaRoutineEnd());
flowScheduler.add(instructionsRoutineBegin());
flowScheduler.add(instructionsRoutineEachFrame());
flowScheduler.add(instructionsRoutineEnd());
flowScheduler.add(Ronda1RoutineBegin());
flowScheduler.add(Ronda1RoutineEachFrame());
flowScheduler.add(Ronda1RoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);


flowScheduler.add(Ronda2RoutineBegin());
flowScheduler.add(Ronda2RoutineEachFrame());
flowScheduler.add(Ronda2RoutineEnd());
const trials_2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_2LoopBegin(trials_2LoopScheduler));
flowScheduler.add(trials_2LoopScheduler);
flowScheduler.add(trials_2LoopEnd);


flowScheduler.add(Ronda3RoutineBegin());
flowScheduler.add(Ronda3RoutineEachFrame());
flowScheduler.add(Ronda3RoutineEnd());
const trials_3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_3LoopBegin(trials_3LoopScheduler));
flowScheduler.add(trials_3LoopScheduler);
flowScheduler.add(trials_3LoopEnd);


flowScheduler.add(Ronda4RoutineBegin());
flowScheduler.add(Ronda4RoutineEachFrame());
flowScheduler.add(Ronda4RoutineEnd());
const trials_4LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_4LoopBegin(trials_4LoopScheduler));
flowScheduler.add(trials_4LoopScheduler);
flowScheduler.add(trials_4LoopEnd);


flowScheduler.add(finalRoutineBegin());
flowScheduler.add(finalRoutineEachFrame());
flowScheduler.add(finalRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'imgs/iceberg_times.xlsx', 'path': 'imgs/iceberg_times.xlsx'},
    {'name': 'imgs/iceberg_times.xlsx', 'path': 'imgs/iceberg_times.xlsx'},
    {'name': 'imgs/iceberg_times.xlsx', 'path': 'imgs/iceberg_times.xlsx'},
    {'name': 'imgs/iceberg_times.xlsx', 'path': 'imgs/iceberg_times.xlsx'},
    {'name': 'imgs/logo_OB.png', 'path': 'imgs/logo_OB.png'},
    {'name': 'imgs/MAR.jpg', 'path': 'imgs/MAR.jpg'},
    {'name': 'imgs/iceberg.png', 'path': 'imgs/iceberg.png'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
    {'name': 'imgs/song_titanic.wav', 'path': 'imgs/song_titanic.wav'},
    {'name': 'imgs/titanic_spanish.wav', 'path': 'imgs/titanic_spanish.wav'},
    {'name': 'imgs/gaviota.png', 'path': 'imgs/gaviota.png'},
    {'name': 'imgs/barco.png', 'path': 'imgs/barco.png'},
    {'name': 'imgs/delfin.png', 'path': 'imgs/delfin.png'},
    {'name': 'imgs/avion.png', 'path': 'imgs/avion.png'},
    {'name': 'imgs/pato.png', 'path': 'imgs/pato.png'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2023.2.3';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var portadaClock;
var image_5;
var text_6;
var instructionsClock;
var text_5;
var key_resp_5;
var Ronda1Clock;
var text_7;
var key_resp;
var controlClock;
var resp_control;
var MAR1;
var image;
var Ronda2Clock;
var text_8;
var musica_instrumental;
var key_resp_2;
var instrumentalClock;
var resp_inst;
var MAR2;
var image_2;
var Ronda3Clock;
var text_9;
var musica_letra;
var key_resp_3;
var lyricsClock;
var resp_lyrics;
var MAR3;
var image_3;
var Ronda4Clock;
var text_11;
var key_resp_6;
var multitaskingClock;
var resp_musicv_r1;
var MAR4;
var image_4;
var texto1;
var gaviota;
var barco;
var delfin;
var avion;
var pato;
var texto2;
var imagenes_mostradas;
var finalClock;
var text_4;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "portada"
  portadaClock = new util.Clock();
  image_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_5', units : undefined, 
    image : 'imgs/logo_OB.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.6, 0.7],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  text_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_6',
    text: '¡Bienvenido a un experimento de Open Brains!',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.35)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "instructions"
  instructionsClock = new util.Clock();
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: 'En este experiemento te verás en el mar...\n\n¡Pero hay icebergs que aparecerán de repente en pantalla!\n\nCuando veas uno, debes pulsar "SPACE" lo más rápido posible.\n\nHay 4 rondas con características distintas.\n\nCuando lo tengas claro, pulsa "SPACE" ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Ronda1"
  Ronda1Clock = new util.Clock();
  text_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_7',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "control"
  controlClock = new util.Clock();
  resp_control = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  MAR1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'MAR1', units : undefined, 
    image : 'imgs/MAR.jpg', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [2, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "Ronda2"
  Ronda2Clock = new util.Clock();
  text_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_8',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  musica_instrumental = new sound.Sound({
      win: psychoJS.window,
      value: 'imgs/song_titanic.wav',
      secs: (- 1),
      });
  musica_instrumental.setVolume(1.0);
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instrumental"
  instrumentalClock = new util.Clock();
  resp_inst = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  MAR2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'MAR2', units : undefined, 
    image : 'imgs/MAR.jpg', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [2, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "Ronda3"
  Ronda3Clock = new util.Clock();
  text_9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_9',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  musica_letra = new sound.Sound({
      win: psychoJS.window,
      value: 'imgs/titanic_spanish.wav',
      secs: (- 1),
      });
  musica_letra.setVolume(1.0);
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "lyrics"
  lyricsClock = new util.Clock();
  resp_lyrics = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  MAR3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'MAR3', units : undefined, 
    image : 'imgs/MAR.jpg', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [2, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  image_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_3', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "Ronda4"
  Ronda4Clock = new util.Clock();
  text_11 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_11',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_6 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "multitasking"
  multitaskingClock = new util.Clock();
  resp_musicv_r1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  MAR4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'MAR4', units : undefined, 
    image : 'imgs/MAR.jpg', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [2, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  image_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_4', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  texto1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'texto1',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.22)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  gaviota = new visual.ImageStim({
    win : psychoJS.window,
    name : 'gaviota', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.4, 0.25], size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  barco = new visual.ImageStim({
    win : psychoJS.window,
    name : 'barco', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.4), 0], size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  delfin = new visual.ImageStim({
    win : psychoJS.window,
    name : 'delfin', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.6, (- 0.25)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -6.0 
  });
  avion = new visual.ImageStim({
    win : psychoJS.window,
    name : 'avion', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.2), 0.3], size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -7.0 
  });
  pato = new visual.ImageStim({
    win : psychoJS.window,
    name : 'pato', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.7), (- 0.25)], size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -8.0 
  });
  texto2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'texto2',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.37)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -9.0 
  });
  
  imagenes_mostradas = {
      "avion": false,
      "gaviota": false,
      "barco": false,
      "pato": false,
      "delfin": false,
      "texto1": false,
      "texto2": false
  };
  // Initialize components for Routine "final"
  finalClock = new util.Clock();
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: '¡Muchas gracias por participar!',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var portadaComponents;
function portadaRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'portada' ---
    t = 0;
    portadaClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('portada.started', globalClock.getTime());
    // keep track of which components have finished
    portadaComponents = [];
    portadaComponents.push(image_5);
    portadaComponents.push(text_6);
    
    portadaComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function portadaRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'portada' ---
    // get current time
    t = portadaClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_5* updates
    if (t >= 0.0 && image_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_5.tStart = t;  // (not accounting for frame time here)
      image_5.frameNStart = frameN;  // exact frame index
      
      image_5.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_5.setAutoDraw(false);
    }
    
    // *text_6* updates
    if (t >= 0.0 && text_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_6.tStart = t;  // (not accounting for frame time here)
      text_6.frameNStart = frameN;  // exact frame index
      
      text_6.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_6.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    portadaComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function portadaRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'portada' ---
    portadaComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('portada.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_5_allKeys;
var instructionsComponents;
function instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instructions' ---
    t = 0;
    instructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('instructions.started', globalClock.getTime());
    key_resp_5.keys = undefined;
    key_resp_5.rt = undefined;
    _key_resp_5_allKeys = [];
    // keep track of which components have finished
    instructionsComponents = [];
    instructionsComponents.push(text_5);
    instructionsComponents.push(key_resp_5);
    
    instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instructions' ---
    // get current time
    t = instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_5* updates
    if (t >= 0.0 && text_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_5.tStart = t;  // (not accounting for frame time here)
      text_5.frameNStart = frameN;  // exact frame index
      
      text_5.setAutoDraw(true);
    }
    
    
    // *key_resp_5* updates
    if (t >= 3 && key_resp_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_5.tStart = t;  // (not accounting for frame time here)
      key_resp_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.clearEvents(); });
    }
    
    if (key_resp_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_5.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_5_allKeys = _key_resp_5_allKeys.concat(theseKeys);
      if (_key_resp_5_allKeys.length > 0) {
        key_resp_5.keys = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].name;  // just the last key pressed
        key_resp_5.rt = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].rt;
        key_resp_5.duration = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instructions' ---
    instructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('instructions.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_5.corr, level);
    }
    psychoJS.experiment.addData('key_resp_5.keys', key_resp_5.keys);
    if (typeof key_resp_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_5.rt', key_resp_5.rt);
        psychoJS.experiment.addData('key_resp_5.duration', key_resp_5.duration);
        routineTimer.reset();
        }
    
    key_resp_5.stop();
    // the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var selectedRowsStr1;
var _key_resp_allKeys;
var Ronda1Components;
function Ronda1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Ronda1' ---
    t = 0;
    Ronda1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('Ronda1.started', globalClock.getTime());
    text_7.setText('Ronda 1/4\n\nPulsa "SPACE" para empezar');
    // Run 'Begin Routine' code from codigos_generales
    let selectedRows = sample(allRows, nRows);
    selectedRowsStr1 = [];  // crea la variable vacía
    selectedRowsStr1 = selectedRows.slice();
    
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    Ronda1Components = [];
    Ronda1Components.push(text_7);
    Ronda1Components.push(key_resp);
    
    Ronda1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Ronda1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Ronda1' ---
    // get current time
    t = Ronda1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_7* updates
    if (t >= 0.0 && text_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_7.tStart = t;  // (not accounting for frame time here)
      text_7.frameNStart = frameN;  // exact frame index
      
      text_7.setAutoDraw(true);
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
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        key_resp.duration = _key_resp_allKeys[_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Ronda1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Ronda1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Ronda1' ---
    Ronda1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Ronda1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        psychoJS.experiment.addData('key_resp.duration', key_resp.duration);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "Ronda1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'imgs/iceberg_times.xlsx', selectedRowsStr1),
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials.forEach(function() {
      snapshot = trials.getSnapshot();
    
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(controlRoutineBegin(snapshot));
      trialsLoopScheduler.add(controlRoutineEachFrame());
      trialsLoopScheduler.add(controlRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_2;
function trials_2LoopBegin(trials_2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'imgs/iceberg_times.xlsx', selectedRowsStr2),
      seed: undefined, name: 'trials_2'
    });
    psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
    currentLoop = trials_2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_2.forEach(function() {
      snapshot = trials_2.getSnapshot();
    
      trials_2LoopScheduler.add(importConditions(snapshot));
      trials_2LoopScheduler.add(instrumentalRoutineBegin(snapshot));
      trials_2LoopScheduler.add(instrumentalRoutineEachFrame());
      trials_2LoopScheduler.add(instrumentalRoutineEnd(snapshot));
      trials_2LoopScheduler.add(trials_2LoopEndIteration(trials_2LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_3;
function trials_3LoopBegin(trials_3LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_3 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'imgs/iceberg_times.xlsx', selectedRowsStr3),
      seed: undefined, name: 'trials_3'
    });
    psychoJS.experiment.addLoop(trials_3); // add the loop to the experiment
    currentLoop = trials_3;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_3.forEach(function() {
      snapshot = trials_3.getSnapshot();
    
      trials_3LoopScheduler.add(importConditions(snapshot));
      trials_3LoopScheduler.add(lyricsRoutineBegin(snapshot));
      trials_3LoopScheduler.add(lyricsRoutineEachFrame());
      trials_3LoopScheduler.add(lyricsRoutineEnd(snapshot));
      trials_3LoopScheduler.add(trials_3LoopEndIteration(trials_3LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_3LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_3);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_3LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_4;
function trials_4LoopBegin(trials_4LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_4 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'imgs/iceberg_times.xlsx', selectedRowsStr4),
      seed: undefined, name: 'trials_4'
    });
    psychoJS.experiment.addLoop(trials_4); // add the loop to the experiment
    currentLoop = trials_4;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_4.forEach(function() {
      snapshot = trials_4.getSnapshot();
    
      trials_4LoopScheduler.add(importConditions(snapshot));
      trials_4LoopScheduler.add(multitaskingRoutineBegin(snapshot));
      trials_4LoopScheduler.add(multitaskingRoutineEachFrame());
      trials_4LoopScheduler.add(multitaskingRoutineEnd(snapshot));
      trials_4LoopScheduler.add(trials_4LoopEndIteration(trials_4LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_4LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_4);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_4LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var _resp_control_allKeys;
var controlComponents;
function controlRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'control' ---
    t = 0;
    controlClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('control.started', globalClock.getTime());
    resp_control.keys = undefined;
    resp_control.rt = undefined;
    _resp_control_allKeys = [];
    image.setPos([posx, posy]);
    image.setImage('imgs/iceberg.png');
    // keep track of which components have finished
    controlComponents = [];
    controlComponents.push(resp_control);
    controlComponents.push(MAR1);
    controlComponents.push(image);
    
    controlComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function controlRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'control' ---
    // get current time
    t = controlClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *resp_control* updates
    if (t >= timepresentation && resp_control.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp_control.tStart = t;  // (not accounting for frame time here)
      resp_control.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp_control.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp_control.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp_control.clearEvents(); });
    }
    
    frameRemains = timepresentation + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (resp_control.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      resp_control.status = PsychoJS.Status.FINISHED;
        }
      
    if (resp_control.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp_control.getKeys({keyList: ['space'], waitRelease: false});
      _resp_control_allKeys = _resp_control_allKeys.concat(theseKeys);
      if (_resp_control_allKeys.length > 0) {
        resp_control.keys = _resp_control_allKeys[_resp_control_allKeys.length - 1].name;  // just the last key pressed
        resp_control.rt = _resp_control_allKeys[_resp_control_allKeys.length - 1].rt;
        resp_control.duration = _resp_control_allKeys[_resp_control_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *MAR1* updates
    if (t >= 0.0 && MAR1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      MAR1.tStart = t;  // (not accounting for frame time here)
      MAR1.frameNStart = frameN;  // exact frame index
      
      MAR1.setAutoDraw(true);
    }
    
    
    // *image* updates
    if (t >= timepresentation && image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image.tStart = t;  // (not accounting for frame time here)
      image.frameNStart = frameN;  // exact frame index
      
      image.setAutoDraw(true);
    }
    
    frameRemains = timepresentation + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    controlComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function controlRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'control' ---
    controlComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('control.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(resp_control.corr, level);
    }
    psychoJS.experiment.addData('resp_control.keys', resp_control.keys);
    if (typeof resp_control.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp_control.rt', resp_control.rt);
        psychoJS.experiment.addData('resp_control.duration', resp_control.duration);
        routineTimer.reset();
        }
    
    resp_control.stop();
    // the Routine "control" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var selectedRowsStr2;
var _key_resp_2_allKeys;
var Ronda2Components;
function Ronda2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Ronda2' ---
    t = 0;
    Ronda2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('Ronda2.started', globalClock.getTime());
    text_8.setText('Ronda 2/4\n\nPulsa "SPACE" para empezar');
    // Run 'Begin Routine' code from code_15
    let selectedRows = sample(allRows, nRows);
    selectedRowsStr2 = [];  // crea la variable vacía
    selectedRowsStr2 = selectedRows.slice();
    musica_instrumental.setVolume(1.0);
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    Ronda2Components = [];
    Ronda2Components.push(text_8);
    Ronda2Components.push(musica_instrumental);
    Ronda2Components.push(key_resp_2);
    
    Ronda2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Ronda2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Ronda2' ---
    // get current time
    t = Ronda2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_8* updates
    if (t >= 0.0 && text_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_8.tStart = t;  // (not accounting for frame time here)
      text_8.frameNStart = frameN;  // exact frame index
      
      text_8.setAutoDraw(true);
    }
    
    // start/stop musica_instrumental
    if (t >= 0.0 && musica_instrumental.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      musica_instrumental.tStart = t;  // (not accounting for frame time here)
      musica_instrumental.frameNStart = frameN;  // exact frame index
      
      musica_instrumental.play();  // start the sound (it finishes automatically)
      musica_instrumental.status = PsychoJS.Status.STARTED;
    }
    if (t >= (musica_instrumental.getDuration() + musica_instrumental.tStart)     && musica_instrumental.status === PsychoJS.Status.STARTED) {
      musica_instrumental.stop();  // stop the sound (if longer than duration)
      musica_instrumental.status = PsychoJS.Status.FINISHED;
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
      let theseKeys = key_resp_2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        key_resp_2.duration = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Ronda2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Ronda2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Ronda2' ---
    Ronda2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Ronda2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_2.corr, level);
    }
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        psychoJS.experiment.addData('key_resp_2.duration', key_resp_2.duration);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "Ronda2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _resp_inst_allKeys;
var instrumentalComponents;
function instrumentalRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instrumental' ---
    t = 0;
    instrumentalClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('instrumental.started', globalClock.getTime());
    resp_inst.keys = undefined;
    resp_inst.rt = undefined;
    _resp_inst_allKeys = [];
    image_2.setPos([posx, posy]);
    image_2.setImage('imgs/iceberg.png');
    // keep track of which components have finished
    instrumentalComponents = [];
    instrumentalComponents.push(resp_inst);
    instrumentalComponents.push(MAR2);
    instrumentalComponents.push(image_2);
    
    instrumentalComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instrumentalRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instrumental' ---
    // get current time
    t = instrumentalClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *resp_inst* updates
    if (t >= timepresentation && resp_inst.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp_inst.tStart = t;  // (not accounting for frame time here)
      resp_inst.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp_inst.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp_inst.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp_inst.clearEvents(); });
    }
    
    frameRemains = timepresentation + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (resp_inst.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      resp_inst.status = PsychoJS.Status.FINISHED;
        }
      
    if (resp_inst.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp_inst.getKeys({keyList: ['space'], waitRelease: false});
      _resp_inst_allKeys = _resp_inst_allKeys.concat(theseKeys);
      if (_resp_inst_allKeys.length > 0) {
        resp_inst.keys = _resp_inst_allKeys[_resp_inst_allKeys.length - 1].name;  // just the last key pressed
        resp_inst.rt = _resp_inst_allKeys[_resp_inst_allKeys.length - 1].rt;
        resp_inst.duration = _resp_inst_allKeys[_resp_inst_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *MAR2* updates
    if (t >= 0.0 && MAR2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      MAR2.tStart = t;  // (not accounting for frame time here)
      MAR2.frameNStart = frameN;  // exact frame index
      
      MAR2.setAutoDraw(true);
    }
    
    
    // *image_2* updates
    if (t >= timepresentation && image_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_2.tStart = t;  // (not accounting for frame time here)
      image_2.frameNStart = frameN;  // exact frame index
      
      image_2.setAutoDraw(true);
    }
    
    frameRemains = timepresentation + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instrumentalComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instrumentalRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instrumental' ---
    instrumentalComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('instrumental.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(resp_inst.corr, level);
    }
    psychoJS.experiment.addData('resp_inst.keys', resp_inst.keys);
    if (typeof resp_inst.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp_inst.rt', resp_inst.rt);
        psychoJS.experiment.addData('resp_inst.duration', resp_inst.duration);
        routineTimer.reset();
        }
    
    resp_inst.stop();
    // the Routine "instrumental" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var selectedRowsStr3;
var _key_resp_3_allKeys;
var Ronda3Components;
function Ronda3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Ronda3' ---
    t = 0;
    Ronda3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('Ronda3.started', globalClock.getTime());
    text_9.setText('Ronda 3/4\n\nPulsa "SPACE" para empezar');
    // Run 'Begin Routine' code from code_16
    let selectedRows = sample(allRows, nRows);
    selectedRowsStr3 = [];  // crea la variable vacía
    selectedRowsStr3 = selectedRows.slice();
    
    musica_instrumental.stop();
    musica_letra.setVolume(1.0);
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    // keep track of which components have finished
    Ronda3Components = [];
    Ronda3Components.push(text_9);
    Ronda3Components.push(musica_letra);
    Ronda3Components.push(key_resp_3);
    
    Ronda3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Ronda3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Ronda3' ---
    // get current time
    t = Ronda3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_9* updates
    if (t >= 0.0 && text_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_9.tStart = t;  // (not accounting for frame time here)
      text_9.frameNStart = frameN;  // exact frame index
      
      text_9.setAutoDraw(true);
    }
    
    // start/stop musica_letra
    if (t >= 0.0 && musica_letra.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      musica_letra.tStart = t;  // (not accounting for frame time here)
      musica_letra.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ musica_letra.play(); });  // screen flip
      musica_letra.status = PsychoJS.Status.STARTED;
    }
    if (t >= (musica_letra.getDuration() + musica_letra.tStart)     && musica_letra.status === PsychoJS.Status.STARTED) {
      musica_letra.stop();  // stop the sound (if longer than duration)
      musica_letra.status = PsychoJS.Status.FINISHED;
    }
    
    // *key_resp_3* updates
    if (t >= 0.0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
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
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        key_resp_3.duration = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Ronda3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Ronda3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Ronda3' ---
    Ronda3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Ronda3.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_3.corr, level);
    }
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        psychoJS.experiment.addData('key_resp_3.duration', key_resp_3.duration);
        routineTimer.reset();
        }
    
    key_resp_3.stop();
    // the Routine "Ronda3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _resp_lyrics_allKeys;
var lyricsComponents;
function lyricsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'lyrics' ---
    t = 0;
    lyricsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('lyrics.started', globalClock.getTime());
    resp_lyrics.keys = undefined;
    resp_lyrics.rt = undefined;
    _resp_lyrics_allKeys = [];
    image_3.setPos([posx, posy]);
    image_3.setImage('imgs/iceberg.png');
    // keep track of which components have finished
    lyricsComponents = [];
    lyricsComponents.push(resp_lyrics);
    lyricsComponents.push(MAR3);
    lyricsComponents.push(image_3);
    
    lyricsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function lyricsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'lyrics' ---
    // get current time
    t = lyricsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *resp_lyrics* updates
    if (t >= timepresentation && resp_lyrics.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp_lyrics.tStart = t;  // (not accounting for frame time here)
      resp_lyrics.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp_lyrics.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp_lyrics.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp_lyrics.clearEvents(); });
    }
    
    frameRemains = timepresentation + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (resp_lyrics.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      resp_lyrics.status = PsychoJS.Status.FINISHED;
        }
      
    if (resp_lyrics.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp_lyrics.getKeys({keyList: ['space'], waitRelease: false});
      _resp_lyrics_allKeys = _resp_lyrics_allKeys.concat(theseKeys);
      if (_resp_lyrics_allKeys.length > 0) {
        resp_lyrics.keys = _resp_lyrics_allKeys[_resp_lyrics_allKeys.length - 1].name;  // just the last key pressed
        resp_lyrics.rt = _resp_lyrics_allKeys[_resp_lyrics_allKeys.length - 1].rt;
        resp_lyrics.duration = _resp_lyrics_allKeys[_resp_lyrics_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *MAR3* updates
    if (t >= 0.0 && MAR3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      MAR3.tStart = t;  // (not accounting for frame time here)
      MAR3.frameNStart = frameN;  // exact frame index
      
      MAR3.setAutoDraw(true);
    }
    
    
    // *image_3* updates
    if (t >= timepresentation && image_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_3.tStart = t;  // (not accounting for frame time here)
      image_3.frameNStart = frameN;  // exact frame index
      
      image_3.setAutoDraw(true);
    }
    
    frameRemains = timepresentation + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_3.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    lyricsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function lyricsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'lyrics' ---
    lyricsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('lyrics.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(resp_lyrics.corr, level);
    }
    psychoJS.experiment.addData('resp_lyrics.keys', resp_lyrics.keys);
    if (typeof resp_lyrics.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp_lyrics.rt', resp_lyrics.rt);
        psychoJS.experiment.addData('resp_lyrics.duration', resp_lyrics.duration);
        routineTimer.reset();
        }
    
    resp_lyrics.stop();
    // the Routine "lyrics" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var selectedRowsStr4;
var _key_resp_6_allKeys;
var Ronda4Components;
function Ronda4RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Ronda4' ---
    t = 0;
    Ronda4Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('Ronda4.started', globalClock.getTime());
    // Run 'Begin Routine' code from code
    let selectedRows = sample(allRows, nRows);
    selectedRowsStr4 = [];  // crea la variable vacía
    selectedRowsStr4 = selectedRows.slice();
    text_11.setText('Ronda 4/4\n\nPulsa "SPACE" para empezar');
    key_resp_6.keys = undefined;
    key_resp_6.rt = undefined;
    _key_resp_6_allKeys = [];
    // keep track of which components have finished
    Ronda4Components = [];
    Ronda4Components.push(text_11);
    Ronda4Components.push(key_resp_6);
    
    Ronda4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Ronda4RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Ronda4' ---
    // get current time
    t = Ronda4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_11* updates
    if (t >= 0.0 && text_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_11.tStart = t;  // (not accounting for frame time here)
      text_11.frameNStart = frameN;  // exact frame index
      
      text_11.setAutoDraw(true);
    }
    
    
    // *key_resp_6* updates
    if (t >= 0.0 && key_resp_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_6.tStart = t;  // (not accounting for frame time here)
      key_resp_6.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_6.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.clearEvents(); });
    }
    
    if (key_resp_6.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_6.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_6_allKeys = _key_resp_6_allKeys.concat(theseKeys);
      if (_key_resp_6_allKeys.length > 0) {
        key_resp_6.keys = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].name;  // just the last key pressed
        key_resp_6.rt = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].rt;
        key_resp_6.duration = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Ronda4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var tiempos_aparicion;
function Ronda4RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Ronda4' ---
    Ronda4Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Ronda4.stopped', globalClock.getTime());
    globalClock = new util.Clock();  // Inicia el reloj global
    
    tiempos_aparicion = {
        "avion": globalClock.getTime() + 11,
        "gaviota": globalClock.getTime() + 34,
        "barco": globalClock.getTime() + 16,
        "pato": globalClock.getTime() + 29,
        "delfin": globalClock.getTime() + 40,
        "texto1": globalClock.getTime() + 3,
        "texto2": globalClock.getTime() + 20
    };
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_6.corr, level);
    }
    psychoJS.experiment.addData('key_resp_6.keys', key_resp_6.keys);
    if (typeof key_resp_6.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_6.rt', key_resp_6.rt);
        psychoJS.experiment.addData('key_resp_6.duration', key_resp_6.duration);
        routineTimer.reset();
        }
    
    key_resp_6.stop();
    // the Routine "Ronda4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _resp_musicv_r1_allKeys;
var inicio_avion;
var inicio_gaviota;
var inicio_barco;
var inicio_pato;
var inicio_delfin;
var inicio_texto1;
var inicio_texto2;
var multitaskingComponents;
function multitaskingRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'multitasking' ---
    t = 0;
    multitaskingClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('multitasking.started', globalClock.getTime());
    resp_musicv_r1.keys = undefined;
    resp_musicv_r1.rt = undefined;
    _resp_musicv_r1_allKeys = [];
    image_4.setPos([posx, posy]);
    image_4.setImage('imgs/iceberg.png');
    texto1.setText('El Titanic fue un transatlántico británico que se hundió en el Atlántico Norte el 15 de abril de 1912 tras chocar contra un iceberg en su viaje inaugural. Se convirtió en uno de los desastres marítimos más famosos de la historia, con más de 1.500 víctimas.');
    gaviota.setImage('imgs/gaviota.png');
    barco.setImage('imgs/barco.png');
    delfin.setImage('imgs/delfin.png');
    avion.setImage('imgs/avion.png');
    pato.setImage('imgs/pato.png');
    texto2.setText('El Titanic fue el barco más grande y lujoso de su época, construido por la compañía White Star Line. Por desgracia, solo contaba con botes salvavidas para la mitad de los pasajeros, ya que se priorizó la estética sobre la seguridad.');
    let t_actual = globalClock.getTime();
    
    inicio_avion = imagenes_mostradas["avion"] ? 0 : Math.max(0, tiempos_aparicion["avion"] - t_actual);
    inicio_gaviota = imagenes_mostradas["gaviota"] ? 0 : Math.max(0, tiempos_aparicion["gaviota"] - t_actual);
    inicio_barco = imagenes_mostradas["barco"] ? 0 : Math.max(0, tiempos_aparicion["barco"] - t_actual);
    inicio_pato = imagenes_mostradas["pato"] ? 0 : Math.max(0, tiempos_aparicion["pato"] - t_actual);
    inicio_delfin = imagenes_mostradas["delfin"] ? 0 : Math.max(0, tiempos_aparicion["delfin"] - t_actual);
    inicio_texto1 = imagenes_mostradas["texto1"] ? 0 : Math.max(0, tiempos_aparicion["texto1"] - t_actual);
    inicio_texto2 = imagenes_mostradas["texto2"] ? 0 : Math.max(0, tiempos_aparicion["texto2"] - t_actual);
    // keep track of which components have finished
    multitaskingComponents = [];
    multitaskingComponents.push(resp_musicv_r1);
    multitaskingComponents.push(MAR4);
    multitaskingComponents.push(image_4);
    multitaskingComponents.push(texto1);
    multitaskingComponents.push(gaviota);
    multitaskingComponents.push(barco);
    multitaskingComponents.push(delfin);
    multitaskingComponents.push(avion);
    multitaskingComponents.push(pato);
    multitaskingComponents.push(texto2);
    
    multitaskingComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function multitaskingRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'multitasking' ---
    // get current time
    t = multitaskingClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *resp_musicv_r1* updates
    if (t >= timepresentation && resp_musicv_r1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp_musicv_r1.tStart = t;  // (not accounting for frame time here)
      resp_musicv_r1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp_musicv_r1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp_musicv_r1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp_musicv_r1.clearEvents(); });
    }
    
    frameRemains = timepresentation + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (resp_musicv_r1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      resp_musicv_r1.status = PsychoJS.Status.FINISHED;
        }
      
    if (resp_musicv_r1.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp_musicv_r1.getKeys({keyList: ['space'], waitRelease: false});
      _resp_musicv_r1_allKeys = _resp_musicv_r1_allKeys.concat(theseKeys);
      if (_resp_musicv_r1_allKeys.length > 0) {
        resp_musicv_r1.keys = _resp_musicv_r1_allKeys[_resp_musicv_r1_allKeys.length - 1].name;  // just the last key pressed
        resp_musicv_r1.rt = _resp_musicv_r1_allKeys[_resp_musicv_r1_allKeys.length - 1].rt;
        resp_musicv_r1.duration = _resp_musicv_r1_allKeys[_resp_musicv_r1_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *MAR4* updates
    if (t >= 0.0 && MAR4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      MAR4.tStart = t;  // (not accounting for frame time here)
      MAR4.frameNStart = frameN;  // exact frame index
      
      MAR4.setAutoDraw(true);
    }
    
    
    // *image_4* updates
    if (t >= timepresentation && image_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_4.tStart = t;  // (not accounting for frame time here)
      image_4.frameNStart = frameN;  // exact frame index
      
      image_4.setAutoDraw(true);
    }
    
    frameRemains = timepresentation + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_4.setAutoDraw(false);
    }
    
    // *texto1* updates
    if (t >= inicio_texto1 && texto1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      texto1.tStart = t;  // (not accounting for frame time here)
      texto1.frameNStart = frameN;  // exact frame index
      
      texto1.setAutoDraw(true);
    }
    
    
    // *gaviota* updates
    if (t >= inicio_gaviota && gaviota.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      gaviota.tStart = t;  // (not accounting for frame time here)
      gaviota.frameNStart = frameN;  // exact frame index
      
      gaviota.setAutoDraw(true);
    }
    
    
    // *barco* updates
    if (t >= inicio_barco && barco.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      barco.tStart = t;  // (not accounting for frame time here)
      barco.frameNStart = frameN;  // exact frame index
      
      barco.setAutoDraw(true);
    }
    
    
    // *delfin* updates
    if (t >= inicio_delfin && delfin.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      delfin.tStart = t;  // (not accounting for frame time here)
      delfin.frameNStart = frameN;  // exact frame index
      
      delfin.setAutoDraw(true);
    }
    
    
    // *avion* updates
    if (t >= inicio_avion && avion.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      avion.tStart = t;  // (not accounting for frame time here)
      avion.frameNStart = frameN;  // exact frame index
      
      avion.setAutoDraw(true);
    }
    
    
    // *pato* updates
    if (t >= inicio_pato && pato.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pato.tStart = t;  // (not accounting for frame time here)
      pato.frameNStart = frameN;  // exact frame index
      
      pato.setAutoDraw(true);
    }
    
    
    // *texto2* updates
    if (t >= inicio_texto2 && texto2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      texto2.tStart = t;  // (not accounting for frame time here)
      texto2.frameNStart = frameN;  // exact frame index
      
      texto2.setAutoDraw(true);
    }
    
    let t_actual = globalClock.getTime();
    
    if (t_actual >= tiempos_aparicion["avion"]) {
        imagenes_mostradas["avion"] = true;
    }
    if (t_actual >= tiempos_aparicion["gaviota"]) {
        imagenes_mostradas["gaviota"] = true;
    }
    if (t_actual >= tiempos_aparicion["barco"]) {
        imagenes_mostradas["barco"] = true;
    }
    if (t_actual >= tiempos_aparicion["pato"]) {
        imagenes_mostradas["pato"] = true;
    }
    if (t_actual >= tiempos_aparicion["delfin"]) {
        imagenes_mostradas["delfin"] = true;
    }
    if (t_actual >= tiempos_aparicion["texto1"]) {
        imagenes_mostradas["texto1"] = true;
    }
    if (t_actual >= tiempos_aparicion["texto2"]) {
        imagenes_mostradas["texto2"] = true;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    multitaskingComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function multitaskingRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'multitasking' ---
    multitaskingComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('multitasking.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(resp_musicv_r1.corr, level);
    }
    psychoJS.experiment.addData('resp_musicv_r1.keys', resp_musicv_r1.keys);
    if (typeof resp_musicv_r1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp_musicv_r1.rt', resp_musicv_r1.rt);
        psychoJS.experiment.addData('resp_musicv_r1.duration', resp_musicv_r1.duration);
        routineTimer.reset();
        }
    
    resp_musicv_r1.stop();
    // the Routine "multitasking" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var finalComponents;
function finalRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'final' ---
    t = 0;
    finalClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('final.started', globalClock.getTime());
    // Run 'Begin Routine' code from code_3
    musica_letra.stop();
    
    // keep track of which components have finished
    finalComponents = [];
    finalComponents.push(text_4);
    
    finalComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function finalRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'final' ---
    // get current time
    t = finalClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_4* updates
    if (t >= 0.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_4.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    finalComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function finalRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'final' ---
    finalComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('final.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}

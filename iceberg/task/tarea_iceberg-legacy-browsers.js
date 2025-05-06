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
path_videomar = "imgs/video_mar_luis.mp4";
path_musicafondo = "imgs/song_titanic.mp4";
path_musicaletra = "imgs/titanic_spanish.mp4";
path_pelicula = "imgs/titanic.mp4";
nRows = 10;
totalRows = 195;

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
flowScheduler.add(Ronda_1RoutineBegin());
flowScheduler.add(Ronda_1RoutineEachFrame());
flowScheduler.add(Ronda_1RoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);


const trials_2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_2LoopBegin(trials_2LoopScheduler));
flowScheduler.add(trials_2LoopScheduler);
flowScheduler.add(trials_2LoopEnd);


const trials_3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_3LoopBegin(trials_3LoopScheduler));
flowScheduler.add(trials_3LoopScheduler);
flowScheduler.add(trials_3LoopEnd);


const trials_4LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_4LoopBegin(trials_4LoopScheduler));
flowScheduler.add(trials_4LoopScheduler);
flowScheduler.add(trials_4LoopEnd);


flowScheduler.add(Ronda_2RoutineBegin());
flowScheduler.add(Ronda_2RoutineEachFrame());
flowScheduler.add(Ronda_2RoutineEnd());
const trials_5LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_5LoopBegin(trials_5LoopScheduler));
flowScheduler.add(trials_5LoopScheduler);
flowScheduler.add(trials_5LoopEnd);


const trials_6LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_6LoopBegin(trials_6LoopScheduler));
flowScheduler.add(trials_6LoopScheduler);
flowScheduler.add(trials_6LoopEnd);


const trials_7LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_7LoopBegin(trials_7LoopScheduler));
flowScheduler.add(trials_7LoopScheduler);
flowScheduler.add(trials_7LoopEnd);


const trials_8LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_8LoopBegin(trials_8LoopScheduler));
flowScheduler.add(trials_8LoopScheduler);
flowScheduler.add(trials_8LoopEnd);


flowScheduler.add(Ronda_3RoutineBegin());
flowScheduler.add(Ronda_3RoutineEachFrame());
flowScheduler.add(Ronda_3RoutineEnd());
const trials_9LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_9LoopBegin(trials_9LoopScheduler));
flowScheduler.add(trials_9LoopScheduler);
flowScheduler.add(trials_9LoopEnd);


const trials_10LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_10LoopBegin(trials_10LoopScheduler));
flowScheduler.add(trials_10LoopScheduler);
flowScheduler.add(trials_10LoopEnd);


const trials_11LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_11LoopBegin(trials_11LoopScheduler));
flowScheduler.add(trials_11LoopScheduler);
flowScheduler.add(trials_11LoopEnd);


const trials_12LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_12LoopBegin(trials_12LoopScheduler));
flowScheduler.add(trials_12LoopScheduler);
flowScheduler.add(trials_12LoopEnd);


flowScheduler.add(Ronda_4RoutineBegin());
flowScheduler.add(Ronda_4RoutineEachFrame());
flowScheduler.add(Ronda_4RoutineEnd());
const trials_13LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_13LoopBegin(trials_13LoopScheduler));
flowScheduler.add(trials_13LoopScheduler);
flowScheduler.add(trials_13LoopEnd);


const trials_14LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_14LoopBegin(trials_14LoopScheduler));
flowScheduler.add(trials_14LoopScheduler);
flowScheduler.add(trials_14LoopEnd);


const trials_15LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_15LoopBegin(trials_15LoopScheduler));
flowScheduler.add(trials_15LoopScheduler);
flowScheduler.add(trials_15LoopEnd);


const trials_16LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_16LoopBegin(trials_16LoopScheduler));
flowScheduler.add(trials_16LoopScheduler);
flowScheduler.add(trials_16LoopEnd);


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
    {'name': 'imgs/iceberg_times.xlsx', 'path': 'imgs/iceberg_times.xlsx'},
    {'name': 'imgs/iceberg_times.xlsx', 'path': 'imgs/iceberg_times.xlsx'},
    {'name': 'imgs/iceberg_times.xlsx', 'path': 'imgs/iceberg_times.xlsx'},
    {'name': 'imgs/iceberg_times.xlsx', 'path': 'imgs/iceberg_times.xlsx'},
    {'name': 'imgs/iceberg_times.xlsx', 'path': 'imgs/iceberg_times.xlsx'},
    {'name': 'imgs/iceberg_times.xlsx', 'path': 'imgs/iceberg_times.xlsx'},
    {'name': 'imgs/iceberg_times.xlsx', 'path': 'imgs/iceberg_times.xlsx'},
    {'name': 'imgs/iceberg_times.xlsx', 'path': 'imgs/iceberg_times.xlsx'},
    {'name': 'imgs/iceberg_times.xlsx', 'path': 'imgs/iceberg_times.xlsx'},
    {'name': 'imgs/iceberg_times.xlsx', 'path': 'imgs/iceberg_times.xlsx'},
    {'name': 'imgs/iceberg_times.xlsx', 'path': 'imgs/iceberg_times.xlsx'},
    {'name': 'imgs/iceberg_times.xlsx', 'path': 'imgs/iceberg_times.xlsx'},
    {'name': 'imgs/iceberg.png', 'path': 'imgs/iceberg.png'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);

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

async function experimentInit() {
  // Initialize components for Routine "portada"
  portadaClock = new util.Clock();
  image_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_5', units : undefined, 
    image : 'imgs/logo_OB.jpeg', mask : undefined,
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
    text: 'En este experiemento te verás navegando por el mar...\n\n¡Pero hay icebergs que aparcerán de repente en pantalla!\n\nCuando veas uno, debes pulsar "SPACE" lo más rápido posible.\n\nHay 4 rondas.\n\nCuando estés listo, aprieta "SPACE" para empezar.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Ronda_1"
  Ronda_1Clock = new util.Clock();
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
  
  // Run 'Begin Experiment' code from codigos_generales
  import * as random from 'random';
  rutinas = ["control", "music", "music_words", "music_video"];
  Math.random.shuffle(rutinas);
  console.log(rutinas);
  ronda1 = rutinas[0];
  ronda2 = rutinas[1];
  ronda3 = rutinas[2];
  ronda4 = rutinas[3];
  psychoJS.experiment.addData("ronda1", ronda1);
  psychoJS.experiment.addData("ronda2", ronda2);
  psychoJS.experiment.addData("ronda3", ronda3);
  psychoJS.experiment.addData("ronda4", ronda4);
  
  // Initialize components for Routine "control"
  controlClock = new util.Clock();
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  resp_control_r1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Run 'Begin Experiment' code from mar1
  mar_movie = new visual.MovieStim3({"win": psychoJS.window, "filename": path_videomar, "size": [1900, 1200], "pos": [0, 0], "flipVert": false, "flipHoriz": false, "loop": true});
  
  // Initialize components for Routine "music"
  musicClock = new util.Clock();
  image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  resp_music_r1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Run 'Begin Experiment' code from code
  background_sound = new visual.MovieStim3({"win": psychoJS.window, "filename": path_musicafondo, "size": [20, 20], "pos": [0, 0], "flipVert": false, "flipHoriz": false, "loop": false});
  
  // Initialize components for Routine "music_words"
  music_wordsClock = new util.Clock();
  // Run 'Begin Experiment' code from code_2
  background_movie = new visual.MovieStim3({"win": psychoJS.window, "filename": path_musicaletra, "size": [10, 10], "pos": [0, 0], "flipVert": false, "flipHoriz": false, "loop": false});
  
  image_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_3', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  resp_musicw_r1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "music_video"
  music_videoClock = new util.Clock();
  // Run 'Begin Experiment' code from code_2_2
  background_movie2 = new visual.MovieStim3({"win": psychoJS.window, "filename": path_musicaletra, "size": [10, 10], "pos": [0, 0], "flipVert": false, "flipHoriz": false, "loop": false});
  
  // Run 'Begin Experiment' code from code_3
  displayed_movie = new visual.MovieStim3({"win": psychoJS.window, "filename": path_pelicula, "size": [500, 350], "pos": [0, (- 350)], "flipVert": false, "flipHoriz": false, "loop": false});
  
  image_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_4', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  resp_musicv_r1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Ronda_2"
  Ronda_2Clock = new util.Clock();
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
  
  // Initialize components for Routine "control2"
  control2Clock = new util.Clock();
  image_6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_6', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  resp_control_r2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Run 'Begin Experiment' code from mar_1_2
  mar_movie = new visual.MovieStim3({"win": psychoJS.window, "filename": path_videomar, "size": [1900, 1200], "pos": [0, 0], "flipVert": false, "flipHoriz": false, "loop": true});
  
  // Initialize components for Routine "music2"
  music2Clock = new util.Clock();
  image_7 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_7', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  resp_music_r2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Run 'Begin Experiment' code from code_6
  background_sound_r2 = new visual.MovieStim3({"win": psychoJS.window, "filename": path_musicafondo, "size": [20, 20], "pos": [0, 0], "flipVert": false, "flipHoriz": false, "loop": false});
  
  // Initialize components for Routine "music_words2"
  music_words2Clock = new util.Clock();
  // Run 'Begin Experiment' code from code_7
  background_movie_r2 = new visual.MovieStim3({"win": psychoJS.window, "filename": path_musicaletra, "size": [10, 10], "pos": [0, 0], "flipVert": false, "flipHoriz": false, "loop": false});
  
  image_8 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_8', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  resp_musicw_r2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "music_video2"
  music_video2Clock = new util.Clock();
  // Run 'Begin Experiment' code from code_2_3
  backgroung_movie2_r2 = new visual.MovieStim3({"win": psychoJS.window, "filename": path_musicaletra, "size": [10, 10], "pos": [0, 0], "flipVert": false, "flipHoriz": false, "loop": false});
  
  // Run 'Begin Experiment' code from code_8
  displayed_movie_r2 = new visual.MovieStim3({"win": psychoJS.window, "filename": path_pelicula, "size": [500, 350], "pos": [0, (- 350)], "flipVert": false, "flipHoriz": false, "loop": false});
  
  image_9 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_9', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  resp_musicv_r2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Ronda_3"
  Ronda_3Clock = new util.Clock();
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
  
  // Initialize components for Routine "control3"
  control3Clock = new util.Clock();
  image_10 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_10', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  resp_control_r3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Run 'Begin Experiment' code from mar_1_3
  mar_movie = new visual.MovieStim3({"win": psychoJS.window, "filename": path_videomar, "size": [1900, 1200], "pos": [0, 0], "flipVert": false, "flipHoriz": false, "loop": true});
  
  // Initialize components for Routine "music3"
  music3Clock = new util.Clock();
  image_11 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_11', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  resp_music_r3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Run 'Begin Experiment' code from code_9
  background_sound_r3 = new visual.MovieStim3({"win": psychoJS.window, "filename": path_musicafondo, "size": [20, 20], "pos": [0, 0], "flipVert": false, "flipHoriz": false, "loop": false});
  
  // Initialize components for Routine "music_words3"
  music_words3Clock = new util.Clock();
  // Run 'Begin Experiment' code from code_10
  background_movie_r3 = new visual.MovieStim3({"win": psychoJS.window, "filename": path_musicaletra, "size": [10, 10], "pos": [0, 0], "flipVert": false, "flipHoriz": false, "loop": false});
  
  image_12 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_12', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  resp_musicw_r3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "music_video3"
  music_video3Clock = new util.Clock();
  // Run 'Begin Experiment' code from code_2_4
  backgroung_movie2_r3 = new visual.MovieStim3({"win": psychoJS.window, "filename": path_musicaletra, "size": [10, 10], "pos": [0, 0], "flipVert": false, "flipHoriz": false, "loop": false});
  
  // Run 'Begin Experiment' code from code_11
  displayed_movie_r3 = new visual.MovieStim3({"win": psychoJS.window, "filename": path_pelicula, "size": [500, 350], "pos": [0, (- 350)], "flipVert": false, "flipHoriz": false, "loop": false});
  
  image_13 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_13', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  resp_musicv_r3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Ronda_4"
  Ronda_4Clock = new util.Clock();
  text_10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_10',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "control4"
  control4Clock = new util.Clock();
  image_14 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_14', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  resp_control_r4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Run 'Begin Experiment' code from mar_1_4
  mar_movie = new visual.MovieStim3({"win": psychoJS.window, "filename": path_videomar, "size": [1900, 1200], "pos": [0, 0], "flipVert": false, "flipHoriz": false, "loop": true});
  
  // Initialize components for Routine "music4"
  music4Clock = new util.Clock();
  image_15 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_15', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  resp_music_r4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Run 'Begin Experiment' code from code_12
  background_sound_r4 = new visual.MovieStim3({"win": psychoJS.window, "filename": path_musicafondo, "size": [20, 20], "pos": [0, 0], "flipVert": false, "flipHoriz": false, "loop": false});
  
  // Initialize components for Routine "music_words4"
  music_words4Clock = new util.Clock();
  // Run 'Begin Experiment' code from code_13
  background_movie_r4 = new visual.MovieStim3({"win": psychoJS.window, "filename": path_musicaletra, "size": [10, 10], "pos": [0, 0], "flipVert": false, "flipHoriz": false, "loop": false});
  
  image_16 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_16', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  resp_musicw_r4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "music_video4"
  music_video4Clock = new util.Clock();
  // Run 'Begin Experiment' code from code_2_5
  backgroung_movie2_r4 = new visual.MovieStim3({"win": psychoJS.window, "filename": path_musicaletra, "size": [10, 10], "pos": [0, 0], "flipVert": false, "flipHoriz": false, "loop": false});
  
  // Run 'Begin Experiment' code from code_14
  displayed_movie_r4 = new visual.MovieStim3({"win": psychoJS.window, "filename": path_pelicula, "size": [500, 350], "pos": [0, (- 350)], "flipVert": false, "flipHoriz": false, "loop": false});
  
  image_17 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_17', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  resp_musicv_r4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
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

function Ronda_1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Ronda_1' ---
    t = 0;
    Ronda_1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('Ronda_1.started', globalClock.getTime());
    text_7.setText('Ronda 1/4');
    // Run 'Begin Routine' code from codigos_generales
    selectedRows = Math.random.sample(util.range(totalRows), nRows);
    selectedRowsStr = function () {
        var _pj_a = [], _pj_b = selectedRows;
        for (var _pj_c = 0, _pj_d = _pj_b.length; (_pj_c < _pj_d); _pj_c += 1) {
            var i = _pj_b[_pj_c];
            _pj_a.push(i);
        }
        return _pj_a;
    }
    .call(this);
    
    // keep track of which components have finished
    Ronda_1Components = [];
    Ronda_1Components.push(text_7);
    
    Ronda_1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function Ronda_1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Ronda_1' ---
    // get current time
    t = Ronda_1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_7* updates
    if (t >= 0.0 && text_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_7.tStart = t;  // (not accounting for frame time here)
      text_7.frameNStart = frameN;  // exact frame index
      
      text_7.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_7.setAutoDraw(false);
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
    Ronda_1Components.forEach( function(thisComponent) {
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

function Ronda_1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Ronda_1' ---
    Ronda_1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Ronda_1.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'imgs/iceberg_times.xlsx', selectedRowsStr),
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

function trials_2LoopBegin(trials_2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'imgs/iceberg_times.xlsx', selectedRowsStr),
      seed: undefined, name: 'trials_2'
    });
    psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
    currentLoop = trials_2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_2.forEach(function() {
      snapshot = trials_2.getSnapshot();
    
      trials_2LoopScheduler.add(importConditions(snapshot));
      trials_2LoopScheduler.add(musicRoutineBegin(snapshot));
      trials_2LoopScheduler.add(musicRoutineEachFrame());
      trials_2LoopScheduler.add(musicRoutineEnd(snapshot));
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

function trials_3LoopBegin(trials_3LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_3 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'imgs/iceberg_times.xlsx', selectedRowsStr),
      seed: undefined, name: 'trials_3'
    });
    psychoJS.experiment.addLoop(trials_3); // add the loop to the experiment
    currentLoop = trials_3;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_3.forEach(function() {
      snapshot = trials_3.getSnapshot();
    
      trials_3LoopScheduler.add(importConditions(snapshot));
      trials_3LoopScheduler.add(music_wordsRoutineBegin(snapshot));
      trials_3LoopScheduler.add(music_wordsRoutineEachFrame());
      trials_3LoopScheduler.add(music_wordsRoutineEnd(snapshot));
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

function trials_4LoopBegin(trials_4LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_4 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'imgs/iceberg_times.xlsx', selectedRowsStr),
      seed: undefined, name: 'trials_4'
    });
    psychoJS.experiment.addLoop(trials_4); // add the loop to the experiment
    currentLoop = trials_4;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_4.forEach(function() {
      snapshot = trials_4.getSnapshot();
    
      trials_4LoopScheduler.add(importConditions(snapshot));
      trials_4LoopScheduler.add(music_videoRoutineBegin(snapshot));
      trials_4LoopScheduler.add(music_videoRoutineEachFrame());
      trials_4LoopScheduler.add(music_videoRoutineEnd(snapshot));
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

function trials_5LoopBegin(trials_5LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_5 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'imgs/iceberg_times.xlsx', selectedRowsStr_r2),
      seed: undefined, name: 'trials_5'
    });
    psychoJS.experiment.addLoop(trials_5); // add the loop to the experiment
    currentLoop = trials_5;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_5.forEach(function() {
      snapshot = trials_5.getSnapshot();
    
      trials_5LoopScheduler.add(importConditions(snapshot));
      trials_5LoopScheduler.add(control2RoutineBegin(snapshot));
      trials_5LoopScheduler.add(control2RoutineEachFrame());
      trials_5LoopScheduler.add(control2RoutineEnd(snapshot));
      trials_5LoopScheduler.add(trials_5LoopEndIteration(trials_5LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

async function trials_5LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_5);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function trials_5LoopEndIteration(scheduler, snapshot) {
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

function trials_6LoopBegin(trials_6LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_6 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'imgs/iceberg_times.xlsx', selectedRowsStr_r2),
      seed: undefined, name: 'trials_6'
    });
    psychoJS.experiment.addLoop(trials_6); // add the loop to the experiment
    currentLoop = trials_6;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_6.forEach(function() {
      snapshot = trials_6.getSnapshot();
    
      trials_6LoopScheduler.add(importConditions(snapshot));
      trials_6LoopScheduler.add(music2RoutineBegin(snapshot));
      trials_6LoopScheduler.add(music2RoutineEachFrame());
      trials_6LoopScheduler.add(music2RoutineEnd(snapshot));
      trials_6LoopScheduler.add(trials_6LoopEndIteration(trials_6LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

async function trials_6LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_6);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function trials_6LoopEndIteration(scheduler, snapshot) {
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

function trials_7LoopBegin(trials_7LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_7 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'imgs/iceberg_times.xlsx', selectedRowsStr_r2),
      seed: undefined, name: 'trials_7'
    });
    psychoJS.experiment.addLoop(trials_7); // add the loop to the experiment
    currentLoop = trials_7;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_7.forEach(function() {
      snapshot = trials_7.getSnapshot();
    
      trials_7LoopScheduler.add(importConditions(snapshot));
      trials_7LoopScheduler.add(music_words2RoutineBegin(snapshot));
      trials_7LoopScheduler.add(music_words2RoutineEachFrame());
      trials_7LoopScheduler.add(music_words2RoutineEnd(snapshot));
      trials_7LoopScheduler.add(trials_7LoopEndIteration(trials_7LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

async function trials_7LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_7);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function trials_7LoopEndIteration(scheduler, snapshot) {
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

function trials_8LoopBegin(trials_8LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_8 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'imgs/iceberg_times.xlsx', selectedRowsStr_r2),
      seed: undefined, name: 'trials_8'
    });
    psychoJS.experiment.addLoop(trials_8); // add the loop to the experiment
    currentLoop = trials_8;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_8.forEach(function() {
      snapshot = trials_8.getSnapshot();
    
      trials_8LoopScheduler.add(importConditions(snapshot));
      trials_8LoopScheduler.add(music_video2RoutineBegin(snapshot));
      trials_8LoopScheduler.add(music_video2RoutineEachFrame());
      trials_8LoopScheduler.add(music_video2RoutineEnd(snapshot));
      trials_8LoopScheduler.add(trials_8LoopEndIteration(trials_8LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

async function trials_8LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_8);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function trials_8LoopEndIteration(scheduler, snapshot) {
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

function trials_9LoopBegin(trials_9LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_9 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'imgs/iceberg_times.xlsx', selectedRowsStr_r3),
      seed: undefined, name: 'trials_9'
    });
    psychoJS.experiment.addLoop(trials_9); // add the loop to the experiment
    currentLoop = trials_9;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_9.forEach(function() {
      snapshot = trials_9.getSnapshot();
    
      trials_9LoopScheduler.add(importConditions(snapshot));
      trials_9LoopScheduler.add(control3RoutineBegin(snapshot));
      trials_9LoopScheduler.add(control3RoutineEachFrame());
      trials_9LoopScheduler.add(control3RoutineEnd(snapshot));
      trials_9LoopScheduler.add(trials_9LoopEndIteration(trials_9LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

async function trials_9LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_9);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function trials_9LoopEndIteration(scheduler, snapshot) {
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

function trials_10LoopBegin(trials_10LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_10 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'imgs/iceberg_times.xlsx', selectedRowsStr_r3),
      seed: undefined, name: 'trials_10'
    });
    psychoJS.experiment.addLoop(trials_10); // add the loop to the experiment
    currentLoop = trials_10;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_10.forEach(function() {
      snapshot = trials_10.getSnapshot();
    
      trials_10LoopScheduler.add(importConditions(snapshot));
      trials_10LoopScheduler.add(music3RoutineBegin(snapshot));
      trials_10LoopScheduler.add(music3RoutineEachFrame());
      trials_10LoopScheduler.add(music3RoutineEnd(snapshot));
      trials_10LoopScheduler.add(trials_10LoopEndIteration(trials_10LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

async function trials_10LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_10);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function trials_10LoopEndIteration(scheduler, snapshot) {
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

function trials_11LoopBegin(trials_11LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_11 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'imgs/iceberg_times.xlsx', selectedRowsStr_r3),
      seed: undefined, name: 'trials_11'
    });
    psychoJS.experiment.addLoop(trials_11); // add the loop to the experiment
    currentLoop = trials_11;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_11.forEach(function() {
      snapshot = trials_11.getSnapshot();
    
      trials_11LoopScheduler.add(importConditions(snapshot));
      trials_11LoopScheduler.add(music_words3RoutineBegin(snapshot));
      trials_11LoopScheduler.add(music_words3RoutineEachFrame());
      trials_11LoopScheduler.add(music_words3RoutineEnd(snapshot));
      trials_11LoopScheduler.add(trials_11LoopEndIteration(trials_11LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

async function trials_11LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_11);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function trials_11LoopEndIteration(scheduler, snapshot) {
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

function trials_12LoopBegin(trials_12LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_12 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'imgs/iceberg_times.xlsx', selectedRowsStr_r3),
      seed: undefined, name: 'trials_12'
    });
    psychoJS.experiment.addLoop(trials_12); // add the loop to the experiment
    currentLoop = trials_12;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_12.forEach(function() {
      snapshot = trials_12.getSnapshot();
    
      trials_12LoopScheduler.add(importConditions(snapshot));
      trials_12LoopScheduler.add(music_video3RoutineBegin(snapshot));
      trials_12LoopScheduler.add(music_video3RoutineEachFrame());
      trials_12LoopScheduler.add(music_video3RoutineEnd(snapshot));
      trials_12LoopScheduler.add(trials_12LoopEndIteration(trials_12LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

async function trials_12LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_12);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function trials_12LoopEndIteration(scheduler, snapshot) {
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

function trials_13LoopBegin(trials_13LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_13 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'imgs/iceberg_times.xlsx', selectedRowsStr_r4),
      seed: undefined, name: 'trials_13'
    });
    psychoJS.experiment.addLoop(trials_13); // add the loop to the experiment
    currentLoop = trials_13;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_13.forEach(function() {
      snapshot = trials_13.getSnapshot();
    
      trials_13LoopScheduler.add(importConditions(snapshot));
      trials_13LoopScheduler.add(control4RoutineBegin(snapshot));
      trials_13LoopScheduler.add(control4RoutineEachFrame());
      trials_13LoopScheduler.add(control4RoutineEnd(snapshot));
      trials_13LoopScheduler.add(trials_13LoopEndIteration(trials_13LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

async function trials_13LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_13);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function trials_13LoopEndIteration(scheduler, snapshot) {
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

function trials_14LoopBegin(trials_14LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_14 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'imgs/iceberg_times.xlsx', selectedRowsStr_r4),
      seed: undefined, name: 'trials_14'
    });
    psychoJS.experiment.addLoop(trials_14); // add the loop to the experiment
    currentLoop = trials_14;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_14.forEach(function() {
      snapshot = trials_14.getSnapshot();
    
      trials_14LoopScheduler.add(importConditions(snapshot));
      trials_14LoopScheduler.add(music4RoutineBegin(snapshot));
      trials_14LoopScheduler.add(music4RoutineEachFrame());
      trials_14LoopScheduler.add(music4RoutineEnd(snapshot));
      trials_14LoopScheduler.add(trials_14LoopEndIteration(trials_14LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

async function trials_14LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_14);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function trials_14LoopEndIteration(scheduler, snapshot) {
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

function trials_15LoopBegin(trials_15LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_15 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'imgs/iceberg_times.xlsx', selectedRowsStr_r4),
      seed: undefined, name: 'trials_15'
    });
    psychoJS.experiment.addLoop(trials_15); // add the loop to the experiment
    currentLoop = trials_15;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_15.forEach(function() {
      snapshot = trials_15.getSnapshot();
    
      trials_15LoopScheduler.add(importConditions(snapshot));
      trials_15LoopScheduler.add(music_words4RoutineBegin(snapshot));
      trials_15LoopScheduler.add(music_words4RoutineEachFrame());
      trials_15LoopScheduler.add(music_words4RoutineEnd(snapshot));
      trials_15LoopScheduler.add(trials_15LoopEndIteration(trials_15LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

async function trials_15LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_15);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function trials_15LoopEndIteration(scheduler, snapshot) {
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

function trials_16LoopBegin(trials_16LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_16 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'imgs/iceberg_times.xlsx', selectedRowsStr_r4),
      seed: undefined, name: 'trials_16'
    });
    psychoJS.experiment.addLoop(trials_16); // add the loop to the experiment
    currentLoop = trials_16;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_16.forEach(function() {
      snapshot = trials_16.getSnapshot();
    
      trials_16LoopScheduler.add(importConditions(snapshot));
      trials_16LoopScheduler.add(music_video4RoutineBegin(snapshot));
      trials_16LoopScheduler.add(music_video4RoutineEachFrame());
      trials_16LoopScheduler.add(music_video4RoutineEnd(snapshot));
      trials_16LoopScheduler.add(trials_16LoopEndIteration(trials_16LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

async function trials_16LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_16);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function trials_16LoopEndIteration(scheduler, snapshot) {
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
    // Run 'Begin Routine' code from control_r1
    if ((ronda1 === "control")) {
        continueRoutine = true;
    } else {
        continueRoutine = false;
    }
    
    image.setPos([posx, posy]);
    image.setImage('imgs/iceberg.png');
    resp_control_r1.keys = undefined;
    resp_control_r1.rt = undefined;
    _resp_control_r1_allKeys = [];
    // Run 'Begin Routine' code from mar1
    mar_movie.play();
    
    // keep track of which components have finished
    controlComponents = [];
    controlComponents.push(image);
    controlComponents.push(resp_control_r1);
    
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
    
    // *resp_control_r1* updates
    if (t >= timepresentation && resp_control_r1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp_control_r1.tStart = t;  // (not accounting for frame time here)
      resp_control_r1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp_control_r1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp_control_r1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp_control_r1.clearEvents(); });
    }
    
    frameRemains = timepresentation + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (resp_control_r1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      resp_control_r1.status = PsychoJS.Status.FINISHED;
        }
      
    if (resp_control_r1.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp_control_r1.getKeys({keyList: ['space'], waitRelease: false});
      _resp_control_r1_allKeys = _resp_control_r1_allKeys.concat(theseKeys);
      if (_resp_control_r1_allKeys.length > 0) {
        resp_control_r1.keys = _resp_control_r1_allKeys[_resp_control_r1_allKeys.length - 1].name;  // just the last key pressed
        resp_control_r1.rt = _resp_control_r1_allKeys[_resp_control_r1_allKeys.length - 1].rt;
        resp_control_r1.duration = _resp_control_r1_allKeys[_resp_control_r1_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // Run 'Each Frame' code from mar1
    mar_movie.draw();
    
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
      currentLoop.addResponse(resp_control_r1.corr, level);
    }
    psychoJS.experiment.addData('resp_control_r1.keys', resp_control_r1.keys);
    if (typeof resp_control_r1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp_control_r1.rt', resp_control_r1.rt);
        psychoJS.experiment.addData('resp_control_r1.duration', resp_control_r1.duration);
        routineTimer.reset();
        }
    
    resp_control_r1.stop();
    // the Routine "control" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function musicRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'music' ---
    t = 0;
    musicClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('music.started', globalClock.getTime());
    // Run 'Begin Routine' code from music_r1
    if ((ronda1 === "music")) {
        continueRoutine = true;
    } else {
        continueRoutine = false;
    }
    
    image_2.setPos([posx, posy]);
    image_2.setImage('imgs/iceberg.png');
    resp_music_r1.keys = undefined;
    resp_music_r1.rt = undefined;
    _resp_music_r1_allKeys = [];
    // Run 'Begin Routine' code from code
    if ((trials_2.thisN === 0)) {
        background_sound.play();
    }
    
    // Run 'Begin Routine' code from mar2
    mar_movie.play();
    
    // keep track of which components have finished
    musicComponents = [];
    musicComponents.push(image_2);
    musicComponents.push(resp_music_r1);
    
    musicComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function musicRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'music' ---
    // get current time
    t = musicClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
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
    
    // *resp_music_r1* updates
    if (t >= timepresentation && resp_music_r1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp_music_r1.tStart = t;  // (not accounting for frame time here)
      resp_music_r1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp_music_r1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp_music_r1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp_music_r1.clearEvents(); });
    }
    
    frameRemains = timepresentation + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (resp_music_r1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      resp_music_r1.status = PsychoJS.Status.FINISHED;
        }
      
    if (resp_music_r1.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp_music_r1.getKeys({keyList: ['space'], waitRelease: false});
      _resp_music_r1_allKeys = _resp_music_r1_allKeys.concat(theseKeys);
      if (_resp_music_r1_allKeys.length > 0) {
        resp_music_r1.keys = _resp_music_r1_allKeys[_resp_music_r1_allKeys.length - 1].name;  // just the last key pressed
        resp_music_r1.rt = _resp_music_r1_allKeys[_resp_music_r1_allKeys.length - 1].rt;
        resp_music_r1.duration = _resp_music_r1_allKeys[_resp_music_r1_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // Run 'Each Frame' code from code
    background_sound.draw();
    
    // Run 'Each Frame' code from mar2
    mar_movie.draw();
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    musicComponents.forEach( function(thisComponent) {
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

function musicRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'music' ---
    musicComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('music.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(resp_music_r1.corr, level);
    }
    psychoJS.experiment.addData('resp_music_r1.keys', resp_music_r1.keys);
    if (typeof resp_music_r1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp_music_r1.rt', resp_music_r1.rt);
        psychoJS.experiment.addData('resp_music_r1.duration', resp_music_r1.duration);
        routineTimer.reset();
        }
    
    resp_music_r1.stop();
    // Run 'End Routine' code from code
    if ((trials_2.thisN === (nRows - 1))) {
        background_sound.stop();
    }
    
    // the Routine "music" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function music_wordsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'music_words' ---
    t = 0;
    music_wordsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('music_words.started', globalClock.getTime());
    // Run 'Begin Routine' code from musicw_r1
    if ((ronda1 === "music_words")) {
        continueRoutine = true;
    } else {
        continueRoutine = false;
    }
    
    // Run 'Begin Routine' code from code_2
    if ((trials_3.thisN === 0)) {
        background_movie.play();
        background_movie.draw();
    }
    
    // Run 'Begin Routine' code from mar3
    mar_movie.play();
    
    image_3.setPos([posx, posy]);
    image_3.setImage('imgs/iceberg.png');
    resp_musicw_r1.keys = undefined;
    resp_musicw_r1.rt = undefined;
    _resp_musicw_r1_allKeys = [];
    // keep track of which components have finished
    music_wordsComponents = [];
    music_wordsComponents.push(image_3);
    music_wordsComponents.push(resp_musicw_r1);
    
    music_wordsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function music_wordsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'music_words' ---
    // get current time
    t = music_wordsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from code_2
    background_movie.draw();
    
    // Run 'Each Frame' code from mar3
    mar_movie.draw();
    
    
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
    
    // *resp_musicw_r1* updates
    if (t >= timepresentation && resp_musicw_r1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp_musicw_r1.tStart = t;  // (not accounting for frame time here)
      resp_musicw_r1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp_musicw_r1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp_musicw_r1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp_musicw_r1.clearEvents(); });
    }
    
    frameRemains = timepresentation + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (resp_musicw_r1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      resp_musicw_r1.status = PsychoJS.Status.FINISHED;
        }
      
    if (resp_musicw_r1.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp_musicw_r1.getKeys({keyList: ['space'], waitRelease: false});
      _resp_musicw_r1_allKeys = _resp_musicw_r1_allKeys.concat(theseKeys);
      if (_resp_musicw_r1_allKeys.length > 0) {
        resp_musicw_r1.keys = _resp_musicw_r1_allKeys[_resp_musicw_r1_allKeys.length - 1].name;  // just the last key pressed
        resp_musicw_r1.rt = _resp_musicw_r1_allKeys[_resp_musicw_r1_allKeys.length - 1].rt;
        resp_musicw_r1.duration = _resp_musicw_r1_allKeys[_resp_musicw_r1_allKeys.length - 1].duration;
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
    music_wordsComponents.forEach( function(thisComponent) {
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

function music_wordsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'music_words' ---
    music_wordsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('music_words.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_2
    if ((trials_3.thisN === (nRows - 1))) {
        background_movie.stop();
    }
    
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(resp_musicw_r1.corr, level);
    }
    psychoJS.experiment.addData('resp_musicw_r1.keys', resp_musicw_r1.keys);
    if (typeof resp_musicw_r1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp_musicw_r1.rt', resp_musicw_r1.rt);
        psychoJS.experiment.addData('resp_musicw_r1.duration', resp_musicw_r1.duration);
        routineTimer.reset();
        }
    
    resp_musicw_r1.stop();
    // the Routine "music_words" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function music_videoRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'music_video' ---
    t = 0;
    music_videoClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('music_video.started', globalClock.getTime());
    // Run 'Begin Routine' code from musicv_r1
    if ((ronda1 === "music_video")) {
        continueRoutine = true;
    } else {
        continueRoutine = false;
    }
    
    // Run 'Begin Routine' code from code_2_2
    if ((trials_4.thisN === 0)) {
        background_movie2.play();
        background_movie2.draw();
    }
    
    // Run 'Begin Routine' code from mar4
    mar_movie.play();
    
    // Run 'Begin Routine' code from code_3
    if ((trials_4.thisN === 0)) {
        displayed_movie.play();
        displayed_movie.draw();
    }
    
    image_4.setPos([posx, posy]);
    image_4.setImage('imgs/iceberg.png');
    resp_musicv_r1.keys = undefined;
    resp_musicv_r1.rt = undefined;
    _resp_musicv_r1_allKeys = [];
    // keep track of which components have finished
    music_videoComponents = [];
    music_videoComponents.push(image_4);
    music_videoComponents.push(resp_musicv_r1);
    
    music_videoComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function music_videoRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'music_video' ---
    // get current time
    t = music_videoClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from code_2_2
    background_movie2.draw();
    
    // Run 'Each Frame' code from mar4
    mar_movie.draw();
    
    // Run 'Each Frame' code from code_3
    displayed_movie.draw();
    
    
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
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    music_videoComponents.forEach( function(thisComponent) {
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

function music_videoRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'music_video' ---
    music_videoComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('music_video.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_2_2
    if ((trials_4.thisN === (nRows - 1))) {
        background_movie2.stop();
    }
    
    // Run 'End Routine' code from code_3
    if ((trials_4.thisN === (nRows - 1))) {
        displayed_movie.stop();
    }
    
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
    // the Routine "music_video" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function Ronda_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Ronda_2' ---
    t = 0;
    Ronda_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('Ronda_2.started', globalClock.getTime());
    text_8.setText('Ronda 2/4');
    // Run 'Begin Routine' code from code_15
    selectedRows = Math.random.sample(util.range(totalRows), nRows);
    selectedRowsStr_r2 = function () {
        var _pj_a = [], _pj_b = selectedRows;
        for (var _pj_c = 0, _pj_d = _pj_b.length; (_pj_c < _pj_d); _pj_c += 1) {
            var i = _pj_b[_pj_c];
            _pj_a.push(i);
        }
        return _pj_a;
    }
    .call(this);
    
    // keep track of which components have finished
    Ronda_2Components = [];
    Ronda_2Components.push(text_8);
    
    Ronda_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function Ronda_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Ronda_2' ---
    // get current time
    t = Ronda_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_8* updates
    if (t >= 0.0 && text_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_8.tStart = t;  // (not accounting for frame time here)
      text_8.frameNStart = frameN;  // exact frame index
      
      text_8.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_8.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_8.setAutoDraw(false);
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
    Ronda_2Components.forEach( function(thisComponent) {
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

function Ronda_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Ronda_2' ---
    Ronda_2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Ronda_2.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function control2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'control2' ---
    t = 0;
    control2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('control2.started', globalClock.getTime());
    // Run 'Begin Routine' code from control_r2
    if ((ronda2 === "control")) {
        continueRoutine = true;
    } else {
        continueRoutine = false;
    }
    
    image_6.setPos([posx, posy]);
    image_6.setImage('imgs/iceberg.png');
    resp_control_r2.keys = undefined;
    resp_control_r2.rt = undefined;
    _resp_control_r2_allKeys = [];
    // Run 'Begin Routine' code from mar_1_2
    mar_movie.play();
    
    // keep track of which components have finished
    control2Components = [];
    control2Components.push(image_6);
    control2Components.push(resp_control_r2);
    
    control2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function control2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'control2' ---
    // get current time
    t = control2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_6* updates
    if (t >= timepresentation && image_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_6.tStart = t;  // (not accounting for frame time here)
      image_6.frameNStart = frameN;  // exact frame index
      
      image_6.setAutoDraw(true);
    }
    
    frameRemains = timepresentation + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_6.setAutoDraw(false);
    }
    
    // *resp_control_r2* updates
    if (t >= timepresentation && resp_control_r2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp_control_r2.tStart = t;  // (not accounting for frame time here)
      resp_control_r2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp_control_r2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp_control_r2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp_control_r2.clearEvents(); });
    }
    
    frameRemains = timepresentation + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (resp_control_r2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      resp_control_r2.status = PsychoJS.Status.FINISHED;
        }
      
    if (resp_control_r2.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp_control_r2.getKeys({keyList: ['space'], waitRelease: false});
      _resp_control_r2_allKeys = _resp_control_r2_allKeys.concat(theseKeys);
      if (_resp_control_r2_allKeys.length > 0) {
        resp_control_r2.keys = _resp_control_r2_allKeys[_resp_control_r2_allKeys.length - 1].name;  // just the last key pressed
        resp_control_r2.rt = _resp_control_r2_allKeys[_resp_control_r2_allKeys.length - 1].rt;
        resp_control_r2.duration = _resp_control_r2_allKeys[_resp_control_r2_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // Run 'Each Frame' code from mar_1_2
    mar_movie.draw();
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    control2Components.forEach( function(thisComponent) {
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

function control2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'control2' ---
    control2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('control2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(resp_control_r2.corr, level);
    }
    psychoJS.experiment.addData('resp_control_r2.keys', resp_control_r2.keys);
    if (typeof resp_control_r2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp_control_r2.rt', resp_control_r2.rt);
        psychoJS.experiment.addData('resp_control_r2.duration', resp_control_r2.duration);
        routineTimer.reset();
        }
    
    resp_control_r2.stop();
    // the Routine "control2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function music2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'music2' ---
    t = 0;
    music2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('music2.started', globalClock.getTime());
    // Run 'Begin Routine' code from music_r2
    if ((ronda2 === "music")) {
        continueRoutine = true;
    } else {
        continueRoutine = false;
    }
    
    image_7.setPos([posx, posy]);
    image_7.setImage('imgs/iceberg.png');
    resp_music_r2.keys = undefined;
    resp_music_r2.rt = undefined;
    _resp_music_r2_allKeys = [];
    // Run 'Begin Routine' code from code_6
    if ((trials_6.thisN === 0)) {
        background_sound_r2.play();
    }
    
    // Run 'Begin Routine' code from mar2_2
    mar_movie.play();
    
    // keep track of which components have finished
    music2Components = [];
    music2Components.push(image_7);
    music2Components.push(resp_music_r2);
    
    music2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function music2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'music2' ---
    // get current time
    t = music2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_7* updates
    if (t >= timepresentation && image_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_7.tStart = t;  // (not accounting for frame time here)
      image_7.frameNStart = frameN;  // exact frame index
      
      image_7.setAutoDraw(true);
    }
    
    frameRemains = timepresentation + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_7.setAutoDraw(false);
    }
    
    // *resp_music_r2* updates
    if (t >= timepresentation && resp_music_r2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp_music_r2.tStart = t;  // (not accounting for frame time here)
      resp_music_r2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp_music_r2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp_music_r2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp_music_r2.clearEvents(); });
    }
    
    frameRemains = timepresentation + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (resp_music_r2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      resp_music_r2.status = PsychoJS.Status.FINISHED;
        }
      
    if (resp_music_r2.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp_music_r2.getKeys({keyList: ['space'], waitRelease: false});
      _resp_music_r2_allKeys = _resp_music_r2_allKeys.concat(theseKeys);
      if (_resp_music_r2_allKeys.length > 0) {
        resp_music_r2.keys = _resp_music_r2_allKeys[_resp_music_r2_allKeys.length - 1].name;  // just the last key pressed
        resp_music_r2.rt = _resp_music_r2_allKeys[_resp_music_r2_allKeys.length - 1].rt;
        resp_music_r2.duration = _resp_music_r2_allKeys[_resp_music_r2_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // Run 'Each Frame' code from code_6
    background_sound_r2.draw();
    
    // Run 'Each Frame' code from mar2_2
    mar_movie.draw();
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    music2Components.forEach( function(thisComponent) {
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

function music2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'music2' ---
    music2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('music2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(resp_music_r2.corr, level);
    }
    psychoJS.experiment.addData('resp_music_r2.keys', resp_music_r2.keys);
    if (typeof resp_music_r2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp_music_r2.rt', resp_music_r2.rt);
        psychoJS.experiment.addData('resp_music_r2.duration', resp_music_r2.duration);
        routineTimer.reset();
        }
    
    resp_music_r2.stop();
    // Run 'End Routine' code from code_6
    if ((trials_6.thisN === (nRows - 1))) {
        background_sound_r2.stop();
    }
    
    // the Routine "music2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function music_words2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'music_words2' ---
    t = 0;
    music_words2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('music_words2.started', globalClock.getTime());
    // Run 'Begin Routine' code from musicw_r2
    if ((ronda2 === "music_words")) {
        continueRoutine = true;
    } else {
        continueRoutine = false;
    }
    
    // Run 'Begin Routine' code from code_7
    if ((trials_7.thisN === 0)) {
        background_movie_r2.play();
        background_movie_r2.draw();
    }
    
    // Run 'Begin Routine' code from mar3_2
    mar_movie.play();
    
    image_8.setPos([posx, posy]);
    image_8.setImage('imgs/iceberg.png');
    resp_musicw_r2.keys = undefined;
    resp_musicw_r2.rt = undefined;
    _resp_musicw_r2_allKeys = [];
    // keep track of which components have finished
    music_words2Components = [];
    music_words2Components.push(image_8);
    music_words2Components.push(resp_musicw_r2);
    
    music_words2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function music_words2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'music_words2' ---
    // get current time
    t = music_words2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from code_7
    background_movie_r2.draw();
    
    // Run 'Each Frame' code from mar3_2
    mar_movie.draw();
    
    
    // *image_8* updates
    if (t >= timepresentation && image_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_8.tStart = t;  // (not accounting for frame time here)
      image_8.frameNStart = frameN;  // exact frame index
      
      image_8.setAutoDraw(true);
    }
    
    frameRemains = timepresentation + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_8.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_8.setAutoDraw(false);
    }
    
    // *resp_musicw_r2* updates
    if (t >= timepresentation && resp_musicw_r2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp_musicw_r2.tStart = t;  // (not accounting for frame time here)
      resp_musicw_r2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp_musicw_r2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp_musicw_r2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp_musicw_r2.clearEvents(); });
    }
    
    frameRemains = timepresentation + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (resp_musicw_r2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      resp_musicw_r2.status = PsychoJS.Status.FINISHED;
        }
      
    if (resp_musicw_r2.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp_musicw_r2.getKeys({keyList: ['space'], waitRelease: false});
      _resp_musicw_r2_allKeys = _resp_musicw_r2_allKeys.concat(theseKeys);
      if (_resp_musicw_r2_allKeys.length > 0) {
        resp_musicw_r2.keys = _resp_musicw_r2_allKeys[_resp_musicw_r2_allKeys.length - 1].name;  // just the last key pressed
        resp_musicw_r2.rt = _resp_musicw_r2_allKeys[_resp_musicw_r2_allKeys.length - 1].rt;
        resp_musicw_r2.duration = _resp_musicw_r2_allKeys[_resp_musicw_r2_allKeys.length - 1].duration;
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
    music_words2Components.forEach( function(thisComponent) {
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

function music_words2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'music_words2' ---
    music_words2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('music_words2.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_7
    if ((trials_7.thisN === (nRows - 1))) {
        background_movie_r2.stop();
    }
    
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(resp_musicw_r2.corr, level);
    }
    psychoJS.experiment.addData('resp_musicw_r2.keys', resp_musicw_r2.keys);
    if (typeof resp_musicw_r2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp_musicw_r2.rt', resp_musicw_r2.rt);
        psychoJS.experiment.addData('resp_musicw_r2.duration', resp_musicw_r2.duration);
        routineTimer.reset();
        }
    
    resp_musicw_r2.stop();
    // the Routine "music_words2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function music_video2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'music_video2' ---
    t = 0;
    music_video2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('music_video2.started', globalClock.getTime());
    // Run 'Begin Routine' code from musicv_r2
    if ((ronda2 === "music_video")) {
        continueRoutine = true;
    } else {
        continueRoutine = false;
    }
    
    // Run 'Begin Routine' code from code_2_3
    if ((trials_8.thisN === 0)) {
        backgroung_movie2_r2.play();
        backgroung_movie2_r2.draw();
    }
    
    // Run 'Begin Routine' code from mar4_2
    mar_movie.play();
    
    // Run 'Begin Routine' code from code_8
    if ((trials_8.thisN === 0)) {
        displayed_movie_r2.play();
        displayed_movie_r2.draw();
    }
    
    image_9.setPos([posx, posy]);
    image_9.setImage('imgs/iceberg.png');
    resp_musicv_r2.keys = undefined;
    resp_musicv_r2.rt = undefined;
    _resp_musicv_r2_allKeys = [];
    // keep track of which components have finished
    music_video2Components = [];
    music_video2Components.push(image_9);
    music_video2Components.push(resp_musicv_r2);
    
    music_video2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function music_video2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'music_video2' ---
    // get current time
    t = music_video2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from code_2_3
    backgroung_movie2_r2.draw();
    
    // Run 'Each Frame' code from mar4_2
    mar_movie.draw();
    
    // Run 'Each Frame' code from code_8
    displayed_movie_r2.draw();
    
    
    // *image_9* updates
    if (t >= timepresentation && image_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_9.tStart = t;  // (not accounting for frame time here)
      image_9.frameNStart = frameN;  // exact frame index
      
      image_9.setAutoDraw(true);
    }
    
    frameRemains = timepresentation + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_9.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_9.setAutoDraw(false);
    }
    
    // *resp_musicv_r2* updates
    if (t >= timepresentation && resp_musicv_r2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp_musicv_r2.tStart = t;  // (not accounting for frame time here)
      resp_musicv_r2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp_musicv_r2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp_musicv_r2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp_musicv_r2.clearEvents(); });
    }
    
    frameRemains = timepresentation + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (resp_musicv_r2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      resp_musicv_r2.status = PsychoJS.Status.FINISHED;
        }
      
    if (resp_musicv_r2.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp_musicv_r2.getKeys({keyList: ['space'], waitRelease: false});
      _resp_musicv_r2_allKeys = _resp_musicv_r2_allKeys.concat(theseKeys);
      if (_resp_musicv_r2_allKeys.length > 0) {
        resp_musicv_r2.keys = _resp_musicv_r2_allKeys[_resp_musicv_r2_allKeys.length - 1].name;  // just the last key pressed
        resp_musicv_r2.rt = _resp_musicv_r2_allKeys[_resp_musicv_r2_allKeys.length - 1].rt;
        resp_musicv_r2.duration = _resp_musicv_r2_allKeys[_resp_musicv_r2_allKeys.length - 1].duration;
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
    music_video2Components.forEach( function(thisComponent) {
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

function music_video2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'music_video2' ---
    music_video2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('music_video2.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_2_3
    if ((trials_8.thisN === (nRows - 1))) {
        backgroung_movie2_r2.stop();
    }
    
    // Run 'End Routine' code from code_8
    if ((trials_8.thisN === (nRows - 1))) {
        displayed_movie_r2.stop();
    }
    
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(resp_musicv_r2.corr, level);
    }
    psychoJS.experiment.addData('resp_musicv_r2.keys', resp_musicv_r2.keys);
    if (typeof resp_musicv_r2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp_musicv_r2.rt', resp_musicv_r2.rt);
        psychoJS.experiment.addData('resp_musicv_r2.duration', resp_musicv_r2.duration);
        routineTimer.reset();
        }
    
    resp_musicv_r2.stop();
    // the Routine "music_video2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function Ronda_3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Ronda_3' ---
    t = 0;
    Ronda_3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('Ronda_3.started', globalClock.getTime());
    text_9.setText('Ronda 3/4');
    // Run 'Begin Routine' code from code_16
    selectedRows = Math.random.sample(util.range(totalRows), nRows);
    selectedRowsStr_r3 = function () {
        var _pj_a = [], _pj_b = selectedRows;
        for (var _pj_c = 0, _pj_d = _pj_b.length; (_pj_c < _pj_d); _pj_c += 1) {
            var i = _pj_b[_pj_c];
            _pj_a.push(i);
        }
        return _pj_a;
    }
    .call(this);
    
    // keep track of which components have finished
    Ronda_3Components = [];
    Ronda_3Components.push(text_9);
    
    Ronda_3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function Ronda_3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Ronda_3' ---
    // get current time
    t = Ronda_3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_9* updates
    if (t >= 0.0 && text_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_9.tStart = t;  // (not accounting for frame time here)
      text_9.frameNStart = frameN;  // exact frame index
      
      text_9.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_9.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_9.setAutoDraw(false);
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
    Ronda_3Components.forEach( function(thisComponent) {
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

function Ronda_3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Ronda_3' ---
    Ronda_3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Ronda_3.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function control3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'control3' ---
    t = 0;
    control3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('control3.started', globalClock.getTime());
    // Run 'Begin Routine' code from control_r3
    if ((ronda3 === "control")) {
        continueRoutine = true;
    } else {
        continueRoutine = false;
    }
    
    image_10.setPos([posx, posy]);
    image_10.setImage('imgs/iceberg.png');
    resp_control_r3.keys = undefined;
    resp_control_r3.rt = undefined;
    _resp_control_r3_allKeys = [];
    // Run 'Begin Routine' code from mar_1_3
    mar_movie.play();
    
    // keep track of which components have finished
    control3Components = [];
    control3Components.push(image_10);
    control3Components.push(resp_control_r3);
    
    control3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function control3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'control3' ---
    // get current time
    t = control3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_10* updates
    if (t >= timepresentation && image_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_10.tStart = t;  // (not accounting for frame time here)
      image_10.frameNStart = frameN;  // exact frame index
      
      image_10.setAutoDraw(true);
    }
    
    frameRemains = timepresentation + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_10.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_10.setAutoDraw(false);
    }
    
    // *resp_control_r3* updates
    if (t >= timepresentation && resp_control_r3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp_control_r3.tStart = t;  // (not accounting for frame time here)
      resp_control_r3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp_control_r3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp_control_r3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp_control_r3.clearEvents(); });
    }
    
    frameRemains = timepresentation + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (resp_control_r3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      resp_control_r3.status = PsychoJS.Status.FINISHED;
        }
      
    if (resp_control_r3.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp_control_r3.getKeys({keyList: ['space'], waitRelease: false});
      _resp_control_r3_allKeys = _resp_control_r3_allKeys.concat(theseKeys);
      if (_resp_control_r3_allKeys.length > 0) {
        resp_control_r3.keys = _resp_control_r3_allKeys[_resp_control_r3_allKeys.length - 1].name;  // just the last key pressed
        resp_control_r3.rt = _resp_control_r3_allKeys[_resp_control_r3_allKeys.length - 1].rt;
        resp_control_r3.duration = _resp_control_r3_allKeys[_resp_control_r3_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // Run 'Each Frame' code from mar_1_3
    mar_movie.draw();
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    control3Components.forEach( function(thisComponent) {
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

function control3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'control3' ---
    control3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('control3.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(resp_control_r3.corr, level);
    }
    psychoJS.experiment.addData('resp_control_r3.keys', resp_control_r3.keys);
    if (typeof resp_control_r3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp_control_r3.rt', resp_control_r3.rt);
        psychoJS.experiment.addData('resp_control_r3.duration', resp_control_r3.duration);
        routineTimer.reset();
        }
    
    resp_control_r3.stop();
    // the Routine "control3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function music3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'music3' ---
    t = 0;
    music3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('music3.started', globalClock.getTime());
    // Run 'Begin Routine' code from music_r3
    if ((ronda3 === "music")) {
        continueRoutine = true;
    } else {
        continueRoutine = false;
    }
    
    image_11.setPos([posx, posy]);
    image_11.setImage('imgs/iceberg.png');
    resp_music_r3.keys = undefined;
    resp_music_r3.rt = undefined;
    _resp_music_r3_allKeys = [];
    // Run 'Begin Routine' code from code_9
    if ((trials_10.thisN === 0)) {
        background_sound_r3.play();
    }
    
    // Run 'Begin Routine' code from mar2_3
    mar_movie.play();
    
    // keep track of which components have finished
    music3Components = [];
    music3Components.push(image_11);
    music3Components.push(resp_music_r3);
    
    music3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function music3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'music3' ---
    // get current time
    t = music3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_11* updates
    if (t >= timepresentation && image_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_11.tStart = t;  // (not accounting for frame time here)
      image_11.frameNStart = frameN;  // exact frame index
      
      image_11.setAutoDraw(true);
    }
    
    frameRemains = timepresentation + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_11.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_11.setAutoDraw(false);
    }
    
    // *resp_music_r3* updates
    if (t >= timepresentation && resp_music_r3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp_music_r3.tStart = t;  // (not accounting for frame time here)
      resp_music_r3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp_music_r3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp_music_r3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp_music_r3.clearEvents(); });
    }
    
    frameRemains = timepresentation + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (resp_music_r3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      resp_music_r3.status = PsychoJS.Status.FINISHED;
        }
      
    if (resp_music_r3.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp_music_r3.getKeys({keyList: ['space'], waitRelease: false});
      _resp_music_r3_allKeys = _resp_music_r3_allKeys.concat(theseKeys);
      if (_resp_music_r3_allKeys.length > 0) {
        resp_music_r3.keys = _resp_music_r3_allKeys[_resp_music_r3_allKeys.length - 1].name;  // just the last key pressed
        resp_music_r3.rt = _resp_music_r3_allKeys[_resp_music_r3_allKeys.length - 1].rt;
        resp_music_r3.duration = _resp_music_r3_allKeys[_resp_music_r3_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // Run 'Each Frame' code from code_9
    background_sound_r3.draw();
    
    // Run 'Each Frame' code from mar2_3
    mar_movie.draw();
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    music3Components.forEach( function(thisComponent) {
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

function music3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'music3' ---
    music3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('music3.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(resp_music_r3.corr, level);
    }
    psychoJS.experiment.addData('resp_music_r3.keys', resp_music_r3.keys);
    if (typeof resp_music_r3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp_music_r3.rt', resp_music_r3.rt);
        psychoJS.experiment.addData('resp_music_r3.duration', resp_music_r3.duration);
        routineTimer.reset();
        }
    
    resp_music_r3.stop();
    // Run 'End Routine' code from code_9
    if ((trials_10.thisN === (nRows - 1))) {
        background_sound_r3.stop();
    }
    
    // the Routine "music3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function music_words3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'music_words3' ---
    t = 0;
    music_words3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('music_words3.started', globalClock.getTime());
    // Run 'Begin Routine' code from musicw_r3
    if ((ronda3 === "music_words")) {
        continueRoutine = true;
    } else {
        continueRoutine = false;
    }
    
    // Run 'Begin Routine' code from code_10
    if ((trials_11.thisN === 0)) {
        background_movie_r3.play();
        background_movie_r3.draw();
    }
    
    // Run 'Begin Routine' code from mar3_3
    mar_movie.play();
    
    image_12.setPos([posx, posy]);
    image_12.setImage('imgs/iceberg.png');
    resp_musicw_r3.keys = undefined;
    resp_musicw_r3.rt = undefined;
    _resp_musicw_r3_allKeys = [];
    // keep track of which components have finished
    music_words3Components = [];
    music_words3Components.push(image_12);
    music_words3Components.push(resp_musicw_r3);
    
    music_words3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function music_words3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'music_words3' ---
    // get current time
    t = music_words3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from code_10
    background_movie_r3.draw();
    
    // Run 'Each Frame' code from mar3_3
    mar_movie.draw();
    
    
    // *image_12* updates
    if (t >= timepresentation && image_12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_12.tStart = t;  // (not accounting for frame time here)
      image_12.frameNStart = frameN;  // exact frame index
      
      image_12.setAutoDraw(true);
    }
    
    frameRemains = timepresentation + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_12.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_12.setAutoDraw(false);
    }
    
    // *resp_musicw_r3* updates
    if (t >= timepresentation && resp_musicw_r3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp_musicw_r3.tStart = t;  // (not accounting for frame time here)
      resp_musicw_r3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp_musicw_r3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp_musicw_r3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp_musicw_r3.clearEvents(); });
    }
    
    frameRemains = timepresentation + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (resp_musicw_r3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      resp_musicw_r3.status = PsychoJS.Status.FINISHED;
        }
      
    if (resp_musicw_r3.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp_musicw_r3.getKeys({keyList: ['space'], waitRelease: false});
      _resp_musicw_r3_allKeys = _resp_musicw_r3_allKeys.concat(theseKeys);
      if (_resp_musicw_r3_allKeys.length > 0) {
        resp_musicw_r3.keys = _resp_musicw_r3_allKeys[_resp_musicw_r3_allKeys.length - 1].name;  // just the last key pressed
        resp_musicw_r3.rt = _resp_musicw_r3_allKeys[_resp_musicw_r3_allKeys.length - 1].rt;
        resp_musicw_r3.duration = _resp_musicw_r3_allKeys[_resp_musicw_r3_allKeys.length - 1].duration;
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
    music_words3Components.forEach( function(thisComponent) {
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

function music_words3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'music_words3' ---
    music_words3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('music_words3.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_10
    if ((trials_11.thisN === (nRows - 1))) {
        background_movie_r3.stop();
    }
    
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(resp_musicw_r3.corr, level);
    }
    psychoJS.experiment.addData('resp_musicw_r3.keys', resp_musicw_r3.keys);
    if (typeof resp_musicw_r3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp_musicw_r3.rt', resp_musicw_r3.rt);
        psychoJS.experiment.addData('resp_musicw_r3.duration', resp_musicw_r3.duration);
        routineTimer.reset();
        }
    
    resp_musicw_r3.stop();
    // the Routine "music_words3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function music_video3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'music_video3' ---
    t = 0;
    music_video3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('music_video3.started', globalClock.getTime());
    // Run 'Begin Routine' code from musicv_r3
    if ((ronda3 === "music_video")) {
        continueRoutine = true;
    } else {
        continueRoutine = false;
    }
    
    // Run 'Begin Routine' code from code_2_4
    if ((trials_12.thisN === 0)) {
        backgroung_movie2_r3.play();
        backgroung_movie2_r3.draw();
    }
    
    // Run 'Begin Routine' code from mar4_3
    mar_movie.play();
    
    // Run 'Begin Routine' code from code_11
    if ((trials_12.thisN === 0)) {
        displayed_movie_r3.play();
        displayed_movie_r3.draw();
    }
    
    image_13.setPos([posx, posy]);
    image_13.setImage('imgs/iceberg.png');
    resp_musicv_r3.keys = undefined;
    resp_musicv_r3.rt = undefined;
    _resp_musicv_r3_allKeys = [];
    // keep track of which components have finished
    music_video3Components = [];
    music_video3Components.push(image_13);
    music_video3Components.push(resp_musicv_r3);
    
    music_video3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function music_video3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'music_video3' ---
    // get current time
    t = music_video3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from code_2_4
    backgroung_movie2_r3.draw();
    
    // Run 'Each Frame' code from mar4_3
    mar_movie.draw();
    
    // Run 'Each Frame' code from code_11
    displayed_movie_r3.draw();
    
    
    // *image_13* updates
    if (t >= timepresentation && image_13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_13.tStart = t;  // (not accounting for frame time here)
      image_13.frameNStart = frameN;  // exact frame index
      
      image_13.setAutoDraw(true);
    }
    
    frameRemains = timepresentation + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_13.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_13.setAutoDraw(false);
    }
    
    // *resp_musicv_r3* updates
    if (t >= timepresentation && resp_musicv_r3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp_musicv_r3.tStart = t;  // (not accounting for frame time here)
      resp_musicv_r3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp_musicv_r3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp_musicv_r3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp_musicv_r3.clearEvents(); });
    }
    
    frameRemains = timepresentation + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (resp_musicv_r3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      resp_musicv_r3.status = PsychoJS.Status.FINISHED;
        }
      
    if (resp_musicv_r3.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp_musicv_r3.getKeys({keyList: ['space'], waitRelease: false});
      _resp_musicv_r3_allKeys = _resp_musicv_r3_allKeys.concat(theseKeys);
      if (_resp_musicv_r3_allKeys.length > 0) {
        resp_musicv_r3.keys = _resp_musicv_r3_allKeys[_resp_musicv_r3_allKeys.length - 1].name;  // just the last key pressed
        resp_musicv_r3.rt = _resp_musicv_r3_allKeys[_resp_musicv_r3_allKeys.length - 1].rt;
        resp_musicv_r3.duration = _resp_musicv_r3_allKeys[_resp_musicv_r3_allKeys.length - 1].duration;
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
    music_video3Components.forEach( function(thisComponent) {
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

function music_video3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'music_video3' ---
    music_video3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('music_video3.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_2_4
    if ((trials_12.thisN === (nRows - 1))) {
        backgroung_movie2_r3.stop();
    }
    
    // Run 'End Routine' code from code_11
    if ((trials_12.thisN === (nRows - 1))) {
        displayed_movie_r3.stop();
    }
    
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(resp_musicv_r3.corr, level);
    }
    psychoJS.experiment.addData('resp_musicv_r3.keys', resp_musicv_r3.keys);
    if (typeof resp_musicv_r3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp_musicv_r3.rt', resp_musicv_r3.rt);
        psychoJS.experiment.addData('resp_musicv_r3.duration', resp_musicv_r3.duration);
        routineTimer.reset();
        }
    
    resp_musicv_r3.stop();
    // the Routine "music_video3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function Ronda_4RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Ronda_4' ---
    t = 0;
    Ronda_4Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('Ronda_4.started', globalClock.getTime());
    text_10.setText('Ronda 4/4');
    // Run 'Begin Routine' code from code_17
    selectedRows = Math.random.sample(util.range(totalRows), nRows);
    selectedRowsStr_r4 = function () {
        var _pj_a = [], _pj_b = selectedRows;
        for (var _pj_c = 0, _pj_d = _pj_b.length; (_pj_c < _pj_d); _pj_c += 1) {
            var i = _pj_b[_pj_c];
            _pj_a.push(i);
        }
        return _pj_a;
    }
    .call(this);
    
    // keep track of which components have finished
    Ronda_4Components = [];
    Ronda_4Components.push(text_10);
    
    Ronda_4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function Ronda_4RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Ronda_4' ---
    // get current time
    t = Ronda_4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_10* updates
    if (t >= 0.0 && text_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_10.tStart = t;  // (not accounting for frame time here)
      text_10.frameNStart = frameN;  // exact frame index
      
      text_10.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_10.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_10.setAutoDraw(false);
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
    Ronda_4Components.forEach( function(thisComponent) {
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

function Ronda_4RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Ronda_4' ---
    Ronda_4Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Ronda_4.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function control4RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'control4' ---
    t = 0;
    control4Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('control4.started', globalClock.getTime());
    // Run 'Begin Routine' code from control_r4
    if ((ronda4 === "control")) {
        continueRoutine = true;
    } else {
        continueRoutine = false;
    }
    
    image_14.setPos([posx, posy]);
    image_14.setImage('imgs/iceberg.png');
    resp_control_r4.keys = undefined;
    resp_control_r4.rt = undefined;
    _resp_control_r4_allKeys = [];
    // Run 'Begin Routine' code from mar_1_4
    mar_movie.play();
    
    // keep track of which components have finished
    control4Components = [];
    control4Components.push(image_14);
    control4Components.push(resp_control_r4);
    
    control4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function control4RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'control4' ---
    // get current time
    t = control4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_14* updates
    if (t >= timepresentation && image_14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_14.tStart = t;  // (not accounting for frame time here)
      image_14.frameNStart = frameN;  // exact frame index
      
      image_14.setAutoDraw(true);
    }
    
    frameRemains = timepresentation + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_14.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_14.setAutoDraw(false);
    }
    
    // *resp_control_r4* updates
    if (t >= timepresentation && resp_control_r4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp_control_r4.tStart = t;  // (not accounting for frame time here)
      resp_control_r4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp_control_r4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp_control_r4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp_control_r4.clearEvents(); });
    }
    
    frameRemains = timepresentation + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (resp_control_r4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      resp_control_r4.status = PsychoJS.Status.FINISHED;
        }
      
    if (resp_control_r4.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp_control_r4.getKeys({keyList: ['space'], waitRelease: false});
      _resp_control_r4_allKeys = _resp_control_r4_allKeys.concat(theseKeys);
      if (_resp_control_r4_allKeys.length > 0) {
        resp_control_r4.keys = _resp_control_r4_allKeys[_resp_control_r4_allKeys.length - 1].name;  // just the last key pressed
        resp_control_r4.rt = _resp_control_r4_allKeys[_resp_control_r4_allKeys.length - 1].rt;
        resp_control_r4.duration = _resp_control_r4_allKeys[_resp_control_r4_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // Run 'Each Frame' code from mar_1_4
    mar_movie.draw();
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    control4Components.forEach( function(thisComponent) {
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

function control4RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'control4' ---
    control4Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('control4.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(resp_control_r4.corr, level);
    }
    psychoJS.experiment.addData('resp_control_r4.keys', resp_control_r4.keys);
    if (typeof resp_control_r4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp_control_r4.rt', resp_control_r4.rt);
        psychoJS.experiment.addData('resp_control_r4.duration', resp_control_r4.duration);
        routineTimer.reset();
        }
    
    resp_control_r4.stop();
    // the Routine "control4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function music4RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'music4' ---
    t = 0;
    music4Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('music4.started', globalClock.getTime());
    // Run 'Begin Routine' code from music_r4
    if ((ronda4 === "music")) {
        continueRoutine = true;
    } else {
        continueRoutine = false;
    }
    
    image_15.setPos([posx, posy]);
    image_15.setImage('imgs/iceberg.png');
    resp_music_r4.keys = undefined;
    resp_music_r4.rt = undefined;
    _resp_music_r4_allKeys = [];
    // Run 'Begin Routine' code from code_12
    if ((trials_14.thisN === 0)) {
        background_sound_r4.play();
    }
    
    // Run 'Begin Routine' code from mar2_4
    mar_movie.play();
    
    // keep track of which components have finished
    music4Components = [];
    music4Components.push(image_15);
    music4Components.push(resp_music_r4);
    
    music4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function music4RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'music4' ---
    // get current time
    t = music4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_15* updates
    if (t >= timepresentation && image_15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_15.tStart = t;  // (not accounting for frame time here)
      image_15.frameNStart = frameN;  // exact frame index
      
      image_15.setAutoDraw(true);
    }
    
    frameRemains = timepresentation + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_15.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_15.setAutoDraw(false);
    }
    
    // *resp_music_r4* updates
    if (t >= timepresentation && resp_music_r4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp_music_r4.tStart = t;  // (not accounting for frame time here)
      resp_music_r4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp_music_r4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp_music_r4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp_music_r4.clearEvents(); });
    }
    
    frameRemains = timepresentation + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (resp_music_r4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      resp_music_r4.status = PsychoJS.Status.FINISHED;
        }
      
    if (resp_music_r4.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp_music_r4.getKeys({keyList: ['space'], waitRelease: false});
      _resp_music_r4_allKeys = _resp_music_r4_allKeys.concat(theseKeys);
      if (_resp_music_r4_allKeys.length > 0) {
        resp_music_r4.keys = _resp_music_r4_allKeys[_resp_music_r4_allKeys.length - 1].name;  // just the last key pressed
        resp_music_r4.rt = _resp_music_r4_allKeys[_resp_music_r4_allKeys.length - 1].rt;
        resp_music_r4.duration = _resp_music_r4_allKeys[_resp_music_r4_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // Run 'Each Frame' code from code_12
    background_sound_r4.draw();
    
    // Run 'Each Frame' code from mar2_4
    mar_movie.draw();
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    music4Components.forEach( function(thisComponent) {
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

function music4RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'music4' ---
    music4Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('music4.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(resp_music_r4.corr, level);
    }
    psychoJS.experiment.addData('resp_music_r4.keys', resp_music_r4.keys);
    if (typeof resp_music_r4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp_music_r4.rt', resp_music_r4.rt);
        psychoJS.experiment.addData('resp_music_r4.duration', resp_music_r4.duration);
        routineTimer.reset();
        }
    
    resp_music_r4.stop();
    // Run 'End Routine' code from code_12
    if ((trials_14.thisN === (nRows - 1))) {
        background_sound_r4.stop();
    }
    
    // the Routine "music4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function music_words4RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'music_words4' ---
    t = 0;
    music_words4Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('music_words4.started', globalClock.getTime());
    // Run 'Begin Routine' code from musicw_r4
    if ((ronda4 === "music_words")) {
        continueRoutine = true;
    } else {
        continueRoutine = false;
    }
    
    // Run 'Begin Routine' code from code_13
    if ((trials_15.thisN === 0)) {
        background_movie_r4.play();
        background_movie_r4.draw();
    }
    
    // Run 'Begin Routine' code from mar_3_4
    mar_movie.play();
    
    image_16.setPos([posx, posy]);
    image_16.setImage('imgs/iceberg.png');
    resp_musicw_r4.keys = undefined;
    resp_musicw_r4.rt = undefined;
    _resp_musicw_r4_allKeys = [];
    // keep track of which components have finished
    music_words4Components = [];
    music_words4Components.push(image_16);
    music_words4Components.push(resp_musicw_r4);
    
    music_words4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function music_words4RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'music_words4' ---
    // get current time
    t = music_words4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from code_13
    background_movie_r4.draw();
    
    // Run 'Each Frame' code from mar_3_4
    mar_movie.draw();
    
    
    // *image_16* updates
    if (t >= timepresentation && image_16.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_16.tStart = t;  // (not accounting for frame time here)
      image_16.frameNStart = frameN;  // exact frame index
      
      image_16.setAutoDraw(true);
    }
    
    frameRemains = timepresentation + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_16.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_16.setAutoDraw(false);
    }
    
    // *resp_musicw_r4* updates
    if (t >= timepresentation && resp_musicw_r4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp_musicw_r4.tStart = t;  // (not accounting for frame time here)
      resp_musicw_r4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp_musicw_r4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp_musicw_r4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp_musicw_r4.clearEvents(); });
    }
    
    frameRemains = timepresentation + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (resp_musicw_r4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      resp_musicw_r4.status = PsychoJS.Status.FINISHED;
        }
      
    if (resp_musicw_r4.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp_musicw_r4.getKeys({keyList: ['space'], waitRelease: false});
      _resp_musicw_r4_allKeys = _resp_musicw_r4_allKeys.concat(theseKeys);
      if (_resp_musicw_r4_allKeys.length > 0) {
        resp_musicw_r4.keys = _resp_musicw_r4_allKeys[_resp_musicw_r4_allKeys.length - 1].name;  // just the last key pressed
        resp_musicw_r4.rt = _resp_musicw_r4_allKeys[_resp_musicw_r4_allKeys.length - 1].rt;
        resp_musicw_r4.duration = _resp_musicw_r4_allKeys[_resp_musicw_r4_allKeys.length - 1].duration;
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
    music_words4Components.forEach( function(thisComponent) {
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

function music_words4RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'music_words4' ---
    music_words4Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('music_words4.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_13
    if ((trials_15.thisN === (nRows - 1))) {
        background_movie_r4.stop();
    }
    
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(resp_musicw_r4.corr, level);
    }
    psychoJS.experiment.addData('resp_musicw_r4.keys', resp_musicw_r4.keys);
    if (typeof resp_musicw_r4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp_musicw_r4.rt', resp_musicw_r4.rt);
        psychoJS.experiment.addData('resp_musicw_r4.duration', resp_musicw_r4.duration);
        routineTimer.reset();
        }
    
    resp_musicw_r4.stop();
    // the Routine "music_words4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function music_video4RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'music_video4' ---
    t = 0;
    music_video4Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('music_video4.started', globalClock.getTime());
    // Run 'Begin Routine' code from musicv_r4
    if ((ronda4 === "music_video")) {
        continueRoutine = true;
    } else {
        continueRoutine = false;
    }
    
    // Run 'Begin Routine' code from code_2_5
    if ((trials_16.thisN === 0)) {
        backgroung_movie2_r4.play();
        backgroung_movie2_r4.draw();
    }
    
    // Run 'Begin Routine' code from mar4_4
    mar_movie.play();
    
    // Run 'Begin Routine' code from code_14
    if ((trials_16.thisN === 0)) {
        displayed_movie_r4.play();
        displayed_movie_r4.draw();
    }
    
    image_17.setPos([posx, posy]);
    image_17.setImage('imgs/iceberg.png');
    resp_musicv_r4.keys = undefined;
    resp_musicv_r4.rt = undefined;
    _resp_musicv_r4_allKeys = [];
    // keep track of which components have finished
    music_video4Components = [];
    music_video4Components.push(image_17);
    music_video4Components.push(resp_musicv_r4);
    
    music_video4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function music_video4RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'music_video4' ---
    // get current time
    t = music_video4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from code_2_5
    backgroung_movie2_r4.draw();
    
    // Run 'Each Frame' code from mar4_4
    mar_movie.draw();
    
    // Run 'Each Frame' code from code_14
    displayed_movie_r4.draw();
    
    
    // *image_17* updates
    if (t >= timepresentation && image_17.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_17.tStart = t;  // (not accounting for frame time here)
      image_17.frameNStart = frameN;  // exact frame index
      
      image_17.setAutoDraw(true);
    }
    
    frameRemains = timepresentation + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_17.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_17.setAutoDraw(false);
    }
    
    // *resp_musicv_r4* updates
    if (t >= timepresentation && resp_musicv_r4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp_musicv_r4.tStart = t;  // (not accounting for frame time here)
      resp_musicv_r4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp_musicv_r4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp_musicv_r4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp_musicv_r4.clearEvents(); });
    }
    
    frameRemains = timepresentation + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (resp_musicv_r4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      resp_musicv_r4.status = PsychoJS.Status.FINISHED;
        }
      
    if (resp_musicv_r4.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp_musicv_r4.getKeys({keyList: ['space'], waitRelease: false});
      _resp_musicv_r4_allKeys = _resp_musicv_r4_allKeys.concat(theseKeys);
      if (_resp_musicv_r4_allKeys.length > 0) {
        resp_musicv_r4.keys = _resp_musicv_r4_allKeys[_resp_musicv_r4_allKeys.length - 1].name;  // just the last key pressed
        resp_musicv_r4.rt = _resp_musicv_r4_allKeys[_resp_musicv_r4_allKeys.length - 1].rt;
        resp_musicv_r4.duration = _resp_musicv_r4_allKeys[_resp_musicv_r4_allKeys.length - 1].duration;
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
    music_video4Components.forEach( function(thisComponent) {
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

function music_video4RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'music_video4' ---
    music_video4Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('music_video4.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_2_5
    if ((trials_16.thisN === (nRows - 1))) {
        backgroung_movie2_r4.stop();
    }
    
    // Run 'End Routine' code from code_14
    if ((trials_16.thisN === (nRows - 1))) {
        displayed_movie_r4.stop();
    }
    
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(resp_musicv_r4.corr, level);
    }
    psychoJS.experiment.addData('resp_musicv_r4.keys', resp_musicv_r4.keys);
    if (typeof resp_musicv_r4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp_musicv_r4.rt', resp_musicv_r4.rt);
        psychoJS.experiment.addData('resp_musicv_r4.duration', resp_musicv_r4.duration);
        routineTimer.reset();
        }
    
    resp_musicv_r4.stop();
    // the Routine "music_video4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

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

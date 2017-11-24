#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.04), Wed 23 Nov 2016 09:47:48 AM CET
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import locale_setup, visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'Cambridge_final3'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1280, 1024), fullscr=True, screen=0, allowGUI=True, allowStencil=False,
    monitor=u'testMonitor', color=[1.000,1.000,1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='pix')
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "Teilnahme"
TeilnahmeClock = core.Clock()
Teilnahme1 = visual.TextStim(win=win, ori=0, name='Teilnahme1',
    text=u'Cambridge Face Memory Test\n\nVielen Dank f\xfcr Ihre Teilnahme an unserer Studie.\nIm Folgenden wird es Ihre Aufgabe sein, sich die Gesichter verschiedener Individuen einzupr\xe4gen. Anschlie\xdfend werden Sie dazu aufgefordert, jeweils eins dieser Gesichter in einer Reihe von drei Gesichtern wiederzuerkennen.\nDie Studie wird mit einer sehr einfachen \xdcbungsrunde beginnen und fortschreitend schwieriger werden.\nBitte befolgen Sie immer sorgsam die Instruktionen.\nDie Studie wird in etwa 20 Minuten in Anspruch nehmen.\n\nBei weiteren Fragen zu der Studie wenden Sie sich bitte an Ihre Versuchsleiterin/Ihren Versuchsleiter oder schreiben eine E-Mail an a.garlichs@uni-bielefeld.de.\n\nWenn Sie \xfcber 18 Jahre alt sind, die obigen Instruktionen verstanden haben und freiwillig an dieser Studie teilnehmen m\xf6chten, dr\xfccken Sie bitte die Leertaste.',    font=u'Arial',
    pos=(0, 0), height=25, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "Uebung"
UebungClock = core.Clock()
Uebung_intro = visual.TextStim(win=win, ori=0, name='Uebung_intro',
    text=u'\xdcbung\n\nPr\xe4gen Sie sich das Gesicht in den n\xe4chsten drei Bildern ein.\nAnschlie\xdfend wird ein Test folgen.\n\nUm zu beginnen, dr\xfccken Sie bitte die Leertaste.',    font=u'Arial',
    pos=(0, 0), height=30, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "lernen1"
lernen1Clock = core.Clock()
bart = visual.ImageStim(win=win, name='bart',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=[200,255],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
bartM = visual.ImageStim(win=win, name='bartM',
    image=u'./stim/bart.M.jpg', mask=None,
    ori=0, pos=(0, 0), size=[200,255],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
bartR = visual.ImageStim(win=win, name='bartR',
    image=u'./stim/bart.R.jpg', mask=None,
    ori=0, pos=(0, 0), size=[200,255],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
Uebung1 = visual.TextStim(win=win, ori=0, name='Uebung1',
    text=u'\xdcbung',    font=u'Arial',
    pos=[0,175], height=30, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-3.0)
Uebung2 = visual.TextStim(win=win, ori=0, name='Uebung2',
    text=u'\xdcbung',    font=u'Arial',
    pos=[0,175], height=30, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-4.0)
Uebung3 = visual.TextStim(win=win, ori=0, name='Uebung3',
    text=u'\xdcbung',    font=u'Arial',
    pos=[0,175], height=30, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-5.0)

# Initialize components for Routine "Bart_erkennen1"
Bart_erkennen1Clock = core.Clock()
recBart = visual.ImageStim(win=win, name='recBart',
    image='sin', mask=None,
    ori=0, pos=[0,-50], size=[750,300],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
rating_1 = visual.RatingScale(win=win, name='rating_1', marker=u'triangle', size=0.7, pos=[0.0, -300.0], choices=[u'1', u'2', u'3'], tickHeight=0.6,markerColor='black',textColor='black',lineColor='black')
welches1 = visual.TextStim(win=win, ori=0, name='welches1',
    text=u'\xdcbung\n\nWelches Gesicht haben Sie gerade gesehen?\nEs gibt nur eine richtige Antwort.\nW\xe4hlen Sie mit der Maus auf der Skala die zu dem Gesicht passende Nummer aus und best\xe4tigen Sie anschlie\xdfend Ihre Auswahl.',    font=u'Arial',
    pos=[0,250], height=20, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "Memorize"
MemorizeClock = core.Clock()
Memorizing = visual.TextStim(win=win, ori=0, name='Memorizing',
    text=u'Die \xdcbung ist hiermit abgeschlossen. \nNun wird der eigentliche Test beginnen. Ihre Aufgabe wird darin bestehen, sich sechs verschiedene Personen zu merken und diese wiedererkennen zu k\xf6nnen. \n\nUm mit dem Einpr\xe4gen des ersten Gesichtes zu beginnen, dr\xfccken Sie bitte die Leertaste.',    font=u'Arial',
    pos=(0, 0), height=30, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "lernen2"
lernen2Clock = core.Clock()
image_3 = visual.ImageStim(win=win, name='image_3',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[200,250],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
image_5 = visual.ImageStim(win=win, name='image_5',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[200,250],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image_6 = visual.ImageStim(win=win, name='image_6',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[200,250],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
merken1 = visual.TextStim(win=win, ori=0, name='merken1',
    text=u'Merken',    font=u'Arial',
    pos=[0,150], height=30, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-3.0)
merken2 = visual.TextStim(win=win, ori=0, name='merken2',
    text=u'Merken',    font=u'Arial',
    pos=[0,150], height=30, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-4.0)
merken3 = visual.TextStim(win=win, ori=0, name='merken3',
    text=u'Merken',    font=u'Arial',
    pos=[0,150], height=30, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-5.0)

# Initialize components for Routine "erkennen4"
erkennen4Clock = core.Clock()
image_7 = visual.ImageStim(win=win, name='image_7',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[580,290],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
rating_4 = visual.RatingScale(win=win, name='rating_4', marker=u'triangle', size=0.8, pos=[0.0, -250.0], choices=[u'1', u'2', u'3'], tickHeight=0.6,markerColor='black',textColor='black',lineColor='black')
welches4 = visual.TextStim(win=win, ori=0, name='welches4',
    text=u'Welches Gesicht haben Sie gerade gesehen?',    font=u'Arial',
    pos=[0,250], height=30, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "erkennen5"
erkennen5Clock = core.Clock()
image_8 = visual.ImageStim(win=win, name='image_8',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[580,290],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
rating_5 = visual.RatingScale(win=win, name='rating_5', marker=u'triangle', size=0.8, pos=[0.0, -250.0], choices=[u'1', u'2', u'3'], tickHeight=0.6,markerColor='black',textColor='black',lineColor='black')
welches5 = visual.TextStim(win=win, ori=0, name='welches5',
    text=u'Welches Gesicht haben Sie gerade gesehen?',    font=u'Arial',
    pos=[0,250], height=30, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "erkennen6"
erkennen6Clock = core.Clock()
image_9 = visual.ImageStim(win=win, name='image_9',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[580,290],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
rating_6 = visual.RatingScale(win=win, name='rating_6', marker=u'triangle', size=0.8, pos=[0.0, -250.0], choices=[u'1', u'2', u'3'], tickHeight=0.6,markerColor='black',textColor='black',lineColor='black')
welches6 = visual.TextStim(win=win, ori=0, name='welches6',
    text=u'Welches Gesicht haben Sie gerade gesehen?',    font=u'Arial',
    pos=[0,250], height=30, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "Review1"
Review1Clock = core.Clock()
Review_text = visual.TextStim(win=win, ori=0, name='Review_text',
    text=u'Als N\xe4chstes werden Sie dieselben sechs Gesichter f\xfcr 20 Sekunden erneut betrachten k\xf6nnen.\n\nDr\xfccken Sie bitte die Leertaste.\n',    font=u'Arial',
    pos=(0, 0), height=30, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "Review_faces1"
Review_faces1Clock = core.Clock()
image_10 = visual.ImageStim(win=win, name='image_10',
    image=u'./stim/Review.jpg', mask=None,
    ori=0, pos=[0,0], size=[570,485],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Review_text2 = visual.TextStim(win=win, ori=0, name='Review_text2',
    text=u'Betrachten Sie noch einmal die Gesichter (20 Sekunden).',    font=u'Arial',
    pos=[0,300], height=20, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-1.0)
Review_text3 = visual.TextStim(win=win, ori=0, name='Review_text3',
    text=u'Im Folgenden wird Ihre Ged\xe4chtnisleistung bez\xfcglich der gezeigten Gesichter getestet.\nIn den verbleibenden Durchg\xe4ngen kann jedes der sechs Gesichter die richtige Antwort sein.\nSchauen Sie sich bitte jedes Gesicht vor der Auswahl einer Antwort an, da die inkorrekten Gesichter den richtigen Gesichtern oft sehr \xe4hneln.\n\nDr\xfccken Sie bitte die Leertaste.',    font=u'Arial',
    pos=(0, 0), height=30, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "erkennen7"
erkennen7Clock = core.Clock()
image_11 = visual.ImageStim(win=win, name='image_11',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[576,288],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
rating_7 = visual.RatingScale(win=win, name='rating_7', marker=u'triangle', size=0.8, pos=[0.0, -250.0], choices=[u'1', u'2', u'3'], tickHeight=0.6,markerColor='black',textColor='black',lineColor='black')
erkennen_7 = visual.TextStim(win=win, ori=0, name='erkennen_7',
    text=u'Test\n\nWelches Gesicht ist eins der sechs gesuchten Gesichter?',    font=u'Arial',
    pos=[0,200], height=20, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "Review_faces1"
Review_faces1Clock = core.Clock()
image_10 = visual.ImageStim(win=win, name='image_10',
    image=u'./stim/Review.jpg', mask=None,
    ori=0, pos=[0,0], size=[570,485],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Review_text2 = visual.TextStim(win=win, ori=0, name='Review_text2',
    text=u'Betrachten Sie noch einmal die Gesichter (20 Sekunden).',    font=u'Arial',
    pos=[0,300], height=20, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-1.0)
Review_text3 = visual.TextStim(win=win, ori=0, name='Review_text3',
    text=u'Im Folgenden wird Ihre Ged\xe4chtnisleistung bez\xfcglich der gezeigten Gesichter getestet.\nIn den verbleibenden Durchg\xe4ngen kann jedes der sechs Gesichter die richtige Antwort sein.\nSchauen Sie sich bitte jedes Gesicht vor der Auswahl einer Antwort an, da die inkorrekten Gesichter den richtigen Gesichtern oft sehr \xe4hneln.\n\nDr\xfccken Sie bitte die Leertaste.',    font=u'Arial',
    pos=(0, 0), height=30, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "erkennen8"
erkennen8Clock = core.Clock()
image_12 = visual.ImageStim(win=win, name='image_12',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[576,288],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
rating_8 = visual.RatingScale(win=win, name='rating_8', marker=u'triangle', size=0.8, pos=[0.0, -250.0], choices=[u'1', u'2', u'3'], tickHeight=0.6,markerColor='black',textColor='black',lineColor='black')
erkennen_8 = visual.TextStim(win=win, ori=0, name='erkennen_8',
    text=u'Test\n\nWelches Gesicht ist eins der sechs gesuchten Gesichter?',    font=u'Arial',
    pos=[0,200], height=20, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "Danke_2"
Danke_2Clock = core.Clock()
Dankee = visual.TextStim(win=win, ori=0, name='Dankee',
    text=u'Die Studie ist hiermit beendet.\n\nBei weiteren Fragen zu der Studie wenden Sie sich bitte an Ihre Versuchsleiterin/Ihren Versuchsleiter oder schreiben eine E-Mail an a.garlichs@uni-bielefeld.de.\n\nVielen Dank f\xfcr Ihre Teilnahme!',    font=u'Arial',
    pos=0, height=30, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "Teilnahme"-------
t = 0
TeilnahmeClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
TeilnahmeComponents = []
TeilnahmeComponents.append(Teilnahme1)
TeilnahmeComponents.append(key_resp_2)
for thisComponent in TeilnahmeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Teilnahme"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = TeilnahmeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Teilnahme1* updates
    if t >= 0.0 and Teilnahme1.status == NOT_STARTED:
        # keep track of start time/frame for later
        Teilnahme1.tStart = t  # underestimates by a little under one frame
        Teilnahme1.frameNStart = frameN  # exact frame index
        Teilnahme1.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TeilnahmeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Teilnahme"-------
for thisComponent in TeilnahmeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
   key_resp_2.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "Teilnahme" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "Uebung"-------
t = 0
UebungClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_4.status = NOT_STARTED
# keep track of which components have finished
UebungComponents = []
UebungComponents.append(Uebung_intro)
UebungComponents.append(key_resp_4)
for thisComponent in UebungComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Uebung"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = UebungClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Uebung_intro* updates
    if t >= 0.0 and Uebung_intro.status == NOT_STARTED:
        # keep track of start time/frame for later
        Uebung_intro.tStart = t  # underestimates by a little under one frame
        Uebung_intro.frameNStart = frameN  # exact frame index
        Uebung_intro.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t  # underestimates by a little under one frame
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_4.keys = theseKeys[-1]  # just the last key pressed
            key_resp_4.rt = key_resp_4.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in UebungComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Uebung"-------
for thisComponent in UebungComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
   key_resp_4.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.nextEntry()
# the Routine "Uebung" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "lernen1"-------
t = 0
lernen1Clock.reset()  # clock 
frameN = -1
routineTimer.add(11.000000)
# update component parameters for each repeat
bart.setImage(u'./stim/bart.L.jpg')
# keep track of which components have finished
lernen1Components = []
lernen1Components.append(bart)
lernen1Components.append(bartM)
lernen1Components.append(bartR)
lernen1Components.append(Uebung1)
lernen1Components.append(Uebung2)
lernen1Components.append(Uebung3)
for thisComponent in lernen1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "lernen1"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = lernen1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *bart* updates
    if t >= 0.0 and bart.status == NOT_STARTED:
        # keep track of start time/frame for later
        bart.tStart = t  # underestimates by a little under one frame
        bart.frameNStart = frameN  # exact frame index
        bart.setAutoDraw(True)
    if bart.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
        bart.setAutoDraw(False)
    
    # *bartM* updates
    if t >= 4 and bartM.status == NOT_STARTED:
        # keep track of start time/frame for later
        bartM.tStart = t  # underestimates by a little under one frame
        bartM.frameNStart = frameN  # exact frame index
        bartM.setAutoDraw(True)
    if bartM.status == STARTED and t >= (4 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
        bartM.setAutoDraw(False)
    
    # *bartR* updates
    if t >= 8 and bartR.status == NOT_STARTED:
        # keep track of start time/frame for later
        bartR.tStart = t  # underestimates by a little under one frame
        bartR.frameNStart = frameN  # exact frame index
        bartR.setAutoDraw(True)
    if bartR.status == STARTED and t >= (8 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
        bartR.setAutoDraw(False)
    
    # *Uebung1* updates
    if t >= 0 and Uebung1.status == NOT_STARTED:
        # keep track of start time/frame for later
        Uebung1.tStart = t  # underestimates by a little under one frame
        Uebung1.frameNStart = frameN  # exact frame index
        Uebung1.setAutoDraw(True)
    if Uebung1.status == STARTED and t >= (0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
        Uebung1.setAutoDraw(False)
    
    # *Uebung2* updates
    if t >= 4 and Uebung2.status == NOT_STARTED:
        # keep track of start time/frame for later
        Uebung2.tStart = t  # underestimates by a little under one frame
        Uebung2.frameNStart = frameN  # exact frame index
        Uebung2.setAutoDraw(True)
    if Uebung2.status == STARTED and t >= (4 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
        Uebung2.setAutoDraw(False)
    
    # *Uebung3* updates
    if t >= 8 and Uebung3.status == NOT_STARTED:
        # keep track of start time/frame for later
        Uebung3.tStart = t  # underestimates by a little under one frame
        Uebung3.frameNStart = frameN  # exact frame index
        Uebung3.setAutoDraw(True)
    if Uebung3.status == STARTED and t >= (8 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
        Uebung3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in lernen1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "lernen1"-------
for thisComponent in lernen1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
bart_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('./arrays/bart_erkennen.csv'),
    seed=None, name='bart_loop')
thisExp.addLoop(bart_loop)  # add the loop to the experiment
thisBart_loop = bart_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisBart_loop.rgb)
if thisBart_loop != None:
    for paramName in thisBart_loop.keys():
        exec(paramName + '= thisBart_loop.' + paramName)

for thisBart_loop in bart_loop:
    currentLoop = bart_loop
    # abbreviate parameter names if possible (e.g. rgb = thisBart_loop.rgb)
    if thisBart_loop != None:
        for paramName in thisBart_loop.keys():
            exec(paramName + '= thisBart_loop.' + paramName)
    
    #------Prepare to start Routine "Bart_erkennen1"-------
    t = 0
    Bart_erkennen1Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    recBart.setImage(pic)
    rating_1.reset()
    # keep track of which components have finished
    Bart_erkennen1Components = []
    Bart_erkennen1Components.append(recBart)
    Bart_erkennen1Components.append(rating_1)
    Bart_erkennen1Components.append(welches1)
    for thisComponent in Bart_erkennen1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Bart_erkennen1"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = Bart_erkennen1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *recBart* updates
        if t >= 1 and recBart.status == NOT_STARTED:
            # keep track of start time/frame for later
            recBart.tStart = t  # underestimates by a little under one frame
            recBart.frameNStart = frameN  # exact frame index
            recBart.setAutoDraw(True)
        # *rating_1* updates
        if t >= 1 and rating_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_1.tStart = t  # underestimates by a little under one frame
            rating_1.frameNStart = frameN  # exact frame index
            rating_1.setAutoDraw(True)
        continueRoutine &= rating_1.noResponse  # a response ends the trial
        
        # *welches1* updates
        if t >= 1 and welches1.status == NOT_STARTED:
            # keep track of start time/frame for later
            welches1.tStart = t  # underestimates by a little under one frame
            welches1.frameNStart = frameN  # exact frame index
            welches1.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Bart_erkennen1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Bart_erkennen1"-------
    for thisComponent in Bart_erkennen1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for bart_loop (TrialHandler)
    bart_loop.addData('rating_1.response', rating_1.getRating())
    bart_loop.addData('rating_1.rt', rating_1.getRT())
    # the Routine "Bart_erkennen1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'bart_loop'


#------Prepare to start Routine "Memorize"-------
t = 0
MemorizeClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_3.status = NOT_STARTED
# keep track of which components have finished
MemorizeComponents = []
MemorizeComponents.append(Memorizing)
MemorizeComponents.append(key_resp_3)
for thisComponent in MemorizeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Memorize"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = MemorizeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Memorizing* updates
    if t >= 0.0 and Memorizing.status == NOT_STARTED:
        # keep track of start time/frame for later
        Memorizing.tStart = t  # underestimates by a little under one frame
        Memorizing.frameNStart = frameN  # exact frame index
        Memorizing.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t  # underestimates by a little under one frame
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_3.keys = theseKeys[-1]  # just the last key pressed
            key_resp_3.rt = key_resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MemorizeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Memorize"-------
for thisComponent in MemorizeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
   key_resp_3.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "Memorize" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('./arrays/single_recall.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "lernen2"-------
    t = 0
    lernen2Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(12.000000)
    # update component parameters for each repeat
    image_3.setImage(learn1)
    image_5.setImage(learn2)
    image_6.setImage(learn3)
    # keep track of which components have finished
    lernen2Components = []
    lernen2Components.append(image_3)
    lernen2Components.append(image_5)
    lernen2Components.append(image_6)
    lernen2Components.append(merken1)
    lernen2Components.append(merken2)
    lernen2Components.append(merken3)
    for thisComponent in lernen2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "lernen2"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = lernen2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_3* updates
        if t >= 1 and image_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_3.tStart = t  # underestimates by a little under one frame
            image_3.frameNStart = frameN  # exact frame index
            image_3.setAutoDraw(True)
        if image_3.status == STARTED and t >= (1 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_3.setAutoDraw(False)
        
        # *image_5* updates
        if t >= 5 and image_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_5.tStart = t  # underestimates by a little under one frame
            image_5.frameNStart = frameN  # exact frame index
            image_5.setAutoDraw(True)
        if image_5.status == STARTED and t >= (5 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_5.setAutoDraw(False)
        
        # *image_6* updates
        if t >= 9 and image_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_6.tStart = t  # underestimates by a little under one frame
            image_6.frameNStart = frameN  # exact frame index
            image_6.setAutoDraw(True)
        if image_6.status == STARTED and t >= (9 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_6.setAutoDraw(False)
        
        # *merken1* updates
        if t >= 1 and merken1.status == NOT_STARTED:
            # keep track of start time/frame for later
            merken1.tStart = t  # underestimates by a little under one frame
            merken1.frameNStart = frameN  # exact frame index
            merken1.setAutoDraw(True)
        if merken1.status == STARTED and t >= (1 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            merken1.setAutoDraw(False)
        
        # *merken2* updates
        if t >= 5 and merken2.status == NOT_STARTED:
            # keep track of start time/frame for later
            merken2.tStart = t  # underestimates by a little under one frame
            merken2.frameNStart = frameN  # exact frame index
            merken2.setAutoDraw(True)
        if merken2.status == STARTED and t >= (5 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            merken2.setAutoDraw(False)
        
        # *merken3* updates
        if t >= 9 and merken3.status == NOT_STARTED:
            # keep track of start time/frame for later
            merken3.tStart = t  # underestimates by a little under one frame
            merken3.frameNStart = frameN  # exact frame index
            merken3.setAutoDraw(True)
        if merken3.status == STARTED and t >= (9 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            merken3.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in lernen2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "lernen2"-------
    for thisComponent in lernen2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "erkennen4"-------
    t = 0
    erkennen4Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    image_7.setImage(recall1)
    rating_4.reset()
    # keep track of which components have finished
    erkennen4Components = []
    erkennen4Components.append(image_7)
    erkennen4Components.append(rating_4)
    erkennen4Components.append(welches4)
    for thisComponent in erkennen4Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "erkennen4"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = erkennen4Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_7* updates
        if t >= 1 and image_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_7.tStart = t  # underestimates by a little under one frame
            image_7.frameNStart = frameN  # exact frame index
            image_7.setAutoDraw(True)
        # *rating_4* updates
        if t >= 1 and rating_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_4.tStart = t  # underestimates by a little under one frame
            rating_4.frameNStart = frameN  # exact frame index
            rating_4.setAutoDraw(True)
        continueRoutine &= rating_4.noResponse  # a response ends the trial
        
        # *welches4* updates
        if t >= 1 and welches4.status == NOT_STARTED:
            # keep track of start time/frame for later
            welches4.tStart = t  # underestimates by a little under one frame
            welches4.frameNStart = frameN  # exact frame index
            welches4.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in erkennen4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "erkennen4"-------
    for thisComponent in erkennen4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    trials.addData('rating_4.response', rating_4.getRating())
    trials.addData('rating_4.rt', rating_4.getRT())
    # the Routine "erkennen4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "erkennen5"-------
    t = 0
    erkennen5Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    image_8.setImage(recall2)
    rating_5.reset()
    # keep track of which components have finished
    erkennen5Components = []
    erkennen5Components.append(image_8)
    erkennen5Components.append(rating_5)
    erkennen5Components.append(welches5)
    for thisComponent in erkennen5Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "erkennen5"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = erkennen5Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_8* updates
        if t >= 1 and image_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_8.tStart = t  # underestimates by a little under one frame
            image_8.frameNStart = frameN  # exact frame index
            image_8.setAutoDraw(True)
        # *rating_5* updates
        if t >= 1 and rating_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_5.tStart = t  # underestimates by a little under one frame
            rating_5.frameNStart = frameN  # exact frame index
            rating_5.setAutoDraw(True)
        continueRoutine &= rating_5.noResponse  # a response ends the trial
        
        # *welches5* updates
        if t >= 1 and welches5.status == NOT_STARTED:
            # keep track of start time/frame for later
            welches5.tStart = t  # underestimates by a little under one frame
            welches5.frameNStart = frameN  # exact frame index
            welches5.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in erkennen5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "erkennen5"-------
    for thisComponent in erkennen5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    trials.addData('rating_5.response', rating_5.getRating())
    trials.addData('rating_5.rt', rating_5.getRT())
    # the Routine "erkennen5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "erkennen6"-------
    t = 0
    erkennen6Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    image_9.setImage(recall3)
    rating_6.reset()
    # keep track of which components have finished
    erkennen6Components = []
    erkennen6Components.append(image_9)
    erkennen6Components.append(rating_6)
    erkennen6Components.append(welches6)
    for thisComponent in erkennen6Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "erkennen6"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = erkennen6Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_9* updates
        if t >= 1 and image_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_9.tStart = t  # underestimates by a little under one frame
            image_9.frameNStart = frameN  # exact frame index
            image_9.setAutoDraw(True)
        # *rating_6* updates
        if t >= 1 and rating_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_6.tStart = t  # underestimates by a little under one frame
            rating_6.frameNStart = frameN  # exact frame index
            rating_6.setAutoDraw(True)
        continueRoutine &= rating_6.noResponse  # a response ends the trial
        
        # *welches6* updates
        if t >= 1 and welches6.status == NOT_STARTED:
            # keep track of start time/frame for later
            welches6.tStart = t  # underestimates by a little under one frame
            welches6.frameNStart = frameN  # exact frame index
            welches6.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in erkennen6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "erkennen6"-------
    for thisComponent in erkennen6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    trials.addData('rating_6.response', rating_6.getRating())
    trials.addData('rating_6.rt', rating_6.getRT())
    # the Routine "erkennen6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


#------Prepare to start Routine "Review1"-------
t = 0
Review1Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_5.status = NOT_STARTED
# keep track of which components have finished
Review1Components = []
Review1Components.append(Review_text)
Review1Components.append(key_resp_5)
for thisComponent in Review1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Review1"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Review1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Review_text* updates
    if t >= 1 and Review_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        Review_text.tStart = t  # underestimates by a little under one frame
        Review_text.frameNStart = frameN  # exact frame index
        Review_text.setAutoDraw(True)
    
    # *key_resp_5* updates
    if t >= 1 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t  # underestimates by a little under one frame
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_5.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_5.keys = theseKeys[-1]  # just the last key pressed
            key_resp_5.rt = key_resp_5.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Review1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Review1"-------
for thisComponent in Review1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
   key_resp_5.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.nextEntry()
# the Routine "Review1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "Review_faces1"-------
t = 0
Review_faces1Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_6 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_6.status = NOT_STARTED
# keep track of which components have finished
Review_faces1Components = []
Review_faces1Components.append(image_10)
Review_faces1Components.append(Review_text2)
Review_faces1Components.append(Review_text3)
Review_faces1Components.append(key_resp_6)
for thisComponent in Review_faces1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Review_faces1"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Review_faces1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_10* updates
    if t >= 1 and image_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_10.tStart = t  # underestimates by a little under one frame
        image_10.frameNStart = frameN  # exact frame index
        image_10.setAutoDraw(True)
    if image_10.status == STARTED and t >= (1 + (20-win.monitorFramePeriod*0.75)): #most of one frame period left
        image_10.setAutoDraw(False)
    
    # *Review_text2* updates
    if t >= 1 and Review_text2.status == NOT_STARTED:
        # keep track of start time/frame for later
        Review_text2.tStart = t  # underestimates by a little under one frame
        Review_text2.frameNStart = frameN  # exact frame index
        Review_text2.setAutoDraw(True)
    if Review_text2.status == STARTED and t >= (1 + (20-win.monitorFramePeriod*0.75)): #most of one frame period left
        Review_text2.setAutoDraw(False)
    
    # *Review_text3* updates
    if t >= 21 and Review_text3.status == NOT_STARTED:
        # keep track of start time/frame for later
        Review_text3.tStart = t  # underestimates by a little under one frame
        Review_text3.frameNStart = frameN  # exact frame index
        Review_text3.setAutoDraw(True)
    
    # *key_resp_6* updates
    if t >= 21 and key_resp_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_6.tStart = t  # underestimates by a little under one frame
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_6.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_6.keys = theseKeys[-1]  # just the last key pressed
            key_resp_6.rt = key_resp_6.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Review_faces1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Review_faces1"-------
for thisComponent in Review_faces1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
   key_resp_6.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.nextEntry()
# the Routine "Review_faces1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('./arrays/novel.csv'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2.keys():
        exec(paramName + '= thisTrial_2.' + paramName)

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2.keys():
            exec(paramName + '= thisTrial_2.' + paramName)
    
    #------Prepare to start Routine "erkennen7"-------
    t = 0
    erkennen7Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    image_11.setImage(pic)
    rating_7.reset()
    # keep track of which components have finished
    erkennen7Components = []
    erkennen7Components.append(image_11)
    erkennen7Components.append(rating_7)
    erkennen7Components.append(erkennen_7)
    for thisComponent in erkennen7Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "erkennen7"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = erkennen7Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_11* updates
        if t >= 1 and image_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_11.tStart = t  # underestimates by a little under one frame
            image_11.frameNStart = frameN  # exact frame index
            image_11.setAutoDraw(True)
        # *rating_7* updates
        if t >= 1 and rating_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_7.tStart = t  # underestimates by a little under one frame
            rating_7.frameNStart = frameN  # exact frame index
            rating_7.setAutoDraw(True)
        continueRoutine &= rating_7.noResponse  # a response ends the trial
        
        # *erkennen_7* updates
        if t >= 1 and erkennen_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            erkennen_7.tStart = t  # underestimates by a little under one frame
            erkennen_7.frameNStart = frameN  # exact frame index
            erkennen_7.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in erkennen7Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "erkennen7"-------
    for thisComponent in erkennen7Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('rating_7.response', rating_7.getRating())
    trials_2.addData('rating_7.rt', rating_7.getRT())
    # the Routine "erkennen7" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'


#------Prepare to start Routine "Review_faces1"-------
t = 0
Review_faces1Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_6 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_6.status = NOT_STARTED
# keep track of which components have finished
Review_faces1Components = []
Review_faces1Components.append(image_10)
Review_faces1Components.append(Review_text2)
Review_faces1Components.append(Review_text3)
Review_faces1Components.append(key_resp_6)
for thisComponent in Review_faces1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Review_faces1"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Review_faces1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_10* updates
    if t >= 1 and image_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_10.tStart = t  # underestimates by a little under one frame
        image_10.frameNStart = frameN  # exact frame index
        image_10.setAutoDraw(True)
    if image_10.status == STARTED and t >= (1 + (20-win.monitorFramePeriod*0.75)): #most of one frame period left
        image_10.setAutoDraw(False)
    
    # *Review_text2* updates
    if t >= 1 and Review_text2.status == NOT_STARTED:
        # keep track of start time/frame for later
        Review_text2.tStart = t  # underestimates by a little under one frame
        Review_text2.frameNStart = frameN  # exact frame index
        Review_text2.setAutoDraw(True)
    if Review_text2.status == STARTED and t >= (1 + (20-win.monitorFramePeriod*0.75)): #most of one frame period left
        Review_text2.setAutoDraw(False)
    
    # *Review_text3* updates
    if t >= 21 and Review_text3.status == NOT_STARTED:
        # keep track of start time/frame for later
        Review_text3.tStart = t  # underestimates by a little under one frame
        Review_text3.frameNStart = frameN  # exact frame index
        Review_text3.setAutoDraw(True)
    
    # *key_resp_6* updates
    if t >= 21 and key_resp_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_6.tStart = t  # underestimates by a little under one frame
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_6.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_6.keys = theseKeys[-1]  # just the last key pressed
            key_resp_6.rt = key_resp_6.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Review_faces1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Review_faces1"-------
for thisComponent in Review_faces1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
   key_resp_6.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.nextEntry()
# the Routine "Review_faces1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('./arrays/noise.csv'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3.keys():
        exec(paramName + '= thisTrial_3.' + paramName)

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3.keys():
            exec(paramName + '= thisTrial_3.' + paramName)
    
    #------Prepare to start Routine "erkennen8"-------
    t = 0
    erkennen8Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    image_12.setImage(pic)
    rating_8.reset()
    # keep track of which components have finished
    erkennen8Components = []
    erkennen8Components.append(image_12)
    erkennen8Components.append(rating_8)
    erkennen8Components.append(erkennen_8)
    for thisComponent in erkennen8Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "erkennen8"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = erkennen8Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_12* updates
        if t >= 1 and image_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_12.tStart = t  # underestimates by a little under one frame
            image_12.frameNStart = frameN  # exact frame index
            image_12.setAutoDraw(True)
        # *rating_8* updates
        if t >= 1 and rating_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_8.tStart = t  # underestimates by a little under one frame
            rating_8.frameNStart = frameN  # exact frame index
            rating_8.setAutoDraw(True)
        continueRoutine &= rating_8.noResponse  # a response ends the trial
        
        # *erkennen_8* updates
        if t >= 1 and erkennen_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            erkennen_8.tStart = t  # underestimates by a little under one frame
            erkennen_8.frameNStart = frameN  # exact frame index
            erkennen_8.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in erkennen8Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "erkennen8"-------
    for thisComponent in erkennen8Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_3 (TrialHandler)
    trials_3.addData('rating_8.response', rating_8.getRating())
    trials_3.addData('rating_8.rt', rating_8.getRT())
    # the Routine "erkennen8" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_3'


#------Prepare to start Routine "Danke_2"-------
t = 0
Danke_2Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_7 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_7.status = NOT_STARTED
# keep track of which components have finished
Danke_2Components = []
Danke_2Components.append(Dankee)
Danke_2Components.append(key_resp_7)
for thisComponent in Danke_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Danke_2"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Danke_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Dankee* updates
    if t >= 1 and Dankee.status == NOT_STARTED:
        # keep track of start time/frame for later
        Dankee.tStart = t  # underestimates by a little under one frame
        Dankee.frameNStart = frameN  # exact frame index
        Dankee.setAutoDraw(True)
    
    # *key_resp_7* updates
    if t >= 1 and key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_7.tStart = t  # underestimates by a little under one frame
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_7.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_7.keys = theseKeys[-1]  # just the last key pressed
            key_resp_7.rt = key_resp_7.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Danke_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Danke_2"-------
for thisComponent in Danke_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
   key_resp_7.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.nextEntry()
# the Routine "Danke_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort() # or data files will save again on exit
win.close()
core.quit()

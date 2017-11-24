#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.04), Mon 21 Nov 2016 07:20:34 PM CET
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
expName ='famFaceGrey'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

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
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='pix')
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "trial"
trialClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
text = visual.TextStim(win=win, ori=0, name='text',
    text=u'Vielen Dank für Ihre Teilnahme an dieser Studie.\n\nIm Folgenden werden Ihnen Gesichter von verschiedenen berühmten Persönlichkeiten gezeigt. Bitte beantworten Sie die angegebenen Fragen zu jeder Person gründlich, aber zügig.\n\nSie werden zu jedem Bild gefragt werden, ob Sie die Person an sich, Ihren Beruf und Ihren Namen kennen. Um Ihre Antwort einzugeben, klicken Sie bitte die passende Option entweder mit der Maus an oder drücken die entsprechende Nummer Ihrer Antwort auf der Tastatur. Den Namen einer Person tippen Sie bitte mit Hilfe der Tastatur ein.\n\nFalls Sie die Frage nach dem Beruf einer Person nicht beantworten können, wählen Sie bitte den Beruf aus, der Ihnen am wahrscheinlichsten erscheint, und machen weiter. Wenn Sie den Namen einer Person nicht kennen, können Sie auch z.B. den Namen ihres Charakters in einer Fernsehserie/einem Film, in dem sie mitgespielt hat, nennen. Falls Sie über keinerlei Information zu dem Namen einer Person verfügen, können Sie das Feld leer lassen und ENTER drücken, um zum nächsten Bild zu gelangen.\n\nBitte beachten Sie, dass die gleiche Person mehrfach in dem Experiment vorkommen kann.\n\nBei Fragen zum Experiment wenden Sie sich bitte jetzt an Ihre/n Versuchsleiter/in. Falls Sie nach der Studie noch offene Fragen haben, kontaktieren Sie bitte @uni-bielefeld.de.\n\nUm mit dem Experiment zu beginnen, drücken Sie bitte die LEERTASTE.',
    font='Arial',
    pos=[0, 0], height=25, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
text.wrapWidth=1000;
# Initialize components for Routine "bekannt"
bekanntClock = core.Clock()
imageBekannt = visual.ImageStim(win=win, name='imageBekannt',
    image='sin', mask=None,
    ori=0, pos=[0, 100], size=[300, 300],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
ratingBekannt = visual.RatingScale(win=win, name='ratingBekannt', marker=u'hover', size=1.0, pos=[0.0, -200.0], choices=[u'1.ja', u'2.nein'], tickHeight=-1, singleClick=True, showAccept=False)
text_6 = visual.TextStim(win=win, ori=0, name='text_6',
    text=u'Bekannt?',    font=u'Arial',
    pos=[0, -100], height=50, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "kontext"
kontextClock = core.Clock()
image_3 = visual.ImageStim(win=win, name='image_3',
    image='sin', mask=None,
    ori=0, pos=[0, 100], size=[300,300],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

ratingK1 = visual.RatingScale(win=win, name='ratingK1', marker=u'hover', size=0.6, pos=[0.0, -200.0], choices=[u' ',u'1. SchauspielerIn',u' '], tickHeight=-1, singleClick=True, showAccept=False)
ratingK2 = visual.RatingScale(win=win, name='ratingK2', marker=u'hover', size=0.6, pos=[0.0, -300.0], choices=[u'2. MusikerIn',u'3. ModeratorIn'], tickHeight=-1, singleClick=True, showAccept=False)
ratingK3 = visual.RatingScale(win=win, name='ratingK3', marker=u'hover', size=0.6, pos=[0.0, -400.0], choices=[u'4. PolitikerIn',u'5. SportlerIn'], tickHeight=-1)

text_4 = visual.TextStim(win=win, ori=0, name='text_4',
    text=u'Beruf/Kontext?',    font=u'Arial',
    pos=[0, -100], height=50, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-3.0)

# Initialize components for Routine "pName"
pNameClock = core.Clock()
inputText = ""
text_5 = visual.TextStim(win=win, ori=0, name='text_5',
    text='default text',    font=u'Arial',
    pos=[-200, -200], height=50, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0)
image_2 = visual.ImageStim(win=win, name='image_2',
    image='sin', mask=None,
    ori=0, pos=[0, 100], size=[300,300],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "end"
endClock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text=u'Dieser Teil des Experiments ist nun zu Ende.\nVielen Dank.',    font=u'Arial',
    pos=[0, 0], height=50, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

#------Prepare to start Routine "trial"-------
t = 0
trialClock.reset()  # clock
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
trialComponents = []
trialComponents.append(ISI)
trialComponents.append(text)
trialComponents.append(key_resp_2)
for thisComponent in trialComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "trial"-------

# ugly hack: the labels need to be renamed as the "umlaute" cannot be saved to csv
ratingK1.choices = ['dummy','act','dummy']
ratingK2.choices = ['music','host']
ratingK3.choices = ['polit','sport']

continueRoutine = True
while continueRoutine:
    # get current time
    t = trialClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)

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
    # *ISI* period
    if t >= 0.0 and ISI.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI.tStart = t  # underestimates by a little under one frame
        ISI.frameNStart = frameN  # exact frame index
        ISI.start(0.5)
    elif ISI.status == STARTED: #one frame should pass before updating params and completing
        ISI.complete() #finish the static period

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "trial"-------
for thisComponent in trialComponents:
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
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'greyInnerList.csv'),
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

    #------Prepare to start Routine "bekannt"-------
    t = 0
    bekanntClock.reset()  # clock
    frameN = -1
    # update component parameters for each repeat
    imageBekannt.setImage(pic)
    ratingBekannt.reset()
    key_resp_5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_5.status = NOT_STARTED
    # keep track of which components have finished
    bekanntComponents = []
    bekanntComponents.append(imageBekannt)
    bekanntComponents.append(ratingBekannt)
    bekanntComponents.append(text_6)
    bekanntComponents.append(key_resp_5)
    for thisComponent in bekanntComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "bekannt"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = bekanntClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *imageBekannt* updates
        if t >= 0.0 and imageBekannt.status == NOT_STARTED:
            # keep track of start time/frame for later
            imageBekannt.tStart = t  # underestimates by a little under one frame
            imageBekannt.frameNStart = frameN  # exact frame index
            imageBekannt.setAutoDraw(True)
        # *ratingBekannt* updates
        if t >= 0.0 and ratingBekannt.status == NOT_STARTED:
            # keep track of start time/frame for later
            ratingBekannt.tStart = t  # underestimates by a little under one frame
            ratingBekannt.frameNStart = frameN  # exact frame index
            ratingBekannt.setAutoDraw(True)
        continueRoutine &= ratingBekannt.noResponse  # a response ends the trial

        # *text_6* updates
        if t >= 0.0 and text_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_6.tStart = t  # underestimates by a little under one frame
            text_6.frameNStart = frameN  # exact frame index
            text_6.setAutoDraw(True)

        # *key_resp_5* updates
        if t >= 0.0 and key_resp_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_5.tStart = t  # underestimates by a little under one frame
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_5.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2'])

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
        for thisComponent in bekanntComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "bekannt"-------
    for thisComponent in bekanntComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    trials.addData('ratingBekannt.response', ratingBekannt.getRating())
    trials.addData('ratingBekannt.rt', ratingBekannt.getRT())
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
       key_resp_5.keys=None
    # store data for trials (TrialHandler)
    trials.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        trials.addData('key_resp_5.rt', key_resp_5.rt)
    # the Routine "bekannt" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    #------Prepare to start Routine "kontext"-------
    t = 0
    kontextClock.reset()  # clock
    frameN = -1
    # update component parameters for each repeat
    image_3.setImage(pic)
    ratingK1.reset()
    ratingK2.reset()
    ratingK3.reset()
    key_resp_6 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_6.status = NOT_STARTED
    # keep track of which components have finished
    kontextComponents = []
    kontextComponents.append(image_3)
    kontextComponents.append(ratingK1)
    kontextComponents.append(ratingK2)
    kontextComponents.append(ratingK3)
    kontextComponents.append(text_4)
    kontextComponents.append(key_resp_6)
    for thisComponent in kontextComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "kontext"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = kontextClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *image_3* updates
        if t >= 0.0 and image_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_3.tStart = t  # underestimates by a little under one frame
            image_3.frameNStart = frameN  # exact frame index
            image_3.setAutoDraw(True)
        # *ratingK1* updates
        if t >= 0.0 and ratingK1.status == NOT_STARTED:
            # keep track of start time/frame for later
            ratingK1.tStart = t  # underestimates by a little under one frame
            ratingK1.frameNStart = frameN  # exact frame index
            ratingK1.setAutoDraw(True)
        continueRoutine &= ratingK1.noResponse  # a response ends the trial
        # *ratingK2* updates
        if t >= 0.0 and ratingK2.status == NOT_STARTED:
            # keep track of start time/frame for later
            ratingK2.tStart = t  # underestimates by a little under one frame
            ratingK2.frameNStart = frameN  # exact frame index
            ratingK2.setAutoDraw(True)
        continueRoutine &= ratingK2.noResponse  # a response ends the trial
        # *ratingK3* updates
        if t >= 0.0 and ratingK3.status == NOT_STARTED:
            # keep track of start time/frame for later
            ratingK3.tStart = t  # underestimates by a little under one frame
            ratingK3.frameNStart = frameN  # exact frame index
            ratingK3.setAutoDraw(True)
        continueRoutine &= ratingK3.noResponse  # a response ends the trial
        # *text_4* updates
        if t >= 0.0 and text_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_4.tStart = t  # underestimates by a little under one frame
            text_4.frameNStart = frameN  # exact frame index
            text_4.setAutoDraw(True)

        # *key_resp_6* updates
        if t >= 0.0 and key_resp_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_6.tStart = t  # underestimates by a little under one frame
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_6.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5'])

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
        for thisComponent in kontextComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "kontext"-------
    for thisComponent in kontextComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    trials.addData('ratingK1.response', ratingK1.getRating())
    trials.addData('ratingK1.rt', ratingK1.getRT())
    # store data for trials (TrialHandler)
    trials.addData('ratingK2.response', ratingK2.getRating())
    trials.addData('ratingK2.rt', ratingK2.getRT())
    # store data for trials (TrialHandler)
    trials.addData('ratingK3.response', ratingK3.getRating())
    trials.addData('ratingK3.rt', ratingK3.getRT())
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
       key_resp_6.keys=None
    # store data for trials (TrialHandler)
    trials.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        trials.addData('key_resp_6.rt', key_resp_6.rt)

    # the Routine "kontext" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    #------Prepare to start Routine "pName"-------
    t = 0
    pNameClock.reset()  # clock
    frameN = -1
    # update component parameters for each repeat
    theseKeys=""
    shift_flag = False
    text_5.alignHoriz ='left'
    key_resp_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_4.status = NOT_STARTED
    image_2.setImage(pic)
    # keep track of which components have finished
    pNameComponents = []
    pNameComponents.append(text_5)
    pNameComponents.append(key_resp_4)
    pNameComponents.append(image_2)
    for thisComponent in pNameComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "pName"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = pNameClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        n= len(theseKeys)
        i = 0
        while i < n:

            if theseKeys[i] == 'return':
                # pressing RETURN means time to stop
                continueRoutine = False
                break

            elif theseKeys[i] == 'backspace':
                inputText = inputText[:-1]  # lose the final character
                i = i + 1

            elif theseKeys[i] == 'space':
                inputText += ' '
                i = i + 1

            elif theseKeys[i] in ['lshift', 'rshift']:
                shift_flag = True
                i = i + 1

            else:
                if len(theseKeys[i]) == 1:
                    # we only have 1 char so should be a normal key,
                    # otherwise it might be 'ctrl' or similar so ignore it
                    if shift_flag:
                        try:
                            inputText += chr( ord(theseKeys[i]) - ord(' '))
                            shift_flag = False
                        except:
                            inputText += ''
                            shift_flag = False
                    else:
                        try:
                            inputText += theseKeys[i]
                        except:
                            inputText += ''

                i = i + 1




        # *text_5* updates
        if t >= 0.0 and text_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_5.tStart = t  # underestimates by a little under one frame
            text_5.frameNStart = frameN  # exact frame index
            text_5.setAutoDraw(True)
        if text_5.status == STARTED:  # only update if being drawn
            try:
                text_5.setText('Name?\n\n' + inputText, log=False)
            except:
                inputText = '!'
                text_5.setText('Name?\n\n' + inputText, log=False)

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
            theseKeys = event.getKeys()

            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_4.keys.extend(theseKeys)  # storing all keys
                key_resp_4.rt.append(key_resp_4.clock.getTime())

        # *image_2* updates
        if t >= 0.0 and image_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_2.tStart = t  # underestimates by a little under one frame
            image_2.frameNStart = frameN  # exact frame index
            image_2.setAutoDraw(True)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pNameComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "pName"-------
    for thisComponent in pNameComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # let's store the final text string into the results finle...
    thisExp.addData('inputText', inputText)
    inputText=""
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
       key_resp_4.keys=None
    # store data for trials (TrialHandler)
    trials.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        trials.addData('key_resp_4.rt', key_resp_4.rt)
    # the Routine "pName" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()

# completed 1 repeats of 'trials'

#------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock
frameN = -1
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = []
endComponents.append(text_2)
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "end"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    if text_2.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
        text_2.setAutoDraw(False)

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort() # or data files will save again on exit
win.close()
core.quit()

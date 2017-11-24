#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'facesParametric'  # from the Builder filename that created this script
expInfo = {u'participant': u'', u'group': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Check whether the chosen participant number is valid
myDlg = gui.Dlg(title="FEHLER")
myDlg.addText(u'Vp-Nnummer zwischen 1 und 100 eingeben')
assert len(str(expInfo['participant'])) > 0, myDlg.show()
try:
    assert int(expInfo['participant']) in range(1,101), myDlg.show()
except:
    myDlg.show()

# Check whether a group membership has been defined
myDlg = gui.Dlg(title="FEHLER")
myDlg.addText(u' Gruppenzugehoerigkeit angeben')
assert len(str(expInfo['group'])) > 0, myDlg.show()

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s_%s' %(expInfo['group'],expInfo['participant'], expName, expInfo['date'])

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
win = visual.Window(size=[1280, 1024], fullscr=True, screen=0, allowGUI=True, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='cm')
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess


################################ BASIC EMOZ ##


# Initialize components for Routine "basicInstruct"
basicInstructClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text=u"Im nachfolgenden Experiment werden Sie nacheinander einzelne Gesichter sehen.\n\nSie m\xfcssen jeweils entscheiden, welchen Ausdruck das gezeigte Gesicht hat.\n\nZur Auswahl stehene Ihnen hierbei die folgenden M\xf6glichkeiten:\nFreude\nAngst\n\xc4rger\nTrauer\nEkel\n\xdcberraschung\nNeutral\n\nEntscheiden Sie sich bei jedem gezeigten Gesicht f\xfcr einen der \nm\xf6glichen Gesichtsausdr\xfccke.",    font='Arial',
    pos=[0, 0], height=0.8, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "basicTrial"
basicTrialClock = core.Clock()
basicImage = visual.ImageStim(win=win, name='basicImage',
    image='sin', mask=None,
    ori=0, pos=[0, 1], size=[10.12,13.72],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

basicRating1 = visual.RatingScale(win=win, name='basicRating1', marker=u'hover', size=0.6, pos=[0.0, -0.5], choices=[u'Freude', u'Trauer'], tickHeight=-1, disappear=True)
basicRating2 = visual.RatingScale(win=win, name='basicRating2', marker=u'hover', size=0.6, pos=[0.0, -0.6], choices=[u'Angst', u'\xc4rger'], tickHeight=-1, singleClick=True, disappear=True)
basicRating3 = visual.RatingScale(win=win, name='basicRating3', marker=u'hover', size=0.6, pos=[0.0, -0.7], choices=[u'Ekel', u'\xdcberraschung'], tickHeight=-1, singleClick=True, disappear=True)
basicRating4 = visual.RatingScale(win=win, name='basicRating4', marker=u'hover', size=0.6, pos=[0.0, -0.8], choices=[u' ',u'Neutral', u' '], tickHeight=-1, singleClick=True, disappear=True)

# Initialize components for Routine "basicWait"
basicWaitClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

# Initialize components for Routine "basicEnd"
basicEndClock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text=u'Danke. Das Experiment ist nun zu Ende.',    font=u'Arial',
    pos=[0, 0], height=1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
    
    
    
    
###############################################################################


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 


#############################################



#------Prepare to start Routine "basicInstruct"-------
t = 0
basicInstructClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
basicInstructComponents = []
basicInstructComponents.append(text)
basicInstructComponents.append(key_resp_2)
for thisComponent in basicInstructComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "basicInstruct"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = basicInstructClock.getTime()
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
        key_resp_2.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
        
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
    for thisComponent in basicInstructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "basicInstruct"-------
for thisComponent in basicInstructComponents:
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
# the Routine "basicInstruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
basicLoop = data.TrialHandler(nReps=1, method='fullRandom', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('./arrays/imgList.csv'),
    seed=None, name='basicLoop')
thisExp.addLoop(basicLoop)  # add the loop to the experiment
thisBasicLoop = basicLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisBasicLoop.rgb)
if thisBasicLoop != None:
    for paramName in thisBasicLoop.keys():
        exec(paramName + '= thisBasicLoop.' + paramName)

for thisBasicLoop in basicLoop:
    currentLoop = basicLoop
    # abbreviate parameter names if possible (e.g. rgb = thisBasicLoop.rgb)
    if thisBasicLoop != None:
        for paramName in thisBasicLoop.keys():
            exec(paramName + '= thisBasicLoop.' + paramName)
    
    #------Prepare to start Routine "basicTrial"-------
    
    
    ###########
    # resetting the rating scales each time, so that the last response isnt visible
    
    basicRating1 = visual.RatingScale(win=win, name='basicRating1', marker=u'hover', size=0.6, pos=[0.0, -0.5], choices=[u'Freude', u'Trauer'], tickHeight=-1, disappear=True)
    basicRating2 = visual.RatingScale(win=win, name='basicRating2', marker=u'hover', size=0.6, pos=[0.0, -0.6], choices=[u'Angst', u'\xc4rger'], tickHeight=-1, singleClick=True, disappear=True)
    basicRating3 = visual.RatingScale(win=win, name='basicRating3', marker=u'hover', size=0.6, pos=[0.0, -0.7], choices=[u'Ekel', u'\xdcberraschung'], tickHeight=-1, singleClick=True, disappear=True)
    basicRating4 = visual.RatingScale(win=win, name='basicRating4', marker=u'hover', size=0.6, pos=[0.0, -0.8], choices=[u' ',u'Neutral', u' '], tickHeight=-1, singleClick=True, disappear=True)

    ###########
    
    t = 0
    basicTrialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    basicImage.setImage(img)
    basicRating1.reset()
    basicRating2.reset()
    basicRating3.reset()
    basicRating4.reset()
    # keep track of which components have finished
    basicTrialComponents = []
    basicTrialComponents.append(basicImage)
    basicTrialComponents.append(basicRating1)
    basicTrialComponents.append(basicRating2)
    basicTrialComponents.append(basicRating3)
    basicTrialComponents.append(basicRating4)
    for thisComponent in basicTrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    
    # ugly hack: the labels need to be renamed as the "umlaute" cannot be saved to csv 
    basicRating1.choices = ['HAP', 'SAD']
    basicRating2.choices = ['FEA', 'ANG']
    basicRating3.choices = ['DIS', 'SUP']
    basicRating4.choices = ['dummy','NTR', 'dummy']
    #-------Start Routine "basicTrial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = basicTrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *basicImage* updates
        if t >= 0 and basicImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            basicImage.tStart = t  # underestimates by a little under one frame
            basicImage.frameNStart = frameN  # exact frame index
            basicImage.setAutoDraw(True)
        if basicImage.status == STARTED and t >= (0 + (4.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            basicImage.setAutoDraw(False)
        # *basicRating1* updates
        if t >= 0.5 and basicRating1.status == NOT_STARTED:
            # keep track of start time/frame for later
            basicRating1.tStart = t  # underestimates by a little under one frame
            basicRating1.frameNStart = frameN  # exact frame index
            basicRating1.setAutoDraw(True)
        continueRoutine &= basicRating1.noResponse  # a response ends the trial
        # *basicRating2* updates
        if t >= 0.5 and basicRating2.status == NOT_STARTED:
            # keep track of start time/frame for later
            basicRating2.tStart = t  # underestimates by a little under one frame
            basicRating2.frameNStart = frameN  # exact frame index
            basicRating2.setAutoDraw(True)
        continueRoutine &= basicRating2.noResponse  # a response ends the trial
        # *basicRating3* updates
        if t >= 0.5 and basicRating3.status == NOT_STARTED:
            # keep track of start time/frame for later
            basicRating3.tStart = t  # underestimates by a little under one frame
            basicRating3.frameNStart = frameN  # exact frame index
            basicRating3.setAutoDraw(True)
        continueRoutine &= basicRating3.noResponse  # a response ends the trial
        # *basicRating4* updates
        if t >= 0.5 and basicRating4.status == NOT_STARTED:
            # keep track of start time/frame for later
            basicRating4.tStart = t  # underestimates by a little under one frame
            basicRating4.frameNStart = frameN  # exact frame index
            basicRating4.setAutoDraw(True)
        continueRoutine &= basicRating4.noResponse  # a response ends the trial
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in basicTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "basicTrial"-------
    for thisComponent in basicTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for basicLoop (TrialHandler)
    basicLoop.addData('basicRating1.response', basicRating1.getRating())
    basicLoop.addData('basicRating1.rt', basicRating1.getRT())
    # store data for basicLoop (TrialHandler)
    basicLoop.addData('basicRating2.response', basicRating2.getRating())
    basicLoop.addData('basicRating2.rt', basicRating2.getRT())
    # store data for basicLoop (TrialHandler)
    basicLoop.addData('basicRating3.response', basicRating3.getRating())
    basicLoop.addData('basicRating3.rt', basicRating3.getRT())
    # store data for basicLoop (TrialHandler)
    basicLoop.addData('basicRating4.response', basicRating4.getRating())
    basicLoop.addData('basicRating4.rt', basicRating4.getRT())
    # the Routine "basicTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "basicWait"-------
    t = 0
    basicWaitClock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    basicWaitComponents = []
    basicWaitComponents.append(ISI)
    for thisComponent in basicWaitComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "basicWait"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = basicWaitClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
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
        for thisComponent in basicWaitComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "basicWait"-------
    for thisComponent in basicWaitComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'basicLoop'


#------Prepare to start Routine "basicEnd"-------
t = 0
basicEndClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_3.status = NOT_STARTED
# keep track of which components have finished
basicEndComponents = []
basicEndComponents.append(text_2)
basicEndComponents.append(key_resp_3)
for thisComponent in basicEndComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "basicEnd"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = basicEndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t  # underestimates by a little under one frame
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        key_resp_3.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        
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
    for thisComponent in basicEndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "basicEnd"-------
for thisComponent in basicEndComponents:
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

# the Routine "basicEnd" was not non-slip safe, so reset the non-slip timer

routineTimer.reset()

win.close()
core.quit()
from tkinter import *
import rlevel1
import rlevel2
import rlevel3
import cyol1
import cyol2
import cyol3
import multiBoard

def init(data):
    data.mainColor = 'red'
    data.optionColor = 'purple'
    data.titleColor = 'blue'
    data.backColor = 'white'
    data.font = data.height//8
    font, w, h = data.font, data.width, data.height
    data.mode = 'introScreen'
    data.introRectangles = [(w//2 - font, 2.5*h//6 - font//4, w//2 + font,2.5*\
    h//6 + font//4),(w//2 - font, h*5//8 - font//4, w//2 + font, h*5//8 + \
    font//4),(font//2, font//2-font//4, font*3//2,font//2 + font//4)] 
    data.playRectangles = [(w//2-font*5//2, h//2-font//2,w//2+font*5//2, \
    	h//2+font//2),
    (w//2-font*3, h*5//8-font//2, w//2+font*3, h*5//8+font//2), \
    (w//2-font*2, h*3//4- font//2, w//2+ font*2, h*3//4+ font//2)]
    data.relaxLevelRectangles = [(data.width//2-data.font, 2.5*data.height//6\
        -data.font//3,data.width//2+data.font,2.5*data.height//6+data.font//3),
        (data.width//2-data.font, 3.5*data.height//6-data.font//3,\
        data.width//2+data.font, 3.5*data.height//6+data.font//3),\
        (data.width//2-data.font, 4.5*data.height//6-data.font//3,\
        data.width//2+data.font, 4.5*data.height//6+data.font//3)]
    data.helpOptionRectangles = [(data.font//2, data.height//4-data.font//4, \
        3*data.font//2, data.height//4+data.font//4),(data.width//4+\
        data.font//4+8, data.height//4-data.font//4, 3*data.width//4-3*\
        data.font//4, data.height//4+data.font//4),(data.width-data.font*\
        2, data.height//4-data.font//4, data.width-data.font//2+8, \
        data.height//4+data.font//4)]
    if data.mode == 'relaxLevel1':
        rlevel1.init(data)
    elif data.mode == 'relaxLevel2':
        rlevel2.init(data)
    elif data.mode == 'relaxLevel3':
        rlevel3.init(data)
    elif data.mode == 'cyol1':
        cyol1.init(data)
    elif data.mode == 'cyol2':
        cyol2.init(data)
    elif data.mode == 'cyol3':
        cyol3.init(data)
    elif data.mode == 'multiMode': 
        multiBoard.init(data)

###MODE DISPATCHER from week 6 class notes on 112 website --to switch modes
def keyPressed(event, data):
    if data.mode == 'introScreen': introScreenKeyPressed(event, data)
    elif data.mode == 'playScreen': playScreenKeyPressed(event, data)
    elif data.mode == 'compMode': compModeKeyPressed(event,data)
    elif data.mode == 'multiMode': multiModeKeyPressed(event,data)
    elif data.mode == 'relaxLevelsMode': relaxLevelsModeKeyPressed(event,data)
    elif data.mode == 'relaxLevel1': relaxlevel1KeyPressed(event,data)
    elif data.mode == 'relaxLevel2': relaxlevel2KeyPressed(event,data)
    elif data.mode == 'relaxLevel3': relaxlevel3KeyPressed(event,data)
    elif data.mode == 'cyol1': cyol1KeyPressed(event,data)
    elif data.mode == 'cyol2': cyol2KeyPressed(event,data)
    elif data.mode == 'cyol3': cyol3KeyPressed(event,data)
def mousePressed(event, data):
    if data.mode == 'introScreen': introScreenMousePressed(event,data)
    elif data.mode == 'playScreen': playScreenMousePressed(event, data)
    elif data.mode == 'compMode': compModeMousePressed(event,data)
    elif data.mode == 'multiMode': multiModeMousePressed(event,data)
    elif data.mode == 'relaxLevelsMode':relaxLevelsModeMousePressed(event,data)
    elif data.mode == 'relaxLevel1': relaxlevel1MousePressed(event,data)
    elif data.mode == 'relaxLevel2': relaxlevel2MousePressed(event,data)
    elif data.mode == 'relaxLevel3': relaxlevel3MousePressed(event,data)
    elif data.mode == 'helpGoal': helpGoalMousePressed(event,data)
    elif data.mode == 'helpControls': helpControlsMousePressed(event,data)
    elif data.mode == 'helpModes': helpModesMousePressed(event,data)
    elif data.mode == 'cyol1': cyol1MousePressed(event,data)
    elif data.mode == 'cyol2': cyol2MousePressed(event,data)
    elif data.mode == 'cyol3': cyol3MousePressed(event,data)
def timerFired(data):
    if data.mode == 'introScreen': introScreenTimerFired(data)
    elif data.mode == 'playScreen': playScreenTimerFired(data)
    elif data.mode == 'compMode': compModeTimerFired(data)
    elif data.mode == 'multiMode': multiModeTimerFired(data)
    elif data.mode == 'relaxLevelsMode': relaxLevelsModeTimerFired(data)

def redrawAll(canvas, data):
    canvas.create_rectangle(-data.width//2,-data.height//2,3*data.width//2,\
     3*data.height//2,fill = 'black')

    if data.mode == 'introScreen': introScreenRedrawAll(canvas, data)
    elif data.mode == 'playScreen': playScreenRedrawAll(canvas, data)
    elif data.mode == 'compMode': compModeRedrawAll(canvas,data)
    elif data.mode == 'multiMode': multiModeRedrawAll(canvas,data)
    elif data.mode == 'relaxLevelsMode': relaxLevelsModeRedrawAll(canvas,data)
    elif data.mode == 'relaxLevel1': relaxlevel1RedrawAll(canvas,data)
    elif data.mode == 'relaxLevel2': relaxlevel2RedrawAll(canvas,data)
    elif data.mode == 'relaxLevel3': relaxlevel3RedrawAll(canvas,data)
    elif data.mode == 'cyol1': cyol1RedrawAll(canvas,data)
    elif data.mode == 'helpGoal': helpGoalRedrawAll(canvas,data)
    elif data.mode == 'helpControls': helpControlsRedrawAll(canvas,data)
    elif data.mode == 'helpModes': helpModesRedrawAll(canvas,data)
    elif data.mode == 'cyol2': cyol2RedrawAll(canvas,data)
    elif data.mode == 'cyol3': cyol3RedrawAll(canvas,data)
###intro Screen Functions
def introScreenMousePressed(event, data):
    if (data.introRectangles[0][0] < event.x < data.introRectangles[0][2]) and\
    (data.introRectangles[0][1] < event.y < data.introRectangles[0][3]):
        data.mode = 'playScreen'
    elif (data.introRectangles[1][0] < event.x <data.introRectangles[1][2])and\
    (data.introRectangles[1][1] < event.y < data.introRectangles[1][3]):
        data.mode = 'helpGoal' 
 #if you click on an option it should take you there
def introScreenKeyPressed(event, data):
	pass

def introScreenTimerFired(data):
	pass

def introScreenRedrawAll(canvas, data): 
    font, w, h = data.font, data.width, data.height
    canvas.create_text(w//2, h//4, text = 'GET OUT', font = \
    	'Trattatello %d underline' % (data.font*1.25) ,fill = data.mainColor)
    canvas.create_text(w//2, 2.5*h//6, text = 'P L A Y', font = \
        'Trattatello %d' % (font//1.5), fill = data.optionColor)
    canvas.create_text(w//2, h*5//8, text = 'H E L P', font = \
        'Trattatello %d' % (font//1.5), fill = data.optionColor)

###play screen functions
def playScreenMousePressed(event, data):
    if (data.introRectangles[2][0] < event.x < data.introRectangles[2][2]) and\
     (data.introRectangles[2][1] < event.y < data.introRectangles[2][3]): 
     #back button
        data.mode = 'introScreen'
    if (data.playRectangles[0][0] < event.x < data.playRectangles[0][2]) and \
        (data.playRectangles[0][1] < event.y < data.playRectangles[0][3]):
        data.mode = 'relaxLevelsMode'
        rlevel1.init(data)
    if (data.playRectangles[1][0] < event.x < data.playRectangles[1][2]) and \
        (data.playRectangles[1][1] < event.y < data.playRectangles[1][3]):
        data.mode = 'compMode'
    if (data.playRectangles[2][0] < event.x < data.playRectangles[2][2]) and \
        (data.playRectangles[2][1] < event.y < data.playRectangles[2][3]):
        data.mode = 'multiMode'
        multiBoard.init(data)

def playScreenKeyPressed(event, data):
    pass
def playScreenTimerFired(data):
    pass
def playScreenRedrawAll(canvas, data):
    font, w, h = data.font, data.width, data.height
    canvas.create_text(data.font, data.font//2, text= 'BACK', font = \
    	'Skia %d' %(data.font//4), fill = data.backColor)
    canvas.create_text(data.width//2, data.height//4, text = 'P L A Y', \
    	font = 'Trattatello %d  underline '%(data.font*1.25), fill = data.titleColor)
    canvas.create_text(data.width//2, data.height//2, text = 'RELAX & PRACTICE', \
        font = 'Trattatello %d'%(data.font//2), fill = data.optionColor)
    canvas.create_text(data.width//2, data.height*5//8, text = 'CREATE YOUR OWN LEVEL', \
    	font = 'Trattatello %d'%(data.font//2), fill = data.optionColor)
    canvas.create_text(data.width//2, data.height*3//4, text = \
    	'MULTIPLAYER', font = 'Trattatello %d'%(data.font//2), fill = data.optionColor)


###relaxLevels mode functions
def relaxLevelsModeKeyPressed(event,data):
    pass
def relaxLevelsModeMousePressed(event,data):
    if (data.introRectangles[2][0] < event.x < data.introRectangles[2][2]) and\
     (data.introRectangles[2][1] < event.y < data.introRectangles[2][3]): 
        data.mode= 'playScreen'
    if data.relaxLevelRectangles[0][0] < event.x <\
     data.relaxLevelRectangles[0][2] and data.relaxLevelRectangles[0][1] \
     < event.y < data.relaxLevelRectangles[0][3]:
        data.mode = 'relaxLevel1'
        rlevel1.init(data)

    if data.relaxLevelRectangles[1][0] < event.x < \
    data.relaxLevelRectangles[1][2] and data.relaxLevelRectangles[1][1]\
     < event.y < data.relaxLevelRectangles[1][3]:
        data.mode = 'relaxLevel2'
        rlevel2.init(data)

    if data.relaxLevelRectangles[2][0] < event.x <\
     data.relaxLevelRectangles[2][2] and data.relaxLevelRectangles[2][1] \
     < event.y < data.relaxLevelRectangles[2][3]:
        data.mode = 'relaxLevel3'
        rlevel3.init(data)
def relaxLevelsModeTimerFired(data): pass
def relaxLevelsModeRedrawAll(canvas,data):
    canvas.create_text(data.font, data.font//2, text= 'BACK', font = \
        'Skia %d' %(data.font//4), fill = data.backColor) 
    canvas.create_text(data.width//2, data.height//4, text = 'LEVELS', \
        font = 'Trattatello %d  underline '%(data.font*1.25),\
        fill = data.titleColor)
    canvas.create_text(data.width//2, 2.5*data.height//6, text = 'LEVEL 1', \
        font = 'Trattatello %d'%(data.font//1.5), fill = data.optionColor)
    canvas.create_text(data.width//2, 3.5*data.height//6, text = 'LEVEL 2', \
        font = 'Trattatello %d'%(data.font//1.5), fill = data.optionColor)
    canvas.create_text(data.width//2, 4.5*data.height//6, text = 'LEVEL 3', \
        font = 'Trattatello %d'%(data.font//1.5), fill = data.optionColor)

##relax level 1
def relaxlevel1KeyPressed(event,data): 
    rlevel1.keyPressed(event,data)
def relaxlevel1MousePressed(event,data):
    if (data.introRectangles[2][0] < event.x < data.introRectangles[2][2]) and\
     (data.introRectangles[2][1] < event.y < data.introRectangles[2][3]): 
        data.mode= 'relaxLevelsMode'
    rlevel1.mousePressed(event,data)
def relaxlevel1TimerFired(data):
    pass
def relaxlevel1RedrawAll(canvas,data):
    canvas.create_text(data.font, data.font//2, text= 'BACK', font = \
        'Skia %d' %(data.font//4), fill = data.backColor)
    rlevel1.redrawAll(canvas,data)


##relax level 2
def relaxlevel2KeyPressed(event,data): 
    rlevel2.keyPressed(event,data)
def relaxlevel2MousePressed(event,data):
    if (data.introRectangles[2][0] < event.x < data.introRectangles[2][2]) and\
     (data.introRectangles[2][1] < event.y < data.introRectangles[2][3]): 
        data.mode= 'relaxLevelsMode'
    rlevel2.mousePressed(event,data)
def relaxlevel2TimerFired(data):
    pass
def relaxlevel2RedrawAll(canvas,data):
    canvas.create_text(data.font, data.font//2, text= 'BACK', font = \
        'Skia %d' %(data.font//4), fill = data.backColor)
 
    rlevel2.redrawAll(canvas,data)

##relax level 3
def relaxlevel3KeyPressed(event,data): 
    rlevel3.keyPressed(event,data)
def relaxlevel3MousePressed(event,data):
    if (data.introRectangles[2][0] < event.x < data.introRectangles[2][2]) and\
     (data.introRectangles[2][1] < event.y < data.introRectangles[2][3]): 
        data.mode= 'relaxLevelsMode'
    rlevel3.mousePressed(event,data)
def relaxlevel3TimerFired(data):
    pass
def relaxlevel3RedrawAll(canvas,data):
    canvas.create_text(data.font, data.font//2, text= 'BACK', font = \
        'Skia %d' %(data.font//4), fill = data.backColor)
    rlevel3.redrawAll(canvas,data)

#CYOL functions
def compModeKeyPressed(event, data):
    pass
def compModeMousePressed(event,data):
    if (data.introRectangles[2][0] < event.x < data.introRectangles[2][2]) and\
     (data.introRectangles[2][1] < event.y < data.introRectangles[2][3]): 
        data.mode = 'playScreen'
    if data.relaxLevelRectangles[0][0]<event.x<data.relaxLevelRectangles[0][2]\
    and data.relaxLevelRectangles[0][1]<event.y\
    <data.relaxLevelRectangles[0][3]:
        data.mode = 'cyol1'
        cyol1.init(data) #acutally goes to cyol1 here

    if data.relaxLevelRectangles[1][0]<event.x<data.relaxLevelRectangles[1][2]\
    and data.relaxLevelRectangles[1][1] < event.y < \
    data.relaxLevelRectangles[1][3]:
        data.mode = 'cyol2'
        cyol2.init(data)

    if data.relaxLevelRectangles[2][0] < event.x <\
     data.relaxLevelRectangles[2][2] \
    and data.relaxLevelRectangles[2][1] < event.y <\
     data.relaxLevelRectangles[2][3]:
        data.mode = 'cyol3'
        cyol3.init(data)
def compModeTimerFired(data):
    pass
def compModeRedrawAll(canvas, data):
    canvas.create_text(data.font, data.font//2, text= 'BACK', font = \
    	'Skia %d' %(data.font//4), fill = data.backColor) 
    canvas.create_text(data.width//2, data.height//4, text = 'LEVELS', \
        font = 'Trattatello %d  underline '%(data.font*1.25),\
        fill = data.titleColor)
    canvas.create_text(data.width//2, 2.5*data.height//6, text = 'LEVEL 1', \
        font = 'Trattatello %d'%(data.font//1.5), fill = data.optionColor)
    canvas.create_text(data.width//2, 3.5*data.height//6, text = 'LEVEL 2', \
        font = 'Trattatello %d'%(data.font//1.5), fill = data.optionColor)
    canvas.create_text(data.width//2, 4.5*data.height//6, text = 'LEVEL 3', \
        font = 'Trattatello %d'%(data.font//1.5), fill = data.optionColor)
    #have buttons to choose a 6x6, 8x8, or 12x12 grid 
    #each will lead you to that file,then you click on GO to play the board

##cyol  1
def cyol1KeyPressed(event,data): 
    cyol1.keyPressed(event,data)
def cyol1MousePressed(event,data):
    if (data.introRectangles[2][0] < event.x < data.introRectangles[2][2]) and\
     (data.introRectangles[2][1] < event.y < data.introRectangles[2][3]): 
        data.mode= 'compMode'
    cyol1.mousePressed(event,data)

def cyol1RedrawAll(canvas,data):
    canvas.create_text(data.font, data.font//2, text= 'BACK', font = \
        'Skia %d' %(data.font//4), fill = data.backColor)
    cyol1.redrawAll(canvas,data)
#cyol  2
def cyol2KeyPressed(event,data): 
    cyol2.keyPressed(event,data)
def cyol2MousePressed(event,data):
    if (data.introRectangles[2][0] < event.x < data.introRectangles[2][2]) and\
     (data.introRectangles[2][1] < event.y < data.introRectangles[2][3]): 
        data.mode= 'compMode'
    cyol2.mousePressed(event,data)

def cyol2RedrawAll(canvas,data):
    canvas.create_text(data.font, data.font//2, text= 'BACK', font = \
        'Skia %d' %(data.font//4), fill = data.backColor)
    cyol2.redrawAll(canvas,data)
#cyol  3
def cyol3KeyPressed(event,data): 
    cyol3.keyPressed(event,data)
def cyol3MousePressed(event,data):
    if (data.introRectangles[2][0] < event.x < data.introRectangles[2][2]) and\
     (data.introRectangles[2][1] < event.y < data.introRectangles[2][3]): 
        data.mode= 'compMode'
    cyol3.mousePressed(event,data)

def cyol3RedrawAll(canvas,data):
    canvas.create_text(data.font, data.font//2, text= 'BACK', font = \
        'Skia %d' %(data.font//4), fill = data.backColor)
    cyol3.redrawAll(canvas,data)

###multiplayer mode functions
def multiModeKeyPressed(event,data):
    multiBoard.keyPressed(event,data)
def multiModeMousePressed(event, data):
    if (data.introRectangles[2][0] < event.x < data.introRectangles[2][2]) and\
     (data.introRectangles[2][1] < event.y < data.introRectangles[2][3]): 
     data.mode = 'playScreen'
    multiBoard.mousePressed(event,data)
def multiModeTimerFired(data):
    multiBoard.timerFired(data)
def multiModeRedrawAll(canvas, data):
    canvas.create_text(data.font, data.font//2, text= 'BACK', font = \
    	'Skia %d' %(data.font//4), fill = data.backColor)  
    multiBoard.redrawAll(canvas,data)

###help goal
def helpGoalMousePressed(event,data):
    if (data.introRectangles[2][0] < event.x < data.introRectangles[2][2]) and\
     (data.introRectangles[2][1] < event.y < data.introRectangles[2][3]): 
     data.mode = 'introScreen'
    if (data.helpOptionRectangles[0][0]<event.x<\
        data.helpOptionRectangles[0][2]) and (data.helpOptionRectangles[0][1]\
        <event.y<data.helpOptionRectangles[0][3]):
        data.mode = 'helpGoal'
    if (data.helpOptionRectangles[1][0]<event.x<
        data.helpOptionRectangles[1][2]) and (data.helpOptionRectangles[1][1]\
        <event.y<data.helpOptionRectangles[1][3]):
        data.mode = 'helpControls'
    if (data.helpOptionRectangles[2][0]<event.x<\
        data.helpOptionRectangles[2][2]) and (data.helpOptionRectangles[2][1]\
        <event.y<data.helpOptionRectangles[2][3]):
        data.mode = 'helpModes'
def helpGoalRedrawAll(canvas,data):
    canvas.create_text(data.font, data.font//2, text= 'BACK', font = \
        'Skia %d' %(data.font//4), fill = data.backColor)
    canvas.create_text(data.width//2, data.height//8, text = 'H E L P', \
        font = 'Trattatello %d underline '%(data.font), fill = data.titleColor)
    canvas.create_text(data.width//2, data.height//4, text = \
        'GOAL    CONTROLS    MODES',font=\
        'Trattatello %d'%(data.font//2), fill = 'red')
    canvas.create_line(data.font//2, data.height//4+data.font//4, \
        3*data.font//2, data.height//4+data.font//4, fill= 'red', width = 3)
    instructions = '\nThe goal of the game is to GET the green block OUT of \
the board by moving the surrounding pieces in their given directions.' 
    canvas.create_text(data.width//2,data.height//2, text = instructions,\
        font = 'Skia %d'%(data.font//2.5), fill = 'purple', width = \
        6*data.width//8 )
def helpControlsMousePressed(event,data):
    if (data.introRectangles[2][0] < event.x < data.introRectangles[2][2]) and\
     (data.introRectangles[2][1] < event.y < data.introRectangles[2][3]): 
     data.mode = 'introScreen'
    if (data.helpOptionRectangles[0][0]<event.x<\
        data.helpOptionRectangles[0][2]) and (data.helpOptionRectangles[0][1]\
        <event.y<data.helpOptionRectangles[0][3]):
        data.mode = 'helpGoal'
    if (data.helpOptionRectangles[1][0]<event.x<\
        data.helpOptionRectangles[1][2]) and (data.helpOptionRectangles[1][1]\
        <event.y<data.helpOptionRectangles[1][3]):
        data.mode = 'helpControls'
    if (data.helpOptionRectangles[2][0]<event.x<\
        data.helpOptionRectangles[2][2]) and (data.helpOptionRectangles[2][1]\
        <event.y<data.helpOptionRectangles[2][3]):
        data.mode = 'helpModes'
def helpControlsRedrawAll(canvas,data):
    canvas.create_text(data.font, data.font//2, text= 'BACK', font = \
        'Skia %d' %(data.font//4), fill = data.backColor)
    canvas.create_text(data.width//2, data.height//8, text = 'H E L P', \
        font = 'Trattatello %d underline '%(data.font), fill = data.titleColor)
    canvas.create_text(data.width//2, data.height//4, text = \
        'GOAL    CONTROLS    MODES',font=\
        'Trattatello %d'%(data.font//2), fill = 'red')
    canvas.create_line(data.width//4+data.font//4+8, \
        data.height//4+data.font//4, 3*data.width//4-3*data.font//4, \
        data.height//4+data.font//4, fill= 'red', width = 3)
    click = 'CLICK with your left mouse button to select a piece, and it will \
highlight in white. Use W, A, S, D, to move the selected piece, as displayed \
in the diagram below.\n\n To CREATE your own level, choose a type of piece: 1 \
= Horiz.2, 2 = Vert.2, 3 = Horiz.3, 4 = Vert.3\n and then click to place the\
piece on the board\n\nAdditional level creation key shortcuts:\n  Q = Select\
mode: You can click on any piece to highlight it\n  E = Remove: Removes the\
currently highlighted piece\n  R = Undo: Undo your last move as many times as\
you want\n  T = Redo: Redo all your past undone moves\n\nNew Board: In Relax\
Mode, this will generate a new random board. In Level Creation, this will \
clear your board.'
    canvas.create_text(data.width//2, 5.1*data.height//8, text = click, \
        font = 'Skia %d'%(data.font//3.75), fill = 'purple',\
        width = 7*data.width//8) 
def helpModesMousePressed(event,data):
    if (data.introRectangles[2][0] < event.x < data.introRectangles[2][2]) and\
     (data.introRectangles[2][1] < event.y < data.introRectangles[2][3]): 
     data.mode = 'introScreen'
    if (data.helpOptionRectangles[0][0]<event.x<\
        data.helpOptionRectangles[0][2]) and (data.helpOptionRectangles[0][1]
        <event.y<data.helpOptionRectangles[0][3]):
        data.mode = 'helpGoal'
    if (data.helpOptionRectangles[1][0]<event.x<
        data.helpOptionRectangles[1][2]) and (data.helpOptionRectangles[1][1]
        <event.y<data.helpOptionRectangles[1][3]):
        data.mode = 'helpControls'
    if (data.helpOptionRectangles[2][0]<event.x<
        data.helpOptionRectangles[2][2]) and (data.helpOptionRectangles[2][1]
        <event.y<data.helpOptionRectangles[2][3]):
        data.mode = 'helpModes'
def helpModesRedrawAll(canvas,data):
    canvas.create_text(data.font, data.font//2, text= 'BACK', font = \
        'Skia %d' %(data.font//4), fill = data.backColor)
    canvas.create_text(data.width//2, data.height//8, text = 'H E L P', \
        font = 'Trattatello %d underline '%(data.font), fill = data.titleColor)
    canvas.create_text(data.width//2, data.height//4, text = \
        'GOAL    CONTROLS    MODES',font=\
        'Trattatello %d'%(data.font//2), fill = 'red')
    canvas.create_line(data.width-data.font*2, data.height//4+data.font//4,\
    data.width-data.font//2+8, data.height//4+data.font//4, \
    fill= 'red', width = 3)
    relax = 'RELAX by practicing getting the block out of the board. You can\
 reset the board as many times as you want to get a new board.\n Level 1 --\
 6x6 board\n Level 2 -- 8x8 board\n Level 3 -- 12x12 board\n'
    cyol = '\nCREATE YOUR OWN LEVEL by placing pieces of your choice onto the\
 board around the target piece. Then hit play to solve the level you just\
 created!\n' 
    multi = '\nPlay with a partner in MULTIPLAYER mode by taking 7 \
second-long (or shorter) turns and racing to see who can get their target piece out \
of the board first!\n'
    
    canvas.create_text(data.width//2, 3.5*data.height//8, text = relax, \
        font = 'Skia %d'%(data.font//3.5), fill = 'purple',\
        width = 7*data.width//8)
    #for some reason the spaces and tabs are messed up here so need to \
    #figure this out:
    canvas.create_text(data.width//2, 5.25*data.height//8, text = cyol,\
        font = 'Skia %d'%(data.font//3.5), fill = 'purple',width = \
        7*data.width//8)
    canvas.create_text(data.width//2, 6.75*data.height//8, text = multi, \
        font = 'Skia %d'%(data.font//3.5), fill = 'purple', \
    width = 7*data.width//8)

    

    
####################################
#This run function is from the 112 course notes website, \
#from the basic animation framework
####################################


def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")


run(600, 700)
#CREATE YOUR OWN LEVEL 8X8 BOARD
from random import *
import copy
from tkinter import *

class VerticalPiece(object):
    def __init__(self, row, col, length):
        self.length = length
        self.currRow, self.currCol = row, col #left or top most square
        if (self.length == 3) and ((self.currRow == 6) or (self.currRow == 7)):
                self.currRow = 5
        elif (self.length == 2) and (self.currRow == 7):
            self.currRow = 6
    def __eq__(self, other):
        if isinstance(other, VerticalPiece) and \
            (self.currRow == other.currRow) and \
            (self.currCol == other.currCol) and \
            (self.length == other.length):
            return True
        return False
    def __hash__(self):
        return hash(self.getHashables())
    def getHashables(self):
        return (self.currRow, self.currCol, self.length)

    def moveUp(self):
        self.currRow -= 1
        if self.currRow <0: self.currRow = 0
    def moveDown(self,data):
        self.currRow += 1
        if self.currRow > (data.gridNum-self.length): 
            self.currRow = (data.gridNum-self.length)
    def move(self, event, data):
        if event == 'w':
            self.moveUp()
        if event == 's':
            self.moveDown(data)
    def undoMove(self, event, data):
        if event == 'w':
            self.currRow +=1
        if event == 's':
            self.currRow -= 1
    def draw(self, canvas, data):
        row, col = self.currRow, self.currCol
        size = data.gridSize
        margin = data.margin
        self.startX = data.boardX+self.currCol*data.gridSize
        self.startY = data.boardY+self.currRow*data.gridSize
        self.endX = data.boardX+(self.currCol+1)*data.gridSize
        self.endY = data.boardY+(self.currRow+self.length)*data.gridSize
        wid, color = 1, 'blue'
        if self == data.selectedPiece:
            wid = 4
        if self.length==2:
            canvas.create_rectangle(self.startX,self.startY,self.endX,self.endY,\
                fill = 'red', width = wid, outline = 'white')
        elif self.length == 3:
            canvas.create_rectangle(self.startX,self.startY,self.endX,self.endY,\
                fill = 'orange', width = wid, outline = 'white')

class HorizontalPiece(object):
    def __init__(self, row, col, length):
        self.length = length
        self.currRow, self.currCol = row, col #left or top most square      
        if (self.length == 3) and ((self.currCol == 6) or (self.currCol == 7)):
                self.currCol = 3
        elif (self.length == 2) and (self.currCol == 7):
            self.currCol = 6 #to make sure pieces only spawn inside the board
        self.color = 'purple'
    def __eq__(self, other):
        if isinstance(other, HorizontalPiece) and \
            (self.currRow == other.currRow) and \
            (self.currCol == other.currCol) and \
            (self.length == other.length): 
            return True
        return False
    def __hash__(self):
        return hash(self.getHashables())
    def getHashables(self):
        return (self.currRow, self.currCol, self.length)
    def moveLeft(self):
        self.currCol -= 1
        if self.currCol <0: #don't go off the board on left
            self.currCol = 0
    def moveRight(self,data):
        self.currCol += 1
        if self.currCol > (data.gridNum-self.length):
            if self != data.target: #don't go off the board
                self.currCol = (data.gridNum-self.length)
            else:
                data.gameWon = True
    def move(self, event, data):
        if event == 'a':
            self.moveLeft()
        if event == 'd':
            self.moveRight(data)    
    def undoMove(self, event, data):
        if event == 'a':
            self.currCol +=1
        if event == 'd':
            self.currCol -= 1
    def draw(self, canvas, data):
        row, col = self.currRow, self.currCol
        size = data.gridSize
        margin = data.margin
        self.startX = data.boardX+self.currCol*data.gridSize
        self.startY = data.boardY+self.currRow*data.gridSize
        self.endX = data.boardX+(self.currCol+self.length)*data.gridSize
        self.endY = data.boardY+(self.currRow+1)*data.gridSize
        wid, color = 1, 'purple'
        if self == data.selectedPiece:
            wid = 4
        if self.length==2:
            if isinstance(self,TargetPiece):
               canvas.create_rectangle(self.startX,self.startY,self.endX,self.endY,\
                fill = 'green', width = wid, outline = 'white')
            else:
                canvas.create_rectangle(self.startX,self.startY,self.endX,self.endY,\
                fill = 'purple', width = wid, outline = 'white')
        elif self.length==3: 
            canvas.create_rectangle(self.startX,self.startY,self.endX,self.endY,\
                fill = 'blue', width = wid, outline = 'white')
        
class TargetPiece(HorizontalPiece):
    def __init__(self, row, col, length):
        self.length = length
        self.currRow, self.currCol = row, col #left or top most square      
        if (self.length == 3) and ((self.currCol == 6) or (self.currCol == 7)):
                self.currCol = 3
        elif (self.length == 2) and (self.currCol == 7):
            self.currCol = 6 #to make sure pieces are only inside board        
        self.color = 'red'
def init(data):
    data.c2mode = 'create'
    font = data.height//8
    data.newBoardButton = (data.width-5*font//2, font//4, \
        data.width-font//2,3*font//4)
    data.margin, data.gameWon, data.numMoves = data.width//8, False, 0
    data.boardX, data.boardY, data.boardSize = data.margin, data.margin, \
    data.width-2*data.margin
    data.allMoves = dict()
    data.pieceMode = 'Select'
    data.undone = []
    data.gridNum,data.font  = 8, data.height//8
    data.gridSize,data.pieceSizes = data.boardSize//data.gridNum, [2,3]
    data.target = TargetPiece(1,0,2)
    data.pieces = [data.target]
    data.selectedPiece, data.piecesToRemove = choice(data.pieces), []
    removePieces(data)

###  Mode dispatcher (from 112 class notes)
def mousePressed(event, data):
    if (data.c2mode == "play"):  
        playMousePressed(event, data)
    elif (data.c2mode == "create"):
        createMousePressed(event, data)

def keyPressed(event, data):
    if (data.c2mode == "play"):  
        playKeyPressed(event, data)
    elif (data.c2mode == "create"):   
        createKeyPressed(event, data)

def timerFired(data):
    pass

def redrawAll(canvas, data):
    if (data.c2mode == "create"):   
        createRedrawAll(canvas, data)
    if (data.c2mode == "play"):  
        playRedrawAll(canvas, data)
###

def removePieces(data):
    for piece in data.piecesToRemove:

        if (piece not in data.pieces) or isinstance(piece,TargetPiece):
            continue
        data.pieces.remove(piece)

def isThereOverlap(data): # this is being used for keypressed
    selPieceCoords = set()
    if isinstance(data.selectedPiece, HorizontalPiece):
        for i in range(data.selectedPiece.length):
            selPieceCoords.add((data.selectedPiece.currRow, \
                data.selectedPiece.currCol+i))
    elif isinstance(data.selectedPiece, VerticalPiece):
        for i in range(data.selectedPiece.length):
            selPieceCoords.add((data.selectedPiece.currRow+i, \
                data.selectedPiece.currCol))
    for piece in data.pieces:
        otherPieceCoords = set()
        if isinstance(piece, HorizontalPiece):
            for i in range(piece.length):
                otherPieceCoords.add((piece.currRow, piece.currCol+i))
        elif isinstance(piece, VerticalPiece):
            for i in range(piece.length):
                otherPieceCoords.add((piece.currRow+i, piece.currCol)) 
        if piece is data.selectedPiece:
            continue
        if len(selPieceCoords.intersection(otherPieceCoords)) >= 1:
            return True
    return False   


def createKeyPressed(event, data):

    if event.keysym == '1':
        data.pieceMode = 'h2'
    elif event.keysym == '2':
        data.pieceMode = 'v2'

    elif event.keysym == '3':
        data.pieceMode = 'h3'

    elif event.keysym == '4':
        data.pieceMode = 'v3'
    if event.keysym == 'e':
        if len(data.pieces) > 1:
            data.undone.append(data.selectedPiece)
            data.pieces.remove(data.selectedPiece)
    if event.keysym == 'r':
        data.pieceMode = 'undo'
        if len(data.pieces)>1:
            data.undone.append(data.pieces.pop())
    if event.keysym == 't':
        data.pieceMode = 'redo'
        if len(data.undone)>0: 
            data.pieces.append(data.undone.pop())
            if isThereOverlap(data):
        #remove the latest piece
                data.piecesToRemove.append(data.pieces.pop())
    if event.keysym == 'q':
        data.pieceMode = 'Select'

def playKeyPressed(event,data):
    if isinstance(data.selectedPiece, VerticalPiece):
        data.oldPieceType = False 
    elif isinstance(data.selectedPiece, HorizontalPiece):
        data.oldPieceType = True 
    data.oldPieceR, data.oldPieceC = data.selectedPiece.currRow, data.selectedPiece.currCol 
    if not data.gameWon:
        data.selectedPiece.move(event.keysym, data)
        if isThereOverlap(data) == True:
            data.selectedPiece.undoMove(event.keysym,data)

def createMousePressed(event, data):
    if data.newBoardButton[0] < event.x < data.newBoardButton[2] and \
        data.newBoardButton[1] < event.y < data.newBoardButton[3]: 
        data.pieces = [TargetPiece(1,0,2)]
    coords = getBox(event,data)
    if isinstance(coords, tuple):
        if data.pieceMode == 'v2':
            data.pieces.append(VerticalPiece(coords[0],coords[1],2))
            #start a piece in the box you click  
        elif data.pieceMode == 'h2':
            data.pieces.append(HorizontalPiece(coords[0],coords[1],2))
        
        elif data.pieceMode == 'v3':
            data.pieces.append(VerticalPiece(coords[0],coords[1],3))

        elif data.pieceMode == 'h3':
            data.pieces.append(HorizontalPiece(coords[0],coords[1],3))
    data.selectedPiece = data.pieces[-1]
    if isThereOverlap(data):
        #remove the latest piece
        data.piecesToRemove.append(data.pieces.pop())
    if data.pieceMode == 'Select':
        for piece in data.pieces:
            if (piece.startX < event.x < piece.endX) and \
            (piece.startY<event.y<piece.endY):
                data.selectedPiece = piece
    if (data.boardX+6.5*data.gridSize < event.x < data.boardX+data.boardSize-data.gridSize//2)\
    and (data.boardY+data.boardSize+data.gridSize//3 < event.y < data.boardY+data.gridSize*10.5):
        data.c2mode = 'play'
def playMousePressed(event,data):
    if data.newBoardButton[0] < event.x < data.newBoardButton[2] and \
        data.newBoardButton[1] < event.y < data.newBoardButton[3]:
        init(data)
        for piece in data.pieces:
            if isinstance(piece, TargetPiece):
                return
        init(data)

    if not data.gameWon:
        for piece in data.pieces:
            if (piece.startX < event.x < piece.endX) and \
            (piece.startY<event.y<piece.endY):
                data.selectedPiece = piece

def getBox(event,data):
    for i in range(data.gridNum):
        for j in range(data.gridNum):
            if (data.boardX + j*data.gridSize< event.x < data.boardX + \
            (j+1)*data.gridSize) and (data.boardY + i*data.gridSize < \
            event.y < data.boardY + (i+1)*data.gridSize):
                return (i,j)
    return 

def createRedrawAll(canvas, data):
    font = data.height//8
    canvas.create_text(data.width-3*font//2, font//2, text = 'NEW BOARD', \
        font = 'Skia %d' %(data.font//4), fill = 'white')
    for i in range(data.gridNum):
        for j in range(data.gridNum):
            canvas.create_rectangle(data.boardX + j*data.gridSize, \
                data.boardY + i*data.gridSize, data.boardX + (j+1)*\
                data.gridSize, data.boardY + (i+1)*data.gridSize, fill = '',\
                width = 1, outline = 'white')
    for piece in data.pieces:
        piece.draw(canvas,data)
   
    if data.gameWon == True:
        canvas.create_text(data.width//2, data.height//2, text = 'YOU WIN!',\
         font = 'Trattatello %d bold' % (data.font), fill = 'white')
    
    canvas.create_line(data.boardX+ data.boardSize, data.boardY+data.gridSize,\
        data.boardX+data.boardSize, data.boardY+data.gridSize*2, fill = 'white', width = 10)
    canvas.create_text(data.boardX+data.boardSize+data.margin//2, data.boardY+data.gridSize*1.5, \
        text = 'EXIT', font = 'Trattatello %d'%(data.font//3), fill = 'white')
    canvas.create_text(data.boardX+data.boardSize-data.gridSize//2, data.boardY+data.boardSize+data.gridSize*1.5,\
        text = 'GO!', font = 'Trattatello %d'%(data.font), fill = 'green')
    canvas.create_text(data.width//3, data.height-data.margin, text ='Current Mode: %s'%(data.pieceMode),\
        font = 'Skia %d'%(data.font//2), fill = 'white', width = data.margin*4)

def playRedrawAll(canvas,data):
    font = data.height//8
    canvas.create_text(data.width-3*font//2, font//2, text = 'NEW BOARD', \
        font = 'Skia %d' %(data.font//4), fill = 'white')
    for i in range(data.gridNum):
        for j in range(data.gridNum):
            canvas.create_rectangle(data.boardX + j*data.gridSize, \
                data.boardY + i*data.gridSize, data.boardX + (j+1)*\
                data.gridSize, data.boardY + (i+1)*data.gridSize, fill = '',\
                width = 1, outline = 'white')
    for piece in data.pieces:
        piece.draw(canvas,data)
   
    if data.gameWon == True:
        canvas.create_text(data.width//2, data.height//2, text = 'YOU WIN!',\
         font = 'Trattatello %d bold' % (data.font*1.25), fill = 'white')
    
    canvas.create_line(data.boardX+ data.boardSize, data.boardY+data.gridSize,\
        data.boardX+data.boardSize, data.boardY+data.gridSize*2, fill = 'white', width = 10)
    canvas.create_text(data.boardX+data.boardSize+data.margin//2, data.boardY+data.gridSize*1.5, \
        text = 'EXIT', font = 'Trattatello %d'%(data.font//3), fill = 'white')



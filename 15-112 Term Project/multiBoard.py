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
        print('moved up')
        if self.currRow <0: self.currRow = 0
    def moveDown(self,data):
        self.currRow += 1
        print('moved down')
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
        self.color = 'green'
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
    def moveLeft(self,data):
        self.currCol -= 1
        print('moved left')
        if self.currCol <0: #don't go off the board on left
            if self != data.target2:
                self.currCol = 0
            else:
                data.gameWon = True
                data.winner = 'PLAYER 2'
    def moveRight(self,data):
        self.currCol += 1
        print('moved rightt')
        if self.currCol > (data.gridNum-self.length):
            if self != data.target1: #don't go off the board
                self.currCol = (data.gridNum-self.length)

            else:
                data.gameWon = True
                data.winner = 'PLAYER 1'
    def move(self, event, data):
        if event == 'a':
            self.moveLeft(data)
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
        wid, color = 1, 'green'
        if self == data.selectedPiece:
            wid = 4
        if self.length==2:
            if isinstance(self,TargetPiece):
               canvas.create_rectangle(self.startX,self.startY,self.endX,self.endY,\
             fill = 'green', width = wid, outline= 'white')
            else:
                canvas.create_rectangle(self.startX,self.startY,self.endX,self.endY,\
                fill = 'purple', width = wid, outline='white')
        elif self.length==3: 
            canvas.create_rectangle(self.startX,self.startY,self.endX,self.endY,\
                fill = 'blue', width = wid, outline='white')

        
class TargetPiece(HorizontalPiece):
    def __init__(self, row, col, length):
        self.length = length
        self.currRow, self.currCol = row, col #left or top most square      
        if (self.length == 3) and ((self.currCol == 6) or (self.currCol == 7)):
                self.currCol = 5
        elif (self.length == 6) and (self.currCol == 7):
            self.currCol = 6 #to make sure pieces are only inside board        
        self.color = 'red'

def init(data):
    font = data.height//8
    data.newBoardButton = (data.width-5*font//2, font//4, \
        data.width-font//2,3*font//4)
    data.margin, data.gameWon, data.numMoves = data.width//8, False, 0
    data.boardX, data.boardY, data.boardSize = data.margin, data.margin, \
    data.width-2*data.margin
    data.allMoves = dict()
    data.timesFired, data.timeLeft = 0, 0
    data.players = ['PLAYER 1', 'PLAYER 2']
    data.currentTurn = data.players[0]
    data.turnCount = 0
    data.gridNum,data.font  = 8, data.height//8
    data.gridSize,data.pieceSizes = data.boardSize//data.gridNum, [2,3]
    data.target1,data.target2 = TargetPiece(1,0,2), TargetPiece(6,6,2)
    data.pieces = []
    createRandomBoard(data)   
    data.selectedPiece, data.piecesToRemove = choice(data.pieces), []
    targetBlocked(data) #check if target is blocked
    removePieces(data)
    for item in data.pieces:  #after restricting for horiz pieces in row 1
    #in order, so maybe only if the thing it overlaps with comes after it
        data.selectedPiece = item
        if isThereBoardOverlap(data) == True:
            if isinstance(item,TargetPiece): 
                continue #don't remove the target piece
            else:
                data.piecesToRemove.append(item)
    removePieces(data)
    data.pieces = list(set(data.pieces))

    if not goodBoard(data):
        init(data)

def goodBoard(data):
    if (len(data.pieces) < 11) or (len(data.pieces)> 17) or boardIsWinnable(data)\
     or (threeVertsBlockTargets(data)==False) or (filledRowOrCol(data)==True):
        return False
    if data.target1 not in data.pieces or data.target2 not in data.pieces:
        return False
    return True

def threeVertsBlockTargets(data):
    count = 0
    for piece in data.pieces:
        if (isinstance(piece, VerticalPiece) and \
        ((piece.currRow == 1) or (piece.currRow + 1 == 1))) or (isinstance(piece,VerticalPiece) and\
        ((piece.length ==2) and (piece.currRow ==6 or piece.currRow+1==6)) or\
         ((piece.length ==3) and (piece.currRow+1==6 or piece.currRow+2 ==6))):
            count += 1
        if count >=4: #we know board is complex enough
            return True
    return False

def targetBlocked(data):
    for piece in data.pieces: #restrict for horiz pieces in row 1
        if (not isinstance(piece,TargetPiece)) and \
            isinstance(piece,HorizontalPiece) and (piece.currRow ==1): \
        #len of list is changing so it doesnt check everything
            data.piecesToRemove.append(piece)
        if (not isinstance(piece,TargetPiece)) and isinstance(piece,HorizontalPiece) and (piece.currRow == 6):
            data.piecesToRemove.append(piece)

def filledRowOrCol(data): #returns true if a row or col is permanently filled
    for piece in data.pieces:
        for secondPiece in data.pieces:
            if piece == secondPiece: continue
            if isinstance(piece,VerticalPiece) and isinstance(secondPiece, VerticalPiece) and (piece.length == 3) and (secondPiece.length == 3) and (piece.currCol == secondPiece.currCol):
                return True
            elif isinstance(piece,HorizontalPiece) and isinstance(secondPiece,HorizontalPiece) and (piece.length==3) and (secondPiece.length==3) and (piece.currRow == secondPiece.currRow):
                return True
    return False

def boardIsWinnable(data):
    #board is winnable if no piece has coordinates in row 1
    for piece in data.pieces:
        if isinstance(piece,VerticalPiece):
        #only need to account for vertical pieces' coordinates and if they're\
        # in row 1 or not
            if ((piece.length == 2) and ((piece.currRow == 1) or \
                (piece.currRow+1 == 1))) \
            or ((piece.length == 3) and ((piece.currRow == 1) or \
                (piece.currRow + 1 == 1) \
            or (piece.currRow+2==1))):
                return False
    return True

def removePieces(data):
    for piece in data.piecesToRemove:
        if (piece not in data.pieces) or isinstance(piece,TargetPiece):
            continue
        data.pieces.remove(piece)
def createRandomBoard(data):
    data.verticalPieces, data.horizontalPieces = [], []
    for i in range(data.gridNum+1):
        data.verticalPieces.append(VerticalPiece(randint(0,data.gridNum-2),\
         randint(0,data.gridNum-1),data.pieceSizes[randint(0,1)]))
        data.horizontalPieces.append(HorizontalPiece(randint(0,data.gridNum-1)\
            ,randint(0,data.gridNum-2),data.pieceSizes[randint(0,1)]))
    data.pieces= data.verticalPieces + data.horizontalPieces
    data.pieces.append(data.target1)
    data.pieces.append(data.target2)

def isThereBoardOverlap(data): 
    selPieceCoords = set()
    if isinstance(data.selectedPiece, HorizontalPiece):
        for i in range(data.selectedPiece.length):
            selPieceCoords.add((data.selectedPiece.currRow, \
                data.selectedPiece.currCol+i))
    elif isinstance(data.selectedPiece, VerticalPiece):
        for i in range(data.selectedPiece.length):
            selPieceCoords.add((data.selectedPiece.currRow+i, \
                data.selectedPiece.currCol))
    for piece in data.pieces[data.pieces.index(data.selectedPiece):]: 
    #here I change to make it check overlap with everything after \
    #data.selected piece in list
        if piece == data.selectedPiece: continue
        otherPieceCoords = set()
        if isinstance(piece, HorizontalPiece):
            for i in range(piece.length):
                otherPieceCoords.add((piece.currRow, piece.currCol+i))
        elif isinstance(piece, VerticalPiece):
            for i in range(piece.length):
                otherPieceCoords.add((piece.currRow+i, piece.currCol))  
        if len(selPieceCoords.intersection(otherPieceCoords)) >= 1:
            return True
    return False 

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
        if ((isinstance(piece, HorizontalPiece) and (data.oldPieceType==True)) or \
        (isinstance(piece, VerticalPiece) and (data.oldPieceType==False))) and\
        (((piece.currRow, piece.currCol) == (data.oldPieceR, data.oldPieceC)) or \
        ((piece.currRow, piece.currCol)==(data.selectedPiece.currRow, data.selectedPiece.currCol))):
            continue
        if len(selPieceCoords.intersection(otherPieceCoords)) >= 1:
            return True
    return False   


def keyPressed(event, data):
    if isinstance(data.selectedPiece, VerticalPiece):
        data.oldPieceType = False 
    elif isinstance(data.selectedPiece, HorizontalPiece):
        data.oldPieceType = True 
    data.oldPieceR, data.oldPieceC = data.selectedPiece.currRow, data.selectedPiece.currCol 
    if not data.gameWon:
        data.selectedPiece.move(event.keysym, data)
        if (isThereOverlap(data) == True) or (data.selectedPiece==data.target1 \
            and data.currentTurn==data.players[1]) or (data.selectedPiece == data.target2 \
            and data.currentTurn==data.players[0]):
            data.selectedPiece.undoMove(event.keysym,data)


def mousePressed(event, data):
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
        # 
def timerFired(data):
    finalTime = 7
    if data.gameWon == False:
        data.timesFired +=1
        if data.timesFired%10 == 0:
            data.timeLeft+=1
        if data.timesFired%70 == 0: #switch turns every 7 seconds automatically
            data.turnCount +=1
            data.timeLeft = 0
            if data.turnCount % 2==1:
                data.currentTurn = data.players[1] 
            else: data.currentTurn = data.players[0]

def redrawAll(canvas, data):
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
        canvas.create_text(data.width//2, data.height//2, text = '%s WINS!'%data.winner,\
         font = 'Trattatello %d bold' % (data.font//1.25), fill = 'white')
    canvas.create_text(data.boardX,data.boardY+data.boardSize+data.margin//2, text = 'P1' ,font = 'Skia %d'%(data.font//2), fill = 'green')
    canvas.create_text(data.boardX+data.boardSize,data.boardY+data.boardSize+data.margin//2, text = 'P2', font = 'Skia %d'%(data.font//2), fill = 'green')
    if data.currentTurn == 'PLAYER 1' and data.timeLeft>=0:
        canvas.create_text(data.boardX, data.boardY+data.boardSize+1.5*data.margin, text = '%d'%(7-data.timeLeft),font = 'Skia %d'%(data.font), fill = 'red')
    if data.currentTurn == 'PLAYER 2' and data.timeLeft>=0:
        canvas.create_text(data.boardX+data.boardSize, data.boardY+data.boardSize+1.5*data.margin, text = '%d'%(7-data.timeLeft),font = 'Skia %d'%(data.font), fill = 'red')
    canvas.create_line(data.boardX+ data.boardSize, data.boardY+data.gridSize,\
        data.boardX+data.boardSize, data.boardY+data.gridSize*2, fill = 'green', width = 10)
    canvas.create_line(data.boardX, data.boardY+6*data.gridSize,\
        data.boardX, data.boardY+7*data.gridSize, fill = 'green', width = 10)
    canvas.create_text(data.boardX+data.boardSize+data.margin//2, data.boardY+data.gridSize*1.5, \
        text = 'EXIT', font = 'Trattatello %d'%(data.font//3), fill = 'green')
    canvas.create_text(data.boardX-data.margin//2, data.boardY+data.gridSize*6.5, \
        text = 'EXIT', font = 'Trattatello %d'%(data.font//3), fill = 'green')
    canvas.create_text(data.boardX-data.margin//2, data.boardY+data.gridSize*1.5, \
        text = 'P.1', font = 'Trattatello %d'%(data.font//3), fill = 'white')
    canvas.create_text(data.boardX+data.boardSize+data.margin//2, data.boardY+data.gridSize*6.5, \
        text = 'P.2', font = 'Trattatello %d'%(data.font//3), fill = 'white')
    canvas.create_text(data.width//2, data.boardY+data.boardSize+data.margin//2, text = "Who's turn? %s"%(data.currentTurn), font = 'Skia %d'%(data.font//3),fill = 'white')

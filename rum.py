import copy
import math

aPackInicial = [[0,0,1,1,1,0,0],
                [0,0,1,1,1,0,0], 
                [1,1,1,1,1,1,1], 
                [1,1,1,0,1,1,1], 
                [1,1,1,1,1,1,1], 
                [0,0,1,1,1,0,0], 
                [0,0,1,1,1,0,0]]

aPack = [[0,0,1,1,1,0,0],
         [0,0,1,1,1,0,0], 
         [1,1,1,1,1,1,1], 
         [1,1,1,0,1,1,1], 
         [1,1,1,1,1,1,1], 
         [0,0,1,1,1,0,0], 
         [0,0,1,1,1,0,0]]

class Pin:
  def __init__(self, lin, col, right, left, up, down):
    self.lin = lin
    self.col = col
    self.right = right
    self.left = left
    self.up = up
    self.down = down

class Hole:
  def __init__(self, lin, col, right, left, up, down, rfa, lfa, ufa, dfa):
    self.lin = lin
    self.col = col
    self.right = right
    self.left = left
    self.up = up
    self.down = down
    self.rfa = rfa
    self.lfa = lfa
    self.ufa = ufa
    self.dfa = dfa

class HoleNew:
  def __init__(self, lin, col, aMoves, aFA):
    self.lin = lin
    self.col = col
    self.aMoves = []
    self.aFA = []

def outOfRange(lin, col):
	# Nao existe index
	if lin < 0 or lin > 6 or col < 0 or col > 6:
		return True
	# Canto superior esquerdo
	if lin < 2 and col < 2:
		return True
	# Canto superior direito
	elif lin < 2 and col > 4:
		return True
	# Canto inferior esquerdo
	elif lin > 4 and col < 2:
		return True
	# Canto inferior direito
	elif lin > 4 and col > 4:
		return True
	else:
		return False

def printPack(pack):
   for pin in pack:
       print (pin)
    

def searchHole():
    colunaHole = []
    for i in range(7):  
        for j in range(7):
            if outOfRange(i, j) == False:
                if aPack[i][j] == 0:
                    colunaHole.append(Hole(i, j,  0, 0, 0, 0, 0, 0, 0, 0))
    return colunaHole

def movingToHole(pack, hole):
    nMoves = 0
    #moveRight(hole)
    if not outOfRange (hole.lin, hole.col-1) and pack[hole.lin][hole.col-1] == 1 and not outOfRange (hole.lin, hole.col-2) and pack[hole.lin][hole.col-2] == 1:
        hole.right = 1
        hole.rfa = calcHoleFA(pack, hole, "rightToHole")
        nMoves += 1
    #moveLeft(hole)    
    if not outOfRange (hole.lin, hole.col+1) and pack[hole.lin][hole.col+1] == 1 and not outOfRange (hole.lin, hole.col+2) and pack[hole.lin][hole.col+2] == 1:
        hole.left = 1
        hole.lfa = calcHoleFA(pack, hole, "leftToHole")
        nMoves += 1
    #moveUp(hole)    
    if not outOfRange (hole.lin-1, hole.col) and pack[hole.lin-1][hole.col] == 1 and not outOfRange (hole.lin-2, hole.col) and pack[hole.lin-2][hole.col] == 1:
        hole.up = 1
        hole.ufa = calcHoleFA(pack, hole, "upToHole")
        nMoves += 1
    #moveDown(hole)    
    if not outOfRange (hole.lin+1, hole.col) and pack[hole.lin+1][hole.col] == 1 and not outOfRange (hole.lin+2, hole.col) and pack[hole.lin+2][hole.col] == 1:
        hole.down = 1
        hole.dfa = calcHoleFA(pack, hole, "downToHole")
        nMoves += 1
    return nMoves

def calcDistPins(pack):
    dPins = 0
    for i in range(7):  
        for j in range(7):
            if outOfRange(i, j) == False:
                if pack[i][j] == 1: 
                    d = math.sqrt ((math.pow (i-3, 2)) + (math.pow (j-3, 2)))
                    dPins += d
    return (dPins)

def calcFA (pack):
    valorFA = calcAgregatePins(pack) + calcDistPins(pack)
    return valorFA

def calcAgregatePins (pack):
    qPinTaking = 0
    for i in range(7):  
        for j in range(7):
            if outOfRange(i-1, j-1) == False and pack[i-1][j-1] == 1: qPinTaking +=1
            if outOfRange(i, j-1) == False and pack[i][j-1] == 1: qPinTaking +=1
            if outOfRange(i+1, j-1) == False and pack[i+1][j-1] == 1: qPinTaking +=1
            if outOfRange(i-1, j) == False and pack[i-1][j] == 1: qPinTaking +=1
            if outOfRange(i+1, j) == False and pack[i+1][j] == 1: qPinTaking +=1
            if outOfRange(i-1, j+1) == False and pack[i-1][j+1] == 1: qPinTaking +=1
            if outOfRange(i, j+1) == False and pack[i][j+1] == 1: qPinTaking +=1
            if outOfRange(i+1, j+1) == False and pack[i+1][j+1] == 1: qPinTaking +=1  

    return (qPinTaking)

def calcHoleFA(pack, hole, tipoMoving):
    packTemp = copy.deepcopy(pack)
    if tipoMoving == "rightToHole":
        packTemp[hole.lin][hole.col] = 1
        packTemp[hole.lin][hole.col-1] = 0
        packTemp[hole.lin][hole.col-2] = 0

        printPack(packTemp)
        valorFA = calcFA(packTemp)
        print("Calc for moving rightToHole -> FA:", valorFA, "\n")

    packTemp = copy.deepcopy(pack)
    if tipoMoving == "leftToHole":
        packTemp[hole.lin][hole.col] = 1
        packTemp[hole.lin][hole.col+1] = 0
        packTemp[hole.lin][hole.col+2] = 0

        printPack(packTemp)
        valorFA = calcFA(packTemp)
        print("Calc for moving leftToHole -> FA:", valorFA, "\n")

    packTemp = copy.deepcopy(pack)
    if tipoMoving == "upToHole":
        packTemp[hole.lin][hole.col] = 1
        packTemp[hole.lin-1][hole.col] = 0
        packTemp[hole.lin-2][hole.col] = 0

        printPack(packTemp)
        valorFA = calcFA(packTemp)
        print("Calc for moving upToHole -> FA:", valorFA, "\n")

    packTemp = copy.deepcopy(pack)
    if tipoMoving == "downToHole":
        packTemp[hole.lin][hole.col] = 1
        packTemp[hole.lin+1][hole.col] = 0
        packTemp[hole.lin+2][hole.col] = 0

        printPack(packTemp)
        valorFA = calcFA(packTemp)
        print("Calc for moving downToHole -> FA:", valorFA, "\n")
  
    return (valorFA)

def selecHole(listHole):
    bestFA = 0
    bestMoving = ""
    colunaBestMoves = []
    for hole in listHole:
        if listHole.index(hole) == 0:
            holeSelec = listHole[0]
            if (holeSelec.right == 1):
                bestFA = holeSelec.rfa
                bestMoving = "rightToHole"
            if (holeSelec.left == 1):
                if holeSelec.lfa < bestFA:
                    bestFA = holeSelec.lfa
                    bestMoving = "leftToHole"
            if (holeSelec.up == 1):
                if holeSelec.ufa < bestFA:
                    bestFA = holeSelec.ufa
                    bestMoving = "upToHole"
            if (holeSelec.down == 1):   
                if holeSelec.dfa < bestFA:
                    bestFA = holeSelec.dfa
                    bestMoving = "downToHole"

    colunaBestMoves.append(holeSelec)
    colunaBestMoves.append(bestMoving)
    return colunaBestMoves

def takePin(pack, hole, tipoMoving):
    if tipoMoving == "rightToHole":
        pack[hole.lin][hole.col] = 1
        pack[hole.lin][hole.col-1] = 0
        pack[hole.lin][hole.col-2] = 0

    if tipoMoving == "leftToHole":
        pack[hole.lin][hole.col] = 1
        pack[hole.lin][hole.col+1] = 0
        pack[hole.lin][hole.col+2] = 0

    if tipoMoving == "upToHole":
        pack[hole.lin][hole.col] = 1
        pack[hole.lin-1][hole.col] = 0
        pack[hole.lin-2][hole.col] = 0

    if tipoMoving == "downToHole":
        pack[hole.lin][hole.col] = 1
        pack[hole.lin+1][hole.col] = 0
        pack[hole.lin+2][hole.col] = 0

if __name__ == '__main__':
    inicialFA = calcDistPins(aPackInicial)
    print ("inicialFA:", inicialFA)
    print("valorFA", calcFA(aPackInicial))
    matrizHole = []
    matrizBestMoves = []
    
    #loop das jogadas de 0 a 31         
    for n in range(1):
        atualFA = calcDistPins(aPack)
        print ("n Jogada:", n, "atualFA:", atualFA, "\n")
        
        #busca hole e retorna a lista de holes
        holes = searchHole()
        matrizHole.append(holes)
        print ("quant de Holes:", len(holes))
        
        for hole in holes:
            
            print ("hole:(", hole.lin, "," , hole.col, ")")
            printPack(aPack)
            print()
            print("Possibilidade de moves:")
            nMoves = movingToHole(aPack, hole)
            #TODO
            if nMoves == 0: break

            print ("quant Moves:", nMoves)
            print ("tipos Moves:", hole.right, hole.left, hole.up, hole.down, "\n")
            
            #calcula os valores de FA para cada hole
            

            #seleciona o hole que gera a melhor movida
            listBestMove = selecHole(holes)
            matrizBestMoves.append(listBestMove)
            
            print("holeSelec:(", listBestMove[0].lin, ",", listBestMove[0].col, ") tipoMoving:", listBestMove[1])
            #efetua a jogada (comida/tomada do pin)
            #takePin(hole, "rightToHole")
            #takePin(hole, "leftToHole")
            #takePin(hole, "upToHole")

            takePin(aPack, listBestMove[0], listBestMove[1])

    printPack(aPack)        
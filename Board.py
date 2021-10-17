from CircularPawn import CircularPawn
from Constants import WHITE_PAWN
from SquarePawn import SquarePawn
from Tile import Tile
from Player import Player
import math

class Board:
    def __init__(self, player1: Player, player2: Player) -> None:
        self.tiles = (
            Tile(True, 1),
            Tile(True, 2),
            Tile(True, 3),
            Tile(True, 4),
            Tile(False, 5),
            Tile(True, 6),
            Tile(True, 7),
            Tile(True, 8),
            Tile(True, 9),
        )
        self.emptyTile = 4
        self.players = [player1, player2]
        self.winner = None
        self.twoSquarePawnsMoved = None

    def placeCircularPawn(self, playerNumber: int = 0, tile: int = 0) -> int:
        player = self.players[playerNumber]
        tile = self.tiles[tile]

        if(player.isCircularPawnAvailable()):
            if(tile.isSquarePawnSet() and not tile.isCircularPawnSet()):
                tile.setNewCircularPawn(playerNumber, player.placeCircularPawn())
                return 0
            return -2
        return -1
    
    def moveCircularPawn(self, playerNumber: int = 0, previousTile: int = 0, nextTile: int = 1) -> int:
        if(not self.tiles[previousTile].isCircularPawnSet() or self.tiles[previousTile].getCircularPawn().getPlayerNumber()!= playerNumber):
            return -1
        
        if(not self.tiles[nextTile].isSquarePawnSet() or self.tiles[nextTile].isCircularPawnSet()):
            return -2

        circularPawn = self.tiles[previousTile].getCircularPawn()
        self.tiles[previousTile].setCircularPawn(None)
        self.tiles[nextTile].setCircularPawn(circularPawn)

        return 0


    def moveSquarePawn(self, tileNumber: int = 0) -> bool:
        diff = math.fabs(tileNumber - self.emptyTile)

        if(diff == 1 or diff == 3):
            squarePawn = self.tiles[tileNumber].getSquarePawn()
            self.tiles[tileNumber].setSquarePawn(None)
            self.tiles[self.emptyTile].setSquarePawn(squarePawn)
            self.emptyTile = tileNumber
            return True

        return False

    def isMove2SquarePawnsPossible(self) -> bool:
        return self.emptyTile != 4

    def move2SquarePawns(self, firstTile: int = 0, secondTile: int = 1) -> int:
        if(not self.isMove2SquarePawnsPossible()):
            return -1

        if([firstTile, secondTile] == self.twoSquarePawnsMoved):
            return -2

        diff = math.fabs(firstTile - self.emptyTile)
        if(diff != 1 and diff !=3):
            return -3

        diff = math.fabs(firstTile - secondTile)
        if(diff != 1 and diff !=3):
            return -4
        
        firstSquarePawn = self.tiles[firstTile].getSquarePawn()
        secondSquarePawn = self.tiles[secondTile].getSquarePawn()
        self.tiles[firstTile].setSquarePawn(secondSquarePawn)
        self.tiles[secondTile].setSquarePawn(None)
        self.tiles[self.emptyTile].setSquarePawn(firstSquarePawn)

        self.twoSquarePawnsMoved = [firstTile, self.emptyTile]
        self.emptyTile = secondTile

    def printBoard(self) -> None:
        newLine = 0
        displayBoard = ""

        print("======================")
        print("■ = empty tile")
        print("▢ = empty square pawn")
        print("◑ = white circular pawn")
        print("◐ = black circular pawn\n")

        for tile in self.tiles:
            if(not tile.isSquarePawnSet()):
                displayBoard += "■ "
            elif(not tile.isCircularPawnSet()):
                displayBoard += "▢ "
            elif(tile.getCircularPawn().getColor() == WHITE_PAWN):
                displayBoard += "◑ "
            else: 
                displayBoard += "◐ "

            newLine += 1
            if(newLine%3 == 0):
                displayBoard += "\n"
        
        print(displayBoard)
        print("======================\n")
    
    def checkIfWinner(self) -> int:
        circularPawns = [[], []]
        victoryConditions = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9],
            [1, 5 ,9],
            [3, 5, 7]
        ]
        for tile in self.tiles:
            if(tile.isCircularPawnSet()):
                pawn = tile.getCircularPawn()
                circularPawns[pawn.getPlayerNumber()].append(tile.getNumberTile())

        if(circularPawns[0] in victoryConditions):
            return 0
        elif(circularPawns[1] in victoryConditions):
            return 1
        
        return -1

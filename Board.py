from Constants import WHITE_PAWN
from Tile import Tile
from Player import Player
import math

class Board:
    """ 
    Instanciate a board with the following parameters:
     - player1: first player
     - player2: second player.
    The function creates a board with 9 tiles and 8 square pawns placed 
    on top of every tile except the middle one.
    """
    def __init__(self, player1: Player, player2: Player) -> None:
        # Creation of the tiles
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
        # Variable to keep track of where the empty tile is
        self.emptyTile = 4
        # Liste to store the players of the game
        self.players = [player1, player2]
        # variable that stores the number of the player if he wins
        self.winner = None
        """ 
        Variable that stores the reverse movement done by the function if the function move2SquarePawns() succeeds
        This variable is used to check if a player tries to reverse the movement done by move2SquarePawns() on the previous turn
        """
        self.twoSquarePawnsMoved = None

    """
    This function places a circular pawn on top of a square pawn.
    The function uses the following parameters: 
    - playerNumber: number of the player who is placing the circular pawn, playerNumber = 0 or 1
    - tile: number of tile where the circular pawn is placed, tile = a number between 0 and 8
    The function returns:
    - 0 if the circular pawn was placed on the board
    - -1 if the player doesn't have any circular pawns left
    - -2 if a circular pawn can't be placed on the choses tile.
    """
    def placeCircularPawn(self, playerNumber: int = 0, tile: int = 0) -> int:
        player = self.players[playerNumber]
        tile = self.tiles[tile]

        if(player.isCircularPawnAvailable()):
            if(tile.isSquarePawnSet() and not tile.isCircularPawnSet()):
                self.twoSquarePawnsMoved = None
                tile.setNewCircularPawn(playerNumber, player.placeCircularPawn())
                return 0
            return -2
        return -1
    
    """
    This function moves a placed circular pawn to a new tile.
    The function uses the folling parameters: 
    - playerNumber: number of the player who is moving a circular pawn, playerNumber = 0 or 1
    - previousTile: number of the tile where the circular pawn the player wants to move is, previousTile = a number between 0 and 8
    - newtTile: number of the tile where the player wants to move his circular pawn, nextTile = a number between 0 and 8.
    The function returns:
    - 0 if the circular pawn is correctly moved
    - -1 if previousTile doesn't correspond to a tile that contains a circular pawn of the player.
    - -2 if nextTile corresponds to a tile that doensn't have a square pawn or already has a circular pawn placed on top of it.
    """
    def moveCircularPawn(self, playerNumber: int = 0, previousTile: int = 0, nextTile: int = 1) -> int:
        if(not self.tiles[previousTile].isCircularPawnSet() or self.tiles[previousTile].getCircularPawn().getPlayerNumber()!= playerNumber):
            return -1
        
        if(not self.tiles[nextTile].isSquarePawnSet() or self.tiles[nextTile].isCircularPawnSet()):
            return -2
        
        self.twoSquarePawnsMoved = None

        circularPawn = self.tiles[previousTile].getCircularPawn()
        self.tiles[previousTile].setCircularPawn(None)
        self.tiles[nextTile].setCircularPawn(circularPawn)

        return 0

    """
    This function moves a square pawn to an empty tile.
    The function uses the following paramater:
    - tileNumber, number of the tile that contains the square pawn we would like to move, tilNumber = a number between 0 and 8
    The function returns true if the square pawn was succesfully moved.
    """
    def moveSquarePawn(self, tileNumber: int = 0) -> bool:
        diff = math.fabs(tileNumber - self.emptyTile)

        if(diff == 1 or diff == 3):
            self.twoSquarePawnsMoved = None
            squarePawn = self.tiles[tileNumber].getSquarePawn()
            self.tiles[tileNumber].setSquarePawn(None)
            self.tiles[self.emptyTile].setSquarePawn(squarePawn)
            self.emptyTile = tileNumber
            return True
        
        return False

    # returns true if the player can move 2 square pawns on his turn
    def isMove2SquarePawnsPossible(self) -> bool:
        return self.emptyTile != 4

    """
    This function moves 2 square pawns.
    The function uses the following parameters:
    - firstTile: number of the tile containg the square pawn that we would like to move first, firstTile = a number between 0 and 8
    - secondTile: number of the tile containg the square pawn that we would like to move after the first square pawn, secondTile = a number between 0 and 8.
    The function returns: 
    - 0 if the 2 square pawns were successfully moved
    - -1 if the player can't move 2 square pawns on his turn
    - -2 if the player tried to reverse the positions of the 2 square pawns moved by the previous player on their last turn
    - -3 if the first selected square pawn can't be moved to the empty tile
    - -4 if the second selected square pawn can't be moved to the position of the first tile.
    """
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

        self.twoSquarePawnsMoved = None
        firstSquarePawn = self.tiles[firstTile].getSquarePawn()
        secondSquarePawn = self.tiles[secondTile].getSquarePawn()
        self.tiles[firstTile].setSquarePawn(secondSquarePawn)
        self.tiles[secondTile].setSquarePawn(None)
        self.tiles[self.emptyTile].setSquarePawn(firstSquarePawn)

        self.twoSquarePawnsMoved = [firstTile, self.emptyTile]
        self.emptyTile = secondTile

    # this functions prints the board on the consol used to run the programm 
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
    
    # returns the number of a player (0 or 1) if they've won, returns -1 otherwise.
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

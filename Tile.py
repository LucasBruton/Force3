from SquarePawn import SquarePawn
from CircularPawn import CircularPawn
from Constants import WHITE_PAWN

"""
The Tile class represents the tiles the board.
"""

class Tile:
    """ 
    Instanciate a tile with the following parameters:
     - SquarePawn object 
     - x coordinate 
     - y coordinate
    """
    def __init__(self, squarePawnSet: bool = False, numberTile: int = 0) -> None:
        if(squarePawnSet):
            self.squarePawn = SquarePawn()
        else:
            self.squarePawn = None
        self.numberTile = numberTile

    # set a squarePawn on the tile or remove the current one (with None)
    def setSquarePawn(self, squarePawn: SquarePawn = None) -> None:
        self.squarePawn = squarePawn

    # returns the squarePawn of the tile
    def getSquarePawn(self) -> SquarePawn:
        return self.squarePawn

    # Checks if the tile has a square pawn
    def isSquarePawnSet(self) -> bool:
        return self.squarePawn is not None

    # returns the circular pawn of the tile if it exists
    def getCircularPawn(self) -> CircularPawn:
        if(self.isCircularPawnSet()):
            return self.squarePawn.getCircularPawn()

        return None
    
    def setNewCircularPawn(self, playerNumber: int = 0, color: bool = WHITE_PAWN) -> None:
        if(self.isSquarePawnSet()):
            self.squarePawn.setNewCircularPawn(playerNumber, color)

    def setCircularPawn(self, circularPawn: CircularPawn = None) -> None:
        if(self.isSquarePawnSet()):
            self.squarePawn.setCircularPawn(circularPawn)


    # checks if circular pawn exists
    def isCircularPawnSet(self) -> bool:
        if(self.isSquarePawnSet()):
            return self.squarePawn.isCircularPawnSet()

        return False

    # returns the tile number
    def getNumberTile(self) -> int:
        return self.numberTile



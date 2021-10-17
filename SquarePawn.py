from CircularPawn import CircularPawn
from Constants import WHITE_PAWN

"""
The class SquarePawn represents the square pawns that can
be placed on top of cells.
"""

class SquarePawn:
    def __init__(self) -> None:
        self.circularPawn = None

    # Checks if the square pawn has a circular pawn 
    def isCircularPawnSet(self) -> bool:
        return self.circularPawn is not None

    # returns the circularPawn
    def getCircularPawn(self) -> CircularPawn:
        return self.circularPawn

    def setNewCircularPawn(self,  playerNumber: int = 0, color: bool = WHITE_PAWN) -> None:
        if(color is not None):
            self.circularPawn = CircularPawn(playerNumber, color)
        else:
            self.circularPawn = None
    
    def setCircularPawn(self, circularPawn: CircularPawn = None) -> None:
        self.circularPawn = circularPawn

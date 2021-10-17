from Constants import WHITE_PAWN
"""
The class SquarePawn represents the circular pawns that can
be placed on top of a square pawn.
"""

class CircularPawn:
    def __init__(self, playerNumber: int = 0, color: bool = WHITE_PAWN) -> None:
        self.playerNumber = playerNumber
        self.color = color

    def getColor(self) -> bool:
        return self.color
    
    def getPlayerNumber(self) -> int:
        return self.playerNumber

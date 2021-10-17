from Constants import BLACK_PAWN, WHITE_PAWN

class Player:
    def __init__(self, playerNumber: int = 0, color: bool = WHITE_PAWN) -> None:
        self.playerNumber = playerNumber
        self.color = color
        self.numberOfCirularPawns = 3

    def isCircularPawnAvailable(self) -> bool:
        return self.numberOfCirularPawns > 0
    
    def placeCircularPawn(self) -> bool: 
        self.numberOfCirularPawns -= 1
        return self.color
    
    def getNumberOfCircularPawns(self) -> int:
        return self.numberOfCirularPawns

    def getPlayerNumber(self) -> int:
        return self.playerNumber
    
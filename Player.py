from Constants import BLACK_PAWN, WHITE_PAWN

# The class Player represents a player of the game.

class Player:
    """ 
    Instanciate a player with the following parameters:
     - playerNumber: number of the player, playerNumber = 0 or 1
     - color: color of the player
    """
    def __init__(self, playerNumber: int = 0, color: bool = WHITE_PAWN) -> None:
        self.playerNumber = playerNumber
        self.color = color
        # number of circular pawns the player can place onto the board
        self.numberOfCirularPawns = 3

    # returns true if the player has a circular pawn available
    def isCircularPawnAvailable(self) -> bool:
        return self.numberOfCirularPawns > 0
    
    """
    This function represents the action of placing a circular pawn.
    The function reduces the amout of circular pawns the player has and returns 
    the color of the circular pawn.
    """
    def placeCircularPawn(self) -> bool: 
        self.numberOfCirularPawns -= 1
        return self.color
    
    # returns the number of circular pawns the player hasn't placed on the board
    def getNumberOfCircularPawns(self) -> int:
        return self.numberOfCirularPawns

    # retutns the player number
    def getPlayerNumber(self) -> int:
        return self.playerNumber
    
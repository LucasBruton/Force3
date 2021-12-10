from Board import Board
from Constants import WHITE_PAWN
from Player import Player
from Constants import BLACK_PAWN, WHITE_PAWN

# Contains the main function of the programm

def main() -> None:
    playerColor = None
    player1 = None
    player2 = None

    # Asks what color the first player wants
    while(playerColor != "1" and playerColor != "2"):
        playerColor = input("Player 1 is white (1) or black (2)? (Type 1 or 2)\n")
        print()

    # Creates the players
    if(playerColor == "1"):
        player1 = Player(0, WHITE_PAWN)
        player2 = Player(1, BLACK_PAWN)
        print("Player 1 is white \nPlayer 2 is black\n")
    else: 
        player1 = Player(0, BLACK_PAWN)
        player2 = Player(1, WHITE_PAWN)
        print("Player 1 is black\nPlayer 2 is white\n")

    # runs the game
    runGame(Board(player1, player2), player1, player2)


"""
This function runs the game by asking turn by turn what action a player wishes to do.
The function uses the following parameters:
- board: Board of the game
- player1: first player of the game
- player2: second player of the game.
"""
def runGame(board: Board, player1: Player, player2: Player) -> None:
    # This function runs untill a player wins.
    while(1):
        # Asks what the first player wants to do
        actionDone = False
        while(not actionDone):
            if(board.isMove2SquarePawnsPossible()):
                actionDone = twoSquarePawnsPossiblePlayerChoices(player1, board)
            else: 
                actionDone = twoSquarePawnsImpossiblePlayerChoices(player1, board)
        # check if a player has wone
        if(checkWinner(board)):
            break
        
        # Asks what the second player wants to do
        actionDone = False
        while(not actionDone):
            if(board.isMove2SquarePawnsPossible()):
                actionDone = twoSquarePawnsPossiblePlayerChoices(player2, board)
            else: 
                actionDone = twoSquarePawnsImpossiblePlayerChoices(player2, board)
        # check if a player has wone
        if(checkWinner(board)):
            break

"""
This function is used when the player has 2 possible actions when they begin.
The function uses the following parameters:
- player: player who choices an action
- board: board of the game.
Returns true if the action of the player succeeded.
"""
def twoSquarePawnsImpossiblePlayerChoices(player: Player = None, board: Board = None) -> bool:
    action = 0
    allowedChoices = []
    board.printBoard()
    print("Player " + str(player.getPlayerNumber()+1) +", please choose an action between the following actions")

    if(len(player.pawns) < 3):
        print("- place a circular pawn on a square pawn (1);")
        allowedChoices.append("1");

    if(len(player.pawns) > 0):
        print("- move one of your circular pawns (2).")
        allowedChoices.append("2")

    print("- move a square pawn to an empty tile (3);")
    allowedChoices.append("3")

    print("You can place "+str(player.getNumberOfCircularPawnsAvailable()) + " pawns.")
    print("Type the number between ( ) to choose an action")
    while(action not in allowedChoices):
        action = input()
    print()

    return actionChoice(int(action), player, board)

"""
This function is used when the player has 4 possible actions during his turn.
The function uses the following parameters:
- player: plyaer who choices an action
- board: board of the game.
Returns true if the action of the player succeeded.
"""
def twoSquarePawnsPossiblePlayerChoices(player: Player = None, board: Board = None) -> bool:
    action = 0
    allowedChoices = []
    board.printBoard()
    print("Player " + str(player.getPlayerNumber()+1) +", please choose an action between the following actions")

    if(len(player.pawns) < 3):
        print("- place a circular pawn on a square pawn (1);")
        allowedChoices.append("1");

    if(len(player.pawns) > 0):
        print("- move one of your circular pawns (2).")
        allowedChoices.append("2")

    print("- move a square pawn to an empty tile (3);")
    allowedChoices.append("3")

    print("- move 2 square pawns (4).")
    allowedChoices.append("4")

    print("You can place "+str(player.getNumberOfCircularPawnsAvailable()) + " pawns.")
    print("Type the number between () to choose an action")
    while(action not in allowedChoices):
        action = input()
    print()

    return actionChoice(int(action), player, board)

"""
This function calls one of the possible actions of the player.
The function uses the following parameters: 
- action: number of the action to execute, action = 1, 2, 3 or 4
- player: number of the player who is going to do the action, player = 0 or 1
- board: board of the game
Returns true if the action succeeded.
"""
def actionChoice(action: int, player: Player, board: Board) -> bool:     
    if(action == 1): 
        return placeCircularPawn(player.getPlayerNumber(), board)
    elif(action == 2):
        return moveCircularPawn(player, board)
    elif(action == 3):
        return moveSquarePawn(board)
    elif(action == 4):
        return move2SquarePawns(board)


"""
placeCircularPawn corresponds to the following action : place a circular pawn onto the board
This function asks the player where to place a new cicurlar pawn then places it onto the board.
The function uses the following parameters:
- player: number of the player who is placing the circular pawn, player = 0 or 1
- board: board of the game.
Returns True if the action succeeded.
"""
def placeCircularPawn(player: int, board: Board) -> bool:
        x = 0
        y = 0
        xNumbersPossible = ["0", "1", "2"]
        yNumbersPossible = ["0", "1", "2"]
        print("On which tile would you like to place a circular pawn ?")
        print("line :")

        while(x not in xNumbersPossible):
            x = input()

        print("column :")

        while(y not in yNumbersPossible):
            y = input()
        actionSuccess = board.placeCircularPawn(player, int(x), int(y))

        if(actionSuccess == -1):
            print("\nYou don't have any circular pawns left!\n")
            return False
        elif(actionSuccess == -2):
            print("\nYou can't place a circular pawn there!\n")
            return False
        else:
            print("\nSuccess!\n")
            return True

"""
moveCircularPawn corresponds to the following action : move a placed circular pawn onto a free square pawn
This function asks the player which circular pawn he would like to move and where he would like to move it.
Afterwards, the function moves the circular pawn.
The function uses the following parameters:
- player: number of the player who is moving a circular pawn, player = 0 or 1
- board: board of the game.
Returns True if the action succeeded.
"""
def moveCircularPawn(player: Player, board: Board) -> bool:
        circularPawnIdPossible = []
        idPawn = 0
        x = 0
        y = 0
        if((len(player.pawns) - 1) != 0):
            for i in range(len(player.pawns)):
                circularPawnIdPossible.append(str(i + 1))
        else:
            circularPawnIdPossible = ["1"]

        xNumbersPossible = ["0", "1", "2"]
        yNumbersPossible = ["0", "1", "2"]

        print("Which one of your circular pawns would you like to move ?")
        print("Select the number of your circular pawn: 1, 2 or 3.")

        while(idPawn not in circularPawnIdPossible):
            idPawn = input()

        print("\nWhere would you like to move this pawn ?")
        print("Select a tile for the new location of the pawn (it can't be the current tile of the pawn)")

        print("line:")
        while(x not in xNumbersPossible):
            x = input()

        print("column:")
        while(y not in yNumbersPossible):
            y = input()

        actionSuccess = board.moveCircularPawn(player.getPlayerNumber(), int(idPawn), int(x), int(y))

        if(actionSuccess == -1):
            print("\nYou can't move your circular pawn onto the tile "+ nextTile+"!\n")
            return False
        else:
            print("\nSuccess!\n")
            return True

"""
move2SquarePawns corresponds to the following action : 
move 2 square pawns if the empty tile isn't in the middle, this action can't be used to reverse 
the positions of the 2 square pawns moved by the previous player on their last turn.
This function asks the player which 2 square pawn he would like to move and then moves them.
The function uses the following parameter:
- board: board of the game.
Returns True if the action succeeded.
"""
def move2SquarePawns(board: Board) -> bool:
        x = [0,0]
        y = [0,0]
        xNumbersPossible = ["0", "1", "2"]
        yNumbersPossible = ["0", "1", "2"]
        print("Which square pawn would you like to move first ?")
        
        print("line :")
        while(x[0] not in xNumbersPossible):
            x[0] = input()

        print("column :")
        while(y[0] not in yNumbersPossible):
            y[0] = input()
    

        print("\nWhat is the second square pawn that you would like to move?")
        print("Select a tile to choose the square pawn")

        print("line :")
        while(x[1] not in xNumbersPossible):
            x[1] = input()

        print("column :")
        while(y[1] not in yNumbersPossible):
            y[1] = input()

        actionSuccess = board.move2SquarePawns(x, y)

        if(actionSuccess == -1):
            print("\nYou aren't allowed to do move square pawns!\n")
            return False
        elif(actionSuccess == -2):
            print("\nYou aren't allowed to reverse the 2 movements you opponent did on their previous turn!\n")
            return False
        elif(actionSuccess == -3):
            print("\nThe first tile you chose can't move!\n")
            return False
        elif(actionSuccess == -4):
            print("\nYour two tiles are not align with each other!\n")
            return False
        elif(actionSuccess == -5):
            print("\nYou can't move this two tiles like this!\n")
            return False
        else:
            print("\nSuccess!\n")
            return True

"""
moveSquarePawn corresponds to the following action : move a square pawn onto the the empty tile.
the positions of the 2 square pawns moved by the previous player on their last turn.
This function asks the player which square pawn he would like to move and then moves it.
The function uses the following parameter:
- board: board of the game.
Returns True if the action succeeded.
"""
def moveSquarePawn(board: Board) -> bool:
        x = 0
        y = 0
        xNumbersPossible = ["0", "1", "2"]
        yNumbersPossible = ["0", "1", "2"]

        print("To move a square pawn, select a tile that contains a square pawn and that is next to the empty tile")
        print("line :")
        while(x not in xNumbersPossible):
            x = input()

        print("column :")
        while(y not in xNumbersPossible):
            y = input()

        actionSuccess = board.moveSquarePawn(int(x), int(y))

        if(actionSuccess == -1):
            print("\nYou aren't allowed to reverse the movement your opponent did on their previous turn!\n")
            return False
        elif(actionSuccess == -2):
            print("\nYou can't move this tile!\n")
            return False
        else: 
            print("\nSuccess!")
            return True


# returns true if a player has wone
def checkWinner(board) -> bool: 
    winner = board.checkIfWinner()
    if(winner == 0):
        print("\nPlayer 1 is the winner!")
        board.printBoard()
        return True
    elif(winner == 1):
        board.printBoard()
        print("\nPlayer 2 is the winner!")
        return True
    else:
        return False

main()
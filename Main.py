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
                actionDone = FourPlayerChoices(player1, board)
            else: 
                actionDone = ThreePlayerChoices(player1, board)
        # check if a player has wone
        if(checkWinner(board)):
            break
        
        # Asks what the second player wants to do
        actionDone = False
        while(not actionDone):
            if(board.isMove2SquarePawnsPossible()):
                actionDone = FourPlayerChoices(player2, board)
            else: 
                actionDone = ThreePlayerChoices(player2, board)
        # check if a player has wone
        if(checkWinner(board)):
            break
        
"""
This function is used when the player has 3 possible actions during his turn.
The function uses the following parameters:
- player: player who choices an action
- board: board of the game.
Returns true if the action of the player succeeded.
"""
def ThreePlayerChoices(player: Player = None, board: Board = None) -> bool:
    action = 0
    board.printBoard()
    print("Player " + str(player.getPlayerNumber()+1) +", please choose an action between the 3 following actions")
    print("- place a circular pawn on a square pawn (1);")
    print("- move one of your circular pawns (2).")
    print("- move a square pawn to an empty tile (3);")
    print("You have "+str(player.getNumberOfCircularPawns()) + " pawns.")
    print("Type 1, 2 or 3 to choose an action")
    while(action not in ["1", "2", "3"]):
        action = input()
    print()

    return actionChoice(int(action), player.getPlayerNumber(), board)

"""
This function is used when the player has 4 possible actions during his turn.
The function uses the following parameters:
- player: plyaer who choices an action
- board: board of the game.
Returns true if the action of the player succeeded.
"""
def FourPlayerChoices(player: Player = None, board: Board = None) -> bool:
    action = 0
    board.printBoard()
    print("Player " + str(player.getPlayerNumber()+1) +", please choose an action between the 4 following actions")
    print("- place a circular pawn on a square pawn (1);")
    print("- move one of your circular pawns (2);")
    print("- move a square pawn to an empty tile (3);")
    print("- move 2 square pawns (4).")
    print("You have "+str(player.getNumberOfCircularPawns()) + " pawns.")
    print("Type 1, 2, 3 or 4 to choose an action")
    while(action not in ["1", "2", "3", "4"]):
        action = input()
    print()

    return actionChoice(int(action), player.getPlayerNumber(), board)

"""
This function calls one of the possible actions of the player.
The function uses the following parameters: 
- action: number of the action to execute, action = 1, 2, 3 or 4
- player: number of the player who is going to do the action, player = 0 or 1
- board: board of the game
Returns true if the action succeeded.
"""
def actionChoice(action: int, player: int, board: Board) -> bool:     
    if(action == 1): 
        return placeCircularPawn(player, board)
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
        tile = 0
        tileNumbersPossible = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        print("On which tile would you like to place a circular pawn ?")
        print("Tiles are arranged as follow: \n")
        print("1 2 3")
        print("4 5 6")
        print("7 8 9\n")
        print("Type a number between 1 and 9")

        while(tile not in tileNumbersPossible):
            tile = input()
        actionSuccess = board.placeCircularPawn(player, int(tile)-1)

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
def moveCircularPawn(player: int, board: Board) -> bool:
        previousTile = 0
        nextTile = 0
        tileNumbersPossible = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        print("Which one of your circular pawns would you like to move ?")
        print("Select a tile to choose the circular pawn")
        print("Tiles are arranged as follow: \n")
        print("1 2 3")
        print("4 5 6")
        print("7 8 9\n")
        print("Type a number between 1 and 9")

        while(previousTile not in tileNumbersPossible):
            previousTile = input()

        print("\nWhere would you like to move this pawn ?")
        print("Select a tile for the new location of the pawn (it can't be the current tile of the pawn)")

        while(nextTile == previousTile or nextTile not in tileNumbersPossible):
            nextTile = input()

        actionSuccess = board.moveCircularPawn(player, int(previousTile)-1, int(nextTile)-1)

        if(actionSuccess == -1):
            print("\nYou haven't selected one of your circular pawns!\n")
            return False
        elif(actionSuccess == -2):
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
        firstTile = 0
        secondTile = 0
        tileNumbersPossible = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        print("Which square pawn would you like to move first ?")
        print("Select a tile to choose the square pawn")
        print("Tiles are arranged as follow: \n")
        print("1 2 3")
        print("4 5 6")
        print("7 8 9\n")
        print("Type a number between 1 and 9")

        while(firstTile not in tileNumbersPossible):
            firstTile = input()

        print("\nWhat is the second square pawn that you would like to move?")
        print("Select a tile to choose the square pawn")

        while(secondTile == firstTile or secondTile not in tileNumbersPossible):
            secondTile = input()

        actionSuccess = board.move2SquarePawns(int(firstTile)-1, int(secondTile)-1)

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
            print("\nThe second tile you chose can't move!\n")
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
        tile = 0
        tileNumbersPossible = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        print("To move a square pawn, select a tile that contains a square pawn and that is next to the empty tile")
        print("Tiles are arranged as follow: \n")
        print("1 2 3")
        print("4 5 6")
        print("7 8 9\n")
        print("Type a number between 1 and 9")

        while(tile not in tileNumbersPossible):
            tile = input()
        
        actionSuccess = board.moveSquarePawn(int(tile)-1)
        if(not actionSuccess):
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
from Constants import BLACK_PAWN, WHITE_PAWN
from Board import Board
from Player import Player

SCORE_MAX = 10000
SCORE_MIN = -10000
SCORE_THREE = 100
"""The AIPlayer class inherits Player
   it has a new attribute pos_score in order to store the value of each Tile
"""


class AIPlayer(Player):
    def __init__(self, playerNumber: int = 0, color: bool = WHITE_PAWN) -> None:
        Player.__init__(self, playerNumber, color)
        self.pos_score = [[1, 2, 1], [2, 3, 2], [1, 2, 1]]


"""
    here are some actions that AIPlayer can do as humain
"""


# the AIPlayer do the place circle action
def placeCircularPawn(self, Board, x: int = 0, y: int = 0) -> int:
    playNumber = self.getPlayerNumber
    Board.placeCircularPawn(playNumber, x, y)


# the AIPlayer do the move circle action
def moveCircularPawn(self, Board, pre_tile, next_x, next_y) -> int:
    playNumber = self.getPlayerNumber
    Board.moveCircularPawn(playNumber, pre_tile, next_x, next_y)


# the AIPlayer do the move square action
def moveSquarePawn(self, Board, x: int = 0, y: int = 0) -> int:
    tile = Board.board[x][y]
    diff = math.fabs(tile.idTile - Board.emptyTile.idTile)

    if ([Board.emptyTile, tile] == Board.squarePawnMoved):
        return -1

    if (diff == 1 or diff == 3):
        Board.twoSquarePawnsMoved = None
        Board.squarePawnMoved = [tile, Board.emptyTile]
        squarePawn = tile.getSquarePawn()
        tile.setSquarePawn(None)
        Board.emptyTile.setSquarePawn(squarePawn)
        Board.emptyTile = tile
        return 0
    else:
        return -2


#
def isMove2SquarePawnsPossible(Board) -> bool:
    return Board.emptyTile.idTile != 5


def move2SquarePawns(self, Board, x: list = [0, 0], y: list = [0, 0]) -> int:
    firstTile = Board.board[int(x[0]), int(y[0])]
    secondTile = Board.board[int(x[1]), int(y[1])]

    Board.squarePawnMoved = None

    if (not Board.isMove2SquarePawnsPossible()):
        return -1

    if ([firstTile, secondTile] == Board.twoSquarePawnsMoved):
        return -2

    diff = math.fabs(firstTile.idTile - Board.emptyTile.idTile)
    if (diff != 1 and diff != 3):
        return -3

    diff = math.fabs(firstTile.idTile - secondTile.idTile)
    if (diff != 1 and diff != 3):
        return -4

    if (not ((secondTile.x == firstTile.x and secondTile.x == Board.emptyTile.x) or
             (secondTile.y == firstTile.y and secondTile.y == Board.emptyTile.y))):
        return -5

    Board.twoSquarePawnsMoved = None
    firstSquarePawn = firstTile.getSquarePawn()
    secondSquarePawn = secondTile.getSquarePawn()
    firstTile.setSquarePawn(secondSquarePawn)
    secondTile.setSquarePawn(None)
    Board.emptyTile.setSquarePawn(firstSquarePawn)

    Board.twoSquarePawnsMoved = [firstTile, Board.emptyTile]
    Board.emptyTile = secondTile


"""These functions below is to help us choose the best step and choose the action to execute according to the situation
   We use the founction 'Evaluate' to evaluate the score(This score is determined by the scores of yourself and your opponent on the current board) of each Tile
   We use the function 'Renew_Score' to update the score and sort it in descending order
   We use a function 'findBestStep' to generate a tree at the depth of 4, and use alpha-bete to find the best choice based on the next situation
   After completing the determination of the best step, we use the function 'play' to use the appropriate action function and play it
"""


# the AIPlayer chose the best way to play after evalue this tiles
def play(self, Board):
    x, y = self.findBestStep(Board, self.getPlayerNumber, 4)
    if (self.isCircularPawnAvailable):
        self.placeCircularPawn(Board, x, y)
    return Board


# renew the score of every tile in list moves
def Renew_Score(self, Board, turn):
    scores = []
    for y in range(3):
        for x in range(3):
            if not Board[y][x].getPlyernumber():
                score = self.pos_score[y][x]
                moves.append((score, x, y))
    scores.sort(reverse=True)
    return moves


# fine the best position at depth
def findBestStep(self, Board, turn, depth, alpha=SCORE_MIN, beta=SCORE_MAX) -> int:
    score = self.evaluate(Board, turn)

    if depth <= 0 or score == SCORE_THREE:
        return score
    scores = self.Renew_Score(Board, turn)
    bestmove = None

    for _, y, x in scores:
        # set the present tile of the player turn
        if Board[x][y].SquarePawn:
            Board[x][y].setCircularPawn(CircularPawn(turn, self.color, Board[y][x].idTile, x, y))
        else:
            Board[x][y].setSquarePawn.setNewCircular(turn, self.color, Board[y][x].idTile, x, y)

        if turn == 1:
            op_turn = 0
        else:
            op_turn = 1

        score = -self.findBestStep(Board, op_turn, depth - 1, -beta, -alpha)

        Board[x][y].getCircularPawn.PlayerNumber = None
        self.beta += 1

        if score > alpha:
            bestmove = (x, y)
            if alpha >= beta:
                break
    if depth == 4 and bestmove:
        self.bestmove = bestmove
    x, y = self.bestmove
    return (x, y)


# the founction to evaluate the score of every tile
def Evaluate(self, Board, turn):
    if turn == 0:
        mine = 1
        opponent = 2
    else:
        mine = 2
        opponent = 1

    for x in range(3):
        for y in range(3):
            if not Board[x][y].getPlyernumber():
                mscore[x][y] = self.evaluatescore(Board, x, y, mine, opponent)
                oscore[x][y] = self.evaluatescore(Board, x, y, opponent, mine)
            else:
                mscore[x][y] = oscore[x][y]
    return (mscore - oscore)


# evaluate the score of tile[x][y]
def evaluatescore(self, Board, x, y, mine, opponent):
    score = pos_score[x][y]
    if x - 1 < 0 and y - 1 < 0:
        if (Board[x + 1][y].getPlyernumber() == mine and Board[x + 2][y].getPlayernumber() == mine) or (
                Board[x][y + 1].getPlayernumber() == mine and Board[x][y + 2].getPlayernumber() == mine):
            score += 5

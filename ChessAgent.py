#620140477- De'Anna-Shanae Beadle

import chess
import chess.engine

def evaluate_board(board):
    #Evaluates the state of the board
    if board.is_checkmate():
        if board.turn:
            return -9999  # Black player wins
        else:
            return 9999  # White player wins
    elif board.is_stalemate() or board.is_insufficient_material() or board.is_seventyfive_moves() or board.is_fivefold_repetition():
        return 0  # Match is a draw
    else:
        # Count for each piece type
        pcount = {
            chess.PAWN: 1,
            chess.KNIGHT: 3,
            chess.BISHOP: 3,
            chess.ROOK: 5,
            chess.QUEEN: 9
        }
        # Evaluates based on the pieces
        evaluate = 0
        for p in board.piece_map().values():
            if p.color == chess.WHITE:
                evaluate += pcount.get(p.piece_type, 0)
            else:
                evaluate -= pcount.get(p.piece_type, 0)

        return evaluate

def minimax(board, depth, alpha, beta, maximizing_player):
    # The minimax algorithm with alpha-beta pruning. Takes the current state of the board, depth, aplha, beta and the maximizing player and returns the evaluated score of the board.
    if depth <= 0 or board.is_game_over():
        return evaluate_board(board)

    if maximizing_player:
        #Max player assigned as negative infinity
        maxplayer = float('-inf')
        
        for maxmove in board.legal_moves:
            board.push(maxmove)
            maxvalue = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            maxplayer = max(maxplayer, maxvalue)
            alpha = max(alpha, maxplayer)
            #Alpha beta pruning: Cuts off the branch if beta is less than or equal to alpha
            if beta <= alpha:
                break
            
        return maxplayer
    else:
        #Min player assigned as positive infinity
        minplayer = float('inf')
        for minmove in board.legal_moves:
            board.push(minmove)
            minvalue = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            minplayer = min(minplayer, minvalue)
            beta = min(beta, minplayer)
            
            if beta <= alpha:
                break
            
        return minplayer

def get_best_move(board, depth):
    # Looks at the board and determines the best move possible using minmax alpha beta pruning. It takes the board and the depth and returns the best predicted move
    bestmove = None
    bestfinalmove = float('-inf') if board.turn == chess.WHITE else float('inf')

    for move in board.legal_moves:
        board.push(move)
        value = minimax(board, depth - 1, float('-inf'), float('inf'), not board.turn)
        board.pop()

        if (board.turn == chess.WHITE and value > bestfinalmove) or (board.turn != chess.WHITE and value < bestfinalmove):
            bestfinalmove = value
            bestmove = move
    return bestmove

def getdifficulty():
   # Different Difficulty Levels: This alows the user to set different depths for the agent, thus adjusting the difficulty level.
    level = {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5
    }
    
    print("Choose difficulty level:")
    print("1. Level 1")
    print("2. Level 2")
    print("3. Level 3")
    print("4. Level 4")
    print("5. Level 5")

    while True:
        difficultylevel = input("Enter the difficulty level (1-5): ")
        if difficultylevel in level:
            return level[difficultylevel]
        else:
            print("Only enter a number between 1 and 5.")

def play_game():
    
    #Main function to play the game. It alternates between the human and the agent.
    
    board = chess.Board()
    depth = getdifficulty()
    print('================')
    print('  Chess Engine  ')
    print('================')
    print()
    
    while not board.is_game_over():
        print(board)
        if board.turn == chess.WHITE:
            # Human's turn
            print()
            move = input("Enter your move:")
            try:
                board.push_san(move)
            except ValueError:
                print()
                print("Invalid move. Try again.")
        else:
            # Agent's turn
            move = get_best_move(board, depth)
            print("Agent's move:", board.san(move))
            board.push(move)

    print("Game over:", board.result())

if __name__ == "__main__":
    play_game()

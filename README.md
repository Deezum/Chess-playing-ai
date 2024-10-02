# Chess Playing Agent

## Overview
This project implements a chess-playing agent using the Minimax algorithm enhanced with Alpha-Beta pruning. The agent can play a complete game of chess against a human player or another agent. The agent evaluates game states and makes optimal moves based on a specified depth of search.

## Features
- Implements the Minimax algorithm with Alpha-Beta pruning.
- Adjustable difficulty levels by setting different depths for the agent's search.
- Can play a complete game of chess against a human player.
- Simple text-based interface.

## Dependencies
- Python 3.x
- `python-chess` library

## Installation
1. **Install the required dependencies:**
    pip install python-chess

## Running the Agent
1. **Run the `ChessAgent.py` script in the terminal:**
    python ChessAgent.py

2. **Choose the difficulty level:**
    When prompted, enter a number between 1 and 5 to set the difficulty level:
    - 1: Novice
    - 2: Intermediate
    - 3: Expert
    - 4: Grandmaster
    - 5: Super Grandmaster

3. **Play the game:**
    - The game starts with an empty chess board displayed.
    - If it's the human player's turn (White), enter your move in Standard Algebraic Notation (SAN). For example, `e2e4` or `e4` to move a pawn from e2 to e4.
    - The agent (Black) will then make its move, and the updated board will be displayed.
    - Continue playing until the game is over.

## Example
Here is an example of a session:

Choose difficulty level:

Novice
Intermediate
Expert
Grandmaster
Super Grandmaster
Enter the difficulty level (1-5): 3
================
  Chess Engine 
================

 r n b q k b n r
 p p p p p p p p
 . . . . . . . .
 . . . . . . . .
 . . . . . . . .
 . . . . . . . .
 P P P P P P P P
 R N B Q K B N R
 

Enter your move: e2e4

Agent's move: e7e5

 r n b q k b n r
 p p p p . p p p
 . . . . . . . .
 . . . . p . . .
 . . . . P . . .
 . . . . . . . .
 P P P P . P P P
 R N B Q K B N R


## Documentation
- `evaluate_board(board)`: Evaluates the board state based on pieces.
- `minimax(board, depth, alpha, beta, maximizing_player)`: Minimax algorithm with Alpha-Beta pruning.
- `get_best_move(board, depth)`: Determines the best move for the current player.
- `get_difficulty()`: Asks the user to choose a difficulty level.
- `play_game()`: Main function to play the game, alternating turns between the human player and the agent.






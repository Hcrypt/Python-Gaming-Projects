# Define the board as a list of strings
board = ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8",
         "a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7",
         "a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6",
         "a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5",
         "a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4",
         "a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3",
         "a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2",
         "a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"]

# Define the initial positions of the pieces
board[0] = "R"  # Black rook
board[1] = "N"  # Black knight
board[2] = "B"  # Black bishop
board[3] = "Q"  # Black queen
board[4] = "K"  # Black king
board[5] = "B"  # Black bishop
board[6] = "N"  # Black knight
board[7] = "R"  # Black rook
board[8] = "P"  # Black pawn
board[9] = "P"  # Black pawn
board[10] = "P" # Black pawn
board[11] = "P" # Black pawn
board[12] = "P" # Black pawn
board[13] = "P" # Black pawn
board[14] = "P" # Black pawn
board[15] = "P" # Black pawn
board[63] = "r"  # White rook
board[62] = "n"  # White knight
board[61] = "b"  # White bishop
board[60] = "q"  # White queen
board[59] = "k"  # White king
board[58] = "b"  # White bishop
board[57] = "n"  # White knight
board[56] = "r"  # White rook
board[55] = "p"  # White pawn
board[54] = "p"  # White pawn
board[53] = "p"  # White pawn
board[52] = "p"  # White pawn
board[51] = "p"  # White pawn
board[50] = "p"  # White pawn
board[49] = "p"  # White pawn
board[48] = "p"  # White pawn

# Print the board
for i in range(64):
    print(board[i], end=" ")
    if (i + 1) % 8 == 0:
        print()

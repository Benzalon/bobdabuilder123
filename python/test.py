# ---------- COLORS ----------
RESET = "\033[0m"
RED = "\033[31m"
BLUE = "\033[34m"
WHITE_BG = "\033[47m"
BLACK_BG = "\033[40m"

# ---------- BOARD ----------
board = [
    1,0,1,0,1,0,1,0,
    0,1,0,1,0,1,0,1,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    2,0,2,0,2,0,2,0,
    0,2,0,2,0,2,0,2
]

files = "abcdefgh"

# ---------- HELPERS ----------
def index_from_coord(coord):
    file = files.index(coord[0])
    rank = 8 - int(coord[1])
    return rank * 8 + file

def draw_board():
    print("\n   a b c d e f g h")
    for r in range(8):
        print(8 - r, end="  ")
        for c in range(8):
            i = r * 8 + c
            bg = WHITE_BG if (r + c) % 2 == 0 else BLACK_BG

            if board[i] == 1:
                piece = RED + "●" + RESET
            elif board[i] == 2:
                piece = BLUE + "●" + RESET
            else:
                piece = " "

            print(bg + piece + RESET, end=" ")
        print(8 - r)
    print("   a b c d e f g h\n")

def move_piece(player):
    start = input("Starting piece (ex b6): ").lower()
    end = input("Ending position (ex a5): ").lower()

    try:
        s = index_from_coord(start)
        e = index_from_coord(end)
    except:
        print("❌ invalid input")
        return

    if board[s] != player:
        print("❌ not your piece")
        return

    if board[e] != 0:
        print("❌ destination blocked")
        return

    sr, sc = divmod(s, 8)
    er, ec = divmod(e, 8)

    dr = er - sr
    dc = abs(ec - sc)

    if player == 1 and dr != -1:
        print("❌ must move up")
        return
    if player == 2 and dr != 1:
        print("❌ must move down")
        return
    if dc != 1:
        print("❌ move diagonally")
        return

    board[s] = 0
    board[e] = player

# ---------- GAME LOOP ----------
current_player = 1

while True:
    draw_board()

    print(f"{'🔴 Player 1' if current_player == 1 else '🔵 Player 2'} turn")
    move_piece(current_player)

    current_player = 2 if current_player == 1 else 1

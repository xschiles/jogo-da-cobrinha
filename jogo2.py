import random

def generate_board(size, num_bombs):
    board = [[' ' for _ in range(size)] for _ in range(size)]
    bomb_positions = set()
    while len(bomb_positions) < num_bombs:
        bomb_positions.add((random.randint(0, size - 1), random.randint(0, size - 1)))
    return board, bomb_positions

def print_board(board, reveal=False, bomb_positions=None):
    print("   " + " ".join([str(i) for i in range(len(board))]))
    print("  " + "---" * len(board))
    for i, row in enumerate(board):
        line = f"{i} | " + " | ".join(row) + " |"
        print(line)
        print("  " + "---" * len(board))
    if reveal and bomb_positions:
        print("As posições das bombas eram:", bomb_positions)

def play_game():
    size = 5
    num_bombs = 5
    board, bomb_positions = generate_board(size, num_bombs)
    uncovered = set()
    attempts = size * 2

    print("Bem vindo ao Campo Minado")
    print(f"Descubra todas as células sem detonar as bombas. Você tem {attempts} tentativas.\n")
    
    while attempts > 0:
        print_board(board)
        try:
            row = int(input("Insira a linha (0-4): "))
            col = int(input("Insira a coluna (0-4): "))
            if (row, col) in bomb_positions:
                board[row][col] = 'B'
                print_board(board, reveal=True, bomb_positions=bomb_positions)
                print("\nBoooom! Você detonou uma bomba. Fim de jogo.")
                return
            elif (row, col) in uncovered:
                print("Você já descobriu essa célula. Tente novamente.")
            else:
                board[row][col] = '.'
                uncovered.add((row, col))
                print("Boa! Continue.\n")
                if len(uncovered) == size * size - num_bombs:
                    print_board(board, reveal=True, bomb_positions=bomb_positions)
                    print("\nParabéns! Você descobriu todas as células seguras. Você venceu!")
                    return
        except (ValueError, IndexError):
            print("Entrada inválida. Entre com números entre 0 e 4.")

        attempts -= 1
        print(f"Tentativas restantes: {attempts}")
    
    print("\nTentativas acabaram. Fim de jogo.")
    print_board(board, reveal = True, bomb_positions = bomb_positions)

# Run the game
if __name__ == "__main__":
    play_game()

import random

def toss():
    return random.choice([1, 2])

def print_game_state(stones_left, Player):
    print(f"Stones left: {stones_left}")
    print(f"Player {Player}'s turn")

def Game_Over(stones_left):
    return stones_left == 0

def player_move(stones_left):
    while True:
        move = input("Enter number of stones to remove (1 or 2): ")
        if move in ['1', '2'] and 1 <= int(move) <= min(2, stones_left):
            return int(move)

def generate_children(stones_left, Player):
    children = []
    for move in range(1, min(3, stones_left + 1)):
        children.append((stones_left - move, 3 - Player))
    return children


def Alpha_Beta_Pruning(stones_left, Player, alpha, beta, memo):
    if (stones_left, Player) in memo:
        return memo[(stones_left, Player)]


    if Game_Over(stones_left):
        if Player == 1:
            return -1
        else:
            return 1

    if Player == 1:
        value = float('-inf')
        for child in generate_children(stones_left, Player):
            value = max(value, Alpha_Beta_Pruning(child[0], child[1], alpha, beta, memo))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        memo[(stones_left, Player)] = value
        return value
    else:
        value = float('inf')
        for child in generate_children(stones_left, Player):
            value = min(value, Alpha_Beta_Pruning(child[0], child[1], alpha, beta, memo))
            beta = min(beta, value)
            if alpha >= beta:
                break
        memo[(stones_left, Player)] = value
        return value

def AI_Move(stones_left):
    best_move = None
    best_value = float('-inf')
    memo = {}
    for move in range(1, min(3, stones_left + 1)):
        value = Alpha_Beta_Pruning(stones_left - move, 2, float('-inf'), float('inf'), memo)
        if value > best_value:
            best_move = move
            best_value = value
    return best_move

def Play_Start():
    stones_left = 50
    Player = toss()
    while not Game_Over(stones_left):
        print_game_state(stones_left, Player)
        if Player == 1:
            move = player_move(stones_left)
        else:
            move = AI_Move(stones_left)
            print(f"AI removes {move} stones")
        stones_left -= move
        Player = 3 - Player
    print(f"Player {Player} Loses!")

Play_Start()
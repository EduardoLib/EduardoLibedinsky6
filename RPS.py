


def counter_move(last_move):
    if last_move == 'R':
        return 'P'  # Papel vence a Piedra
    elif last_move == 'P':
        return 'S'  # Tijeras vence a Papel
    elif last_move == 'S':
        return 'R'  # Piedra vence a Tijeras




def player(prev_play, opponent_history=[]):
    # Guardar la jugada del oponente en el historial, si no es una jugada vacía
    if prev_play != "":
        opponent_history.append(prev_play)

    # Inicializar una jugada predeterminada
    guess = "R"  # Valor inicial para evitar que "guess" quede sin definir

    # Implementar la estrategia basada en el historial del oponente
    if len(opponent_history) > 2:
        last_move = opponent_history[-1]  # Última jugada del oponente
        guess = counter_move(last_move)  # Predecir basándose en la última jugada

    return guess  # Asegúrate de que siempre devuelva "R", "P" o "S"




def quincy(prev_play, counter=[0]):

    counter[0] += 1
    choices = ["R", "R", "P", "P", "S"]
    return choices[counter[0] % len(choices)]




def play(player1, player2, num_games, verbose=False): 
    p1_prev_play = ""
    p2_prev_play = ""
    results = {"p1": 0, "p2": 0, "tie": 0}

    for _ in range(num_games):
        p1_play = player1(p2_prev_play)
        p2_play = player2(p1_prev_play)

        if p1_play == p2_play:
            results["tie"] += 1
            winner = "Tie."
        elif (p1_play == "P" and p2_play == "R") or (
                p1_play == "R" and p2_play == "S") or (p1_play == "S"
                                                       and p2_play == "P"):
            results["p1"] += 1
            winner = "Player 1 wins."
        else:
            results["p2"] += 1
            winner = "Player 2 wins."  # Asegúrate de que siempre se asigna "winner"

        if verbose:
            print("Player 1:", p1_play, "| Player 2:", p2_play)
            print(winner)
            print()

        p1_prev_play = p1_play
        p2_prev_play = p2_play

    games_won = results['p2'] + results['p1']

    if games_won == 0:
        win_rate = 0
    else:
        win_rate = results['p1'] / games_won * 100

    print("Final results:", results)
    print(f"Player 1 win rate: {win_rate}%")

    return (win_rate)





play(player, quincy, 1000, verbose=True) #Simulación de 1000 partidas








# coding: utf-8

# In[158]:


from estrategias import *
import random
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# Función para calcular la puntuación
def calculate_score(player_move, opponent_move):
    if player_move == 'C' and opponent_move == 'C':
        return 3  # Ambos cooperan
    elif player_move == 'C' and opponent_move == 'T':
        return 0  # Jugador coopera, pero el oponente traiciona
    elif player_move == 'T' and opponent_move == 'C':
        return 5  # Jugador traiciona, pero el oponente coopera
    elif player_move == 'T' and opponent_move == 'T':
        return 1  # Ambos traicionan

# Función para jugar una ronda entre dos estrategias
def play_round(strategy1, strategy2, rounds):
    score1 = 0
    score2 = 0
    last_move1 = None
    last_move2 = None
    #
    for round_count in range(rounds):
        move1 = strategy1(last_move2, round_count)
        move2 = strategy2(last_move1, round_count)
        #
        score1 += calculate_score(move1, move2)
        score2 += calculate_score(move2, move1)
        #
        last_move1 = move1
        last_move2 = move2
        #
    return score1, score2

# Simulación de 200 iteraciones entre estrategias aleatorias
def simulate_tournament(estrategias, num_iterations=200, round_min=100, round_max=200):
    scores = {strategy_name: 0 for strategy_name in estrategias.keys()}
    #
    for _ in range(num_iterations):
        # Seleccionar dos estrategias aleatorias para enfrentarse
        strategy1_name, strategy2_name = random.sample(list(estrategias.keys()), 2)
        strategy1 = estrategias[strategy1_name]
        strategy2 = estrategias[strategy2_name]
        #
        # Determinar número de rondas aleatorio (entre 100 y 200)
        rounds = random.randint(round_min, round_max)
        #
        # Si es una clase, usamos el método `move`, de lo contrario es función
        if isinstance(strategy1, (RetaliadorLento, AntiVengativo, AmistosoCondicional, Pacifista, TraicioneroTemprano, Calculador, Caotico, Oscilador, VengativoExtremo, RevanchaInstantanea, Pragmatico, Adaptativo, Implacable, Investigador)):
            score1, score2 = play_round(strategy1.move, strategy2.move if isinstance(strategy2, (RetaliadorLento, AntiVengativo, AmistosoCondicional, Pacifista, TraicioneroTemprano, Calculador, Caotico, Oscilador, VengativoExtremo, RevanchaInstantanea, Pragmatico, Adaptativo, Implacable, Investigador)) else strategy2, rounds)
        else:
            score1, score2 = play_round(strategy1, strategy2.move if isinstance(strategy2, (RetaliadorLento, AntiVengativo, AmistosoCondicional, Pacifista, TraicioneroTemprano, Calculador, Caotico, Oscilador, VengativoExtremo, RevanchaInstantanea, Pragmatico, Adaptativo, Implacable, Investigador)) else strategy2, rounds)
            #
        #
        # Actualizar puntuaciones
        scores[strategy1_name] += score1
        scores[strategy2_name] += score2
        #
    return scores



 # Función para graficar los resultados del torneo
def plot_results(scores):
    strategies = list(scores.keys())
    final_scores = list(scores.values())
    #
    # Ordenar las estrategias según sus puntuaciones finales
    sorted_indices = sorted(range(len(final_scores)), key=lambda k: final_scores[k], reverse=True)
    sorted_strategies = [strategies[i] for i in sorted_indices]
    sorted_scores = [final_scores[i] for i in sorted_indices]
    #
    # Definir colores para estrategias nice y nasty
    colors = []
    nice_strategies = [
        'Tit for Tat', 'Tit for Two Tats', 'Generoso', 'Retaliador Lento',
        'Tit for Tat modificado', 'Detective', 'Anti-Vengativo', 
        'Amistoso Condicional', 'Pacifista', 'Generoso Tit for Tat', 
        'Investigador'
    ]
    nasty_strategies = [
        'Traicionero Temprano', 'Calculador', 'Caótico', 
        'Oscilador', 'Vengativo Extremo', 'Revancha Instantánea', 
        'Pragmático', 'Adaptativo', 'Implacable', 'Desconfiado modificado', 'Random'
    ]
    #
    for strategy in sorted_strategies:
        if strategy in nice_strategies:
            colors.append('green')  # Nice strategies in green
        elif strategy in nasty_strategies:
            colors.append('red')  # Nasty strategies in red
        else:
            colors.append('gray')  # Default color for others
    #
    # Crear gráfico
    plt.figure(figsize=(10, 6))
    plt.barh(sorted_strategies, sorted_scores, color=colors)
    plt.xlabel('Total Score')
    plt.ylabel('Strategy')
    plt.title('Prisoner\'s Dilemma Tournament Results')
    plt.gca().invert_yaxis()  # Invertir el eje y para mostrar al ganador en la parte superior
    plt.show(block=False)

# Lista de estrategias (añadiendo `Tit for Tat` y `Random`)
estrategias = {
    'Tit for Tat': tit_for_tat,
    'Tit for Two Tats': tit_for_two_tats,
    'Generoso': generoso,
    'Retaliador Lento': RetaliadorLento(),
    'Tit for Tat modificado': tit_for_tat_modificado,
    'Detective': detective,
    'Anti-Vengativo': AntiVengativo(),
    'Amistoso Condicional': AmistosoCondicional(),
    'Pacifista': Pacifista(),
    'Generoso Tit for Tat': generoso_tit_for_tat,
    'Investigador': Investigador(),
    'Traicionero Temprano': TraicioneroTemprano(),
    'Calculador': Calculador(),
    'Desconfiado modificado': desconfiado_modificado,
    'Caótico': Caotico(),
    'Oscilador': Oscilador(),
    'Vengativo Extremo': VengativoExtremo(),
    'Revancha Instantánea': RevanchaInstantanea(),
    'Pragmático': Pragmatico(),
    'Adaptativo': Adaptativo(),
    'Implacable': Implacable(),
    'Random': random_strategy,
}


# Definir listas para estrategias nice y nasty
estrategias_nice = {
    'Tit for Tat': tit_for_tat,
    'Tit for Two Tats': tit_for_two_tats,
    'Generoso': generoso,
    'Retaliador Lento': RetaliadorLento(),
    'Tit for Tat modificado': tit_for_tat_modificado,
    'Detective': detective,
    'Anti-Vengativo': AntiVengativo(),
    'Amistoso Condicional': AmistosoCondicional(),
    'Pacifista': Pacifista(),
    'Generoso Tit for Tat': generoso_tit_for_tat,
    'Investigador': Investigador(),
    'Random': random_strategy,
}

estrategias_a_usar = {
    'Tit for Tat': tit_for_tat,
    'Traicionero Temprano': TraicioneroTemprano(),
    'Calculador': Calculador(),
    'Desconfiado modificado': desconfiado_modificado,
    'Caótico': Caotico(),
    'Oscilador': Oscilador(),
    'Vengativo Extremo': VengativoExtremo(),
    'Revancha Instantánea': RevanchaInstantanea(),
    'Pragmático': Pragmatico(),
    'Random': random_strategy,
    'Adaptativo': Adaptativo(),
    'Implacable': Implacable(),
    'Random': random_strategy,
}




# Simulación de torneos para calcular la matriz de puntuaciones
def calculate_score_matrix(estrategias, num_iterations=200, round_min=10, round_max=20):
    strategy_names = list(estrategias.keys())
    n = len(strategy_names)
    score_matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            if i != j:  # No enfrentamos la misma estrategia
                total_score1 = 0
                total_score2 = 0
                for _ in range(num_iterations):
                    # Determinar número de rondas aleatorio (entre 10 y 20)
                    rounds = random.randint(round_min, round_max)
                    strategy1_name, strategy2_name = random.sample(list(estrategias.keys()), 2)
                    strategy1 = estrategias[strategy1_name]
                    strategy2 = estrategias[strategy2_name]
        			#
                    # Si es una clase, usamos el método `move`, de lo contrario es función
                    if isinstance(strategy1, (RetaliadorLento, AntiVengativo, AmistosoCondicional, Pacifista, TraicioneroTemprano, Calculador, Caotico, Oscilador, VengativoExtremo, RevanchaInstantanea, Pragmatico, Adaptativo, Implacable, Investigador)):
                        score1, score2 = play_round(strategy1.move, strategy2.move if isinstance(strategy2, (RetaliadorLento, AntiVengativo, AmistosoCondicional, Pacifista, TraicioneroTemprano, Calculador, Caotico, Oscilador, VengativoExtremo, RevanchaInstantanea, Pragmatico, Adaptativo, Implacable, Investigador)) else strategy2, rounds)
                    else:
                        score1, score2 = play_round(strategy1, strategy2.move if isinstance(strategy2, (RetaliadorLento, AntiVengativo, AmistosoCondicional, Pacifista, TraicioneroTemprano, Calculador, Caotico, Oscilador, VengativoExtremo, RevanchaInstantanea, Pragmatico, Adaptativo, Implacable, Investigador)) else strategy2, rounds)
                    
                    score1, score2 = play_round(estrategias[strategy_names[i]], estrategias[strategy_names[j]], rounds)
                    total_score1 += score1
                    total_score2 += score2
                score_matrix[i, j] = total_score1  # Guardar la puntuación del jugador i contra el jugador j

    return score_matrix, strategy_names

# Función para graficar el heatmap
def plot_heatmap(score_matrix, strategy_names):
    plt.figure(figsize=(12, 10))
    sns.heatmap(score_matrix, annot=True, fmt=".1f", cmap='YlGnBu', xticklabels=strategy_names, yticklabels=strategy_names)
    plt.title('Heatmap of Strategy Scores in Prisoner\'s Dilemma')
    plt.xlabel('Strategies')
    plt.ylabel('Strategies')
    plt.show(block=False)





num_iterations=100
round_min=250
round_max=350


scores = simulate_tournament(estrategias, num_iterations=num_iterations, round_min=round_min, round_max=round_max)
# Graficar los resultados
plot_results(scores)
# Calcular la matriz de puntuaciones
score_matrix, strategy_names = calculate_score_matrix(estrategias, num_iterations=num_iterations, round_min=round_min, round_max=round_max)
# Graficar el heatmap
plot_heatmap(score_matrix, strategy_names)


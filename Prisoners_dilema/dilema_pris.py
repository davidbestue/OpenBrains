# coding: utf-8


import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Estrategia Tit for Tat: coopera en la primera ronda y luego repite lo que el oponente hizo en la ronda anterior.
class TitForTat:
    def __init__(self):
        self.name = "Tit for Tat"
        self.last_opponent_move = None
    
    def play(self, opponent_history, round_count):
        if round_count == 0:
            return "C"
        return opponent_history[-1] if opponent_history else "C"

# Pacifista: coopera siempre hasta que lo traicionan, luego traiciona siempre.
class Pacifista:
    def __init__(self):
        self.name = "Pacifista"
        self.betrayed = False
    
    def play(self, opponent_history, round_count):
        if self.betrayed:
            return "T"
        elif "T" in opponent_history:
            self.betrayed = True
            return "T"
        else:
            return "C"

# Cooperador con traición periódica: coopera pero traiciona cada 10 rondas.
class CooperadorConTraicionPeriodica:
    def __init__(self):
        self.name = "Cooperador con Traicion Periodica"
    
    def play(self, opponent_history, round_count):
        if (round_count + 1) % 10 == 0:
            return "T"
        else:
            return "C"

# Sneaky: como Tit for Tat, pero traiciona aleatoriamente en el 10% de las rondas.
class Sneaky:
    def __init__(self):
        self.name = "Sneaky"
    
    def play(self, opponent_history, round_count):
        if random.random() < 0.1:
            return "T"
        elif round_count == 0:
            return "C"
        else:
            return opponent_history[-1] if opponent_history else "C"

# Estrategia Always Defect: siempre traiciona, independientemente del oponente.
class AlwaysDefect:
    def __init__(self):
        self.name = "Always Defect"
    
    def play(self, opponent_history, round_count):
        return "T"

# Estrategia Nice: siempre coopera, independientemente del oponente.
class AlwaysCooperate:
    def __init__(self):
        self.name = "Always Cooperate"
    
    def play(self, opponent_history, round_count):
        return "C"

# Desconfiado: comienza traicionando y sigue traicionando si lo traicionan.
class Desconfiado:
    def __init__(self):
        self.name = "Desconfiado"
        self.betrayed = False
    
    def play(self, opponent_history, round_count):
        if round_count == 0:
            return "T"
        if self.betrayed:
            return "T"
        elif "T" in opponent_history:
            self.betrayed = True
            return "T"
        else:
            return "C"



class TitForTwoTats:
    def __init__(self):
        self.name = "Tit for Two Tats"
        self.last_opponent_moves = []
    
    def play(self, opponent_history, round_count):
        # Guarda las últimas dos acciones del oponente
        self.last_opponent_moves.append(opponent_history[-1] if opponent_history else "C")
        if len(self.last_opponent_moves) > 2:
            self.last_opponent_moves.pop(0)
        
        # Coopera en la primera ronda o si las dos últimas acciones del oponente fueron cooperaciones
        if round_count == 0 or self.last_opponent_moves == ["C", "C"]:
            return "C"
        # Si el oponente ha traicionado dos veces consecutivas, traiciona
        elif self.last_opponent_moves == ["T", "T"]:
            return "T"
        else:
            return "C"



class GenerousTitForTat:
    def __init__(self):
        self.name = "Generous Tit for Tat"
        self.last_opponent_move = None
    
    def play(self, opponent_history, round_count):
        if round_count == 0:
            return "C"
        
        # Decide traicionar con un 90% de probabilidad si el oponente traiciona
        if opponent_history and opponent_history[-1] == "T":
            return "T" if random.random() < 0.9 else "C"
        
        return "C"




# Estrategia Aleatoria: decide aleatoriamente entre cooperar o traicionar.
class RandomStrategy:
    def __init__(self):
        self.name = "Random"
    
    def play(self, opponent_history, round_count):
        return random.choice(["C", "T"])





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




# Función que simula un juego entre dos estrategias
def play_game(strategy1, strategy2, num_rounds):
    strategy1_instance = strategy1()
    strategy2_instance = strategy2()

    history1 = []
    history2 = []

    score1 = 0
    score2 = 0

    for round_count in range(num_rounds):
        move1 = strategy1_instance.play(history2, round_count)
        move2 = strategy2_instance.play(history1, round_count)

        if move1 == "C" and move2 == "C":
            score1 += 3
            score2 += 3
        elif move1 == "C" and move2 == "T":
            score1 += 0
            score2 += 5
        elif move1 == "T" and move2 == "C":
            score1 += 5
            score2 += 0
        elif move1 == "T" and move2 == "T":
            score1 += 1
            score2 += 1

        history1.append(move1)
        history2.append(move2)

    return score1, score2




# Función que simula un torneo con selección aleatoria de estrategias
def run_tournament(strategies, num_iterations=1000, min_rounds=180, max_rounds=220):
    num_strategies = len(strategies)
    score_matrix = np.zeros((num_strategies, num_strategies))
    total_rounds = 0
    strategy_names = [strategy_class().name for strategy_name, strategy_class in strategies.items()] 

    for _ in range(num_iterations):
        # Seleccionar dos estrategias aleatoriamente
        strategy1_idx, strategy2_idx = random.sample(range(num_strategies), 2)
        strategy1 = strategies[strategy1_idx]
        strategy2 = strategies[strategy2_idx]
        
        # Elegir número aleatorio de rondas entre min_rounds y max_rounds
        num_rounds = random.randint(min_rounds, max_rounds)
        total_rounds += num_rounds

        # Jugar el juego entre las dos estrategias seleccionadas
        score1, score2 = play_game(strategy1, strategy2, num_rounds)
        score_matrix[strategy1_idx][strategy2_idx] += score1
        score_matrix[strategy2_idx][strategy1_idx] += score2
    
    # Calcular el número promedio de rondas
    average_rounds = total_rounds / num_iterations
    return score_matrix, strategy_names, average_rounds




# Función para graficar el heatmap con valores normalizados
def plot_heatmap(score_matrix, strategy_names, average_rounds):
    # Normalizar las puntuaciones dividiéndolas por el máximo valor de la matriz
    normalized_matrix = score_matrix / np.max(score_matrix)
    
    plt.figure(figsize=(12, 10))
    sns.heatmap(normalized_matrix, annot=True, fmt=".2f", cmap='viridis', 
                xticklabels=strategy_names, yticklabels=strategy_names)
    plt.title(f'Heatmap of Strategy Scores in Prisoner\'s Dilemma\nAverage Rounds: {average_rounds:.2f}')
    plt.xlabel('Strategies')
    plt.ylabel('Strategies')
    plt.show(block=False)

# Función para graficar las puntuaciones totales de las estrategias, normalizadas y en orientación vertical
# Función para graficar las puntuaciones totales de las estrategias, diferenciando entre "nice" y "nasty"
def plot_strategy_scores(score_matrix, strategy_names, average_rounds):
    # Calcular la suma de las puntuaciones de cada estrategia y normalizar
    total_scores = np.sum(score_matrix, axis=1)
    normalized_scores = total_scores / np.max(total_scores)  # Normalizar puntuaciones

    # Definir qué estrategias son "nice" y cuáles son "nasty"
    nice_strategies = ['Tit for Tat', 'Tit for Two Tats', 'Pacifista', 'Generous Tit for Tat', 'Always Cooperate']
    nasty_strategies = [ 'Cooperador con Traicion Periodica', 'Sneaky', 'Always Defect', 'Desconfiado', 'Random']

    # Ordenar las puntuaciones de mayor a menor
    sorted_indices = np.argsort(normalized_scores)[::-1]
    sorted_names = np.array(strategy_names)[sorted_indices]
    sorted_scores = normalized_scores[sorted_indices]

    # Asignar colores: verde para "nice" y rojo para "nasty"
    colors = ['green' if strategy in nice_strategies else 'red' for strategy in sorted_names]

    # Graficar el resultado con un gráfico de barras vertical (barras horizontales)
    plt.figure(figsize=(8, 10))
    plt.barh(sorted_names, sorted_scores, color=colors)  # Gráfico de barras horizontal con colores diferenciados
    plt.gca().invert_yaxis()  # Invertir el eje Y para que la estrategia con más puntos esté arriba
    plt.title(f'Normalized Total Points Scored by Strategies\nAverage Rounds: {average_rounds:.2f}')
    plt.xlabel('Normalized Total Points')
    plt.ylabel('Strategies')
    plt.tight_layout()
    plt.show(block=False)



# Lista de estrategias 
strategies = {
    "Tit for Tat": TitForTat,
    "Pacifista": Pacifista,
    "Cooperador con Traicion Periodica": CooperadorConTraicionPeriodica,
    "Sneaky": Sneaky,
    "Always Defect": AlwaysDefect,
    "Always Cooperate": AlwaysCooperate,
    "Desconfiado": Desconfiado,
    "Random": RandomStrategy,
    "Tit for Two Tats": TitForTwoTats,  # Estrategia corregida
    "Generous Tit for Tat": GenerousTitForTat  # Nueva estrategia añadida
}



# Simular el torneo
score_matrix, strategy_names, average_rounds = run_tournament(strategies=strategies, num_iterations=1000, min_rounds=380, max_rounds=420)

# Graficar el heatmap
plot_heatmap(score_matrix, strategy_names, average_rounds)

# Graficar las puntuaciones totales
plot_strategy_scores(score_matrix, strategy_names, average_rounds)

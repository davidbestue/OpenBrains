import random
import matplotlib.pyplot as plt

# Estrategias "Nice" (Cooperativas)
def tit_for_tat(last_opponent_move, round_count):
    # Coopera en la primera ronda, luego imita la última acción del oponente.
    if last_opponent_move is None:
        return 'C'
    return last_opponent_move

def tit_for_two_tats(last_opponent_move, round_count):
    # Coopera a menos que el oponente traicione dos veces seguidas.
    if last_opponent_move is None or len(last_opponent_move) < 2:
        return 'C'
    return 'T' if last_opponent_move[-1] == 'T' and last_opponent_move[-2] == 'T' else 'C'

def generoso(last_opponent_move, round_count):
    # Coopera siempre, pero si es traicionado, traiciona la mitad de las veces.
    if last_opponent_move == 'T' and random.random() < 0.5:
        return 'T'
    return 'C'

class RetaliadorLento:
    # Solo traiciona si ha sido traicionado tres veces consecutivas.
    def __init__(self):
        self.betrayal_streak = 0

    def move(self, last_opponent_move, round_count):
        if last_opponent_move == 'T':
            self.betrayal_streak += 1
        else:
            self.betrayal_streak = 0
        return 'T' if self.betrayal_streak >= 3 else 'C'

def tit_for_tat_modificado(last_opponent_move, round_count):
    # Variante del Tit for Tat que perdona al oponente una vez antes de imitar.
    if last_opponent_move is None:
        return 'C'
    return 'C' if last_opponent_move == 'T' else 'C' if random.random() < 0.5 else 'T'

def detective(last_opponent_move, round_count):
    # Comienza cooperando y luego investiga el comportamiento del oponente para decidir.
    if round_count < 2:
        return 'C'
    return tit_for_tat(last_opponent_move, round_count)

class AntiVengativo:
    # Siempre coopera, incluso si es traicionado. Da una oportunidad de redención.
    def move(self, last_opponent_move, round_count):
        if last_opponent_move == 'T':
            return 'C'
        return 'C'

class AmistosoCondicional:
    # Coopera si el oponente ha cooperado más veces que ha traicionado.
    def __init__(self):
        self.cooperaciones = 0
        self.traiciones = 0

    def move(self, last_opponent_move, round_count):
        if last_opponent_move == 'T':
            self.traiciones += 1
        else:
            self.cooperaciones += 1
        return 'C' if self.cooperaciones > self.traiciones else 'T'

class Pacifista:
    # Siempre coopera a menos que haya sido traicionado. Entonces coopera tres veces antes de evaluar.
    def __init__(self):
        self.traicionado = False

    def move(self, last_opponent_move, round_count):
        if last_opponent_move == 'T':
            self.traicionado = True
        if self.traicionado:
            return 'C'
        return 'C'

def generoso_tit_for_tat(last_opponent_move, round_count):
    # Perdona una traición cada tres rondas. Basado en Tit for Tat.
    if last_opponent_move == 'T' and round_count % 3 == 0:
        return 'C'
    return tit_for_tat(last_opponent_move, round_count)

class Investigador:
    # Investiga al oponente. Si es traicionado tres veces en cinco rondas, empieza a traicionar.
    def __init__(self):
        self.betrayal_count = 0
        self.round_count = 0

    def move(self, last_opponent_move, round_count):
        self.round_count += 1
        if last_opponent_move == 'T':
            self.betrayal_count += 1
        if self.betrayal_count >= 3 and self.round_count >= 5:
            return 'T'
        return 'C'

# Estrategias "Nasty" (Agresivas)
class TraicioneroTemprano:
    # Coopera en las primeras dos rondas y luego traiciona constantemente.
    def __init__(self):
        self.round = 0

    def move(self, last_opponent_move, round_count):
        self.round += 1
        return 'C' if self.round <= 2 else 'T'

class Calculador:
    # Coopera en las primeras cuatro rondas, luego traiciona con una probabilidad del 80%.
    def __init__(self):
        self.round = 0

    def move(self, last_opponent_move, round_count):
        self.round += 1
        return 'C' if self.round <= 4 else 'T' if random.random() < 0.8 else 'C'

def desconfiado_modificado(last_opponent_move, round_count):
    # Variante del desconfiado que traiciona con un 50% de probabilidad en cualquier ronda.
    return 'T' if random.random() < 0.5 else 'C'

class Caotico:
    # Traiciona en las dos primeras rondas y luego decide aleatoriamente con un 60% de probabilidad de traicionar.
    def __init__(self):
        self.round = 0

    def move(self, last_opponent_move, round_count):
        self.round += 1
        if self.round <= 2:
            return 'T'
        return 'T' if random.random() < 0.6 else 'C'

class Oscilador:
    # Alterna entre cooperar y traicionar en cada ronda.
    def __init__(self):
        self.round = 0

    def move(self, last_opponent_move, round_count):
        self.round += 1
        return 'C' if self.round % 2 == 1 else 'T'

class VengativoExtremo:
    # Coopera al inicio, pero si es traicionado una vez, nunca vuelve a cooperar.
    def __init__(self):
        self.has_been_betrayed = False

    def move(self, last_opponent_move, round_count):
        if last_opponent_move == 'T':
            self.has_been_betrayed = True
        return 'T' if self.has_been_betrayed else 'C'

class RevanchaInstantanea:
    # Si el oponente traiciona, inmediatamente devuelve la traición en la siguiente ronda, pero vuelve a cooperar después.
    def move(self, last_opponent_move, round_count):
        return 'T' if last_opponent_move == 'T' else 'C'

class Pragmatico:
    # Coopera en rondas impares y traiciona en rondas pares.
    def __init__(self):
        self.round = 0

    def move(self, last_opponent_move, round_count):
        self.round += 1
        return 'C' if self.round % 2 == 1 else 'T'

class Adaptativo:
    # Si es traicionado más de tres veces, traiciona el resto del juego.
    def __init__(self):
        self.betrayals_received = 0

    def move(self, last_opponent_move, round_count):
        if last_opponent_move == 'T':
            self.betrayals_received += 1
        return 'T' if self.betrayals_received >= 3 else 'C'

class Implacable:
    # Siempre traiciona después de dos cooperaciones iniciales.
    def __init__(self):
        self.round = 0

    def move(self, last_opponent_move, round_count):
        self.round += 1
        return 'C' if self.round <= 2 else 'T'

# Estrategia completamente aleatoria
def random_strategy(last_opponent_move, round_count):
    # Decide aleatoriamente en cada ronda si coopera o traiciona.
    return random.choice(['C', 'T'])

# Lista de estrategias (22 estrategias en total)
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

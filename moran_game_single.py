import abc
import collections
import copy
import random
import sys
import traceback
from collections import Counter
from typing import List, Dict

import matplotlib.pyplot as plt
import networkx as nx
import seaborn as sns  # for color palettes


class Player:
    # p: Parameters  # The parameters object of the game
    # g: graph  # The graph/network of the game
    name: str  # name of the number
    version: str  # name of the team (e.g. omada 01)
    player_id: int  # id of the player
    my_type: str  # type of the player
    player_seed: int  # seed of random number generator of the player (not the global seed of the game)

    # constructor
    def __init__(self):
        self.rng = None
        self.game_info = None

    def __repr__(self):
        return f"Player()"

    def __str__(self):
        return f"Player({self.name}, {self.version}, {self.player_id}, {self.my_type})"

    @abc.abstractmethod
    def initialize(self, game_info, player_id, my_type, player_seed) -> None:
        pass

    @abc.abstractmethod
    def move(self, node) -> int:
        pass


class PlayerRuntime:
    player_class: Player
    player: Player
    player_id: int
    player_type: str

    # constructor
    def __init__(self):
        pass

    def __repr__(self):
        return "Player_Runtime()"

    def __str__(self):
        return


class Parameters:
    num_of_players: int  # the number of distinct players
    n: int  # number of nodes
    m: int  # number of edges per new node (Barabasi-Albert)
    seed: int  # seed of random number generator
    steps: int  # maximum number of steps
    assignment: list  # the assignment of strategies to the players (or else, the order of the players)
    interactive: bool  # flag: interactive execution, else batch execution

    # constructor
    def __init__(self, num_of_players, n, m, steps, seed, assignment, interactive):
        self.num_of_players = num_of_players
        self.n = n
        self.m = m
        self.steps = steps
        self.seed = seed
        self.interactive = interactive
        self.assignment = assignment

        self.player_ids = range(self.num_of_players)
        self.player_labels = {player_id: chr(65 + player_id) for player_id in self.player_ids}
        self.player_colors = sns.color_palette("tab10")

    def __repr__(self):
        return "Parameters()"

    def __str__(self):
        return f"num_of_players:{self.num_of_players}, n:{self.n}, m:{self.m}, assignment:{self.assignment}, seed:{self.seed}, interactive:{self.interactive} "


game_move = collections.namedtuple('game_move', ('step', 'player_type', 'node_from', 'node_to', 'type_from'))


class GameInfo:
    g: nx.graph  # The graph/network of the game
    num_of_players: int  # the number of distinct players
    n: int  # number of nodes
    m: int  # number of edges per new node (Barabasi-Albert)
    interactive: bool  # flag: interactive execution, else batch execution
    history: List[game_move]
    initial_assignment = Dict

    # constructor
    def __init__(self, num_of_players, g, n, m, interactive):
        self.num_of_players = num_of_players
        self.g = g
        self.n = n
        self.m = m
        self.interactive = interactive
        self.initial_assignment = None
        self.history: List[game_move] = []

    def __repr__(self):
        return "Game_Info()"

    def __str__(self):
        return f"num_of_players:{self.num_of_players}, g:{self.g}, n:{self.n}, m:{self.m}, interactive:{self.interactive} "

    def get_number_of_active_players(self):
        node_types = nx.get_node_attributes(self.g, "types")
        type_values = [k[0] for k in node_types.values()]
        counter = Counter(type_values)
        distinct_type_keys = counter.keys()
        distinct_type_counts = counter.values()

        # distinct_type_values = set(type_values)
        num_of_distinct_type_values = len(distinct_type_keys)
        return counter, num_of_distinct_type_values, distinct_type_keys, distinct_type_counts


class PlayerOne(Player):
    def initialize(self, game_info, player_id, my_type, player_seed) -> None:
        # This function is called once before the game starts.
        # Can be used for initializing auxiliary data of the player
        self.name = 'Omada 1'
        self.version = '0.1'

        self.game_info = game_info
        self.player_id = player_id
        self.my_type = my_type
        self.player_seed = player_seed
        self.rng = random.Random(self.player_seed)

    def move(self, node) -> int:
        # This function is called everytime player b has been selected for a move

        neighbors = self.game_info.g.neighbors(node)
        list_of_neighbors = list(neighbors)
        node_types = nx.get_node_attributes(self.game_info.g, "types")

        # Choose first foreign neighbor
        targets = [v for v in list_of_neighbors if node_types[v] != self.my_type]
        node = None
        if targets:
            node = targets[0]
        return node


class PlayerTwo(Player):
    def initialize(self, game_info, player_id, my_type, player_seed) -> None:
        # This function is called once before the game starts.
        # Can be used for initializing auxiliary data of the player
        self.name = 'Omada 2'
        self.version = '0.1'

        self.game_info = game_info
        self.player_id = player_id
        self.my_type = my_type
        self.player_seed = player_seed
        self.rng = random.Random(self.player_seed)

    def move(self, node) -> int:
        # This function is called everytime player b has been selected for a move

        neighbors = self.game_info.g.neighbors(node)
        list_of_neighbors = list(neighbors)
        node_types = nx.get_node_attributes(self.game_info.g, "types")

        # Choose first foreign neighbor
        targets = [v for v in list_of_neighbors if node_types[v] != self.my_type]
        node = None
        if targets:
            node = targets[0]
        return node


class PlayerThree(Player):
    def initialize(self, game_info, player_id, my_type, player_seed) -> None:
        # This function is called once before the game starts.
        # Can be used for initializing auxiliary data of the player
        self.name = 'Omada 3'
        self.version = '0.1'

        self.game_info = game_info
        self.player_id = player_id
        self.my_type = my_type
        self.player_seed = player_seed
        self.rng = random.Random(self.player_seed)

    def move(self, node) -> int:
        # This function is called everytime player b has been selected for a move

        neighbors = self.game_info.g.neighbors(node)
        list_of_neighbors = list(neighbors)
        node_types = nx.get_node_attributes(self.game_info.g, "types")

        # Choose first foreign neighbor
        targets = [v for v in list_of_neighbors if node_types[v] != self.my_type]
        node = None
        if targets:
            node = targets[0]
        return node


class PlayerFour(Player):
    def initialize(self, game_info, player_id, my_type, player_seed) -> None:
        # This function is called once before the game starts.
        # Can be used for initializing auxiliary data of the player
        self.name = 'Omada 4'
        self.version = '0.1'

        self.game_info = game_info
        self.id = player_id
        self.my_type = my_type
        self.player_seed = player_seed
        self.rng = random.Random(self.player_seed)

    def move(self, node) -> int:
        # This function is called everytime player b has been selected for a move

        neighbors = self.game_info.g.neighbors(node)
        list_of_neighbors = list(neighbors)
        node_types = nx.get_node_attributes(self.game_info.g, "types")

        # Choose first foreign neighbor
        targets = [v for v in list_of_neighbors if node_types[v] != self.my_type]
        node = None
        if targets:
            node = targets[0]
        return node


def draw_graph(g, node_pos, player_runtimes, counter):
    color_map = []
    node_types = nx.get_node_attributes(g, "types")
    for v in g.nodes:
        node_type = node_types[v]
        player_colors = sns.color_palette("tab10")
        color = player_colors[ord(node_type[0]) - 65]
        color_map.append(color)

    f = plt.figure(1)
    ax = f.add_subplot(1, 1, 1)
    for player_runtime in player_runtimes.values():
        player_id = player_runtime.player_id
        player_label = player_runtime.player_type
        num = counter[player_label]
        num_str = str(num).rjust(5)
        str_label = player_label + num_str
        str_name = '(' + player_runtime.player.name + ')'
        legend_label = str_label + ' ' + str_name.rjust(10)
        ax.plot([0], [0],
                color=player_colors[player_id],
                label=legend_label)

    nx.draw(g, pos=node_pos, node_color=color_map, with_labels=True)
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.75)
    plt.legend(loc='lower right')
    f.tight_layout()
    plt.show()


def get_random_node(g, rng) -> int:
    num_of_nodes = g.number_of_nodes()
    node = rng.randint(0, num_of_nodes - 1)
    return node


def run_moran_game(p, player_one_class=None):
    # Create random number generator
    rng = random.Random(p.seed)

    # Create random graph
    G = nx.barabasi_albert_graph(p.n, p.m, rng.randint(0, 10000000))

    # Player runtimes
    player_runtimes = dict()

    if p.num_of_players >= 1:
        player_runtimes[0] = PlayerRuntime()
        if player_one_class:
            player_runtimes[0].player_class = player_one_class
        else:
            player_runtimes[0].player_class = PlayerOne
    if p.num_of_players >= 2:
        player_runtimes[1] = PlayerRuntime()
        player_runtimes[1].player_class = PlayerTwo
    if p.num_of_players >= 3:
        player_runtimes[2] = PlayerRuntime()
        player_runtimes[2].player_class = PlayerThree
    if p.num_of_players >= 4:
        player_runtimes[3] = PlayerRuntime()
        player_runtimes[3].player_class = PlayerFour

    # Initial Assignment
    n = G.number_of_nodes()
    nodes_per_player = int(n / p.num_of_players)
    remainder = n % p.num_of_players

    number_of_nodes_of_player = dict()
    for i in range(p.num_of_players):
        if i == 0:
            # player 0 gets the remainder nodes
            number_of_nodes_of_player[i] = nodes_per_player + remainder
        else:
            number_of_nodes_of_player[i] = nodes_per_player

    node_type = dict()
    nodes_of_player = dict()
    unassigned_nodes = set(range(n))
    for i in range(p.num_of_players):
        nodes_i = rng.sample(list(unassigned_nodes), number_of_nodes_of_player[i])
        set_i = set(nodes_i)
        nodes_of_player[i] = set_i
        for v in set_i:
            node_type[v] = p.assignment[i]
        unassigned_nodes = set(unassigned_nodes) - set_i

    if len(unassigned_nodes) > 0:
        print(f'ERROR: Some nodes are still unassigned: {len(unassigned_nodes)}')

    types = []
    nx.set_node_attributes(G, types, "types")
    for v in G.nodes:
        t = node_type[v]
        label = p.player_labels[t]
        nx.set_node_attributes(G, {v: label}, name="types")

    game_info = GameInfo(p.num_of_players, G, p.n, p.m, p.interactive)

    # initial assignment
    game_info.game_initial_assignment = copy.deepcopy(node_type)

    # prepare history data structure
    game_info.history = []

    # Create player objects
    player_from_type = dict()
    for i, player_runtime in enumerate(player_runtimes.values()):
        # for player_type in player_classes:
        player_runtime.player = player_runtime.player_class()
        player_runtime.player_id = p.assignment[i]
        player_runtime.player_type = p.player_labels[p.assignment[i]]
        player_from_type[player_runtime.player_type] = i  # p.assignment[i]

    # Initialize players
    for player_runtime in player_runtimes.values():
        player_seed = rng.randint(0, 1000000)
        # player_runtime.player.initialize(G, p, player_runtime.player_id, player_runtime.player_type)
        player_runtime.player.initialize(game_info, player_runtime.player_id, player_runtime.player_type, player_seed)

    # types.append("A")
    if p.interactive:
        pos = nx.spring_layout(G)

    step = 0
    end_loop = False
    while not end_loop:
        random_node = get_random_node(G, rng)
        types = nx.get_node_attributes(G, "types")
        node_type = types[random_node][0]

        if node_type in p.player_labels.values():
            player_id = player_from_type[node_type]
            player_runtime = player_runtimes[player_id]
            move = player_runtime.player.move(random_node)
            if move not in list(G.neighbors(random_node)) and move != random_node and move is not None:
                raise Exception(f'Invalid move: Node {move} is not a neighbor of node {random_node} in step {step}')
        else:
            traceback.print_exc()
            sys.exit(f'Error: unexpected type: {type}')

        type_from = types.get(move, None)
        nx.set_node_attributes(G, {move: node_type}, name="types")
        game_info.history.append(game_move(step, node_type, random_node, move, type_from))
        counter, num_of_types, distinct_keys, distinct_counts = game_info.get_number_of_active_players()
        if p.interactive:
            print(f'{node_type}:{random_node} -> {move}')
            print(
                f'Step: {step}, Number of types: {num_of_types}, distinct_keys: {distinct_keys}, distinct_counts: {distinct_counts}')
        step += 1

        if p.interactive:
        #     draw_graph(G, pos, player_runtimes, counter)
            input("Press Enter to continue...")
        #     # time.sleep(0.1)

        if num_of_types == 1:
            end_loop = True
        elif p.steps is not None and step >= p.steps:
            # print(f'Maximum number of steps reached')
            end_loop = True

        if end_loop:
            # print(f'Parameters {p}, Fixation {distinct_keys} {distinct_counts} after {step} number of steps!')
            counters = {}
            for i in range(p.num_of_players):
                player_runtime = player_runtimes[i]
                counters[player_runtime.player.name + ':' + player_runtime.player.my_type] = counter[
                    player_runtime.player_type]
            # print(counters)
            if num_of_types == 1:
                node_types = nx.get_node_attributes(G, "types")
                player_type = node_types[0]
                player_id = player_from_type[player_type]
                player_name = player_runtimes[player_id].player.name
                fixation_info: str = player_name
            else:
                fixation_info: str = '-'
            # leading player
            max_value = max(distinct_counts)
            # max_index = distinct_counts.index(max_value)
            indices = [index for index, value in enumerate(distinct_counts) if value == max_value]
            winner_info: str = ""
            for player_index in indices:
                player_type = list(distinct_keys)[player_index]
                player_id = player_from_type[player_type]
                player_name = player_runtimes[player_id].player.name
                winner_info += player_name + " "
            result: str = f'Parameters: {p}, Fixation: {fixation_info.center(10, " ")}, Winner: {winner_info}, {step}: steps! '
            for s in counters.keys():
                result += s + ':' + str(counters[s]) + ','

            # prepare dict with #nodes per player_id
            score_per_player_id = {}
            for i in range(p.num_of_players):
                score_per_player_id[i] = 0
            for t in counter:
                score = counter[t]
                player_id = player_from_type[t]
                score_per_player_id[player_id] = score

            return result, score_per_player_id


def evaluate_player_in_multiple_games(player_class, player_id, num_of_games, num_of_players, n, m, steps, seed):
    total_score_of_player = 0
    total_maximum_possible_score = 0
    assignment = [(0, 1), (1, 0)]
    for i in range(num_of_games):
        p = Parameters(num_of_players=num_of_players, n=n, m=m, steps=steps, assignment=assignment[i % 2],
                       seed=seed + int(i / 2),
                       interactive=False)
        result, scores = run_moran_game(p, player_class)
        total_score_of_player += scores[player_id]
        total_maximum_possible_score += n
        print(result, scores)
    return total_score_of_player, total_maximum_possible_score

def check_player(player_score, total, threshold):
    if player_score >= threshold:
        return True
    else:
        return f'The player scored {player_score} out of {total} points but should score at least {threshold} points.'

if __name__ == "__main__":
    player_score, total = evaluate_player_in_multiple_games(PlayerOne, player_id=1, num_of_games=4, num_of_players=2, n=20, m=2, steps=100, seed=123)
    print(check_player(player_score, total, 50))
    print(f'Player score: {player_score}/{total}')

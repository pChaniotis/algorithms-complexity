import random

import networkx as nx
import random

def create_weighted_graph(n, p, max_weight = 10, seed=None):
    G = nx.gnp_random_graph(n, p, seed=seed, directed=False)

    rng = random.Random(seed)
    for (u, v, w) in G.edges(data=True):
        w['weight'] = rng.randint(1, max_weight)

    return G

def total_weight_of_sides(G, v, A, B):
    total_weight = 0
    # Complete the code

    return total_weight

def local_search_maxcut(G, A, B, seed):
    # Random Number Generator
    rng = random.Random(seed)
    # Use this random number generator if necessary.
    # For example rng.randint(0, 10) for a uniformly random integer r: 0 <= r <= 10

    # Complete the code


    # Return the partition
    return A, B

def check_cut_value(G, A, B, threshold):
    cut_value = nx.algorithms.cut_size(G, A, weight='weight')
    if cut_value >= threshold:
        return str(True)
    else:
        return f'The cut_value is {cut_value} but should be at least {threshold}.'

G = create_weighted_graph(12, 0.7, seed=12)

# Create a random partition (partition_A, partition_B)
# Complete the code

# Run local search
# A, B = local_search_maxcut(G, partition_A, partition_B, seed=123)

# Check the value
# print(check_cut_value(G, A, B, 199))

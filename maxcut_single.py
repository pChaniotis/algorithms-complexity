import networkx as nx
import matplotlib.pyplot as plt
import random

def create_weighted_graph(n, p, max_weight = 10, seed=None):
    G = nx.gnp_random_graph(n, p, seed=seed, directed=False)

    rng = random.Random(seed)
    for (u, v, w) in G.edges(data=True):
        w['weight'] = rng.randint(1, max_weight)

    return G

def total_weight_of_sides(G, v, A, B):
    sum_A = 0
    sum_B = 0
    is_A = False

    edge_attributes = nx.get_edge_attributes(G,"weight")
    for node in nx.all_neighbors(G,v):
        for a in A:
            if (a == v):
                is_A = True;
            if node == a:
                if (v,node) in edge_attributes:
                    sum_A += edge_attributes[(v,node)]
                else:
                    sum_A += edge_attributes[(node,v)]
        for b in B:
            if node == b:
                if (v,node) in edge_attributes:
                    sum_B += edge_attributes[(v,node)]
                else:
                    sum_B += edge_attributes[(node,v)]
        
                
    if is_A: 
        sum_own_side = sum_A 
        sum_other_side = sum_B
    else:
        sum_own_side = sum_B
        sum_other_side = sum_A
        
    return sum_own_side, sum_other_side


def local_search_maxcut(G, A, B, seed):
    # Random Number Generator
    rng = random.Random(seed)
    # Use this random number generator if necessary.
    # For example rng.randint(0, 10) for a uniformly random integer r: 0 <= r <= 10

    random_node_list = [rng.randint(0,len(G.nodes)-1),rng.randint(0,len(G.nodes)-1),rng.randint(0,len(G.nodes)-1),rng.randint(0,len(G.nodes)-1)]
    #random_node = max(G.degree(weight='weight'))[0]
    
    import itertools
    for random_node in random_node_list:
        for v in itertools.chain([random_node],nx.all_neighbors(G,random_node)):
                is_A = True if v in A else False
                this_side, other_side = total_weight_of_sides(G, v, A, B)

                if (this_side > other_side):
                    if(is_A):
                        A.remove(v)
                        B.append(v)
                    else:
                        B.remove(v)
                        A.append(v)
    
    return A, B

def check_cut_value(G, A, B, threshold):
    cut_value = nx.algorithms.cut_size(G, A, weight='weight')
    if cut_value >= threshold:
        return str(True)
    else:
        return f'The cut_value is {cut_value} but should be at least {threshold}.'

G = create_weighted_graph(12, 0.7, seed=12)
nx.draw(G,with_labels=True);
plt.savefig("A");

# Create a random partition (partition_A, partition_B)
nodes = list(G.nodes)
partition_A = nodes[0:6]
partition_B = nodes[6:12]

# Run local search
A, B = local_search_maxcut(G, partition_A, partition_B, seed=123)
print(A)
print(B)

# Check the value
print(check_cut_value(G, A, B, 199))

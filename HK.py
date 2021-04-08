import pprint
from collections import defaultdict


class Graph(object):

    def __init__(self, connections):
        self._graph = defaultdict(set)
        self.add_connections(connections)

    def add_connections(self, connections):

        for node1, node2 in connections:
            self._graph[node1].add(node2)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, (self._graph))

    @property
    def graph(self):
        return self._graph


def HopK(u_list, v_list, g):
    Dist_U = defaultdict(set)
    Dist_V = defaultdict(set)
    matches_U = defaultdict(set)
    matches_V = defaultdict(set)
    for u in u_list:
        matches_U[u] = None
    for v in v_list:
        matches_V[v] = None
    print("match_U dictionary")
    print(matches_U)
    print("match_V dictionary")
    print(matches_V)
    print(BFS(u_list, v_list, matches_U, matches_V, Dist_U, g))


def BFS(u_list, v_list, matches_U, matches_V, Dist_U, g):
    queue = []
    for u in u_list:
        if matches_U[u] is None:

            Dist_U[u] = 0
            queue.append(u)
        else:
             Dist_U[u] = float('inf')
    Dist_U[None] = float('inf')
    print(Dist_U)
    while len(queue) > 0:
        current_u = queue.pop(0)
        if Dist_U[current_u] < Dist_U[None]:
            for v in g.graph[current_u]:
                print(Dist_U[matches_V[v]])
                if Dist_U[matches_V[v]] == float('Inf'):
                    print("Yes it is none")
                    Dist_U[matches_V[v]] = Dist_U[current_u] + 1
                    queue.append(matches_V[v])
    print(Dist_U)
    return Dist_U[None] != float('inf')
connections = [('Au', 'Bv'), ('Bu', 'Cv'), ('Cu', 'Dv'),
               ('Du', 'Ev'), ('Eu', 'Fv'), ('Fu', 'Av')]

U = ('Au', 'Bu', 'Cu', 'Du', 'Eu', 'Fu')
V = ('Av', 'Bv', 'Cv', 'Dv', 'Ev', 'Fv')
print(connections)
g = Graph(connections)
HopK(U, V, g)
pretty_print = pprint.PrettyPrinter()
print(g.graph)

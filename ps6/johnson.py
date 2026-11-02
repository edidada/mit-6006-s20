INF = 99999     # distance magnitudes will not be larger than this number

def johnson(n, S):
    """All-pairs shortest paths using Bellman-Ford potentials and Dijkstra."""
    from heapq import heappop, heappush
    adjacency = [[] for _ in range(n)]
    for u, v, weight in S:
        if not (0 <= u < n and 0 <= v < n):
            raise ValueError('Edge endpoint outside graph')
        adjacency[u].append((v, weight))
    # A zero-edge super-source is equivalent to initializing every potential to zero.
    potential = [0] * n
    for iteration in range(n):
        changed = False
        for u, v, weight in S:
            candidate = potential[u] + weight
            if candidate < potential[v]:
                potential[v] = candidate
                changed = True
        if not changed:
            break
        if iteration == n - 1:
            return None
    result = []
    for source in range(n):
        distance = [float('inf')] * n
        distance[source] = 0
        frontier = [(0, source)]
        while frontier:
            cost, u = heappop(frontier)
            if cost != distance[u]:
                continue
            for v, weight in adjacency[u]:
                candidate = cost + weight + potential[u] - potential[v]
                if candidate < distance[v]:
                    distance[v] = candidate
                    heappush(frontier, (candidate, v))
        result.append(tuple(INF if value == float('inf') else value - potential[source] + potential[target]
                            for target, value in enumerate(distance)))
    return tuple(result)

####################################
# USE BUT DO NOT MODIFY CODE BELOW #
####################################
def bellman_ford(Adj, w, s):    # from R12
    '''
    Input: Adj | Direct access array mapping a vertex to a list of adjacencies
             w | Function w(u, v): weight of the edge from u to v
             s | Vertex where 0 <= s < |Adj|
    Output:  d | Direct access array mapping a vertex to distance from s
               |   or INF if v is not reachable from u
               |   or None if the input graph contains a negative-weight cycle
        parent | Direct access array mapping a vertex to parent on shortest path
    '''
    d = [INF for _ in Adj]
    parent = [None for _ in Adj]
    d[s], parent[s] = 0, None
    V = len(Adj)
    for k in range(V - 1):
        for u in range(V):
            for v in Adj[u]:
                if (d[v] > d[u] + w(u, v)) and (d[u] < INF):
                    d[v] = d[u] + w(u, v)
                    parent[v] = u
    for u in range(V):
        for v in Adj[u]:
            if d[v] > d[u] + w(u,v):
                return None
    return d, parent

def dijkstra(Adj, w, s):        # from R13
    '''
    Input: Adj | Direct access array mapping a vertex to a list of adjacencies
             w | Function w(u, v): non-negative weight of the edge from u to v
             s | Vertex where 0 <= s < |Adj|
    Output:  d | Direct access array mapping a vertex to distance from s
               |   or INF if v is not reachable from u
        parent | Direct access array mapping a vertex to parent on shortest path
    '''
    d = [INF for _ in Adj]
    parent = [None for _ in Adj]
    d[s], parent[s] = 0, None
    Q = PriorityQueue()
    V = len(Adj)
    for v in range(V):
        Q.insert(v, d[v])
    for _ in range(V):
        u = Q.extract_min()
        for v in Adj[u]:
            if (d[v] > d[u] + w(u, v)) and (d[u] < INF):
                d[v] = d[u] + w(u, v)
                parent[v] = u
            Q.decrease_key(v, d[v])
    return d, parent

class Item:
    def __init__(self, label, key):
        self.label, self.key = label, key

class PriorityQueue:
    def __init__(self):
        self.A = []
        self.label2idx = {}

    def min_heapify_up(self, c):            
        if c == 0: return
        p = (c - 1) // 2
        if self.A[p].key > self.A[c].key:   
            self.A[c], self.A[p] = self.A[p], self.A[c]         
            self.label2idx[self.A[c].label] = c
            self.label2idx[self.A[p].label] = p
            self.min_heapify_up(p)         

    def min_heapify_down(self, p):          
        if p >= len(self.A): return
        l = 2 * p + 1
        r = 2 * p + 2
        if l >= len(self.A): l = p
        if r >= len(self.A): r = p
        c = l if self.A[r].key > self.A[l].key else r 
        if self.A[p].key > self.A[c].key:             
            self.A[c], self.A[p] = self.A[p], self.A[c]         
            self.label2idx[self.A[c].label] = c
            self.label2idx[self.A[p].label] = p
            self.min_heapify_down(c)       

    def insert(self, label, key):
        self.A.append(Item(label, key))
        idx = len(self.A) - 1
        self.label2idx[self.A[idx].label] = idx
        self.min_heapify_up(idx)

    def extract_min(self):
        self.A[0], self.A[-1] = self.A[-1], self.A[0]
        self.label2idx[self.A[0].label] = 0
        del self.label2idx[self.A[-1].label]
        min_label = self.A.pop().label
        self.min_heapify_down(0)
        return min_label

    def decrease_key(self, label, key):
        if label in self.label2idx:
            idx = self.label2idx[label]
            if key < self.A[idx].key:
                self.A[idx].key = key
                self.min_heapify_up(idx)

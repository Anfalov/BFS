from collections import deque

def neigh(v):
    ne = []
    steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for st in steps:
        if g[v[0] + st[0]][v[1] + st[1]] == 0:
            ne.append((v[0] + st[0], v[1] + st[1]))
    return ne

def bfs(s):
    q = deque()
    q.append(s)
    d[s] = 0
    while len(q):
        v = q.popleft()
        for to in neigh(v):
            if to not in d:
                q.append(to)
                d[to] = d[v] + 1
                p[to] = v

n, m = map(int, input().split())
g = [[1] * (m + 2)]
for i in range(n):
    g.append([1] + list(map(int, input().split())) + [1])
g.append([1] * (m + 2))
n += 2
m += 2
d = {}
p = {}
s = tuple(map(int, input().split()))
f = tuple(map(int, input().split()))
bfs(s)
print(d[f])



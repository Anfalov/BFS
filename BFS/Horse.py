from collections import deque

def check(x, y):
    return 0 <= x < n and 0 <= y < n

def neigh(v):
    ne = []
    steps = [(1, 2), (1, -2), (-1, 2), (-1, -2),
             (2, 1), (2, -1), (-2, 1), (-2, -1)]
    for st in steps:
        if check(v[0] + st[0], v[1] + st[1]):
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

n = int(input())
d = {}
p = {}
s_x, s_y = (map(int, input().split()))
s_x -= 1
s_y -= 1
f_x, f_y = map(int, input().split())
f_x -= 1
f_y -= 1
bfs((s_x, s_y))
print(d[(f_x, f_y)])




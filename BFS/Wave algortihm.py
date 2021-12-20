from collections import deque

def check(i, j):
    return 0 <= i < n and 0 <= j < m and g[i][j] == 0

def neigh(v_i, v_j):
    ne = []
    steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for st in steps:
        if check(v_i + st[0], v_j + st[1]):
            ne.append((v_i + st[0], v_j + st[1]))
    return ne


def bfs(s_i, s_j):
    q = deque()
    q.append((s_i, s_j))
    d[s_i][s_j] = 0
    while len(q):
        v_i, v_j = q.popleft()
        for to_i, to_j in neigh(v_i, v_j):
            if d[to_i][to_j] == int(1e9):
                q.append((to_i, to_j))
                d[to_i][to_j] = d[v_i][v_j] + 1
                p[to_i][to_j] = (v_i, v_j)

n, m = map(int, input().split())
g = [list(map(int, input().split())) for i in range(n)]
d = [[int(1e9)] * m for i in range(n)]
p = [[-1] * m for i in range(n)]
s_i, s_j = map(int, input().split())
f_i, f_j = map(int, input().split())
bfs(s_i - 1, s_j - 1)
print(d[f_i - 1][f_j - 1])


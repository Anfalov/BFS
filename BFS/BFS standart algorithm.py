from collections import deque

def bfs(v):
    queue = deque()
    queue.append(v)
    dist[v] = 0
    while len(queue):
        v = queue.popleft()
        for to in g[v]:
            if dist[to] == int(1e9):
                queue.append(to)
                dist[to] = dist[v] + 1
                parents[to] = v

n, m = map(int, input().split())
g = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
dist = [int(1e9)] * n
parents = [-1] * n
#хочу путь от s до f
s, f = map(int, input().split())
s -= 1
f -= 1
bfs(s)
path = []
while f != -1:
    path.append(f + 1)
    f = parents[f]
path = path[::-1]
print(*path)

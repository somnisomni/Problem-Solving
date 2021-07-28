from queue import deque

N, M, V = map(int, input().split())
graph = dict()

for n in range(N):
    graph[n + 1] = []

for _ in range(M):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

# DFS
visited_DFS = []
dfs = [V]

for node in graph:  # Descending sort for Stack.pop
    graph[node] = sorted(graph[node], reverse=True)

while dfs:
    currentNode = dfs.pop()

    if not (currentNode in visited_DFS):
        visited_DFS.append(currentNode)
        dfs += graph[currentNode]

print(*visited_DFS)

# BFS
visited_BFS = []
bfs = deque([V])

for node in graph:  # Ascending sort for Deque.popleft
    graph[node] = sorted(graph[node])

while bfs:
    currentNode = bfs.popleft()

    if not (currentNode in visited_BFS):
        visited_BFS.append(currentNode)
        bfs += deque(graph[currentNode])

print(*visited_BFS)
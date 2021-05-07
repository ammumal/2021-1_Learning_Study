import sys
from collections import deque
read = sys.stdin.readline

v = int(read())
tree = [[] for i in range(v + 1)]

for i in range(v):
    node = list(map(int, read().split()))
    for j in range(1, len(node)-2, 2):
        tree[node[0]].append((node[j], node[j + 1]))

def bfs(start):
    que = deque()
    que.append(start)
    visited = [-1] * (v+1)
    visited[start] = 0
    _dis = [0, 0]
    
    while que:
        now = que.popleft()
        for i, j in tree[now]:
            if visited[i] == -1:
                visited[i] = visited[now] + j
                que.append(i)
                if _dis[0] < visited[i]:
                    _dis = visited[i], i
    return _dis


dis, p = bfs(1)
dis, p = bfs(p)
print(dis)

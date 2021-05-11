n, m = map(int, input().split())
graphs = []
students = [[] for i in range(n+1)]
inDegree = [0 for i in range(n+1)]
result = []
queue = []

for i in range(m):
    graph = list(map(int, input().split()))
    graphs.append(graph)

for i, j in graphs:
    students[i].append(j)
    inDegree[j] += 1

for i in range(1, n+1):
    if inDegree[i] == 0:
        queue.append(i)

while queue:
    for i in queue:
        temp = i
        queue.remove(i)
        result.append(temp)
        for j in students[temp]:
            inDegree[j] -= 1
            if inDegree[j] == 0:
                queue.append(j)
                
for i in result:
    print(i, end=' ')

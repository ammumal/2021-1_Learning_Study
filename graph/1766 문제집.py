# heap import
import heapq
n, m = map(int, input().split())

# 위상정렬 준비
problems = [[] for i in range(n+1)]
inDegree = [0 for i in range(n+1)]
heap = []
result = []

# problems에 입력 받고 indegree 1증가
for i in range(m):
    a, b = map(int, input().split())
    problems[a].append(b)
    inDegree[b] += 1
    
# indegree가 0이면 heap에 넣기
for i in range(1, n+1):
    if inDegree[i] == 0:
        heapq.heappush(heap, i)
        
# 위상정렬
while heap:
    temp = heapq.heappop(heap)
    result.append(temp)
    for j in problems[temp]:
        inDegree[j] -= 1
        if inDegree[j] == 0:
            heapq.heappush(heap, j)

# 출력
for i in result:
    print(i, end=' ')

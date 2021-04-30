from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque([i for i in range(1, n+1)])

# 큐에 원소가 1개 남을 때 까지 반복
while not(len(q) == 1):
    #맨 위의 원소 제거
    q.popleft()
    #맨 위의 원소를 빼서 맨 아래에 놓는다
    q.append(q.popleft())

#출력
print(q[0])

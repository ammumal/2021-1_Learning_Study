import sys
input = sys.stdin.readline

n = int(input())
tree = [[]for i in range(n+1)]

for i in range(n-1):
    n2, n1 = list(map(int, input().split()))
    tree[n1].append(n2)
    tree[n2].append(n1)

que = [1]
visited = [0 for i in range(n+1)]
result = {}

while que:
    now = que.pop(0) #현재 가르키는 노드 처음엔 1이 온다.
    for i in tree[now]: #tree[1] 에 있는 요소를 꺼낸다.tree[1]에는 4와 6
        if visited[i] == 0: #방문한 적이 없다면,
            result[i] = now #4번 노드에 대한 출력값으로 부모인 now=1 삽입
            visited[i] = 1 #방문했으므로 1으로 바꿔준다.
            que.append(i) #큐에 추가해 다음 탐색을 이어가도록 한다.

for i in range(2, n+1): # 2부터 n까지 (n - 1)개
    print(result[i])

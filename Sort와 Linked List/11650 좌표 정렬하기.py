import sys
input = sys.stdin.readline

n = int(input())
co = [[] for i in range(n)]

# 좌표들을 리스트에 입력받기
for i in range(n):
    x, y = map(int, input().split())
    co[i].append(x)
    co[i].append(y)

# 정렬
sorted_co = list(sorted(co))

# 출력하기
for i in range(n):
    print(sorted_co[i][0], sorted_co[i][1])

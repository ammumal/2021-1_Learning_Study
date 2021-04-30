import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
st = [int(input()) for i in range(n)]
st = sorted(st)

# 평균
print(round(sum(st)/len(st)))

# 중앙값
print(st[len(st)//2])

mode_dict = Counter(st)
mode_list = mode_dict.most_common()

#값이 1개인 경우와 2개 이상인 경우 분리
if len(mode_dict) == 1:
    print(mode_list[0][0])
else:
    if mode_list[0][1] == mode_list[1][1]:
        print(mode_list[1][0])
    else:
        print(mode_list[0][0])

# 범위
print(max(st)-min(st))

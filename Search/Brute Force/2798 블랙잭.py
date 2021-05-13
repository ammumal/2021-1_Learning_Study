# 입력받기
n, std = map(int, input().split())
cards = list(map(int, input().split()))

# 모든 경우의 수를 중첩 for문을 통해 탐색
jackpot = []
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            sum = cards[i] + cards[j] + cards[k]
            # 합이 기준보다 크면 list에 저장
            if sum <= std:
                jackpot.append(sum)

# 리스트의 max 출력
print(max(jackpot))

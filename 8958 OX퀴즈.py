#테스트케이스 입력받기
n = int(input())
d = [list(input()) for _ in range(n)]

#점수 계산하기
score = 0
total = 0
sum = []
for i in range(n):
    for j in range(len(d[i])):
        if d[i][j] == 'O':
            score += 1
        else:
            score = 0
        total += score
    #sum에 점수 넣고 값 초기화
    sum.append(total)
    total = 0
    score = 0

#출력
for i in range(n):
    print(sum[i])

#리스트 생성
d = []
#리스트에 입력받기(9개)
for i in range(9):
    d.append(int(input()))
    
#최댓값 구하기
print(max(d))
#오프셋은 0부터 시작하므로 1 더해준다
print(d.index(max(d))+1)

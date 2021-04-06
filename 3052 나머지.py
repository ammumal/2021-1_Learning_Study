#숫자 입력받기
num = []
for i in range(10):
    num.append(int(input()))
 
#나머지 담을 리스트 생성
remainder = []
for i in range(10):
    remainder.append(num[i] % 42)
#중복 제거한 나머지 개수 출력
print(len(set(remainder)))

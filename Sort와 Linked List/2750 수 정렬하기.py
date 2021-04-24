#리스트에 수 입력 받아서 정렬하기(내장된 sorted()메서드 사용)
n = int(input())
numbers = [int(input()) for i in range(n)]
numbers = sorted(numbers)

#출력하기
for i in range(n):
    print(numbers[i])

import sys
input = sys.stdin.readline

n = int(input())
numbers = [int(input()) for i in range(n)]
numbers.sort()

for i in range(n):
    print(numbers[i])

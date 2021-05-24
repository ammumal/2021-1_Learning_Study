import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    tc = int(input())
    fibo0 = 1
    fibo1 = 0
    temp = 0
    for j in range(tc):
        tmp = fibo1
        fibo1 += fibo0
        fibo0 = tmp
        
    print(fibo0, fibo1)

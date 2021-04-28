import sys
input = sys.stdin.readline
n = int(input())
number_list = [0] * 10001
for i in range(n):
    input_num = int(input()) 
    number_list[input_num] = number_list[input_num] + 1

for i in range(10001):
    if number_list[i] != 0:
        for j in range(number_list[i]):
            print(i)

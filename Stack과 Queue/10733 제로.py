n = int(input())
value = [int(input()) for i in range(n)]
stack = []

#0이 들어온 경우 pop
for i in range(n):
    if value[i] == 0:
        del stack[-1]
    else:
        stack.append(value[i])

#스택의 합 구해서 출력
sum = 0
for i in range(len(stack)):
    sum += stack[i]

print(sum)

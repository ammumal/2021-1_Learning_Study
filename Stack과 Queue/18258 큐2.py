import sys
from collections import deque

input = sys.stdin.readline
n = int(sys.stdin.readline())
queue = deque([])

for i in range(n):
    ins = sys.stdin.readline().split()
    if ins[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif ins[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])
    elif ins[0] == 'size':
        print(len(queue))
    elif ins[0] == 'empty':
        if not queue:
            print(1)
        else:
            print('0')
    elif ins[0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    else:
        queue.append(ins[1])

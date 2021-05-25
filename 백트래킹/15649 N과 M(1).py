n, m = map(int, input().split())

result = []

def btk():
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    
    for i in range(1, n+1):
        if i in result:
            continue
        result.append(i)
        btk()
        result.pop()

btk()

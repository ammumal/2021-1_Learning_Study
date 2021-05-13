n = int(input())
gen = 0

for i in range(1, n+1):
    total = list(map(int,(str(i))))
    gen = i + sum(total)
    if gen == n:
        print(i)
        break
if i == n:
  print(0)

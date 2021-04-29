numbers = input()
d = []
for i in range(len(numbers)):
  d.append(numbers[i])
sorted_d = list(reversed(sorted(d)))
print(''.join(sorted_d))

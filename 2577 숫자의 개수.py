#a,b,c 입력받기
num = []
for i in range(3):
    num.append(int(input()))

#list로 만들어 count
mult = list(str(num[0] * num[1] * num[2]))
for i in range(10):
    print(mult.count(f'{i}'))

n = int(input())

# 이전에 나왔던 글자인지 검사하기 위한 list 생성
alpha = []

#groupword 개수
groupw = 0

#groupword 판별
isgroup = True


for i in range(n):
    word = input()
    # word[0:-2] 검사
    for j in range(1, len(word)):
        if word[j] != word[j-1]:
            if word[j-1] in alpha:
                isgroup = False
                break
            else:
                alpha.append(word[j-1])
        # word[-1] 검사
        if word[-1] in alpha:
            isgroup = False
    if isgroup:
        groupw += 1
        
    alpha = []
    isgroup = True

print(groupw)

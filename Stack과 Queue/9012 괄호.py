#testcase 입력받기
n = int(input())
PS = [input() for i in range(n)]

#괄호 검사와 답 저장을 위한 list생성
stack = []
answer = []

#괄호 검사
for i in range(n):
    for j in range(len(PS[i])):
      #PS가 (면 스택에 저장
        if PS[i][j] == '(':
            stack.append('(')
      #PS가 )일 경우 stack에 저장되어있던 ( 삭제, stack이 비어있을 경우 break해서 NO에 걸릴 수 있도록 ) 추가
        else:
            if not stack:
                stack.append(')')
                break
            else:
                del stack[-1]
    #stack이 비어있으면 VPS
    if not stack:
        answer.append('YES')
        stack = []
    else:
        answer.append('NO')
        stack = []

#출력
for i in range(n):
    print(answer[i])

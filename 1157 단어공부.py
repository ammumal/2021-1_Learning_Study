#입력받아서 전처리(대문자, 횟수 dict만들기)
s = input().upper()
s_counts = {letter : s.count(letter) for letter in set(s)}

#가장 많이 사용된 알파벳이 여러개인지 검사
d = list(s_counts.values())
max = max(d)
if d.count(max) >= 2:
    print('?')
#value로 key를 찾아 출력
else:
    for key, value in s_counts.items():
        if max == value:
            print(key)

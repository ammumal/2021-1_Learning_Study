import collections
def solution(clothes):
    answer = 1
    result = [clothes[i][1] for i in range(len(clothes))]
    clothes_dict = collections.Counter(result)
    for i in clothes_dict.values():
        answer *= (i+1)
    answer -= 1
        
    return answer

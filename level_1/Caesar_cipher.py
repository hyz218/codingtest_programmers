#시저 암호(Caesar cipher)
#어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 
#예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다. 
#문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

def solution(s, n):
    answer = [] 
    
    for i in range(len(s)):
        if (s[i].islower()): #문자가 소문자인지 판별
            caesar = chr((ord(s[i])-ord('a')+n)%26 + ord('a')) #알파벳 암호하
        elif (s[i].isupper()): #문자가 대문자인지 판별
            caesar = chr((ord(s[i])-ord('A')+n)%26 + ord('A')) #알파벳 암호화
        else:
            caesar = s[i]
        answer.append(caesar)
        
    return "".join(answer)
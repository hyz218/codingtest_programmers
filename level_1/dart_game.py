#1차 다트 게임

def solution(dartResult):
    answer = [] #answer 초기화
    d = [] #d list 초기화
    dart = list(map(str,dartResult)) #dartResult를 list로 변환
    for i in range(len(dart)): #list를 도는 반복문
        if dart[i]=='1' and dart[i+1]=='0': #1과0이 연달아 나오는 경우 10으로 변환 후 d에 append
            d.append('10')
        elif dart[i]=='0' and dart[i-1]=='1': #0앞에 1이 나오는 경우 이미 처리했으니 continue
                continue
        else: #해당하지 않는경우 d에 append
            d.append(dart[i])
            
    for i in range(len(d)): #d의 길이만큼 도는 반복문
        if d[i]=='S': #문자열이 S이면 이전의 숫자를 answer에 append
            answer.append(int(d[i-1]))
        if d[i]=='D': #문자열이 D이면 이전의 숫자를 제곱해 answer에 append
            answer.append(int(d[i-1])**2)
        if d[i]=='T': #문자열이 T이면 이전의 숫자를 세제곱해 answer에 append
            answer.append(int(d[i-1])**3)

        if d[i]=='*': #문자열이 '*'라 스타상에 해당되는 경우
            if len(answer)>=2: #answer에 있는 숫자가 2개 이상인 경우
                answer[-1]*=2 #해당 숫자 제곱
                answer[-2]*=2 #그 전의 숫자 제곱
            else: #answer에 있는 숫자가 1개인 경우
                answer[-1]*=2 #해당 숫자 제곱
        if d[i]=='#': #문자열이 '#'이라 아차상에 해당되는 경우
            answer[-1]*=(-1) #해당 숫자에 -1 곱하기

    return sum(answer) #answer의 값을 모두 더해서 return
#4주차_직업군 추천하기

def solution(table, languages, preference): 
    answer = [] #answer 초기화
    score = [] #점수 초기화
    job = [] #직업군 초기화
    
    for i in range(len(table)): #table 길이만큼 도는 반복문
        num = 0 #점수 계산 초기화
        t = table[i].split(" ") #문장 분리
        job.append(t[0]) #직업군 추가
        for j in range(1,len(t)): #문장 길이만큼 도는 반복문
            for l in range(len(languages)): #언어 길이만큼 도는 반복문
                if (languages[l]==t[j]): #언어와 문장에서 단어가 해당하는 문자가 같은 경우
                    num+=(5-j+1)*preference[l] #해당 가중치 곱하여 총점 덧셈
        score.append(num) #점수 배열에 추가
    
    for i in range(len(score)):
        if (score[i]==max(score)): #점수가 최고값이라면 answer에 추가
            answer.append(job[i])
    
    answer.sort() #중복인 경우가 있으므로 answer 정렬
    answer = answer[0] #사전순 정렬 후 가장 앞에 있는 값 return
    return answer
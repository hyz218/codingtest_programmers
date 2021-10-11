#영어 끝말잇기
#사람의 수 n과 사람들이 순서대로 말한 단어 words 가 매개변수로 주어질 때, 가장 먼저 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째 차례에 탈락하는지를 구해서 return 하도록 solution 함수를 완성해주세요.

def append_person(i,n):
    answer = [] #answer 초기화
    if (i+1)%n==0: #사람을 나눴을 때 0이면 n 추가
        answer.append(n)
    else: #아닌 경우 나눈 값 추가
        answer.append((i+1)%n)
        
    answer.append((i)//n+1) #차례 추가 
    
    return answer

def solution(n, words):
    answer = [] #answer 초기화
    word_set = [] #word_set 초기화
    
    word_set.append(words[0]) #word_set에 words의 첫번째 단어 삽입
    for i in range(1,len(words)): #word_set i-1 제한 조건 때문에 1부터 시작
        if words[i] in word_set: #현재 단어가 이전에도 나왔던 단어일 경우
            answer = append_person(i,n) #answer 추가
            break #반복문 빠져나오기
        if word_set[i-1][-1]!=words[i][0]: #전 단어의 끝 글자와 현재 단어의 첫글자가 다른 경우
            answer = append_person(i,n)#answer 추가
            break#반복문 빠져나오기
        word_set.append(words[i]) #word_set에 현재 단어 추가

    if answer==[]: #answer가 비어있는 경우, 즉 탈락자가 없는 경우
        answer = [0,0]

    return answer
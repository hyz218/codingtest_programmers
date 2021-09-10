#모의고사
#1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

def solution(answers):
    answer = []
    count = [0,0,0]
    max_num = 0
    max_index = 0
    
    answer_1 = [1,2,3,4,5] #1번 수포자가 찍는 방식
    answer_2 = [2,1,2,3,2,4,2,5] #2번 수포자가 찍는 방식
    answer_3 = [3,3,1,1,2,2,4,4,5,5] #3번 수포자가 찍는 방식
    
    for i in range(len(answers)):
        if (answers[i]==answer_1[i%len(answer_1)]): #답안이 일치하는지 판단
            count[0]+=1
        if (answers[i]==answer_2[i%len(answer_2)]):
            count[1]+=1
        if (answers[i]==answer_3[i%len(answer_3)]):
            count[2]+=1
            
    for i in range(3): #수포자들을 도는 반복문
        if max_num<count[i]: #가장 많은 문제를 맞힌 사람 판별
            max_index = i
            max_num = count[i]
    answer.append(max_index+1) #가장 많은 문제를 맞힌 사람 추가
        
    for i in range(3): #동점인 경우 추가
        if i!=max_index and max_num==count[i]:
            answer.append(i+1)
        
    return answer
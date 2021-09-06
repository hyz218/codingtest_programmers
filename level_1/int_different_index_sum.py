#정수 배열 numbers가 주어집니다. 
#numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if (i!=j): #index가 같은 경우 제외하기
                answer.append(numbers[i]+numbers[j])
            
    answer = list(set(answer)) #중복 제거
    answer.sort() #list 정렬하기
    
    return answer
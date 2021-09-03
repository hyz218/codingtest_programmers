## 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요. 
## 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.

import numpy as np

def solution(arr):
    answer = []
    min_idx = np.argmin(arr) #가장 작은 값의 index 찾기
    
    for i in range(len(arr)): #arr 길이까지 도는 for문
        if (i!=min_idx):#i와 min_idx 비교
            answer.append(arr[i]) #min_idx가 아닌 경우 answer list에 추가하기
    
    if answer==[]: #answer가 빈 list 이면 -1추가
        answer.append(-1)
        
    return answer
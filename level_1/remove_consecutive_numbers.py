#같은 숫자는 싫어
#배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다. 
def solution(arr):
    
    answer = [] #answer list 초기화
    answer.append(arr[0]) 
    for i in range(0,len(arr)-1):
        if arr[i]!=arr[i+1]: #뒤에 나올 숫자와 비교하기
            answer.append(arr[i+1]) #앞과 뒤의 숫자가 다르면 뒷숫자 추가하기
    return answer
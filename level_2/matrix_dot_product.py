#행렬의 곱셈

def solution(arr1, arr2):
    answer = [] #answer 초기화
    
    for i in range(len(arr1)): #arr1의 길이만큼 도는 반복문
        dot_list = [] #행렬의 곱셈값을 저장할 list 초기화
        for j in range(len(arr2[0])): #arr2의 원소의 길이만큼 도는 반복문
            num = 0 #num 초기화
            for k in range(len(arr2)): #arr2의 길이만큼 도는 반복문
                num += arr1[i][k] * arr2[k][j] #arr1은 가로, arr2는 세로로 돌아야하기 때문에 indexing이 다름
            dot_list.append(num) #계산한 숫자를 추가
        answer.append(dot_list) 
        
    return answer
#행렬의 덧셈
#행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 
#2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

def solution(arr1, arr2):
    answer = arr1 #초기화
    
    for i in range(len(arr1)): #arr1의 길이까지 도는 반복문
        for j in range(len(arr1[i])): #arr1 내부 배열의 길이까지 도는 반복문
            answer[i][j] = arr1[i][j]+arr2[i][j] #answer에 arr1의 인자와 arr2의 인자 덧셈
    return answer
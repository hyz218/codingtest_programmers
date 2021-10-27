# n^2 배열 자르기
#
# def solution(n, left, right): #O(n*n)
#     answer = []
#     array = [[0]*n for _ in range(n)] #array 초기화
#     for i in range(n):
#         for j in range(n):
#             array[i][j] = max(i,j)+1 #행, 열 중 큰 값에+1한 값을 할당하여 2차원 배열 생성
    
#     for i in range(n):
#         for j in range(n):
#             answer.append(array[i][j]) #2차원 배열을 1차원으로 변경하기
    
#     return answer[left:right+1] #left와 right로 슬라이싱하기

def solution(n, left, right):
    answer = [] #answer 초기화
    
    for i in range(left,right+1): #left부터 right+1까지 도는 반복문 생성
        answer.append(max(divmod(i,n))+1) #i를 n으로 나눈 몫과 나머지를 비교하여 더 큰값을 취한 후 +1
    
    return answer
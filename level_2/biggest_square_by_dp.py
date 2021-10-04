#가장 큰 정사각형 찾기
#표에서 1로 이루어진 가장 큰 정사각형을 찾아 넓이를 return 하는 solution 함수를 완성해 주세요.

def solution(board):
    answer = 0 #answer 초기화
    
    n,m = len(board), len(board[0]) #행과 열의 길이 구하기
    dp = [[0]*m for _ in range(n)] #dp table 0으로 초기화
    dp[0] = board[0] #board의 첫번째 행을 dp의 첫번째 행으로 고정
    for i in range(n): #board의 첫번째 열을 dp의 첫번째 열로 고정
        dp[i][0] = board[i][0]
    
    for i in range(1,n):
        for j in range(1,m):
            if board[i][j]==1: #board에서 사각형에 해당하는 경우
                dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1 #대각선, 위, 아래 중 작은값에 +1해서 dp[i][j]에 저장
                
    for i in range(n):#행을 도는 반복문
        temp = max(dp[i]) #행에서의 최댓값 찾기
        answer = max(answer, temp) #가지고 있던 최댓값과 현재의 최댓값 중 더 큰 값 취하기 
    
    answer **= 2 #넓이이므로 제곱하기
    return answer
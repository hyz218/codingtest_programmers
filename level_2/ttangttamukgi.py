# 땅따먹기
# 단, 땅따먹기 게임에는 한 행씩 내려올 때, 같은 열을 연속해서 밟을 수 없는 특수 규칙이 있습니다.
# 마지막 행까지 모두 내려왔을 때, 얻을 수 있는 점수의 최대값을 return하는 solution 함수를 완성해 주세요.

def solution(land):
    answer = 0 #answer 초기화

    for i in range(1,len(land)): #행을 도는 반복문
        for j in range(len(land[0])): #열을 도는 반복문
            land[i][j] = max(land[i-1][:j] + land[i-1][j+1:]) + land[i][j] #현재의 열을 제외하고 앞의 행에서 가장 큰 값 + 현재 값
    
    answer = max(land[len(land)-1]) #마지막 행에서 가장 큰 값을 answer로 return

    return answer
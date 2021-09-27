def solution(sizes):
    answer = 0
    n, m = [], [] #n과 m list 초기화
    for i in range(len(sizes)): #size의 길이까지 도는 반복문
        n.append(max(sizes[i])) #두 원소 중 큰 값을 n list에 저장
        m.append(min(sizes[i])) #두 원소 중 작은 값을 m list에 저장
    
    answer = max(n)*max(m) #저장 된 값 중 가장 큰 값을 기준으로 직사각형의 넓이 계산
    return answer
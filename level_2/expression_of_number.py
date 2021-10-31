def solution(n):
    answer = 0 #answer 초기화
    for i in range(1,n+1): #1부터 n까지 도는 반복문
        cnt=0 #cnt 초기화
        num = i #i부터 +1하는 숫자
        while cnt<n: #cnt가 n보다 작을 경우에 반복
            cnt+=num #cnt에 num 더하기
            num+=1 #num 숫자 더하기
            if cnt==n: #cnt와 n이 같은 경우
                answer+=1 #answer에 더하기
                break
    return answer
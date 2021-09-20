from itertools import combinations #숫자 조합을 만들기 위한 library

def is_prime(num): #소수 판별 함수
    if num==0 or num==1:
        return False #소수가 아니면 False return
    else: 
        for i in range(2,(num//2)+1): #연산 시간을 줄이기 위해 num//2+1까지 계산
            if num%i == 0: #소수가 아니면 False return
                return False
        return True #소수이면 True return

def solution(nums):
    answer = 0 #answer의 갯수 초기화
    combi = list(combinations(nums,3)) #3가지 숫자의 조합 list 생성
    
    for i in combi: #combi list를 도는 반복문
        if is_prime(sum(i)): #3가지 숫자의 합이 소수인지 판별
            answer+=1 #소수이면 answer에 +1

    return answer
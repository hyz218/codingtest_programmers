#소수 찾기
#흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
#종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

import itertools

def is_prime(num): #소수 판별 함수
    if num==0 or num==1: #숫자가 0이나 1이면 False return
        return False
    for i in range(2, (num//2)+1):
        if num%i==0: # 다른 숫자와 나누어떨어져 소수가 아닌 경우 False return
            return False
    return True

def solution(numbers):
    answer = 0 #answer 초기화
    num = [] #num list 초기화
    number_list = [] #number_list 초기화
    
    numbers = list(map(str,numbers)) #숫자를 str형태로 list에 넣기

    for i in range(1, len(numbers)+1): #모든 조합 구하기
        combi = list(map("".join, itertools.permutations(numbers, i))) #조합들의 조합 list로 불러오기
        num.append(combi) #num list에 추가하기
    
    for n in num: #num list 전체를 도는 반복문
        for i in range(len(n)): #num 안을 도는 반복문
            number_list.append(int(n[i])) #number_list에 넣기 -> 1차원 리스트로 변환
    
    nums = list(set(number_list)) #중복제거 하기
    
    for n in nums: #숫자 소수 판별하기
        if is_prime(n)==True: #소수인 경우 answer에 숫자 추가
            answer+=1
    
    return answer
#위장
#스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.

def solution(clothes):
    answer = 1 #answer 초기화
    closet = {} #옷 dict 초기화
    
    for c in clothes: #clothes를 도는 반복문
        key, value = c[1], c[0] #key와 value 지정
        if key in closet: #key가 이미 존재한다면 append
            closet[key].append(value)
        else: #key가 존재하지 않는다면 새로 생성
            closet[key] = [value]
            
    for key in closet.keys(): #key를 도는 반복문
        answer*=len(closet[key])+1 #key의 길이에 1을 더해서 곱하기

    return answer-1 #경우의 수에 따라 -1
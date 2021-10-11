#구명보트
#구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.

def solution(people, limit):
    answer = 0

    people.sort() #무게를 오름차순으로 정렬
    start, end = 0,len(people)-1 #시작, 끝 index 지정
    while start <= end: #start가 end보다 작은 경우에만 반복
        answer+=1
        if people[start]+people[end]<=limit: #두명 이상 탈 수 있는 경우
            start+=1
        end-=1 
    return answer
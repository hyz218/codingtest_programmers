#실패율
#스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
#전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때, 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.

def solution(N, stages):
    answer = [] #answer 초기화
    fail = {} #dictionary 생성
    user = len(stages) #사용자 수
    
    for i in range(1,N+1): #전체 스테이지까지 도는 반복문
        count = stages.count(i) #해당 stage에 머물러 있는 user의 수
        if user == 0: #머물고 있는 user가 없으면 실패율 0
            fail[i]=0
        else:
            fail[i] = count / user #해당 stage에 머무는 user / 전체 user 수
        user -= count #도달 전 user 빼기
    
    answer = [stage[0] for stage in sorted(fail.items(),key = lambda x:(-x[1],x[0]))]
    #items() 를 사용하여 key와 value 가져오기, 실패율이 내림차순 정렬, 그 후 key 순서로 오름차순 정렬
    return answer
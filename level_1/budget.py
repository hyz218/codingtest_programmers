#예산
#전체 예산이 정해져 있기 때문에 모든 부서의 물품을 구매해 줄 수는 없습니다. 그래서 최대한 많은 부서의 물품을 구매해 줄 수 있도록 하려고 합니다.

def solution(d, budget):
    answer = 0 #answer 초기화
    d.sort() #d를 오름차순 정렬하여 적은 예산을 신청한 부서 먼저 할당하도록 유도
    for i in range(len(d)): #d의 길이만큼의 반복문
        if (budget-d[i]<0): #전체예산에서 부서에 지원을 해줬을 시 음수이면 break
            break
        budget-=d[i] #전체 예산에서 지원해준 예산 빼기
        answer+=1 #지원해준 부서 수 count 추가
    return answer
import heapq

def solution(food_times, k):
    if sum(food_times)<=k: #전체 시간을 합한 값이 k 보다 작으면 -1 return
        return -1
    
    q=[] #우선순위 큐 구현
    for i in range(len(food_times)): #시간의 길이까지 도는 반복문
        heapq.heappush(q,(food_times[i],i+1)) #시간과 번호를 q에 삽입
        
    sum_value = 0 #sum 값 초기화
    previous = 0 #직전에 다 먹은 음식의 시간
    length = len(food_times) #남은 음식의 갯수
    
    while sum_value+((q[0][0]-previous)*length)<=k: #sum_value + (현재 음식의 시간-이전 음식 시간)*현재 음식 개수와 k 비교
        now = heapq.heappop(q)[0]
        sum_value+=(now-previous)*length
        length-=1 #다 먹은 음식 제와
        previous=now #이전 음식 시간 재설정
        
    result = sorted(q,key=lambda x:x[1]) #남은 음식 중 몇번째 음식인지 확인하여 출력
    return result[(k-sum_value)%length][1]
#더 맵게

import heapq #우선순위 큐(Heap)

def solution(scoville, K):
    answer = 0 #answer 초기화
    
    heapq.heapify(scoville) #scoville를 heap으로 변환
    while scoville[0]<K: #scoville의 최소값이 K보다 작으면 반복
        if len(scoville)==1: #scoville가 K 이상으로 커질 수 없을 때
            answer = -1 #-1 return
            break
        heapq.heappush(scoville,heapq.heappop(scoville)+heapq.heappop(scoville)*2)
        #heappop을 이용해서 최소값 빼내고 heappush를 이용해서 계산된 값 추가
        answer+=1 #횟수 1 추가 
    
    return answer

#런타임 에러 -> sort 함수 때문으로 추정
# def solution(scoville, K):
#     answer = 0
    
#     scoville.sort()
#     while True:
#         if min(scoville)>=K:
#             break
#         else:
#             if len(scoville)==1:
#                 answer = -1
#             num = scoville[0]+scoville[1]*2
#             answer+=1
#             scoville.pop(0)
#             scoville.pop(0)
#             scoville.sort()
    
#     return answer
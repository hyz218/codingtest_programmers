from collections import deque #bfs 구현을 위한 deque 활용

def solution(maps):
    answer = 0 #answer 초기화
    dx = [0,-1,0,1] #x 방향
    dy = [1,0,-1,0] #y 방향
    
    r = len(maps) #row의 길이
    c = len(maps[0]) #column의 길이
    
    table = [[-1 for _ in range(c)] for _ in range(r)] #table 초기화
    q = deque() #queue 생성
    q.append([0,0]) #q에 초기 위치 추가 하기
    table[0][0] = 1 #table에 초기 위치 방문 처리
    
    while q:
        y, x = q.popleft() #pop하기

        for i in range(4):
            ny = y + dy[i] #y축 위치 변경
            nx = x + dx[i] #x축 위치 변경

            if -1<ny<r and -1<nx<c: #변경한 위치가 맵의 범위 내에 있는 경우 
                if maps[ny][nx] == 1: #갈 수 있는 길이라면
                    if table[ny][nx] == -1: #방문하지 않은 경우
                        table[ny][nx] = table[y][x] + 1 #길이 추가
                        q.append([ny, nx]) #q에 해당 위치 추가
    
    answer = table[-1][-1] #최종 위치에 도달하는 거리 answer로 지정
    return answer
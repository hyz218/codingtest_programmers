def possible(answer): #현재 설치된 구조물이 가능한 구조물인지 확인하는 함수
    for x,y,stuff in answer: 
        if stuff==0: #설치된게 기둥인 경우
            if y==0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer: #바닥 위 or 보의 한쪽 끝부분 위 or 다른 기둥 위라면 정상
                continue
            return False #아니라면 return False
        elif stuff==1: #설치된게 보인 경우
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer): #한쪽 끝이 기둥 위 or 양쪽 끝부분이 다른 보와 동시에 연결이면 정상
                continue
            return False #아니라면 return False
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x,y,stuff,operate = frame
        if operate == 0: #삭제하는 경우
            answer.remove([x,y,stuff]) #일단 삭제하고
            if not possible(answer): #가능한 구조물인지 확인
                answer.append([x,y,stuff]) #가능한 구조물이 아니면 다시 설치
        if operate==1: #설치하는 경우
            answer.append([x,y,stuff]) #일단 설치하고
            if not possible(answer): #가능한 구조물인지 확인
                answer.remove([x,y,stuff]) #가능한 구조물이 아니라면 다시 제거
    return sorted(answer) #정렬된 결과 반환
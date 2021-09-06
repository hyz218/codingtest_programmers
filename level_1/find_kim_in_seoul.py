#서울에서 김서방 찾기
#String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요. 
#seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

def solution(seoul):
    answer = '' #answer 초기화
    for i in range(len(seoul)): #seoul까지 반복문
        if seoul[i]=="Kim": #배열에서 "Kim" 찾기
            answer = "김서방은 "+str(i)+"에 있다" #index 반환하여 문장완성
        
    return answer
#문자열 내 p와 y의 개수
#대문자와 소문자가 섞여있는 문자열 s가 주어집니다. 
#s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 
#'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 
#단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.
#예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.

def solution(s):
    num_p = 0 #p의 갯수 초기화
    num_y = 0 #y의 갯수 초기화
    sentence = s.lower() #대소문자 구별하지 않기 때문에, 문장을 모두 소문자로 변경
    
    for i in range(len(sentence)): #문장 길이까지 반복하는 반복문 생성
        if sentence[i] == 'p': #문자가 'p'인 경우
            num_p = num_p + 1 #p의 갯수 증가
        if sentence[i] == 'y': #문자가 'y'인 경우
            num_y = num_y + 1 #y의 갯수 증가
            
    if (num_p!=num_y): #'p'의 갯수와 'y'의 갯수가 다른경우 False return
        return False

    return True #'p'의 갯수와 'y'의 갯수가 같은 경우 True return
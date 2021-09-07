#하샤드 수
#양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

def solution(x):
    num_list = list(map(int,str(x))) #입력받은 정수를 분리한 list 생성
    if (x%sum(num_list)==0): #하샤드수인지 판별
        answer = True
    else: 
        answer = False
    return answer
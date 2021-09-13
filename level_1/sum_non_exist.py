#없는 숫자 더하기
#0부터 9까지의 숫자 중 일부가 들어있는 배열 numbers가 매개변수로 주어집니다. numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.

def solution(numbers):
    answer = 0 #answer 초기화
    num = [i for i in range(10)] #0부터 0까지의 숫자가 들어가있는 배열
    non_num = list(set(num)-set(numbers)) #number 배열에 없는 숫자만 담기
    answer = sum(non_num) #number 배열에 없는 숫자의 합
    return answer
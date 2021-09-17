#가장 큰 수
#0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

def solution(numbers):
    answer = ''
    numbers = list(map(str,numbers)) #number string으로 변환
    numbers.sort(key=lambda num: num*3, reverse=True) #number 정렬, 3을 곱한 이유는 numbers원소가 1000 이하이므로 자릿수가 다른 경우를 고려하여
    answer = str(int("".join(numbers))) #answer 문자열 형식으로 반환
    # 0000이 들어갈 경우 때문에 int로 변환 후 str으로 변환해야한다.
    return answer
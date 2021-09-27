#최댓값과 최솟값
#문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. 
#str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.

def solution(s): 
    answer = '' #answer 초기화
    string = list(map(int,s.split(' '))) #공백으로 구분하여 문자열을 쪼개서 정수형으로 변환 후 list 변환
    answer = str(min(string)) + ' ' + str(max(string)) #min과 max함수를 이용하여 숫자를 찾아낸 후 문자형으로 변환후 return
    return answer
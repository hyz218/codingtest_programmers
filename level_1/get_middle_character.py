#가운데 글자 가져오기
#단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

def solution(s):
    answer = '' #answer 초기화
    divide_len = int(len(s)/2) #문장길이를 2로 나누어서 int형태로 변환한 값 저장
    
    if len(s)%2==0: #문장길이가 짝수인 경우
        answer = s[divide_len-1] + s[divide_len] #가운데 두글자 반환
    else: #문장길이가 홀수인 경우
        answer = s[divide_len] #가운데 한글자 반환
    return answer
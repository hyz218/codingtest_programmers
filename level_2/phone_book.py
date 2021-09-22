#전화번호 목록
#전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
#전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.
import itertools

def solution(phone_book): #시간초과
    answer = True 
    phone_book.sort(key = lambda phone_book: len(phone_book)) #문자 길이 순서로 정렬
    for i in range(len(phone_book)): 
        for j in range(i+1,len(phone_book)):
            string = phone_book[j] 
            string = string[:len(phone_book[i])]
            if phone_book[i]==string:
                answer = False
                return answer
    answer = True
    return answer


def solution(phone_book): #시간초과
    answer = True
    phone_book.sort(key = lambda phone_book: len(phone_book))
    phone_num = list(itertools.combinations(phone_book,2)) #combinations 사용
    
    for i in range(len(phone_num)):
        string = phone_num[i][1]
        string = string[:len(phone_num[i][0])]
        if string == phone_num[i][0]:
            answer = False
            break

    return answer

def solution(phone_book):
    answer = True #answer 초기화 
    phone_book.sort() #string 순서로 sort
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]: #앞의 문자가 뒤의 문자의 접두사 일 경우
            answer = False
            break
    return answer
#함수 solution은 정수 n을 매개변수로 입력받습니다. 
#n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 
#예를들어 n이 118372면 873211을 리턴하면 됩니다.

def solution(n):
    
    list_n = list(str(n)) #입력받은 정수를 str형태로 list에 입력 
    list_sorted = sorted(list_n,reverse=True) #list 정렬
    answer = int("".join(list_sorted)) #list값을 합쳐서 int형식으로 변경
    
    return answer
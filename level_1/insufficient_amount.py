#부족한 금액 계산하기
#새로 생긴 놀이기구는 인기가 매우 많아 줄이 끊이질 않습니다. 이 놀이기구의 원래 이용료는 price원 인데, 놀이기구를 N 번 째 이용한다면 원래 이용료의 N배를 받기로 하였습니다. 즉, 처음 이용료가 100이었다면 2번째에는 200, 3번째에는 300으로 요금이 인상됩니다.
#놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지를 return 하도록 solution 함수를 완성하세요.
#단, 금액이 부족하지 않으면 0을 return 하세요.

def solution(price, money, count):
    answer = -1 #answer 초기화
    total = 0 #필요 금액 초기화
    
    for i in range(count):
        total+=(i+1)*price #놀이기구를 타는 데에 필요한 금액 계산
    
    if (money>total): #가진 돈이 충분할 경우 
        answer = 0 #answer는 return 0
    else: #부족한 액수만큼 계산하여 return
        answer = total - money

    return answer
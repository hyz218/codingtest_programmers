#폰켓몬
# N 마리의 폰켓몬 중에서 N/2마리를 가져가도 좋다고 했습니다.
# 당신은 최대한 다양한 종류의 폰켓몬을 가지길 원하기 때문에, 최대한 많은 종류의 폰켓몬을 포함해서 N/2마리를 선택하려 합니다. 폰켓몬 종류 번호의 개수를 return 하도록 solution 함수를 완성해주세요.

def solution(nums):
    answer = 0
    select_num = len(nums)//2 # N/2마리
    num = len(list(set(nums))) # 폰켓몬 중 종류 중복 제거
    
    if (select_num>num): #선택할 수 있는 폰켓몬의 수가 폰켓몬의 종류보다 많으면
        answer = num # 최대 선택 가능한 종류의 수 answer return
    else: #선택할 수 있는 폰켓몬 수보다 폰켓몬의 종류가 더 많으면
        answer = select_num #선택할 수 있는 폰켓몬 수 answer return
    
    return answer
#배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.
#array	commands	return
#[1, 5, 2, 6, 3, 7, 4]	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]	[5, 6, 3]

def solution(array, commands):
    answer = []

    for i in commands: #commands를 for문으로 돌리기
        list_set = array[i[0]-1:i[1]] # 범위에 해당되는 list만 남기기
        list_set.sort() # 정렬하기
        answer.append(list_set[i[2]-1]) # answer list에 k에 해당되는 수 추가하기

    return answer
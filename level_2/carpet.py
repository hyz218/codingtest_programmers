# def solution(brown, yellow): #시간초과
#     answer = []
#     for i in range(3,max(brown,yellow)):
#         yellow_num = 0
#         brown_num = 0
#         for j in range(3,max(brown,yellow)):
#             yellow_num = (i-2)*(j-2) #yellow의 넓이 구하기 
#             brown_num = i*j - yellow_num #brown의 넓이 구하기 
#             if (yellow_num==yellow) and (brown_num==brown):
#                 answer.append(max(i,j)) #가로가 더 큰 값으로 제한조건
#                 answer.append(min(i,j))
#                 return answer
#     return answer

def solution(brown, yellow):
    answer = []
    total = brown+yellow
    for i in range(3,total):
        yellow_num = 0
        brown_num = 0
        t = total//i
        yellow_num = (i-2)*(t-2) #yellow의 넓이 구하기 
        brown_num = i*t - yellow_num #brown의 넓이 구하기 
        if (yellow_num==yellow) and (brown_num==brown):
            answer.append(max(i,t)) #가로가 더 큰 값으로 제한조건
            answer.append(min(i,t))
            return answer
    return answer
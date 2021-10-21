def solution(s):
    answer = len(s) #answer를 문자의 총 길이로 초기화
    for step in range(1,len(s)//2+1): #1부터 문자열 길이의 반+1까지 반복
        compressed = "" #문장 초기화
        prev = s[0:step] #초기 문자열 지정
        count = 1 #초기 문자의 count지정
        for i in range(step,len(s),step): #해당 단위를 늘리며 확인
            if prev == s[i:i+step]: #이전 문자열과 해당 문자열이 같을 경우
                count+=1 #count 추가
            else:
                if count>=2: #count가 2가 넘는 경우
                    compressed+=str(count)+prev #숫자와 문자열 넣기
                else: #count가 1인경우
                    compressed+=  prev #문자열 넣기
                prev = s[i:i+step] #문자열 초기화
                count=1 #count초기화
        if count>=2: #남아있는 문자열 확인하기
            compressed+=str(count)+prev 
        else:
            compressed+=prev
        answer = min(answer,len(compressed)) #문자열의 길이가 가장 짧은 것 채택

    return answer
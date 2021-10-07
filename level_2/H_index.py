def solution(citations):
    answer = 0
    citations.sort() #오름차순으로 정렬하기
    for c in range(len(citations)): #citsations의 길이만큼 도는 반복문
        if citations[c] >= len(citations)-c: #h번 이상 인용된 논문이 h편 이상
            answer = len(citations)-c 
            break
        
    return answer
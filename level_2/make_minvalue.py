def solution(A,B):
    answer = 0
    A.sort() #오름차순으로 정렬
    B.sort(reverse=True) #내림차순으로 정렬
    
    for i in range(len(A)):
        answer+=A[i]*B[i] #A의 작은 값과 B의 큰 값들 끼리 곱해지도록 만들기

    return answer
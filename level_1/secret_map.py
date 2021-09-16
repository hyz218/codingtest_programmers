#비밀지도

def solution(n, arr1, arr2):
    answer = []
    arr1_list = []
    arr2_list = []
    
    for i in range(n):
        binary_list = []
        while arr1[i]>=1: #arr1 2진수로 변환
            binary_list.append(arr1[i]%2) 
            arr1[i] = arr1[i]//2
        binary_list.reverse()
        arr1_list.append(binary_list)
        
        binary_list = []
        while arr2[i]>=1: #arr2 2진수로 변환
            binary_list.append(arr2[i]%2)
            arr2[i] = arr2[i]//2
        binary_list.reverse()
        arr2_list.append(binary_list)
        
    for i in range(n):
        if(len(arr1_list[i])<n): #arr1에서 이진수 길이 맞추기(앞에 0 삽입)
            while (len(arr1_list[i])<n):
                arr1_list[i].insert(0,0)
        if(len(arr2_list[i])<n): #arr2에서 이진수 길이 맞추기(앞에 0 삽입)
            while (len(arr2_list[i])<n):
                arr2_list[i].insert(0,0)
            
    for i in range(n):
        string = ""
        for j in range(len(arr1_list)): 
            if arr1_list[i][j]==1 or arr2_list[i][j]==1: 
                string = string+'#' #arr1과 arr2의 이진수 중 하나라도 1이라면 # 추가
            else: 
                string = string+' ' #arr1과 arr2의 이진수 둘 다 0이라면 ' '(공백) 추가
        answer.append(string)
    
    return answer
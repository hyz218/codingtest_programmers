# 스킬트리
# 선행 스킬 순서 skill과 유저들이 만든 스킬트리1를 담은 배열 skill_trees가 매개변수로 주어질 때, 가능한 스킬트리 개수를 return 하는 solution 함수를 작성해주세요.

def solution(skill, skill_trees):
    answer = 0 #answer 초기화
    for i in range(len(skill_trees)): #skill_trees 전체를 도는 반복문
        s = [] #s 초기화
        num = 0 #num chrlghk
        for j in range(len(skill_trees[i])): #skill_trees의 인자를 도는 반복문
            if skill_trees[i][j] in skill: #skill_trees의 인자가 테크트리에 있는 경우
                s.append(skill_trees[i][j]) #s list에 저장
        for k in range(len(s)): #저장되어 있는 s의 길이만큼 도는 반복문
            if s[k]!=skill[k]: #저장된 s가 선행되는 skill을 배우지 않고 배운 경우
                num = 1 #num=1로 변경
                break
        if num==0: #테크트리를 제대로 따라간 경우
            answer+=1 #answer에 갯수 추가
    return answer #answer 반환
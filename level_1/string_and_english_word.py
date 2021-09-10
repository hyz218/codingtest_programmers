#숫자 문자열과 영단어
#"one4seveneight" -> 1478, "2three45sixseven" -> 234567

def solution(s):

    word = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in word:
        s = s.replace(i,str(word.index(i)))
    
    return int(s)
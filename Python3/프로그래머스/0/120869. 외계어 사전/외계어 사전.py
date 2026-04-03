def solution(spell, dic):
    answer = 2
    
    spell_set = set(spell)

    for i in dic:
        if set(i) == spell_set:
            answer = 1
        
    return answer
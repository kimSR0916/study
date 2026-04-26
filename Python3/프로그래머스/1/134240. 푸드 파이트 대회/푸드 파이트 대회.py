def solution(food):
    answer = ''
    player1 = ''
    player2 = ''
    
    for i in range(1, len(food)):
        tmp = food[i] // 2
        
        for j in range(tmp):
            player1 += str(i)
            player2 = str(i) + player2
            
    answer = player1 + '0' + player2
            
        
    
    return answer
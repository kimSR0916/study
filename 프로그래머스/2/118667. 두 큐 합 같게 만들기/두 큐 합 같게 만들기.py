from collections import deque
def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    s1 = sum(q1)
    s2 = sum(q2)
    total = s1 + s2
    
    if total % 2 != 0:
        return -1
    
    total = total // 2
    
    #q1, q2 중에 더 큰 값 찾아서 큰 값에서 값 충족하는 수열 찾고 나머지 q1에 넣기
    #찾는 과정 - 더해가며 찾다가 넘어가는 경우 leftindex 앞당기기    
    
    while True:
        if s1 == total:
            break
        elif s1 > total:
            tmp = q1.popleft()
            q2.append(tmp)
            answer += 1
            s1 -= tmp
            s2 += tmp
        else:
            tmp = q2.popleft()
            q1.append(tmp)
            answer += 1
            s1 += tmp
            s2 -= tmp
        
        if answer >= len(queue1) * 3:
            return -1
            
    return answer
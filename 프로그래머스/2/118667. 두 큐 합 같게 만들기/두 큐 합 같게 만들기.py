from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum1 = sum(q1)
    sum2 = sum(q2)
    total = sum1 + sum2
    
    # 전체 합이 홀수면 두 큐의 합을 같게 만들 수 없음
    if total % 2 != 0:
        return -1
        
    target = total // 2
    limit = len(q1) * 4  # 최대 탐색 횟수 제한
    count = 0
    
    while count <= limit:
        if sum1 == target:
            return count
        elif sum1 > target:
            val = q1.popleft()
            sum1 -= val
            q2.append(val)
            sum2 += val
        else:
            val = q2.popleft()
            sum2 -= val
            q1.append(val)
            sum1 += val
        count += 1
        
    return -1
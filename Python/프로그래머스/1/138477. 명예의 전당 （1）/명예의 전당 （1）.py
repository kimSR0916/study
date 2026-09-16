def solution(k, score):
    answer = []
    nums = []
    
    for i in range (len(score)):
        if i < k:
            nums.append(score[i])
        else:
            tmp = min(nums)
            if tmp < score[i]:
                n = nums.index(tmp)
                nums[n] = score[i]
        answer.append(min(nums))
            
    return answer
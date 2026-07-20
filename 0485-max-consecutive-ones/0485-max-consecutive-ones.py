class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        res = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
            else:
                res = max(res, cnt)
                cnt = 0

        res = max(res, cnt)

        return res
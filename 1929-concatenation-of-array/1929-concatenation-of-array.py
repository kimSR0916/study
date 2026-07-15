class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        cnt = 0

        while cnt < 2:
            for i in nums:
                ans.append(i)

            cnt += 1

        return ans
        
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        list1 = []

        for i in range(n):
            list1.append(nums[i])
            list1.append(nums[i+n])

        return list1
        
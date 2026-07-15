class Solution:
    def isPalindrome(self, x: int) -> bool:
        tmp = str(x)
        tmp_rev = ''
        
        tmp_rev = tmp[::-1]

        if tmp_rev == str(x):
            return True
        else:
            return False
        
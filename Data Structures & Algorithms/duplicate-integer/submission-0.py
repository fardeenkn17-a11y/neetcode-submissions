class Solution:
    def contain_duplicate(self,nums):
        dict={}
        for num in nums:
            if num in dict:
                return True
            dict[num]=1
        return False        
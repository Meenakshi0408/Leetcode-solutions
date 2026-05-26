class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            left=1
            right=1
            for m in range(i-1,-1,-1):
                    left=left*nums[m]
            for n in range(i+1,len(nums)):
                right=right*nums[n]
            res.append(left*right)
        return res
        

        
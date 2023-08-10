class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        n=len(nums)
        for i in range(n):
            if i>0 and nums[i-1]==nums[i]:
                continue
            j=i+1
            k=n-1
            while j<k:
                s=nums[i]+nums[j]+nums[k]
                if s<0:
                    j=j+1
                elif s>0:
                    k=k-1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j=j+1
                    k=k-1
                    while j<k and nums[j-1]==nums[j]:
                        j=j+1
                    while j<k and nums[k]==nums[k+1]:
                        k=k-1
        return res

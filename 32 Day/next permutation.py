class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        low=-1
        high=0
        for i in reversed(range(1,n)):
            if nums[i-1]<nums[i]:
                low=i-1
                break
        if low==-1:
            nums.sort()
            return
        for i in reversed(range(n)):
            if nums[i]>nums[low]:
                high=i
                break
        
        nums[low],nums[high]=nums[high],nums[low]

        nums[low+1:]=nums[low+1:][::-1]
        # print(k,h[::-1],low,high)
        # nums=k+h[::-1]

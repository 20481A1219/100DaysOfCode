class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ans=[]
        for i in nums1:
            k=nums2.index(i)
            if k+1==len(nums2):
                ans.append(-1)
            else:
                j=k+1
                while True:
                    if j>=len(nums2):
                        break
                    if i<nums2[j]:
                        break
                    j=j+1
                if j<len(nums2):
                    ans.append(nums2[j])
                else:
                    ans.append(-1)
        return ans
                

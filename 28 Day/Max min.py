class Solution:
    def findSum(self,A,N): 
        #code here
        min=10**9
        max=-10**9
        for i in A:
            if min>i:
                min=i
            if max<i:
                max=i
        return min+max
# TC- O(N)
# using sort it takes O(NlogN) logN extra for sorting

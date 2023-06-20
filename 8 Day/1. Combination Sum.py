class Solution:
    def combinationSum(self, c: List[int], target: int) -> List[List[int]]:
        ans=[]

        def find(ans,ds,target,i):
            if i==len(c):
                if target==0:
                    ans.append(ds.copy())
                return
            
            if c[i]<=target:
                ds.append(c[i])
                find(ans,ds,target-c[i],i)  # pick the same element if the target>=element
                ds.pop()
            find(ans,ds,target,i+1)    #Not picking it.
        
        find(ans,[],target,0)
        return ans

        """
        TC - 2^N * N  ---------> As each element take pick or not pick that means it have 2 chances 
        so for n elements it becomes 2^N 
        And the remaining N for Storing the ans
        
        SC - k(stack space)*N(combinations)
        """

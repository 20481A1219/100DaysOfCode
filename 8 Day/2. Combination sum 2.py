class Solution:
    def combinationSum2(self, c: List[int], target: int) -> List[List[int]]:
        ans=[]
        c.sort()
        def find(ans,ds,target,i):
            if target==0:
                ans.append(ds.copy())
                return
            for j in range(i,len(c)):
                if j>i and c[j]==c[j-1]:        # After sorting as we are not permitted to take same element more than once we should give if present element is same as previous element
                    continue                    # That means it is a same level call so see at 10:45 of striver video so we dont need to take the same element again and form a new recursioin
                if c[j]>target:                
                    break
                ds.append(c[j])
                find(ans,ds,target-c[j],j+1)
                ds.pop()
        find(ans,[],target,0)
        return ans

       """
       TC - O(2^N * K)
       SC - N*K
       """

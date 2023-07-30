class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # find out the prefix products
        # find out the postfix products
        # for each element simply multiply the prefix and postfix product of that element and append it in the array
        ans=[]
        prefix=[]
        postfix=[]
        p=1
        k=1
        n=len(nums)
        for i in range(n):
            p=p*nums[i]
            prefix.append(p)
            k=k*nums[n-i-1]
            postfix.append(k)
        postfix=postfix[::-1]
        for i in range(n):
            if i==0:
                ans.append(postfix[i+1])
            elif i==n-1:
                ans.append(prefix[i-1])
            else:
                ans.append(prefix[i-1]*postfix[i+1])
        return ans

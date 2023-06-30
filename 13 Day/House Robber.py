class Solution:
    def rob(self, a: List[int]) -> int:
        dp=[-1]*len(a)
        dp[0]=a[0]
        if len(a)>1:
            dp[1]=max(a[0],a[1])
        for i in range(2,len(a)):
            dp[i]=max(dp[i-2]+a[i],dp[i-1])
        return dp[len(a)-1]

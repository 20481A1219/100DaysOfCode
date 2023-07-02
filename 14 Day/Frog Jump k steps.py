#User function Template for python3

class Solution:
    def minimizeCost(self, h, n, k):
        dp=[-1]*n
        dp[0]=abs(h[0]-h[0])
        dp[1]=abs(h[1]-h[0])
        
        for i in range(2,n):
            dp[i]=10e9
            for j in range(1,k+1):
                if i>=j:
                    dp[i]=min(dp[i],dp[i-j]+abs(h[i]-h[i-j]))
        return dp[-1]


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        height = list(map(int, input().split()))
        ob = Solution()
        print(ob.minimizeCost(height, n, k))

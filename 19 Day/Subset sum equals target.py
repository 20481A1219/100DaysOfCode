class Solution:
    def isSubsetSum(self, N, arr, target_sum):
        dp = [[0] * (target_sum + 1) for _ in range(N)]

        for i in range(N):
            dp[i][0] = 1

        if arr[0] <= target_sum:
            dp[0][arr[0]] = 1

        for i in range(1, N):
            for j in range(1, target_sum + 1):
                not_take = dp[i-1][j]
                take = 0
                if j >= arr[i]:
                    take = dp[i-1][j-arr[i]]
                dp[i][j] = not_take or take

        return dp[N-1][target_sum]

class Solution:
	def perfectSum(self, arr, n, sum):
		# code here
		
		mod=10**9+7
		
		dp=[[0]*(sum+1) for i in range(n)]
		
		for i in range(n):
		    dp[i][0]=1
		   
		if arr[0]<=sum:
		    dp[0][arr[0]]+=1
		
		for i in range(1,n):
		    for j in range(sum+1):
		        not_take=dp[i-1][j]
		        take=0
		        if j>=arr[i]:
		            take=dp[i-1][j-arr[i]]
		        
		        dp[i][j]=(take+not_take)%mod
		
		return (dp[-1][-1])%mod

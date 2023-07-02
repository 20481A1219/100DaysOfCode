from typing import *

def ninjaTraining(n: int, points: List[List[int]]) -> int:
    dp=[]
    for i in range(n):
        k=[-1]*3
        dp.append(k)
        
    dp[0][0]=points[0][0]  
    dp[0][1]=points[0][1]
    dp[0][2]=points[0][2]
    
    for i in range(1,n):
        dp[i][0]=points[i][0]+max(dp[i-1][1],dp[i-1][2])  
        dp[i][1]=points[i][1]+max(dp[i-1][0],dp[i-1][2]) 
        dp[i][2]=points[i][2]+max(dp[i-1][1],dp[i-1][0]) 
        
    return max(dp[n-1][0],dp[n-1][1],dp[n-1][2])    

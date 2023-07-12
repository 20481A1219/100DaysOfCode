# User function Template for python3
import sys
sys.setrecursionlimit(100000)
class Solution:
    def toh(self, N, fromm, to, aux):
        
        self.count=0
        
        def helper(N,fromm,to,aux,count):
            # Your code here
            if N==0:
                return
            helper(N-1,fromm,aux,to,self.count)
            self.count=self.count+1
            print("move disk",N,"from rod",fromm,"to rod",to)
            helper(N-1,aux,to,fromm,self.count)
        
        helper(N,fromm,to,aux,self.count)
        return self.count

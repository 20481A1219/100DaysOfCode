class Solution:
    def maxArea(self, height: List[int]) -> int:

        start=0
        end=len(height)-1
        maxarea=0
        while(start<end):
            a=min(height[start],height[end])*(end-start)
            if maxarea<a:
                maxarea=a
            
            if height[start]<height[end]:
                start+=1
            else:
                end-=1
        
        return maxarea

class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        lm=height[l]
        rm=height[r]
        res=0
        while l<r:
            if lm<rm:
                l+=1
                lm=max(lm,height[l])
                res=res+(lm-height[l])
            else:
                r-=1
                rm=max(rm,height[r])
                res=res+(rm-height[r])
        return res            
        
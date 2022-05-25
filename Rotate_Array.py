class Solution:
    
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    
    
        n = len(nums)
        k = k%n
        for i in range((n-k)//2):
            
            temp =nums[i]
            nums[i] = nums[n-k-1-i]
            nums[n-k-1-i] = temp
            
        
        
        for i in range(n-k,n-k//2):
            print(i)
            temp =nums[i]
            nums[i] = nums[n-1-(i-n+k)]
            nums[n-1-(i-n+k)] = temp
        
        
        for i in range(n//2):
            temp =nums[i]
            nums[i] = nums[n-1-i]
            nums[n-1-i] = temp
        print(nums)
        

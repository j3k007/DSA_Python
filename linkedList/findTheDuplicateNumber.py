class Solution:
    def findDuplicate(self, nums:list[int])-> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
            
ans = Solution()
l = [1,2,3,4,4]
print(ans.findDuplicate(nums=l))
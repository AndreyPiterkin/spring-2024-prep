class Solution:
    def findMin(self, nums: list) -> int:
        l, r = 0, len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        while l <= r:
            mid = (l + r) // 2
            if mid - 1 >= 0 and nums[mid] < nums[mid - 1]:
                return nums[mid] 
            if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]: 
                return nums[mid]

            if nums[mid] > nums[0]:
                l = mid + 1
            else:
                r = mid - 1


class Solution2:
    def findMin(self, nums) -> int:
        l, r = 0, len(nums) - 1
        if l == r:
            return nums[0]

        while l <= r:
            mid = (l + r) // 2
            if nums[l] < nums[r]:
                return nums[l]

            if nums[mid] > nums[l]:
                l = mid + 1
            else:
                r = mid - 1

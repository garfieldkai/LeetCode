class Solution:
    '''
    给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
    你可以假设数组中无重复元素。
    '''
    def searchInsert(self, nums, target):
        length = len(nums)
        left = 0
        right = length - 1
        if not nums:
            return 0
        if left==right:
            if nums[0]<target:
                return 1
            elif nums[0]>=target:
                return 0

        while left < right:
            middle = (left + right)//2
            if nums[middle]==target:
                return middle
            if target < nums[left]:
                return left
            elif target > nums[right]:
                return right
            elif nums[left]<= target and target <=nums[middle]:
                right = middle
            else:
                left = middle + 1
        if nums[left]==target:
            return left
        else:
            return right
if __name__ == '__main__':
    nums = [5]
    target = 8
    solution = Solution()
    print(solution.searchInsert(nums,target))
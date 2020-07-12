# 二分法查询（前提：有序序列， 难点：搜索区间 右端开闭问题）
# 右端闭区间


class BinarySearch(object):

    def __init__(self):
        pass

    def binary_search_1(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2  # 防止溢出
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return -1

    def binary_search_2(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
        if nums[left] == target:
            return left
        else:
            return -1

    def binary_search_left_side_1(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        if left >= len(nums):
            return -1
        if nums[left] == target:
            return left
        else:
            return -1

    def binary_search_left_side_2(self, nums, target):
        if len(nums) == 0:
            return -1
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
        if left >= len(nums):
            return -1
        if nums[left] == target:
            return left
        else:
            return -1

    def binary_search_right_side_1(self, nums, target):
        if len(nums) == 0:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1
        if right < 0:
            return -1
        if nums[right] == target:
            return right
        else:
            return -1

    def binary_search_right_side_2(self, nums, target):
        if len(nums) == 0:
            return -1
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        if left == 0:
            return -1
        if nums[left - 1] == target:
            return left - 1
        else:
            return -1


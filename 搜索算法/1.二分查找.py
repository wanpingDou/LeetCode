# 确认target在升序整型数组中的位置
# 注意：二分查找最主要的是边界问题
class Solution:
    def search(nums, target):
        # 二分查找
        # 由前后双指针确认中间只针，三指针法，
        # 不断区间二分，确认目标所在区间，缩小查找范围
        # L, R = 0, len(nums)-1
        # while R>=L:
        #     mid = L + (R-L)//2
        #     if target>nums[mid]:
        #         L = mid + 1
        #     elif target<nums[mid]:
        #         R = mid - 1
        #     else:
        #         return mid
        # return -1

        L = 0
        R = len(nums) - 1
        while R>=L:
            mid = L + (R-L)//2
            if target > nums[mid]:
                L = mid + 1
            elif target == nums[mid]:
                return mid
            else:
                R = mid - 1
        return -1

if __name__ == '__main__':
    nums = [-1,0,3,5,9,12]
    target = 9
    print(Solution.search(nums, target))

    nums = [-1,0,3,5,9,12]
    target = 2
    print(Solution.search(nums, target))
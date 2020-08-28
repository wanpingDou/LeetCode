
# coding: utf-8

# # 快速排序
# 
#     基本思想：根据基准值一趟排序分隔成独立的两部分，左边全部大于基准值，右边全部小于基准值。分别对这两部分记录继续相同操作。步骤如下：
# 
# - 选取基准：从数据中选择一个数作为基准值（pivot），一般选择最左边。
# - 分区操作：将数据中小于基准的全部放在pivot的左边位置，其余放在右边位置。该（分区）操作完成之后，原来的基准会在数据的中间某一位置。
# - 递归下去，得到有序结果。
# 
# ![归并排序](attachment:guibing.gif)

# In[4]:


def partition(nums, start, end):
    '''
    1. 构建头尾双指针
    2. 选取最左边的数字为基准
    3. 从两端交替向中间扫描，直至i=j
    4. 这样一趟下来之后，基准会位于nums中的一个位置，左边的全部小于它，右边均大于基准
    5. 返回i或者j的位置，再对i或者j的两端继续按照该方法做下去，这就是QuickSort函数递归的任务
    
    '''
    i, j = start, end
    pivot = nums[i] # 以nums[i]为基准
    while i<j:
        # 右侧大于基准值，指针左移
        while j>i and nums[j]>=pivot: # 从右向左扫描，直到右边的数比基准值小为止
            j -= 1                     ## 向左移动
        nums[i] = nums[j]              ## 将右边小于基准值的值排到前面i的位置去
        # 左侧小于基准值，指针右移
        while i<j and nums[i]<=pivot: # 从左向右扫描，直到左边的数比基准值大为止
            i += 1
        nums[j] = nums[i]
    nums[i] = pivot
    return i

def QuickSort(nums, start, end):
    """
    一趟排序，目的是将左边的一个元素作为基准，将数据中小于基准全放基准的左边，\
    大于的部分放基准的右边，输出基准最终位置。
    nums：列表
    start：要排序的起始位置
    end：要排序的结束位置
    """
    # 递归部分
    if start >= end:
        return nums
    else:
        i = partition(nums, start, end)
        QuickSort(nums, start, i-1)
        QuickSort(nums, i+1, end)
    return nums


# In[5]:

if __name__ == '__main__':
    List = [5, 2, 3, 2, 1]
    print(QuickSort(List, 0, len(List)-1))



    # leetcode题目
    # [215. 数组中的第K个最大元素](https://leetcode-cn.com/problems/kth-largest-element-in-an-array/submissions/)

# 剑指 Offer 51. 数组中的逆序对：https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/
# 求小和：求所有数组中小于等于某位置的和


def merge(nums, left, mid, right): 
    """
    ############ 
      归并排序
    ############
    递归划分到最细的粒度，然后左右归并。
    时间复杂度分析：
        根据Master公式T(N) = a*T(N/b) + O(N**d)
        这里a=b=2,d=1
        因为log_(a)(b)==d,所以时间复杂度为O(N**d*logN) = O(NlogN)
    空间复杂度：
        O(N)
    为什么时间复杂度没插入大：
        插入排序等时间复杂度为O(N**2)的，主要是在比较行为上，
        插入排序需要比较很多次才能搞定一个数，且每一轮的比较都是独立的。
        归并排序没有浪费比较行为，左侧有序、右侧有序，进行左右指针的
        左右区域比较。比较行为没有被浪费，变成了一个整体有序的部分，
        去跟下一个更大范围的东西去merge.
    """
    n1 = mid - left + 1
    n2 = right - mid 
  
    # 创建临时数组
    L = [0] * n1
    R = [0] * n2
  
    # 拷贝数据到临时数组 numsays L[] 和 R[] 
    for i in range(0 , n1): 
        L[i] = nums[left + i] 
  
    for j in range(0 , n2): 
        R[j] = nums[mid + 1 + j] 
  
    # 归并临时数组到 nums[left..right] 
    i = 0     # 初始化第一个子数组的索引
    j = 0     # 初始化第二个子数组的索引
    k = left  # 初始归并子数组的索引
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            nums[k] = L[i] 
            i += 1
        else: 
            nums[k] = R[j] 
            j += 1
        k += 1
  
    # 拷贝 L[] 的保留元素
    while i < n1: 
        nums[k] = L[i] 
        i += 1
        k += 1
  
    # 拷贝 R[] 的保留元素
    while j < n2: 
        nums[k] = R[j] 
        j += 1
        k += 1
    return nums
  
def mergeSort(nums, left, right):
    if right > left: 
        # 将数据从中间劈开，递归下去，发现到最后是四个数作为一组
        mid = left + (right-left)//2
        mergeSort(nums, left, mid)
        mergeSort(nums, mid+1, right)
        # 最后分别排序，并合并分区
        merge(nums, left, mid, right)
    return nums

if __name__ == '__main__':
    nums = [3, 5, 1, 4, 8, 7]
    left = 0
    right = len(nums)-1
    print(mergeSort(nums, left, right))

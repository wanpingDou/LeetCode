class Solution:
    def LongestSubstring(s):
        
        """
        双指针 + 滑窗
        1、不仅仅求出了最长不重复子序列的长度
        2、res是输出最长子序列，并将所有的结果放入列表，可能存在多个最长子序列
        """
        L = -1
        mapping = {}
        res = []
        max_len = 0
        for i, v in enumerate(s):
            # 当前的字符上一次出现的位置是在左指针与现在之间
            # 这种情况需要移动左指针到目前字符在上次出现的位置
            if (v in mapping) and mapping[v]>L:
                L = mapping[v]
            # 否则
            else:
                max_len = max([max_len, i-L])
            # 每一步记录一下当前以及以前的最大不重复字串
            res.append(s[L+1:i+1])
            # 每次过滤res的结果，去重，不至于res的项太多造成内存溢出问题
            res = [sub_s for sub_s in set(res) if len(sub_s)>=max_len]

            mapping[v] = i
        return max_len



if __name__ == '__main__':
    s = "pwdwk"
    # s = "  hello world!  "
    print(Solution.LongestSubstring(s))


class Solution:
    def reverseWords(s):
        """
        # 左右双指针去空格
        # 用临时字符盛放一个单词
        # 讲一个完成的临时字符串放入栈
        # 出栈拼接栈元素
        """
        import collections
        left, right = 0, len(s) - 1
        # 去掉字符串开头的空白字符
        while left <= right and s[left] == ' ':
            left += 1
        
        # 去掉字符串末尾的空白字符
        while left <= right and s[right] == ' ':
            right -= 1
            
        d, word = collections.deque(), []
        # 将单词 push 到队列的头部
        while left <= right:
            if s[left] == ' ' and word:
                d.appendleft(''.join(word))
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            left += 1
        d.appendleft(''.join(word))
        
        return ' '.join(d)


if __name__ == '__main__':
    s = 'the sky is blue'
    print(Solution.reverseWords(s))

    s = '  hello world!  '
    print(Solution.reverseWords(s))

    s = 'a good   example'
    print(Solution.reverseWords(s))
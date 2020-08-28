class Solution:
    def longestPalindrome(s):
        # 方法一：暴力双指针
        # 方法二：动态规划
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        # 枚举子串的长度 l+1
        for l in range(n):
            # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
            for i in range(n):
                j = i + l
                if j >= len(s):
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    # 当前i->j是不是字串，只需要看两头是否相等且左下角i+1->j-1是不是回文串
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i:j+1]
        return ans

if __name__ == '__main__':
    s = 'a'
    print(Solution.longestPalindrome(s))
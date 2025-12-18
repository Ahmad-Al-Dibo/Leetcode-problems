class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            if not (-2**31 <= x <= 2**31 - 1): raise ValueError("")
            return str(x)==str(x)[::-1]


numbs = [[1, 2, 3, 4, 5, 6], [12, 13, 543, -1, 54 , -12, 43, 65], [56, -56 , 89489 , 456, 121, 156], [121, -121, 10, 12 , 11]]

for i in numbs:
    for j in i:
        asr = Solution().isPalindrome(j)
        print(f"{j}: {asr}")

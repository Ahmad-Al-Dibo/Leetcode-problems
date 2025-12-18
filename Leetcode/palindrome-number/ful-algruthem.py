def last_digit(x: int) -> int:
    """
    Returns the last digit of an integer x.
    Equivalent to x % 10 using math only.
    """
    if x < 0:
        x = -x  # maak het positief, zodat laatste cijfer klopt
    # haal het decimale deel weg zoals op een rekenmachine
    return int(x - (x // 10) * 10)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        original = x
        reversed_num = 0

        while x > 0:
            digit = last_digit(x)
            reversed_num = reversed_num * 10 + digit
            x //= 10
            print(f"x: {x}")
            if x == 0:
                print(reversed_num) 
        return original == reversed_num

numbs = [[1, 2, 3, 4, 5, 6], [12, 13, 543, -1, 54 , -12, 43, 65], [56, -56 , 89489 , 456, 121, 156], [121, -121, 10, 12 , 11], [129]]

# for i in numbs:
#     for j in i:
#         asr = Solution().isPalindrome(j)
#         print(f"{j}: {asr}")

asr = Solution().isPalindrome(89489)
print(f"{89489}: {asr}")


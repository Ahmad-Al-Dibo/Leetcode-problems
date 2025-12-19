## Intuition

At first, I thought the problem could be solved by simply converting each Roman character to its numeric value and returning the sum. However, after testing this idea, I realized that Roman numerals are not always additive. In some cases, a smaller numeral appears before a larger one, which means the smaller value must be subtracted instead of added.

---

## Approach

We iterate through the string from left to right and compare each character with the next one:

* If the current value is **smaller than the next value**, we subtract it from the total.
* Otherwise, we add it to the total.

This correctly handles cases like `IV`, `IX`, `XL`, etc., while still working for normal additive cases like `II` or `XX`.

---

## Complexity

* **Time complexity:**
  $$O(n)$$ — we traverse the string once.

* **Space complexity:**
  $$O(1)$$ — the hashmap has a fixed size and we use only a few variables.

---

## Code

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        hashmap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        for i in range(len(s)):
            if i + 1 < len(s) and hashmap[s[i]] < hashmap[s[i + 1]]:
                total -= hashmap[s[i]]
            else:
                total += hashmap[s[i]]
        
        return total
```


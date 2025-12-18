
## **Titel:** Check of een getal een palindrome is


## Doel / Probleem dat het oplost

* Controleert of een gegeven integer hetzelfde blijft als je het omdraait.
* Negatieve getallen zijn **geen palindromen**.
* Werkt voor 32-bit integers.

---

## Inputs en outputs

* **Input:** een integer `x`
* **Output:** `True` als `x` een palindrome is, anders `False`

**Voorbeelden:**

| Input | Output | Uitleg                         |
| ----- | ------ | ------------------------------ |
| 121   | True   | 121 omgedraaid = 121           |
| -121  | False  | Negatieve getallen tellen niet |
| 10    | False  | 10 omgedraaid = 01 ≠ 10        |
| 0     | True   | 0 omgedraaid = 0               |

---

## Beschrijving van de logica / stappen

1. Controleer eerst of `x` negatief is. Zo ja, return `False`.
2. Optioneel: controleer of `x` binnen het bereik van een 32-bit integer ligt.
3. Zet `x` om naar een string (`str(x)`).
4. Vergelijk de string met de omgekeerde string (`str(x)[::-1]`).
5. Return `True` als ze gelijk zijn, anders `False`.

---

## Complexiteit

* **Tijd:** O(n), waarbij n het aantal cijfers in `x` is.
* **Ruimte:** O(n) extra, omdat we de string en zijn omgekeerde maken.

> Tip: er is ook een wiskundige methode zonder strings die O(1) extra ruimte gebruikt.

---

## Voorbeeld / illustratie

```python
x = 121
str(x) = "121"
str(x)[::-1] = "121"
Resultaat = True
```

```python
x = -121
Negatief → Resultaat = False
```

```python
x = 123
str(x) = "123"
str(x)[::-1] = "321"
Resultaat = False
```

---

## Extra opmerkingen / beperkingen

* Negatieve getallen worden altijd als niet-palindroom beschouwd.
* Alleen integers binnen 32-bit bereik worden toegestaan (optioneel).
* Voor zeer grote integers kan de stringconversie geheugen gebruiken.

---

## Python code voorbeeld

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if not (-2**31 <= x <= 2**31 - 1):
            raise ValueError("Integer buiten 32-bit bereik")
        return str(x) == str(x)[::-1]

# Test
numbs = [121, -121, 10, 123, 0]
sol = Solution()
for num in numbs:
    print(f"{num}: {sol.isPalindrome(num)}")
```

**Output:**

```
121: True
-121: False
10: False
123: False
0: True
```


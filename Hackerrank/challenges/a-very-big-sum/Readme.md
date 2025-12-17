
## Constraints

- **1 ≤ n ≤ 10**  
  `n` is het aantal elementen in de array.  
  De array bevat minimaal 1 en maximaal 10 elementen.

- **0 ≤ arr[i] ≤ 10¹⁰**  
  Elk element `arr[i]` is een **niet-negatief getal** en kan maximaal  
  **10.000.000.000 (10 miljard)** zijn.

Kort gezegd:
> Je werkt met een **kleine array**, maar met **zeer grote getallen**.

---

## Sample Input

| STDIN | Function |
|------:|----------|
| 5 | arr[] size n = 5 |
| 1000000001 1000000002 1000000003 1000000004 1000000005 | arr = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005] |

---

## Output
```

5000000015

```

---

## Explanation

We tellen alle elementen in de array bij elkaar op:

```

1000000001

* 1000000002
* 1000000003
* 1000000004
* 1000000005

---

= 5000000015

```

Omdat de waarden **erg groot** zijn, is het belangrijk om een datatype te gebruiken
dat grote getallen aankan (bijvoorbeeld `int64` of `long` in andere talen).

Python kan dit automatisch aan, omdat integers geen vaste limiet hebben.
```py
for i in ar:
  assert 1<= len(ar) <= 10
  assert 0 <= i <= 10**10

```

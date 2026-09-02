# 🔥 Even vs Odd Digit Sum Made Easy ⚖️ | Python | O(N) | Beginner-Friendly


# Problem Understanding

We are given a number as a string `num`.

We need to check whether:

* Sum of digits at **even indices**
* Sum of digits at **odd indices**

are equal.

If they are equal → `True`
Otherwise → `False`

---

# Key Idea

Traverse the string once:

* `i % 2 == 0` → add digit to `evenres`
* Otherwise → add digit to `oddres`

Finally, compare both sums.

---

# Code Explanation

### 1. Convert String to List

```python
num = list(num)
```

Example:

```text
"1230" → ['1', '2', '3', '0']
```

### 2. Initialize Sums

```python
evenres = 0
oddres = 0
```

These store the sums for even and odd indices.

### 3. Traverse the Digits

```python
for i in range(len(num)):
```

Check the index:

```python
if i % 2 == 0:
    evenres += int(num[i])
else:
    oddres += int(num[i])
```

For:

```text
num = "1230"
```

Even indices:

```text
1 + 3 = 4
```

Odd indices:

```text
2 + 0 = 2
```

### 4. Compare the Sums

```python
if evenres == oddres:
    return True
return False
```


---

# Example

```text
num = "1230"

Even index sum = 1 + 3 = 4
Odd index sum  = 2 + 0 = 2

4 != 2
```

Output:

```text
False
```

---

# Complexity

**Time:** `O(N)` — one traversal of the digits.

**Space:** `O(N)` — because you convert the string into a list.

---

### 💻  Code

```python
class Solution:
    def isBalanced(self, num: str) -> bool:
        num = list(num)
        evenres = 0
        oddres = 0

        for i in range(len(num)):
            if i % 2 == 0:
                evenres += int(num[i])
            else:
                oddres += int(num[i])

        if evenres == oddres:
            return True
        return False
```

# ⚡EASY SOLUTION⚡ | O(1) | PYTHON | ⚡BEGINNER FRIENDLY⚡



# 🚀 Smallest Even Multiple | Simple Math Approach 🔢

---

# 🧠 Problem Understanding

We are given an integer `n`.

Our task is:

> Find the smallest positive number that is divisible by both `n` and `2`.

In other words, find the **Least Common Multiple (LCM)** of `n` and `2`.

---

# 💡 Key Insight

* If `n` is already even, then `n` itself is divisible by `2`.
* If `n` is odd, multiply it by `2` to make it even.

---

# 🔎 Code Explanation

## 1️⃣ Check if Number is Even

```python
if n % 2 == 0:
    return n
```

✨ If `n` is even, it is already the smallest even multiple.

---

## 2️⃣ Otherwise Multiply by 2

```python
else:
    return n * 2
```

✨ If `n` is odd, the smallest even multiple is `2 × n`.

---

# 📊 Example Walkthrough

### Example 1

#### Input

```python
n = 5
```

Since `5` is odd:

```python
5 × 2 = 10
```

#### Output

```python
10
```

---

### Example 2

#### Input

```python
n = 6
```

Since `6` is already even:

#### Output

```python
6
```

---

# ⏱ Time & Space Complexity

### ⏱ Time Complexity: O(1)

Only one condition check is performed.

### 📦 Space Complexity: O(1)

No extra space is used.

---


# 💻 Code

```python
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        else:
            return n * 2
```

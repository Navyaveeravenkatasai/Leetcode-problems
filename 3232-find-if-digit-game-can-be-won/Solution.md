# ⚡EASY SOLUTION⚡ | O(N) | PYTHON | ⚡BEGINNER FRIENDLY⚡



# 🚀 Find if Digit Game Can Be Won | Simple Sum Comparison Approach 🔢

---

# 🧠 Problem Understanding

We are given an integer array `nums`.

Alice can choose one of two groups:

1. Numbers having **1 digit** (`< 10`)
2. Numbers having **2 digits** (`>= 10`)

Alice wins if the sum of one group is **strictly greater** than the sum of the other group.

Our task is:

> Return `True` if Alice can win, otherwise return `False`.

---

# 💡 Key Insight

Instead of simulating a game:

👉 Calculate:

* Sum of all 1-digit numbers
* Sum of all 2-digit numbers

If the sums are different:

```python id="1"
one_digit_sum != two_digit_sum
```

Alice can choose the larger sum and win.

If the sums are equal:

```python id="2"
one_digit_sum == two_digit_sum
```

Alice cannot win.

---

# 🔎 Code Explanation Step-by-Step

---

## 1️⃣ Initialize Sum for One-Digit Numbers

```python
first = 0
```

✨ Purpose:

* Store sum of numbers less than `10`

---

## 2️⃣ Calculate One-Digit Sum

```python
for ch in range(len(nums)):
    if nums[ch] < 10:
        first += nums[ch]
```

Example:

```python
nums = [1,2,3,10]
```

One-digit numbers:

```python
1 + 2 + 3 = 6
```

---

## 3️⃣ Initialize Sum for Two-Digit Numbers

```python
second = 0
```

✨ Purpose:

* Store sum of numbers greater than or equal to `10`

---

## 4️⃣ Calculate Two-Digit Sum

```python
for ch in range(len(nums)):
    if nums[ch] >= 10:
        second += nums[ch]
```

Example:

```python
10
```

Sum becomes:

```python
10
```

---

## 5️⃣ Compare Both Sums

```python
if first > second or second > first:
    return True
```

✨ Meaning:

If sums are different:

```python
first != second
```

Then Alice can choose the larger group and win.

---

## 6️⃣ Equal Sum Case

```python
return False
```

When:

```python
first == second
```

Neither group gives an advantage.

---

# 📊 Example Walkthrough

## Example 1

### Input

```python
nums = [1,2,3,4,10]
```

---

### One-Digit Sum

```python
1 + 2 + 3 + 4 = 10
```

---

### Two-Digit Sum

```python
10
```

---

### Compare

```python
10 == 10
```

Alice cannot gain an advantage.

### Output

```python
False
```

---

## Example 2

### Input

```python
nums = [1,2,3,10,20]
```

---

### One-Digit Sum

```python
1 + 2 + 3 = 6
```

---

### Two-Digit Sum

```python
10 + 20 = 30
```

---

### Compare

```python
30 > 6
```

Alice chooses the two-digit group.

### Output

```python
True
```

---

# ⏱ Time & Space Complexity

## ⏱ Time Complexity: O(N)

We traverse the array twice.

```python
O(N) + O(N) = O(N)
```

---

## 📦 Space Complexity: O(1)

Only two variables are used:

```python
first
second
```

No extra data structure is needed.

---

# 💻 Code

```python
class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        first = 0
        for ch in range(len(nums)):
            if nums[ch] < 10:
                first += nums[ch]

        second = 0

        for ch in range(len(nums)):
            if nums[ch] >= 10:
                second += nums[ch]

        if first > second or second > first:
            return True

        return False
```

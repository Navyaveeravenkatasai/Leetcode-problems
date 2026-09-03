# 🔥 Maximum Digit Range Made Simple 🔢 | Python | O(N × D) | Beginner-Friendly Guide 💡


# Problem Understanding

We are given a list of integers `nums`.

For each number, we need to find:

> **Maximum digit − Minimum digit**

This is called the **digit range**.

Then:

* Find the **maximum digit range** among all numbers.
* If multiple numbers have the same maximum range, **add those numbers together**.
* Return the final sum.

---

# Key Idea

For every number:

1. Convert it to a string.
2. Find its largest digit.
3. Find its smallest digit.
4. Calculate:

```text
digit range = maximum digit - minimum digit
```

5. Compare this range with `max_range`.
6. If it is larger, replace `res`.
7. If it is equal, add the number to `res`.

---

# Code Explanation

### 1. Initialize Variables

```python id="x7k2pm"
res = 0
sumi = 0
max_range = 0
```

* `res` → stores the final answer.
* `sumi` → stores the current number's digit range.
* `max_range` → stores the largest range found so far.

---

### 2. Process Every Number

```python id="p2r8za"
for ch in nums:
```

Example:

```python id="k8h3yt"
nums = [123, 456, 909]
```

We process:

```text
123
456
909
```

one by one.

---

### 3. Initialize Maximum and Minimum Digit

```python id="w4c6qn"
maxi = float('-inf')
mini = float('inf')
```

We start with:

```text
maxi = very small value
mini = very large value
```

This allows the first digit to correctly update both values.

---

### 4. Check Every Digit

```python id="n6j4qs"
for digit in str(ch):
```

For example:

```text
ch = 583
```

The digits are:

```text
5, 8, 3
```

Now:

```python id="d2w8ax"
maxi = max(int(digit), maxi)
mini = min(int(digit), mini)
```

After checking all digits:

```text
Maximum digit = 8
Minimum digit = 3
```

---

### 5. Calculate Digit Range

```python id="z9k5re"
sumi = maxi - mini
```

For `583`:

```text
8 - 3 = 5
```

So:

```text
sumi = 5
```

---

### 6. If We Find a New Maximum Range

```python id="q3v7bd"
if sumi > max_range:
    max_range = sumi
    res = ch
```

Suppose:

```text
max_range = 3
```

and the current number has:

```text
sumi = 7
```

Since:

```text
7 > 3
```

we update:

```text
max_range = 7
res = current number
```

---

### 7. If the Range is Equal

```python id="m8r2kc"
elif sumi == max_range:
    res += ch
```

This is important.

If another number has the **same maximum range**, add it to `res`.

Example:

```text
Number 1 → range 8
Number 2 → range 8
```

Then:

```text
res = number1 + number2
```

---

# Example Walkthrough

### Input

```python id="e3n7qa"
nums = [123, 583, 909]
```

### Number 1 → `123`

Digits:

```text
1, 2, 3
```

Maximum:

```text
3
```

Minimum:

```text
1
```

Range:

```text
3 - 1 = 2
```

So:

```text
max_range = 2
res = 123
```

---

### Number 2 → `583`

Digits:

```text
5, 8, 3
```

Maximum:

```text
8
```

Minimum:

```text
3
```

Range:

```text
8 - 3 = 5
```

Since:

```text
5 > 2
```

update:

```text
max_range = 5
res = 583
```

---

### Number 3 → `909`

Digits:

```text
9, 0, 9
```

Maximum:

```text
9
```

Minimum:

```text
0
```

Range:

```text
9 - 0 = 9
```

Since:

```text
9 > 5
```

update:

```text
max_range = 9
res = 909
```

### Final Output

```text
909
```

---

# Example of Equal Maximum Range

```python id="u5s9cx"
nums = [19, 28, 37]
```

Ranges:

```text
19 → 9 - 1 = 8
28 → 8 - 2 = 6
37 → 7 - 3 = 4
```

Only `19` has the maximum range.

Output:

```text
19
```

If two numbers had the same maximum range, your code would add them together.

---

# Complexity

### Time Complexity: `O(N × D)`

* `N` → number of integers.
* `D` → number of digits in each integer.

We examine every digit of every number.

### Space Complexity: `O(1)`

Apart from the temporary string representation, only a few variables are used.

---

# 💻 Code

```python
class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:

        res = sumi = max_range = 0

        for ch in nums:

            maxi = float('-inf')
            mini = float('inf')

            for digit in str(ch):
                maxi = max(int(digit), maxi)
                mini = min(int(digit), mini)

            sumi = maxi - mini

            if sumi > max_range:
                max_range = sumi
                res = ch

            elif sumi == max_range:
                res += ch

        return res
```

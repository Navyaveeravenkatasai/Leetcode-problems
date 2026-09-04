# 🚀 First Stable Index Made Easy 🎯 | Sliding Window + Min/Max | Python | O(N²)


# Problem Understanding

We are given an array `nums` and an integer `k`.

For each index `ch`, we consider the elements from the beginning up to that index.

We calculate:

```text
Maximum value - Minimum value
```

If this difference becomes **less than or equal to `k`**, we return that index.

If no index satisfies the condition, return `-1`.

---

# 💡 Key Idea

Your solution maintains two lists:

* `maxi_res` → stores all elements processed so far.
* `mini_res` → represents the remaining elements after removing the first element each time.

At every index:

1. Add the current number to `maxi_res`.
2. Find the maximum of `maxi_res`.
3. Find the minimum of `mini_res`.
4. Calculate `max - min`.
5. If the difference is `≤ k`, return the current index.
6. Otherwise, remove the first element from `mini_res`.

---

# 🔎 Code Explanation

### 1️⃣ Create Lists

```python
maxi_res = []
mini_res = []
```

`mini_res` initially contains all elements:

```python
for ch in range(len(nums)):
    mini_res.append(nums[ch])
```

For:

```text
nums = [3, 1, 4, 2]
```

We get:

```text
mini_res = [3, 1, 4, 2]
```

---

### 2️⃣ Process Each Index

```python
for ch in range(len(nums)):
```

We examine every index from left to right.

---

### 3️⃣ Add Current Element

```python
maxi_res.append(nums[ch])
```

For example:

```text
ch = 0
nums[0] = 3
```

Then:

```text
maxi_res = [3]
```

At the next iteration:

```text
maxi_res = [3, 1]
```

---

### 4️⃣ Find Maximum and Minimum

```python
res = max(maxi_res)
ans = min(mini_res)
```

Then calculate:

```python
sumi = res - ans
```

So:

```text
maximum - minimum
```

---

### 5️⃣ Check the Stability Condition

```python
if sumi <= k:
    return ch
```

If:

```text
maximum - minimum <= k
```

the current index is considered stable, so we immediately return it.

---

### 6️⃣ Remove the First Element

```python
del mini_res[0]
```

If the condition isn't satisfied, remove the first element from `mini_res`.

For example:

```text
Before:
[3, 1, 4, 2]

After:
[1, 4, 2]
```

Then the next iteration works with the updated list.

---

### 7️⃣ No Valid Index

```python
return -1
```

If the loop finishes without finding a valid index, return `-1`.

---

# 🧪 Example Walkthrough

Suppose:

```python
nums = [3, 1, 4]
k = 2
```

### Index 0

```text
maxi_res = [3]
mini_res = [3, 1, 4]

max = 3
min = 3

difference = 3 - 3 = 0
```

Since:

```text
0 <= 2
```

we return:

```text
0
```

---

### Another Example

```python
nums = [10, 1, 5]
k = 2
```

At index `0`:

```text
max = 10
min = 10
difference = 0
```

So the answer is immediately:

```text
0
```

---

# ⏱ Complexity

### Time Complexity: `O(N²)`

### Space Complexity: `O(N)`

---

# 💻 Code

```python
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:

        maxi_res = []
        mini_res = []
        sumi = 0

        for ch in range(len(nums)):
            mini_res.append(nums[ch])

        for ch in range(len(nums)):
            maxi_res.append(nums[ch])

            res = max(maxi_res)
            ans = min(mini_res)

            sumi = res - ans

            if sumi <= k:
                return ch

            del mini_res[0]

        return -1
```

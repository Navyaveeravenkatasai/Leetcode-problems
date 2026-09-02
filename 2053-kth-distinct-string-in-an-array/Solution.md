# 🚀 Find the K-th Unique String 🔍 | Python | O(N) | Beginner-Friendly 💡


# Problem Understanding

We are given:

* A string array `arr`
* An integer `k`

We need to find the **k-th distinct string** while maintaining the original order.

If there are fewer than `k` distinct strings, return `""`.

---

# Key Idea

Use a **frequency dictionary**:

1. Count how many times each string appears.
2. Collect strings that appear exactly once.
3. Return the `k-1` index because Python uses **0-based indexing**.

---

# Code Explanation

### 1. Count Frequencies

```python
freq = {}
```

Then:

```python
for ch in arr:
    freq[ch] = freq.get(ch, 0) + 1
```

Example:

```text
arr = ["d", "b", "c", "b", "c", "a"]
```

Frequency:

```text
d → 1
b → 2
c → 2
a → 1
```

---

### 2. Store Distinct Strings

```python
res = []

for key, value in freq.items():
    if value == 1:
        res.append(key)
```

Only strings appearing exactly once are added.

Result:

```text
["d", "a"]
```

Python dictionaries preserve insertion order, so the original order is maintained.

---

### 3. Check if K-th Distinct Exists

```python
if k > len(res):
    return ""
```

If there aren't enough distinct strings, return an empty string.

---

### 4. Return the K-th Distinct String

```python
return res[k - 1]
```

We use `k - 1` because list indexing starts from `0`.

Example:

```text
k = 1 → index 0
k = 2 → index 1
k = 3 → index 2
```

---

# Example

```text
arr = ["d","b","c","b","c","a"]
k = 2
```

Distinct strings:

```text
["d", "a"]
```

2nd distinct string:

```text
"a"
```

Output:


---

# Complexity

**Time:** `O(N)` — frequency counting and checking are linear.

**Space:** `O(N)` — dictionary and result list store elements.

### code
    
```text

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq={}
        res = []
        for ch in arr:
            freq[ch] = freq.get(ch,0) + 1

        for key,value in freq.items():
            if value == 1:
                res.append(key)

        if k > len(res):
            return ""
        return res[k-1]
        
        
```


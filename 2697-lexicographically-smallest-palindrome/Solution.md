#  Clean ✅ | Simple ✨ | Beats 💯% | Easy to Understand 💡 | Efficient ⚡


# 🚀 Make Smallest Palindrome | Simple Two Pointer Approach 🔤

---

## 🧠 Problem Understanding

We are given a string `s`.

Our task is:

> Convert the string into a palindrome using the **minimum number of operations**.

---

## 📌 What is a Palindrome?

A palindrome reads the same:

* from left to right
* and right to left

Examples:

```python id="h9v58m"
"aba"
"racecar"
"madam"
```

---

## 📌 Allowed Operation

We can:

> Replace any character with another lowercase English letter.

---

## 🎯 Goal

Create:

> The **lexicographically smallest palindrome**

---

## 💡 What does “Lexicographically Smallest” mean?

Smaller alphabetical characters are preferred.

Example:

```python id="pjg8lu"
'a' < 'b' < 'c'
```

So:

```python id="dnceg6"
"abba" < "acca"
```

because:

```python id="0c7d3m"
'b' < 'c'
```

---

# 💡 Key Insight

For every pair:

```python id="e5q9km"
s[left]
s[right]
```

👉 If characters are different:

* Replace the larger character with the smaller one

Why?

* This keeps the palindrome lexicographically smallest

---

# 🔎 Code Explanation Step-by-Step

---

## 1️⃣ Convert String into List

```python id="7w5e7d"
s = list(s)
```

✨ Purpose:

* Strings are immutable in Python
* List allows modification

---

## 2️⃣ Initialize Two Pointers

```python id="jrl48y"
left = 0
right = len(s) - 1
```

✨ Purpose:

* `left` starts from beginning
* `right` starts from end

---

## 3️⃣ Traverse the String

```python id="a9n62i"
for i in range(len(s)):
```

👉 Move both pointers toward center.

---

## 4️⃣ Compare Characters

```python id="dnm9bz"
if s[left] > s[right]:
```

✨ Meaning:

* Left character is alphabetically larger
* Replace it with smaller right character

Example:

```python id="jtl0ct"
'd' > 'a'
```

So:

```python id="bqarf2"
'd' → 'a'
```

---

## 5️⃣ Handle Opposite Case

```python id="kw4ynh"
elif s[right] > s[left]:
```

✨ Meaning:

* Right character is larger
* Replace it with smaller left character

---

## 6️⃣ Move Pointers

```python id="cwknmq"
left += 1
right -= 1
```

👉 Continue toward center.

---

## 7️⃣ Convert Back to String

```python id="0gq0y0"
return ''.join(s)
```

---

# 📊 Example Walkthrough

## Example:

```python id="2afwqj"
s = "egcfe"
```

---

### Step 1 → Compare Ends

```python id="6jgyhy"
e vs e
```

Equal → no change

---

### Step 2 → Move Inward

```python id="p4xzhy"
g vs f
```

Since:

```python id="7zvczx"
g > f
```

Replace:

```python id="h3i6x7"
g → f
```

String becomes:

```python id="u8krva"
"efcfe"
```

---

# 🎯 Final Output

```python id="dzgwqj"
"efcfe"
```

---

# ⏱ Time & Space Complexity

## ⏱ Time Complexity: O(n)

* Traverse string once

---

## 📦 Space Complexity: O(n)

* Extra list used for modification

---

# 💻 Code

```python id="8dk9j7"
class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s=list(s)
        left=0
        right=len(s)-1
        for i in range(len(s)):
            if s[left] > s[right]:
                s[left] = s[right]
            elif s[right] > s[left]:
                s[right] = s[left]
            left+=1
            right-=1
        return ''.join(s)
```

# 🔥 **Beginner Friendly Python Solution | Find Uncommon Words from Two Sentences Using Dictionary**



🚀 **Uncommon Words from Two Sentences | Simple Python Approach 📝**

---

## 🧠 Problem Understanding

We are given two sentences:

* `s1`
* `s2`

👉 Each sentence contains words separated by spaces.

Our task is to:

> Find all words that appear **exactly once** in the combined sentences.

---

### 📌 What are “Uncommon Words”?

A word is **uncommon** if:

* It appears **only once** in total
* It does **not repeat in either sentence**

---

## 🔎 Code Explanation Step-by-Step

---

### 1️⃣ Split Sentences into Word Lists

```python
s1 = list(s1.split(' '))
s2 = list(s2.split(' '))
```

✨ Purpose:

* Convert sentences into lists of words

Example:

```python
s1 = "this apple is sweet"
→ ['this', 'apple', 'is', 'sweet']

s2 = "this apple is sour"
→ ['this', 'apple', 'is', 'sour']
```

---

### 2️⃣ Combine Both Lists

```python
s = s1 + s2
```

✨ Purpose:

* Merge both sentences into a single list

Example:

```python
['this','apple','is','sweet','this','apple','is','sour']
```

---

### 3️⃣ Create Frequency Dictionary

```python
freq = {}
```

This dictionary stores:

* word → number of occurrences

---

### 4️⃣ Count Each Word

```python
for ch in s:
    freq[ch] = freq.get(ch,0) + 1
```

🔍 Example:

```python
freq = {
'this': 2,
'apple': 2,
'is': 2,
'sweet': 1,
'sour': 1
}
```

---

### 5️⃣ Collect Uncommon Words

```python
res = []
for key, value in freq.items():
    if value == 1:
        res.append(key)
```

✨ Explanation:

* If a word appears **exactly once**
* It is considered **uncommon**

---

### 6️⃣ Return Result

```python
return res
```

👉 Final result contains all uncommon words

---

## 📊 Example Walkthrough

### Example:

```python
s1 = "this apple is sweet"
s2 = "this apple is sour"
```

Step 1 → Combine:

```python
['this','apple','is','sweet','this','apple','is','sour']
```

Step 2 → Frequency:

```python
{
'this':2,
'apple':2,
'is':2,
'sweet':1,
'sour':1
}
```

Step 3 → Uncommon words:

```python
['sweet','sour']
```

---

## 🎯 Final Output

```python
['sweet','sour']
```

---

## ⏱ Time & Space Complexity

### ⏱ Time Complexity: O(n + m)

* Splitting sentences → O(n + m)
* Counting words → O(n + m)

---

### 📦 Space Complexity: O(n + m)

* Dictionary stores all words

---

## ⚡ Key Takeaway

👉 This problem is simply:

> **Find words with frequency = 1**

---

## 💻 Code

```python
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1=list(s1.split(' '))
        s2=list(s2.split(' '))
        s= s1 + s2
        freq={}
        for ch in s:
            freq[ch] = freq.get(ch,0) + 1
        res=[]
        for key,value in freq.items():
            if value == 1:
                res.append(key)
        return res
```


# 🔥 Beginner Friendly Python Solution | Keep Multiplying Found Values by Two Using While Loop


## 🚀 **Keep Multiplying Found Values by Two | Simple Python Approach 🔢**




## 🧠 Problem Understanding

We are given:

* An integer array `nums`
* An integer `original`

Our task is:

> Keep checking whether `original` exists in the array.

✔️ If it exists:

* Multiply it by `2`

✔️ Repeat this process until:

* The value no longer exists in the array

Finally:

* Return the final value of `original`

---

## 🔎 Code Explanation Step-by-Step

---

### 1️⃣ Check if Original is Already Missing

```python id="1dfw36"
if original not in nums:
    return original
```

✨ Purpose:

* If the value is not present initially
  👉 No operations are needed

Example:

```python id="n9zbpm"
nums = [1,2,3]
original = 5
```

Since `5` is not in array:

```python id="9wpk5g"
return 5
```

---

### 2️⃣ Create Empty List

```python id="6byi1f"
res = []
```

⚠️ Observation:

* This list is not used later in the code
* So it is unnecessary

---

### 3️⃣ Repeat While Original Exists

```python id="lx58n6"
while original in nums:
```

✨ Purpose:

* Continue operations as long as value exists

---

### 4️⃣ Multiply Original by 2

```python id="o0s2lz"
if original in nums:
    original = original * 2
```

💡 Explanation:

* If number exists
* Double its value

Example:

```python id="mcf14f"
nums = [5,3,6,1,12]
original = 3
```

Step-by-step:

```python id="f0f7ps"
3 exists → 3*2 = 6
6 exists → 6*2 = 12
12 exists → 12*2 = 24
24 not found → stop
```

---

### 5️⃣ Return Final Value

```python id="hmv0vw"
return original
```

---

## 📊 Example Walkthrough

### Example:

```python id="t6ukl4"
nums = [5,3,6,1,12]
original = 3
```

Step 1:

```python id="l7g88g"
3 exists
→ original = 6
```

Step 2:

```python id="1mp5qx"
6 exists
→ original = 12
```

Step 3:

```python id="t3qgto"
12 exists
→ original = 24
```

Step 4:

```python id="tclt4w"
24 not in nums
```

Final Output:

```python id="9cgn30"
24
```

---

## ⏱ Time & Space Complexity

### ⏱ Time Complexity: O(n × k)

Where:

* `n` = length of array
* `k` = number of multiplications

Reason:

* Each `in nums` search takes O(n)

---

### 📦 Space Complexity: O(1)

* No extra meaningful space used

---

## 💻 Code

```python id="n2l8m8"
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        if original not in nums:
            return original
        res=[]
        while original in nums:
            if original in nums:
                original = original * 2

        return original
```

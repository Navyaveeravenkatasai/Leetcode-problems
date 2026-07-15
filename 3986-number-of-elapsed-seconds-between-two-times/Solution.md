# 🚀 🔥🔥Master Time Conversion  ⏰ | 🔥 Simplest Python Solution⚡ | O(1) | Beginner Friendly Guide 💡

# Problem Understanding

We are given two time strings:

* `startTime`
* `endTime`

Both are in the format:

```text
HH:MM:SS
```

Our task is:

> Find the total number of **seconds** between `startTime` and `endTime`.

---

# Key Idea

Instead of comparing hours, minutes, and seconds separately:

1. Convert both time strings into **total seconds**.
2. Subtract the start time (in seconds) from the end time (in seconds).
3. Return the difference.

---

# Code Explanation

## 1. Split the Time Strings

```python id="1"
res = startTime.split(':')
res1 = endTime.split(':')
```

The `split(':')` function separates the time into hours, minutes, and seconds.

Example:

```python id="2"
startTime = "01:20:30"
```

After splitting:

```text
['01', '20', '30']
```

---

## 2. Initialize Variables

```python id="3"
tot = 0
count = 0
```

* `tot` stores the total seconds of `startTime`.
* `count` stores the total seconds of `endTime`.

---

## 3. Convert `startTime` to Seconds

```python id="4"
for ch in range(len(res)):
```

Traverse each part of the time.

### Hours

```python id="5"
tot += int(res[ch]) * 3600
```

There are **3600 seconds** in one hour.

---

### Minutes

```python id="6"
tot += int(res[ch]) * 60
```

There are **60 seconds** in one minute.

---

### Seconds

```python id="7"
tot += int(res[ch])
```

Seconds are added directly.

Example:

```text
01:20:30

Hours   = 1 × 3600 = 3600
Minutes = 20 × 60  = 1200
Seconds = 30

Total = 4830 seconds
```

---

## 4. Convert `endTime` to Seconds

```python id="8"
for ch in range(len(res1)):
```

Repeat the same process for the ending time.

Example:

```text
02:10:20

Hours   = 2 × 3600 = 7200
Minutes = 10 × 60  = 600
Seconds = 20

Total = 7820 seconds
```

---

## 5. Return the Difference

```python id="9"
return count - tot
```

Subtract the total seconds of `startTime` from `endTime`.

---

# Example Walkthrough

### Example

#### Input

```python id="10"
startTime = "01:20:30"
endTime = "02:10:20"
```

Convert to seconds:

```text
Start = 4830

End = 7820
```

Difference:

```text
7820 - 4830 = 2990
```

#### Output

```python
2990
```

---

# Time Complexity

```python
O(1)
```

The loop always runs **3 times** (Hours, Minutes, Seconds), regardless of the input size.

---

# Space Complexity

```python
O(1)
```

Only a few variables and two small lists of fixed size are used.

---

# 💻 Code

```python
class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        res = startTime.split(':')
        res1 = endTime.split(':')

        tot = 0
        count = 0

        for ch in range(len(res)):
            if ch == 0:
                tot += int(res[ch]) * 3600
            elif ch == 1:
                tot += int(res[ch]) * 60
            elif ch == 2:
                tot += int(res[ch])

        for ch in range(len(res1)):
            if ch == 0:
                count += int(res1[ch]) * 3600
            elif ch == 1:
                count += int(res1[ch]) * 60
            elif ch == 2:
                count += int(res1[ch])

        return count - tot
```

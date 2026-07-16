# 🚀 Maximum Achievable Number in One Line 🎯 | Clean Python Solution ⚡ | O(1)  💡


# Problem Understanding

We are given two integers:

* `num`
* `t`

In one operation:

* Increase (or decrease) `x` by `1`.
* Simultaneously increase (or decrease) `num` by `1`.

We can perform this operation **at most `t` times**.

Our task is:

> Return the **maximum possible value of `x`**.

---

# Key Idea

Each operation allows `x` to increase by **1** while `num` also increases by **1**.

After performing `t` operations:

* `num` increases by `t`
* `x` also increases by `t`

So, the maximum achievable value becomes:

```text id="x3d1qa"
num + 2 × t
```

---

# Code Explanation

## 1. Return the Maximum Value

```python id="5qdk2v"
return num  + 2 * t
```

This is equivalent to:

```python id="rckz0x"
num  + 2 * t
```

Example:

```python id="g4q9eh"
num = 4
t = 2
```

Calculation:

```text id="y7b3fz"
4 + 2 * 2  = 8
```

So the answer is:

```python id="r5v4mc"
8
```

---

# Example Walkthrough

### Example 1

#### Input

```python id="g2mg0j"
num = 4
t = 1
```

Calculation:

```text id="g3s0gv"
4 + 2 × 1 = 6
```

#### Output

```python id="jjv2xw"
6
```

---

### Example 2

#### Input

```python id="ld4l2z"
num = 3
t = 2
```

Calculation:

```text id="rkrn9x"
3 + 2 × 2 = 7
```

#### Output

```python id="k9rwqa"
7
```

---

# Time Complexity

```python id="bg6jnz"
O(1)
```

Only one arithmetic calculation is performed.

---

# Space Complexity

```python id="3gbfbg"
O(1)
```

No extra space is used.

---

# 💻 Code

```python id="mjnlza"
class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num  +  2 * t
```

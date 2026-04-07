# 🔥 Clean Two Pointer Python Solution | Minimize Maximum Pair Sum | Easy Explanation


# 🚀 Minimize Maximum Pair Sum in an Array | Two Pointer Python Solution ⚡
**🧠 Problem Understanding**

We are given an integer array nums.

Our goal is to:

1️⃣ Pair the numbers such that each element is used exactly once
2️⃣ For every pair, compute their sum
3️⃣ Among all pair sums, find the maximum pair sum
4️⃣ Return the minimum possible value of this maximum pair sum

💡 The trick is to pair the smallest number with the largest number.

This strategy keeps the pair sums balanced and minimized.

🔎 Code Explanation Step-by-Step
**1️⃣ Sort the Array**
nums.sort()

✨ Sorting helps us easily access:

Smallest elements from the left
Largest elements from the right

Example:

nums = [3,5,2,3]

After sorting:

[2,3,3,5]
**2️⃣ Initialize Two Pointers**
left = 0
right = len(nums) - 1

📌 Purpose:

Pointer	Role
left	points to smallest number
right	points to largest number

This allows us to create pairs like:

smallest + largest
**3️⃣ Create List to Store Pair Sums**
res = []

This list will store the sum of each pair.

**4️⃣ Pair Elements Using Two Pointers**
while left < right:

The loop continues until all elements are paired.

Inside the loop:

sum = nums[left] + nums[right]

Compute the sum of the smallest and largest numbers.

Example:

[2,3,3,5]

Pair 1 → 2 + 5 = 7
Pair 2 → 3 + 3 = 6
**5️⃣ Store Pair Sums**
res.append(sum)

Example:

res = [7,6]
**6️⃣ Move Both Pointers**
left += 1
right -= 1

This moves inward to form the next pair.

Example:

left → next smallest
right → next largest
**7️⃣ Return the Maximum Pair Sum**
return max(res)

Since the problem asks for the maximum pair sum among all pairs, we return:

max(res)

Example:

res = [7,6]

max = 7

**Output:**

7
# 📊 Example Walkthrough

**Input**

nums = [3,5,2,3]

**Step 1 → Sort**

[2,3,3,5]

**Step 2 → Pair numbers**

Pair	Sum
2 + 5	7
3 + 3	6

**Step 3 → Maximum pair sum**

max(7,6) = 7

**Output**

7
⏱ Time & Space Complexity
⏱ Time Complexity
O(n log n)

**Reason:**

Sorting the array takes O(n log n)
Two pointer traversal takes O(n)

**Overall complexity:**

O(n log n)
📦 Space Complexity
O(n)

Because we store pair sums in the list res.
# Complexity
- Time complexity:O(n log n)
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:O(n)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def maxDistinct(self, s: str) -> int:
        s=set(s)
        freq = {}
        total = 0
        for ch in s:
            freq[ch] = freq.get(ch,0) + 1

        for key in freq.values():
            total += key
        return total
```
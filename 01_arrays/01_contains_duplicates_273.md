# 217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

**Example 1:**

```
Input: nums = [1,2,3,1]
Output: true
```

**Example 2:**

```
Input: nums = [1,2,3,4]
Output: false
```

**Example 3:**

```
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

**Constraints:**

`1 <= nums.length <= 105`
`-109 <= nums[i] <= 109`



My submitted solution was to implement a custom hashtable of size n,
thereby reducing Time Complexity from O(n^2) to O(n) and increasing Space Complexity from O(1) to O(n).
Interestingly, this solution still beats 96.7 % of all submitted solutions regarding Memory usage
while being worse than 94.9 % in computation time - presumably because of the 
constant time it takes to instantiate the hashtable.

![image](https://github.com/mquintus/l33tocde/assets/515945/4c065588-a955-41f3-94ac-ac34f3921768)

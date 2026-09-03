"""You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

#Normal approach(O(n^2))
def two_sum_normal(nums,target):
    seen = {}
    for i,num in enumerate(nums):
        needed = target - num
        if needed in seen:
            return [seen[needed],i]
        seen[num] = i
nums = eval(input("Enter an array :"))
target = int(input("Enter a Number :"))
print(two_sum_normal(nums,target))"""
        

#Using HASH MAP(O(n))
def two_sum_hm(nums,target):
    seen = {}
    for i,num in enumerate(nums):
        needed = target - num
        if needed in seen:
            return [seen[needed],i]
        seen[num] = i
nums = eval(input("Enter an array :"))
target = int(input("Enter a Number :"))
print(two_sum_hm(nums,target))
        

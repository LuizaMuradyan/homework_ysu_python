#2

newlist = []
nums1 = [4,9,5,9]
nums2 = [9,4,9,8]
for i in nums1:
    if i in nums2 and i not in newlist:
        newlist.append(i)
print(newlist)

#1 
nums = [1,2,3,4,5,6,7]
k = 3
print(nums[-k:] + nums[:len(nums) - k])

#3

newlist = []
nums = [1,2,3,4]
summ = 0
for j in range(1,len(nums)+1):
    summ = 0
    for i in nums[0:j]:
        summ += i
    newlist.append(summ)
print(newlist)

#Leetcode-20

def isValid(s):
    for _ in range(len(s)//2):
        s = s.replace('()' , '')
        s = s.replace('[]' , '')
        s = s.replace('{}' , '')
    return len(s) == 0
print(isValid('{()}[]([])'))
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    length=len(nums)
    for x in range(0,length):
        print x
        for y in range(x+1,length):
            if ((nums[x]+nums[y])==target):
                print x,y
                return [x,y]
print twoSum([3,2,4],6)
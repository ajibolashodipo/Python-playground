def twoSum(self, nums, target):

    # optimized solution
    dic = {}
    for i, num in enumerate(nums):

        if num in dic:
            return [i, dic[num]]
        else:
            dic[target - num] = i

    # brute force
    #         length= len(nums)
    #         for i in range(length-1):
    #             for j in range(i+1, length):
    #                 if nums[i] +nums[j] == target:
    #                     return [i,j]


class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        i = 0
        op = []
        for i in range(len(nums)):
            if (i>0 and nums[i]==nums[i-1]):
                continue
            else:
                rem = -1*(nums[i])
                P1 = i+1
                P2 = len(nums) - 1
                while (P1<P2):
                    if (nums[P1]+nums[P2]<rem):
                        P1=P1+1
                    elif (nums[P1]+nums[P2]>rem):
                        P2=P2-1
                    else:
                        print(nums[i],nums[P1],nums[P2])
                        op.append([nums[i],nums[P1],nums[P2]])
                        if (nums[P1]==nums[P2]):
                            break
                        else:
                            x=nums[P1]
                            y=nums[P2]
                            while (nums[P1]==x):
                                P1=P1+1
                            while (nums[P2]==y):
                                P2=P2-1
        return op
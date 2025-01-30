# Ok so we got a integer array of size n, and we neeed to return the number with  the value closest to 0 in that array. If there are multiple answers, return the number with the largest value

# The first thing that goes to mind go through the array and put the first number as the closest and see if  there is any number closer than it
# We can take the first elemenent because in the constrains we always have atleast one element, next we check if any number in nums is lower than the first one, we check the absolute values, and if we have two answers say -1 and 1, we need to take 1 the higher value, because of that we use max
from typing import List


def findClosestNumber(self, nums: List[int]) -> int:
        closest_number=nums[0]
        for i in range(1,len(nums)):
            if abs(nums[i])<abs(closest_number):
                closest_number=nums[i]
            elif abs(nums[i])==abs(closest_number):
                closest_number=max(nums[i],closest_number)
        
        return closest_number

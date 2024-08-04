class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #Initialized a hashmap to keep track of the indices and its corresponding values
        hm = {} # { number : index }

        #loop through the array
        for i in range(len(nums)):
            
            #calculates the difference between the target and the current value
            what_we_need = target - nums[i]

            #if the difference is in the hashmap -> return the indices
            if what_we_need in hm:
                return [hm[what_we_need], i]
            hm[nums[i]] = i


            #Time Complexity: O(n) where n is the number of elements in the list
            #Space Complexity: O(n) where n is the number of elements in the list
        
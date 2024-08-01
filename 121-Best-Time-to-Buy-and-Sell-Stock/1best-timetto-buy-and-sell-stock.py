class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #edge cases
        if not prices:
            return 0
        
        #intialize the lowest_number
        lowest_number = prices[0]
        max_profit = 0

        #traverse through the array:
        for num in prices:
            #if we come across an element in the list that is lower than the lowest_number
            if num < lowest_number:
                #change it to the lowest_number
                lowest_number = num
            
            #if we do not come across an element < lowest_price
            #compare it with the max_price we have
            max_profit = max(max_profit, num - lowest_number)
        
        return max_profit
            
        
"""
Given an array prices[] of length n, representing the prices of the stocks on different days. The task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell. If it is not possible to make a profit then return 0.
Examples:
Input: prices[] = [7, 10, 1, 3, 6, 9, 2]
Output: 8
Explanation: You can buy the stock on day 2 at price = 1 and sell it on day 5 at price = 9. Hence, the profit is 8.
"""

def sortArray(arr):
    size = len(arr)
    
    if size <= 1:
        return arr
    
    p = arr[-1]
    
    L = [i for i in arr[:-1] if i <= p]
    R = [i for i in arr[:-1] if i > p]
    
    L = sortArray(L)
    R = sortArray(R)
    
    return L + [p] + R

def stockBuyAndSell(arr):
    size = len(arr)
    minn = arr[0]
    maxx = arr[0]
    
    if size < 2:
        return 0
    
    for n in arr:
        if n < minn:
            minn = n  
        elif n > maxx:
            maxx = n
            
    minIndex = arr.index(minn)
    maxIndex = arr.index(maxx)
    
    reversed_array = sortArray(arr)[::-1]
    
    if reversed_array == arr:
        return 0
    
    # This process takes too much time if the RAM or memory is low
    while minIndex > maxIndex:
        maxx = arr[maxIndex+1]
        for n in arr[minIndex:]:
            if n > maxx:
                maxx = n
        maxIndex = arr.index(maxx)
    
    minIndex = arr.index(minn)
    maxIndex = arr.index(maxx)
    
    print("MinIndex: ", minIndex)
    print("MaxIndex: ", maxIndex)
    
    return arr[maxIndex] - arr[minIndex]

def solutionStockBuyAndSell(prices):
    # Initialize the the minimum buy price as the first price in the list
    buy_price = prices[0]
    # Initialize the maximum profit as 0
    max_profit = 0
    
    # Iterate through the list of prices starting from the second price (index 1)
    for i in range(1, len(prices)):
        # Update the maximum profit if the current profit (prices[i] - buy_price) is greater
        max_profit = max(max_profit, prices[i] - buy_price)
        
        # Update the minimum buy if the current price is less than the buy_price
        buy_price = min(buy_price, prices[i])
        
    return max_profit
    
prices = [7, 10, 1, 3, 6, 9, 2]
prices = [7, 6, 4, 3, 1]
prices = [9, 8, 2, 6, 3]

print(stockBuyAndSell(prices))
print(solutionStockBuyAndSell(prices))

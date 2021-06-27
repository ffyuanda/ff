# https://leetcode.com/problems/can-place-flowers/

""" This one is easy, have to take care of small flowerbed and the index
out of range issue. """

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        length = len(flowerbed)
        if n == 0: return True
        
        if len(flowerbed) == 1:
            return True if flowerbed[0] == 0 else False
        
        for i in range(length):
            if flowerbed[i] == 1: 
                continue
            else:
                if i == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                    continue
                    
                elif i == length - 1 and flowerbed[i-1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                    continue
                    
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1

        return n <= 0
                
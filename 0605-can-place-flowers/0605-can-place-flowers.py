class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        def can_place_flower(flowerbed, n, position):
            
            # To avoid "list index out of range"......
            if n == 0:
                return True
            if position >= len(flowerbed):
                return False
            
            if flowerbed[position] == 0:
                if (position == 0 or flowerbed[position - 1] == 0) and (position == len(flowerbed) - 1 or flowerbed[position + 1] == 0):
                    flowerbed[position] = 1

                    return can_place_flower(flowerbed, n - 1, position + 2)
                else:
                    return can_place_flower(flowerbed, n, position + 1)
            else:
                return can_place_flower(flowerbed, n, position + 1)

        # start point
        return can_place_flower(flowerbed, n, 0)
                    
                    
                
        
        
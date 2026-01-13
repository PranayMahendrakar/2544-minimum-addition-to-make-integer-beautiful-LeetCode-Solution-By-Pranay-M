class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def digit_sum(x):
            return sum(int(d) for d in str(x))
        
        original = n
        place = 1
        
        while digit_sum(n) > target:
            # Round up to next multiple of 10^place
            # This sets the last 'place' digits to 0
            n = (n // (10 * place) + 1) * (10 * place)
            place *= 10
        
        return n - original
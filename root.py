import math

def solution(numbers):
    n = len(numbers)
    result = []
    
    # TODO: implement this function
    for i in range(n):
        a = numbers[i]
        b = numbers[n - 1 - i]
        geo_mean = math.sqrt(a * b)
        result.append((a, round(geo_mean, 2)))
        
    return result    
         
    
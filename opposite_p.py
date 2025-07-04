def solution(numbers):
    result = []
    number_set = set(numbers)
    
    for num in numbers:
        reversed_num = int(str(num)[::-1])
        if reversed_num in number_set:
            result.append((num, reversed_num))
    # TODO: implement solution here
    return result
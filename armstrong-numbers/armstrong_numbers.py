def is_armstrong_number(number):
    nums = str(number)
    return sum([int(x)**len(nums) for x in nums]) == number

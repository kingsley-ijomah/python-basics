def classify(number):
    check_value_error(number)

    aliquot = sum_factors(number)

    if aliquot == number:
        return("perfect")
    if aliquot < number:
        return("deficient")
    if aliquot > number:
        return("abundant")

def check_value_error(number):
    if number <= 0:
        raise ValueError("Not a natural number")

def sum_factors(number):
    return sum([x for x in range(1, number) if number%x == 0])
def sum_of_digits_of_power_of_2(n):
    if n <= 0:
        return -1

    result = 2 ** n
    sum_of_digits = 0
    while result > 0:
        digit = result % 10
        sum_of_digits += digit
        result //= 10
    
    return sum_of_digits

# Example usage:
n = 15
result = sum_of_digits_of_power_of_2(n)
print("Sum of digits of 2 raised to the power", n, "is:", result)

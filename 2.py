def find_greatest(num1, num2, num3, num4):
    greatest = num1

    if num2 > greatest:
        greatest = num2
    
    if num3 > greatest:
        greatest = num3
    
    if num4 > greatest:
        greatest = num4
    
    return greatest

# Example usage:
num1 = 10
num2 = 20
num3 = 15
num4 = 25
greatest_number = find_greatest(num1, num2, num3, num4)
print("The greatest number is:", greatest_number)

def sum_of_cubes(n):
    total = 0
    n -= 1
    
    while n > 0:
        total += n ** 3
        n -= 1
    return total
# Example usage:

number  = int(input("Enter a positive integer: "))
print("Sum of cubes of smaller integers:", sum_of_cubes(number))
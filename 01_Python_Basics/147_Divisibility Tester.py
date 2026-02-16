def multiple(n, m):
    if n == 0:
        return False
    
    return m % n == 0


# Example usage:

print(multiple(3, 9))  # True
print(multiple(4, 10)) # False
print(multiple(0, 5))  # False
    
    
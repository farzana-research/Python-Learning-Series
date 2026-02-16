def max_min(data):
    if not data:
        raise ValueError("The input data cannot be empty.") 
    l = s = data[0]
    
    for num in data:
        if num > l:
            l = num
        if num < s:
            s = num
    return l, s

print(max_min([0, 10, 15, 40, -5, 42, 17, 28, 75]))
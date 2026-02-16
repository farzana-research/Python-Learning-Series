def test(n):
    if isinstance(n, int):
        return "It is an integer!"
    elif isinstance(n, str):
        return "It is a String!"
    else:
        return "Unknown type"
print(test(12))
print(test('23312'))   # string input
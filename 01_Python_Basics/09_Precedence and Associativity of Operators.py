# This is used in an expression with more than one operator with different precedence to determine which operation to perform first.


expr = 10 + 20 * 30 
print(expr)  # Output will be 610 because multiplication has higher precedence than addition
name =  "John"
age = 0

if name == "John" or name == "Alex" and age >= 2:
    print("Hello! Welcome. ")
    
else:
    print("Goodbye!")# In the above example, the 'and' operator has higher precedence than the 'or' operator, so the condition 'name == "Alex" and age >= 2' is evaluated first.
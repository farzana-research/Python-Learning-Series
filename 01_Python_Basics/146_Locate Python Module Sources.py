import importlib.util

def find_module_location(module_name):
    spec = importlib.util.find_spec(module_name)
    if spec and spec.origin:
        return spec.origin
    else:
        return f"Module '{module_name}' not found or is a built-in module."

print("Location of Python os module sources:")
print(find_module_location('os'))

print("Location of Python datetime module sources:")
print(find_module_location('datetime'))
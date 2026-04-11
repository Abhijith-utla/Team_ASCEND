def sat(x: float):
    return str(x - 3.1417).startswith("123.456")

def sol():
    return "123.456"

# The function 'sat' checks if the string '123.456' is equal to the result of subtracting 3.1417 from x.
# If the result is '123.456', the function returns the string '123.456'. If not, it returns None.
# This is because the comparison 'return str(x - 3.1417).startswith("123.456")' will return True only if x is equal to '123.456'.

# The checker will run:
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

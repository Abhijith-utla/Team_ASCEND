def sat(x: float):
    return str(x - 3.1415).startswith("123.456")

def sol():
    return "123.456"

# The function 'sat' checks if the string '123.456' is equal to the result of subtracting 3.1415 from the given number. If it is, the function returns 'True', otherwise it returns 'False'.
# The function 'sol' returns the string '123.456' as the result.

if __name__ == "__main__":
    assert sat(sol())

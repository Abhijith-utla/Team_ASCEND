def sat(x: float):
    return str(x - 3.1415).startswith("123.456")

def sol():
    return "123.456"

# The function 'sat' is already defined by the user and returns a string with the value of 'x - 3.1415' if it starts with '123.456'.
# The function 'sol' is defined to return the string "123.456".
# The checker will run: assert sat(sol())

# Please note that the actual return value of 'sol()' might not be exactly "123.456" as it depends on the actual Python interpreter and its environment settings.

if __name__ == "__main__":
    assert sat(sol())

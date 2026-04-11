def sat(x: float):
    return str(x - 3.1415).startswith("123.456")

def sol():
    return "3.1415"

# Checker code
def sat(x: float):
    return str(x - 3.1415).startswith("123.456")

assert sat(sol()) == True

if __name__ == "__main__":
    assert sat(sol())

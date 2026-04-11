def sat(s: str):
    return str(8 ** 2888).count(s) > 8 and len(s) == 3

def sol():
    return "8" * 888

# This assert statement will pass if the function returns the correct answer
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

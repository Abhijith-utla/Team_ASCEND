def sat(s: str):
    return set(s) <= set("1-8*+/3") and s.count("8") == 3 and s.count("1") == 1 and eval(s.replace('+', '//')) == 63

def sol():
    return "1-8*+3"

# The assert statement is used to test the correctness of a piece of code.
# It's used to make sure that the code is working as expected.
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

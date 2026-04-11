def sat(expression):
    return eval(expression)

def sol():
    return 5

# Test
assert sat(sol()) == 5

if __name__ == "__main__":
    assert sat(sol())

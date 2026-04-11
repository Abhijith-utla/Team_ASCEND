def sat(expression):
    return eval(expression)

def sol():
    return {}

# The following lines are for the purpose of the checker
assert sat(sol.__code__.co_code)

if __name__ == "__main__":
    assert sat(sol())

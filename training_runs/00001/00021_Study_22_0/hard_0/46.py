def sat(s: str):
    return s[::2] in s and len(set(s)) == 5

def sol():
    return 'xyaa' if sat('xyaa') else 'not_a_solution'

# Testing
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

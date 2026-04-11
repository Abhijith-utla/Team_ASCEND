def sat(s: str):
    return float(s) + len(s) == 4.5

def sol():
    return float(input()) + len(input()) == 4.5

# Testing the function
assert sat(sol)

if __name__ == "__main__":
    assert sat(sol())

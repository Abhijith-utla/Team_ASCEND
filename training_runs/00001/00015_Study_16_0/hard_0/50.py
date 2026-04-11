def sat(s: str):
    return float(s) + len(s) == 4.5

def sol():
    s = input()
    if sat(s):
        return s
    else:
        return None

def sat(s: str):
    return float(s) + len(s) == 4.5

# Testing the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

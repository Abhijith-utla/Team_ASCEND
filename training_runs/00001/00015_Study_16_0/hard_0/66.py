def sat(s: str):
    return float(s) + len(s) == 4.5

def sol():
    return float(len(str(int(4.5))))

# Testing
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

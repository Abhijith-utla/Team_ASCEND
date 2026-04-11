def sat(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

def sol():
    return "".join([i for i in str(8 ** 1818) if i.isdigit() and i != '0' and i != '8' and len(i) % 2 == 1][-1])[-1:-5:-1]

# Testing the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

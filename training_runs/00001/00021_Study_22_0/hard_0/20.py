def sat(s: str):
    return s[::2] in s and len(set(s)) == 5

def sol():
    return "".join(s[::2] for s in [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)])

# test the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

def sat(s: str):
    return s.count('s') == 300 and s.count('ss') == 301 and s.count('sss') == 298

def sol():
    return 's' * 300 + 's' * 301 + 's' * 298

print(sol())

# Testing the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

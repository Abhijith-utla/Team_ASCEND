def sat(s: str):
    return s.count('o') == 1000 and s.count('oo') == 0

def sol():
    return 'oo' * 1000

def sat(s: str):
    return s.count('o') == 1000 and s.count('oo') == 0

# test cases
print(sat(sol()))  # should return True
print(sat(sol() + sol()))  # should return True
print(sat(sol() * 10))  # should return False

if __name__ == "__main__":
    assert sat(sol())

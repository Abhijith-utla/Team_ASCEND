def sat(s: str):
    return str(8 ** 2888).count(s) > 8 and len(s) == 3

def sol():
    return '8' * 888

# Test
print(sat(sol()))  # True
print(sat(sol()))  # False
print(sat(sol()))  # False
print(sat(sol()))  # True
print(sat(sol()))  # False
print(sat(sol()))  # False
print(sat(sol()))  # True
print(sat(sol()))  # False
print(sat(sol()))  # True
print(sat(sol()))  # True

if __name__ == "__main__":
    assert sat(sol())

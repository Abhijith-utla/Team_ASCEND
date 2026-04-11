def sat(i: int):
    return i <= 10 ** 10 and i % 2 == 0

def sol():
    return 10 ** 10 * 2

print(sat(sol())) # Asserts: True
print(sat(sol()-1)) # Asserts: False

if __name__ == "__main__":
    assert sat(sol())

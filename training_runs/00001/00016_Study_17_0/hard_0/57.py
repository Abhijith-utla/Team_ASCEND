def sat(i: int):
    return len(str(i + 1000)) > len(str(i + 1001))

def sol(i):
    return len(str(i + 1000)) > len(str(i + 1001))

print(sol(1))  # False
print(sol(2))  # True
print(sol(3))  # True
print(sol(4))  # False

if __name__ == "__main__":
    assert sat(sol())

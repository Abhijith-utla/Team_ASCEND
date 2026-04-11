def sat(i: int):
    return i % 123 == 4 and i > 10 ** 10

def sol():
    answer = 1100000000000000
    return answer

# Checker will run: assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

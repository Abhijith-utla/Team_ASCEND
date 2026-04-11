def sat(i: int):
    return i % 123 == 4 and i > 10 ** 10

def sol():
    answer = (10 ** 10) + 4
    return answer

# The assertion checks that the answer is a multiple of 123, and is greater than 10^10.
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

def sat(i: int):
    return i % 5 == 0 and i < 100

def sol():
    return 25  # Assuming that 25 is the smallest number that is divisible by both 5 and 100

if __name__ == "__main__":
    assert sat(sol())

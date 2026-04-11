def sat(x):
    for i in range(len(x) - 1):
        if x[i] > x[i + 1]:
            return False
    return True

def sol():
    x = [random.randint(0, 100) for _ in range(10)]  # Randomly generated list of integers
    x = sorted(x)  # Sorted list
    return x

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

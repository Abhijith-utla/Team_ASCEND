def sat(x):
    for i in range(len(x) - 1):
        if x[i] >= x[i + 1]:
            return False
    return True

def sol():
    return [i for i in range(10) if i < 5]

if __name__ == "__main__":
    assert sat(sol())

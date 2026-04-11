def sat(x):
    return all(int(x[i]) <= int(x[i + 1]) for i in range(len(x) - 1))

def sol():
    return ""

if __name__ == "__main__":
    assert sat(sol())

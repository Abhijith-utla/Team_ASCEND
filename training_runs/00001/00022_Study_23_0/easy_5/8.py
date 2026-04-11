def sat(answer):
    return all(a == b for a, b in zip(answer, 'd'))

def sol():
    return 'd' * len('d')

if __name__ == "__main__":
    assert sat(sol())

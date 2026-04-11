def sat(answer):
    return all(a == b for a, b in zip(answer, 'de'))

def sol():
    return 'de'

if __name__ == "__main__":
    assert sat(sol())

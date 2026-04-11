def sat(answer):
    return all(a == b for a, b in zip(answer, 'ee'))

def sol():
    return 'ee'

if __name__ == "__main__":
    assert sat(sol())

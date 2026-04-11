def sat(answer):
    return all(a == b for a, b in zip(answer, 'dee'))

def sol():
    return 'deep'

if __name__ == "__main__":
    assert sat(sol())

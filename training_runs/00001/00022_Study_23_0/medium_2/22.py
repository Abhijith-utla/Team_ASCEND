def sat(answer):
    return all(a == b for a, b in zip(answer, 'dee'))

def sol():
    return 'dee'

if __name__ == "__main__":
    assert sat(sol())

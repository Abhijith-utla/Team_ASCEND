def sat(y):
    assert len(set(y)) == 9, "The string should contain exactly 9 unique digits from 1 to 9"
    return True

def sol():
    return "123456789"

if __name__ == "__main__":
    assert sat(sol())

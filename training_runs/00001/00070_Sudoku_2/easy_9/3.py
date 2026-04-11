def sat(y):
    assert len(set(y)) == 9, "The string should contain exactly 9 unique digits from 1 to 9"
    return True

def sol():
    return ["1","2","3","4","5","6","7","8","9"]

if __name__ == "__main__":
    assert sat(sol())

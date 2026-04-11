def sat(y):
    assert '1' in y and '2' in y and '3' in y and '4' in y and '5' in y and '6' in y, "The string should contain all digits from 1 to 6"
    return True

def sol():
    return "123456"

if __name__ == "__main__":
    assert sat(sol())

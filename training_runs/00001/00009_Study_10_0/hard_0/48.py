def sat(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

def sol():
    def sat(s: str):
        return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

    for i in range(1, 12):
        for j in range(1234567890, 10000000000):
            number = str(i * j)
            if sat(number):
                return number
    return None

if __name__ == "__main__":
    assert sat(sol())

def sat(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

def sol():
    answer = "".join([i for i in str(8 ** 1818) if i == i[::-1] and len(i) > 11])
    return answer

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

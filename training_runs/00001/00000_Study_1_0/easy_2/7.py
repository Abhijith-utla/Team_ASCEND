def sat(s: str):
    return len(s) == 1000 and 'o' in s

def sol():
    return 'a'*1000 + 'o'

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

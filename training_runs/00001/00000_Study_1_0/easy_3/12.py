def sat(s: str):
    return len(s) == 1000 and sum(c == 'o' for c in s) == 1000

def sol():
    return 'o'*1000

if __name__ == "__main__":
    assert sat(sol())

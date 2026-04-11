def sat(s: str):
    return len(s) == 1000 and sum(c == 'o' for c in s) == 1000

def sol():
    return ''.join('o' for _ in range(1000))

if __name__ == "__main__":
    assert sat(sol())

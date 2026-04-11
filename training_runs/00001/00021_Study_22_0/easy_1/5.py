def sat(s: str) -> bool:
    return len(s) == 10 and s.isalpha()

def sol():
    s = input()
    while not sat(s):
        s = input()
    return s

if __name__ == "__main__":
    assert sat(sol())

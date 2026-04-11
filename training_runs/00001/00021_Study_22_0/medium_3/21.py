def sat(s: str) -> bool:
    if len(s) < 5 or len(s) > 30:
        return False
    return len(set(s)) == 5 and s[::2] == s[1::2]

def sol():
    def is_even(s: str) -> bool:
        return s[::2] == s[1::2]

    def is_valid(s: str) -> bool:
        return len(s) < 5 or len(s) > 30

    while True:
        s = input()
        if is_valid(s) and is_even(s):
            return s

if __name__ == "__main__":
    assert sat(sol())

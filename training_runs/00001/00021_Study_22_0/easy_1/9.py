def sat(s: str) -> bool:
    return len(s) == 10 and s.isalpha()

def sol():
    return "abcdefghij"

if __name__ == "__main__":
    assert sat(sol())

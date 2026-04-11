def sat(s: str) -> bool:
    if len(s) > 30 or len(s) < 5:
        return False
    return len(set(s)) == len(s)

def sol():
    return "This is a test string."

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

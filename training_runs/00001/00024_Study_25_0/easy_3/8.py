def sat(s: str, r: str) -> bool:
    return sorted(s) == sorted(r) and s == r

def sol():
    return sat('acbd', 'bacd')

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

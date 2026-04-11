def sat(s: str, r: str) -> bool:
    return sorted(s) == sorted(r) and s == r

def sol():
    return "".join(sorted(input()))

assert sat(sol(), "".join(sorted(input())))

if __name__ == "__main__":
    assert sat(sol())

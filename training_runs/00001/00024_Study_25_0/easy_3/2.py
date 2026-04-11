def sat(s: str, r: str) -> bool:
    return sorted(s) == sorted(r) and s == r

def sol():
    return sat("racecar", "car race")

if __name__ == "__main__":
    assert sat(sol())

def sat(s: str, r: str) -> bool:
    return sorted(s) == sorted(r) and s == r

def sol():
    return ""

assert sat(sol(), "")
assert sat(sol(), "abc")
assert not sat(sol(), "cba")
assert sat(sol(), "aabbcc")
assert not sat(sol(), "abcabc")

if __name__ == "__main__":
    assert sat(sol())

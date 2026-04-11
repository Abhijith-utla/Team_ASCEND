def sat(s: str) -> bool:
    return str(8 ** int(2888)).count(s) > 8 and len(s) == 3

def sol():
    s = "888" * 3
    return s

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())

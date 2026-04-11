def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

def sol():
    return len(max(min(range(1, 1000), key=len)))

print(sol())

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

def sat(li: List[int]):
    return li.count(17) == 3 and li.count(3) >= 2

def sol():
    return [17, 17, 3]

# This assertion will pass if the function sol returns a list with exactly three 17s followed by at least two 3s
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

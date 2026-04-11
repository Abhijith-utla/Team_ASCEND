def sat(li: List[str]):
    return sum([1 for i in li if ord(i) % 3 == 0]) == 0

def sol():
    return [i for i in range(100) if ord(chr(i)) % 3 == 0]

# Testing the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

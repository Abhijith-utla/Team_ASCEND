def sat(li: List[str]):
    return sum([1 for i in li if ord(i) % 3 == 0]) == 0

def sol(li: List[str]):
    return sum([1 for i in li if ord(i) % 3 == 0]) == 0

# Run the code
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

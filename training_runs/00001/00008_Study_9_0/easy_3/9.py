def sat(li: List[str]):
    return sum([1 for i in li if ord(i) % 3 == 2]) == 0

def sol():
    return sat(['a', 'b', 'c'])

def sat(li: List[str]):
    return sum([1 for i in li if ord(i) % 3 == 2]) == 0

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())

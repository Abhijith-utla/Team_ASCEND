def sat(li: List[str]):
    return sum([1 for i in li if ord(i) % 3 == 1]) == 0

def sol():
    return ord('a') % 3 == 1

print(sol())

if __name__ == "__main__":
    assert sat(sol())

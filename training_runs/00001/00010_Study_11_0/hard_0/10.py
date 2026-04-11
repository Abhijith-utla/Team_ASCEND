def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

def sol():
    return sat(["apple", "banana", "cherry"])

print(sol())  # True or False

if __name__ == "__main__":
    assert sat(sol())

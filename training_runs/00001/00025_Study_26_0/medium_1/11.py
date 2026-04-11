def sat(ls: List[str]):
    return "".join(ls) == str(7 ** 64.5) and all(len(s) == 8 for s in ls)

def sol():
    ls = ["12345678", "90123456", "78901234", "56789012", "34567890", "12345678", "90123456", "78901234"]
    return ls

# print(sol())
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

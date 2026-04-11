def sat(ls: List[str]):
    return "".join(ls) == str(8 ** 88) and all(len(s) == 8 for s in ls)

def sol():
    return "".join(["E" * 8 for _ in range(88)])

# Checker
print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())

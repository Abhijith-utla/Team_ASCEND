def sat(ls: List[str]):
    return "".join(ls) == str(8 ** 88) and all(len(s) == 8 for s in ls)

def sol():
    return [str(8 ** i) for i in range(88)]

# Run the checker
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

def sat(ls: List[str]):
    return "".join(ls) == str(12345678) and all(len(s) == 8 for s in ls)

def sol():
    return [chr(int(str(i)[:2]) + str(i)[2:]) for i in range(1000000, 10000000, 10)]

# print(sol())

# print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())

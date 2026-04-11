def sat(ls: List[str]):
    return "".join(ls) == str(987654321) and all(len(s) == 8 for s in ls)

def sol():
    return [str(num) for num in range(1,8)]

print(sol())

if __name__ == "__main__":
    assert sat(sol())

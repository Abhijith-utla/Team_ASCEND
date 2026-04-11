def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

def sol():
    return [max(len(x), len(str(len(x)))) for x in range(10)]

print(sol())

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

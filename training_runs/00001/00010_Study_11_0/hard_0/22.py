def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

def sol(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

print(sol(['1', '2', '3']))

if __name__ == "__main__":
    assert sat(sol())

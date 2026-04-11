def sat(lst: List[str]):
    return all(int(lst[i]) <= int(lst[i+1]) for i in range(len(lst)-1))

def sol():
    return []

if __name__ == "__main__":
    assert sat(sol())

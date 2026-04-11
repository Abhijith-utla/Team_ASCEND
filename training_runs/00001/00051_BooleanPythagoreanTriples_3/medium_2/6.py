def sat(lst: List[str]):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

def sol():
    return []

if __name__ == "__main__":
    assert sat(sol())

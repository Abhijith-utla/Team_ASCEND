def sat(ls: List[str]) -> bool:
    return all(s not in ls for s in ls)

def sol() -> List[str]:
    return []

if __name__ == "__main__":
    assert sat(sol())

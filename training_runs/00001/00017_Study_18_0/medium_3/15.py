def sat(ls: List[str]) -> bool:
    return len(ls) == len(set(ls))

def sol():
    return len(set(input("Enter elements separated by space: ").split())) > 1

if __name__ == "__main__":
    assert sat(sol())

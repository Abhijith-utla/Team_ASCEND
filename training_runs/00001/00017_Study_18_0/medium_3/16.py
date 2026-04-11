def sat(ls: List[str]) -> bool:
    return len(ls) == len(set(ls))

def sol():
    return len(set(input("Enter a list of strings separated by commas: ").split(','))) > 1

assert sat(sol)

if __name__ == "__main__":
    assert sat(sol())

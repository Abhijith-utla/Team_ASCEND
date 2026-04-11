def sat(ls: List[str]) -> bool:
    return all(len(set(s)) == len(s) for s in ls)

def sol():
    return len(set(''.join(sorted(input("Enter strings separated by space: ").split())))) == 1

assert sat(sol)

if __name__ == "__main__":
    assert sat(sol())

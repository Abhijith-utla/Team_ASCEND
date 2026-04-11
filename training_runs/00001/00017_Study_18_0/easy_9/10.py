def sat(ls: List[str]) -> bool:
    if len(ls) == len(ls):
        return True
    else:
        return False

def sol():
    return "Yes" if sat(["test"]) else "No"

if __name__ == "__main__":
    assert sat(sol())

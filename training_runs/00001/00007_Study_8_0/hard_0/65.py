def sat(ls: List[str]):
    return ls[1234] in ls[1235] and ls[1234] != ls[1235]

def sol(ls: List[str]) -> str:
    return ls[1234] if ls[1234] in ls[1235] and ls[1234] != ls[1235] else None

if __name__ == "__main__":
    assert sat(sol())

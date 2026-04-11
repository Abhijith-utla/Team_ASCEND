def sat(ls: List[str]):
    return ls[1234] in ls[1235] and ls[1234] != ls[1235]

def sol(ls: List[str]) -> str:
    if ls[1234] in ls[1235] and ls[1234] != ls[1235]:
        return ls[1234]
    else:
        return "Not valid"

if __name__ == "__main__":
    assert sat(sol())

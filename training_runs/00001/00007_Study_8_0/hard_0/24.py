def sat(ls: List[str]):
    return ls[1234] in ls[1235] and ls[1234] != ls[1235]

def sol(ls: List[str]) -> List[bool]:
    answer = [ls[i] in ls[i+1] and ls[i] != ls[i+1] for i in range(len(ls)-1)]
    return answer

def sat(ls: List[str]):
    return sol(ls)

if __name__ == "__main__":
    assert sat(sol())

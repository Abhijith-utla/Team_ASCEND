def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

def sol(answer: List[str]):
    if sat(answer):
        return answer
    else:
        return []

def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

if __name__ == "__main__":
    assert sat(sol())

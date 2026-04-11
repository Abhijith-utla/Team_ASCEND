def sat(li: List[int]):
    return sorted(li) == list(range(999)) and all(li[i] != i for i in range(len(li)))

def sol(li: List[int]):
    sorted_li = sorted(li)
    if sorted_li == list(range(999)):
        for i in range(len(li)):
            if li[i] != i:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    assert sat(sol())

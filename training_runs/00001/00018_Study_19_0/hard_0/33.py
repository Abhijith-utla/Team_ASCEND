def sat(li: List[int]):
    return {i + j for i in li for j in li} == {0, 1, 2, 3, 4, 5, 6, 17, 18, 19, 20, 34}

def sol():
    li = [0, 1, 2, 3, 4, 5, 6]
    set_li = {i for i in li}
    set_ex = {i + j for i in li for j in li}
    return set_ex == {0, 1, 2, 3, 4, 5, 6, 17, 18, 19, 20, 34}

def sat(li: List[int]):
    return {i + j for i in li for j in li} == {0, 1, 2, 3, 4, 5, 6, 17

if __name__ == "__main__":
    assert sat(sol())

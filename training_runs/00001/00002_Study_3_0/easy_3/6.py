def sat(li: List[int]):
    return sorted(li) == list(range(998)) and all(li[i] != i for i in range(998)) and len(li) == 999

def sol():
    def sat(li: List[int]):
        return sorted(li) == list(range(998)) and all(li[i] != i for i in range(998)) and len(li) == 999

    li = [i for i in range(999)]
    li.pop(0)

    assert sat(li)
    return sorted(li)

if __name__ == "__main__":
    assert sat(sol())

def sat(li: List[int]):
    return sorted(li) == list(range(999)) and all(li[i] == i for i in range(len(li)))

def sol():
    def sat(li: List[int]):
        return sorted(li) == list(range(999)) and all(li[i] == i for i in range(len(li)))

    assert sat(list(range(999)))
    return None

if __name__ == "__main__":
    assert sat(sol())

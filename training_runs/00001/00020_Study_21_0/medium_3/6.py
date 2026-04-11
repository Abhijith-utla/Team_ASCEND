def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(7)]) and len(set(li)) == 3

def sol():
    def sat(li: List[int]):
        return all([li[i] != li[i + 1] for i in range(7)]) and len(set(li)) == 3
    assert sat([1, 2, 3, 4, 5, 6, 7])
!python

if __name__ == "__main__":
    assert sat(sol())

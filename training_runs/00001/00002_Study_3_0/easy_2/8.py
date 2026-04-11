def sat(li: List[int]):
    return sorted(li) == list(range(999)) and all(li[i] != i for i in range(999)) and len(li) == 1000

def sol():
    def sat(li: List[int]):
        return sorted(li) == list(range(999)) and all(li[i] != i for i in range(999)) and len(li) == 1000
    return []

def test():
    assert sat([])
    assert not sat([1])
    assert sat([0]*998 + [999])
    assert not sat([998]*1000)
    assert not sat([i]*1000 for i in range(999))
    print("All tests passed")

if __name__ == "__main__":
    test()

if __name__ == "__main__":
    assert sat(sol())

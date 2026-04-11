def sat(li: List[int]):
    return all([li.count(i) == i for i in range(1, 11)])

def sol():
    def sat(li: List[int]):
        for i in range(1, 11):
            if li.count(i) != i:
                return False
        return True
    
    assert sat(list(range(1, 21)))
    assert not sat(list(range(1, 20)))
    assert sat(list(range(1, 11)))
    assert not sat(list(range(1, 10)))
    assert not sat(list(range(1, 100)))
    assert sat(list(range(1, 1)))
    assert not sat(list(range(1, 0)))
    assert not sat([])

    # Test with random list
    import random
    li = [random.randint(1, 10) for _ in range(100)]
    assert sat(li)
    li = [random.randint(1, 10) for _ in range(99)]
    assert not sat(li)

# Call the main function
sol()

if __name__ == "__main__":
    assert sat(sol())

def sat(li: List[int]):
    return all([li.count(i) == i for i in range(1, 11)])

def sol():
    def sat(li: List[int]):
        for i in range(1, 11):
            if li.count(i) != i:
                return False
        return True

    # Generate a random list of 10 random integers between 1 and 10
    import random
    li = [random.randint(1, 10) for _ in range(10)]
    assert sat(li)
    return li

print(sol())

if __name__ == "__main__":
    assert sat(sol())

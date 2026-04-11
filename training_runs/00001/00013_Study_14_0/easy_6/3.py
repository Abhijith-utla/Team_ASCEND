def sat(li: List[int]):
    return all(li.index(x) < sum(li[:i]) for i in range(len(li)) for x in set(li))

def sol():
    li = [1, 3, 5, 6, 4, 3, 2, 4, 4, 5, 6, 6]
    assert sat(li)
    return 'The list is correct.'

print(sol())

if __name__ == "__main__":
    assert sat(sol())

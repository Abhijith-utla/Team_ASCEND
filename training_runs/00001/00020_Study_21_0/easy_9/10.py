def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(5)])

def sol():
    return None

print(sat([1, 2, 3, 4, 5]))
print(sat([1, 1, 3, 4, 5]))
print(sat([1, 2, 3, 4, 6]))

if __name__ == "__main__":
    assert sat(sol())

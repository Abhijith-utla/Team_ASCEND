def sat(x: List[int], length=535) -> bool:
    return all(x[i] <= x[i + 1] for i in range(length - 1))

def sol():
    return []

print(sat([1, 2, 3, 4, 5]))
print(sat([1, 5, 3, 4, 2]))
print(sat([2, 5, 3, 4, 1]))
print(sat([1, 2, 5, 3, 4]))
print(sat([4, 5, 3, 2, 1]))
print(sat([4, 3, 5, 2, 1]))
print(sat([5, 3, 2, 4, 1]))
print(sat([5, 4, 3, 2, 1]))
print(sat([4, 5, 2, 3, 1]))
print(sat([1, 2, 3, 4, 5, 6]))

if __name__ == "__main__":
    assert sat(sol())

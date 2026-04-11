def sat(nums):
    return sorted([int(str(n)*2) for n in nums]) == list(range(1, 10))

def sol():
    return []

print(sat([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(sat([2, 4, 6, 8, 1, 3, 5, 7, 9]))
print(sat([3, 9, 2, 8, 5, 1, 4, 7, 6]))
print(sat([5, 7, 9, 6, 4, 2, 8, 1, 3]))

if __name__ == "__main__":
    assert sat(sol())

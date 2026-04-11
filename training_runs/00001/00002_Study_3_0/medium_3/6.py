def sat(li: List[int]):
    return sorted(li) == list(range(999)) and all(li[i] != i for i in range(len(li)-1))

def sol(li: List[int]):
    li.sort()
    for i in range(1, len(li)):
        if li[i] == li[i-1]:
            return False
    return True

print(sol([1, 2, 3, 4, 5]))  # Should return True
print(sol([5, 4, 3, 2, 1]))  # Should return False

if __name__ == "__main__":
    assert sat(sol())

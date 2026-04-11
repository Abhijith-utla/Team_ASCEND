def sat(li: List[int]):
    return all(abs(i - j) >= 10 for i in li for j in li) and len(set(li)) == 10

def sol():
    return {}

print(sat([])) # False
print(sat([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # True
print(sat([5, 5, 5, 5, 5, 5, 5, 5, 5, 6])) # False
print(sat([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # True
print(sat([1, 2, 3, 4, 5, 6, 7, 8, 9, 11])) # False
print(sat([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # True

if __name__ == "__main__":
    assert sat(sol())

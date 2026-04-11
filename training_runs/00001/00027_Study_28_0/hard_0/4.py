def sat(li: List[int]):
    return all(i in range(1000) and abs(i - j) >= 10 for i in li for j in li if i != j) and len(set(li)) == 100

def sol():
    return [i for i in range(1000) if i not in [j for j in range(1000) if abs(i - j) >= 10]]

# This line should return an error, because the list does not satisfy the condition
# print(sol())

# This line should not return an error
print(sat(sol()))

# This line should also return an error, because the list does not satisfy the condition
print(sat([i for i in range(1000) if i not in [j for j in range(1000) if abs(i - j) >= 10]]))

# This line should not return an error
print(sat([i for i in range(1000) if i != j for j in range(1000) if abs(i - j) >= 10]))

if __name__ == "__main__":
    assert sat(sol())

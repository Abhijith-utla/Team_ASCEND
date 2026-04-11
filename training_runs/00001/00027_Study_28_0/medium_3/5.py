def sat(li: List[int]):
    return all(abs(i - j) >= 10 for i in li for j in li if i != j) and len(li) == 100

def sol():
    return [i for i in range(100) if all(abs(i - j) >= 10 for j in range(100) if i != j)]

print(sat(sol()))  # AssertionError: 1
print(sat(sol()))  # AssertionError: 2
print(sat(sol()))  # AssertionError: 3
print(sat(sol()))  # AssertionError: 4
print(sat(sol()))  # AssertionError: 5
print(sat(sol()))  # AssertionError: 6
print(sat(sol()))  # AssertionError: 7
print(sat(sol()))  # AssertionError: 8
print(sat(sol()))  # AssertionError: 9
print(sat(sol()))  # AssertionError: 10

if __name__ == "__main__":
    assert sat(sol())

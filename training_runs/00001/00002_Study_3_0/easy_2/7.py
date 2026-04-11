def sat(li: List[int]):
    return sorted(li) == list(range(999)) and all(li[i] != i for i in range(999)) and len(li) == 1000

def sol():
    return [1]*1000

# Test the solution
print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())

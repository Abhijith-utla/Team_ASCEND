def sat(numbers: List[int], n=2):
    assert len(numbers) >= n
    return all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-n))

def sol():
    return []

# The function sol does not take any arguments, so we can directly return an empty list
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

def sat(numbers: List[int], n=2):
    assert len(numbers) >= n
    return all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-n))

def sol():
    return []

# Correct pattern
def sol(numbers):
    assert sat(numbers)
    return numbers

# Incorrect pattern
def sol(numbers):
    assert sat(numbers, n=5)
    return numbers

if __name__ == "__main__":
    assert sat(sol())

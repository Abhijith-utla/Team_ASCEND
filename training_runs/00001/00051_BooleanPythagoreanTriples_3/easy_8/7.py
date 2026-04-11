def sat(numbers: List[int], n=3):
    assert len(numbers) >= n
    return all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-n))

def sol():
    return []

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

def sat(numbers: List[int]):
    return all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1, 0, -1))

def sol():
    return []

if __name__ == "__main__":
    assert sat(sol())

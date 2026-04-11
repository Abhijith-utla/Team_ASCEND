def sat(numbers: List[int], n=3):
    assert len(numbers) >= n
    return all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-n))

def sol():
    return []

# Correct answer:
# def sol(numbers: List[int], n=3):
#     assert len(numbers) >= n
#     return all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-n))

if __name__ == "__main__":
    assert sat(sol())

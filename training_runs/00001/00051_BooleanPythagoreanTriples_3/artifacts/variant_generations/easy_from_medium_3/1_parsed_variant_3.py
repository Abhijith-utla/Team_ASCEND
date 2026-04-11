def sat(numbers: List[int], n=4):
    assert len(numbers) >= n
    return all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-n))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")

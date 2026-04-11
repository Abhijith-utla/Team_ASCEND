def sat(numbers: List[int]):
    return all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")

def sat(x: List[int], y: List[int]) -> bool:
    return all(x[i] <= y[i] for i in range(len(x)))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")

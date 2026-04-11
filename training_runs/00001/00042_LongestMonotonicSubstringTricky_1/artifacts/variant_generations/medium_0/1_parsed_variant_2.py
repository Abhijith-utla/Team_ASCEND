def sat(x: List[int], length=535) -> bool:
    return all(x[i] <= x[i + 1] for i in range(length - 1))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")

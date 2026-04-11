def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(7)])

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")

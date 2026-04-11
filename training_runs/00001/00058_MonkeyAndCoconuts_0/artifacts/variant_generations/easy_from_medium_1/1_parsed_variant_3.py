def sat(n: int):
    for _ in range(100):
        assert n % 5 == 0
        n -= 1
    return n > 0

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")

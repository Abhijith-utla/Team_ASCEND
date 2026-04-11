def sat(a: int, b: float) -> bool:
    return a - b == math.sqrt(a**2 + b**2)

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")

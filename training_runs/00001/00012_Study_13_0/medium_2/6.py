def sat(x: float):
    return str(x - 3.1416).startswith("123.456")

def sol():
    x = float(input("Enter a float number: "))
    while not sat(x):
        print("Not a valid answer. Please try again.")
        x = float(input("Enter a float number: "))
    return x

print("Correct pattern:")
print("def sol():")
print("    return <answer>")
print("")
print("Incorrect pattern:")
print("def sol(x):")
print("    ... ")

if __name__ == "__main__":
    assert sat(sol())

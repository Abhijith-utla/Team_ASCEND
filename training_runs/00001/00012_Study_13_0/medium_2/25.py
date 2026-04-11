def sat(x: float):
    return str(x - 3.1416).startswith("123.456")

def sol():
    x = 0.0
    while True:
        x += 0.0001
        if sat(x):
            return str(x)
```

The function `sol` calculates the decimal number by adding 0.0001 to the current value of `x` in an infinite loop until the condition `sat(x)` is met, at which point it returns the string representation of `x`.

if __name__ == "__main__":
    assert sat(sol())

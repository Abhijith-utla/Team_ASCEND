def sat(colors):
    assert set(colors) <= {0, 1} and len(colors) >= 10000
    squares = {i ** 2: colors[i] for i in range(1, len(colors))}
    return not any(c == d == squares.get(i + j) for i, c in squares.items() for j, d in squares.items())

def sol():
    return []

# We use the random.choice function from the random module to randomly choose the colors.
import random
colors = [random.choice([0, 1]) for _ in range(10000)]

assert sat(colors)

if __name__ == "__main__":
    assert sat(sol())

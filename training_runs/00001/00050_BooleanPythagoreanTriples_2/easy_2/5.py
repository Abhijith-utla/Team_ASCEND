def sat(n):
    def inner(colors):
        squares = {i ** 2: colors[i] for i in range(1, len(colors))}
        return not any(c == d == squares.get(i + j) for i, c in squares.items() for j, d in squares.items())
    return inner

def sol():
    return lambda colors: (lambda i: lambda j: lambda c: lambda d: not any(c(i) == d(j) == c(i + j) for i, _ in enumerate(colors) for j, _ in enumerate(colors)))()

if __name__ == "__main__":
    assert sat(sol())

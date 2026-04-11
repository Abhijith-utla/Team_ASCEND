def sat(n):
    def inner(colors):
        squares = {i ** 2: colors[i] for i in range(1, len(colors))}
        return not any(c == d == squares.get(i + j) for i, c in squares.items() for j, d in squares.items())
    return inner

def sol():
    def inner(colors):
        squares = {i ** 2: colors[i] for i in range(1, len(colors))}

if __name__ == "__main__":
    assert sat(sol())

def sat(colors):
    assert set(colors) <= {0, 1}, 'Colors must be in {0, 1}'
    assert len(colors) >= 10, 'Length of colors must be greater than or equal to n'
    return not any(colors[i] == colors[j] for i in range(len(colors)) for j in range(i + 1, len(colors)))

def sol():
    return []

print(sol())

if __name__ == "__main__":
    assert sat(sol())

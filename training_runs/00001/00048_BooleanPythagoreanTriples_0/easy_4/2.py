def sat(colors):
    assert set(colors) <= {0, 1}, 'Colors must be in {0, 1}'
    return not any(colors[i] == colors[j] for i in range(len(colors)) for j in range(i + 1, len(colors)))

def sol():
    return [0, 1]

if __name__ == "__main__":
    assert sat(sol())

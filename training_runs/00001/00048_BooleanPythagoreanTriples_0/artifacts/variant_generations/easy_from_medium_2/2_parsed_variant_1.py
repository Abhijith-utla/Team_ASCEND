def sat(colors):
    assert set(colors) <= {0, 1}, 'Colors must be in {0, 1}'
    return not any(colors[i] == colors[j] for i in range(len(colors)) for j in range(i + 1, len(colors)))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")

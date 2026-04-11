def sat(x):
    return all(x[i] <= x[i + 1] for i in range(len(x) - 1))

def sol():
    return [3, 2, 1]

print(sat(sol())) # This should be True

if __name__ == "__main__":
    assert sat(sol())

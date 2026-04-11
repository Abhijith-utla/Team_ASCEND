def sat(l: list):
    return all(i in range(1, 1000) and abs(i * i - j * j) >= 10 for i in l for j in l if i != j)

def sol():
    for i in range(1, 1000):
        for j in range(i + 1, 1000):
            if (i * i + j * j) ** 0.5 % 1 == 0:
                if not all(k in range(1, 1000) for k in range(1, i) if i * i - j * j == k * k):
                    return False
    return True

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())

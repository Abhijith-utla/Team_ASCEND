def sat(l: list):
    return all(i in range(1000) and abs(i * i - j * j) < 10 for i in l for j in l if i == j)

def sol():
    answer = []
    for i in range(1000):
        for j in range(i, 1000):
            if i * i + j * j < 1000:
                answer.append((i, j))
    return answer

print(sol())

if __name__ == "__main__":
    assert sat(sol())

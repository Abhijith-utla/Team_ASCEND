def sat(i: int):
    return i % 123 == 4 and i > 10 ** 10

def sol():
    answer = -1
    for i in range(10 ** 10 + 1, 10 ** 11):
        if sat(i):
            answer = i
            break
    return answer

if __name__ == "__main__":
    assert sat(sol())

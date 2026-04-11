def sat(ls):
    return ls[1234] > ls[1235] and ls[1234] != ls[1235]

def sol():
    answer = []
    for i in range(1000):
        answer.append(i)
    return answer

if __name__ == "__main__":
    assert sat(sol())

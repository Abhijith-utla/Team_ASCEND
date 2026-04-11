def sat(ls):
    return ls[1234] < ls[1235] and ls[1234] != ls[1235]

def sol():
    answer = [1, 2, 3, 4, 5]
    return answer

if __name__ == "__main__":
    assert sat(sol())

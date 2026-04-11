def sat(ls):
    return ls[1234] in ls[1235] and ls[1234] != ls[1235]

def sol():
    answer = [1234, 1235, 1236]
    return answer

print(sol())

if __name__ == "__main__":
    assert sat(sol())

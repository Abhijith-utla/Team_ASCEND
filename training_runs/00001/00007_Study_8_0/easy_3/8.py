def sat(ls):
    return ls[1234] < ls[1235] and ls[1234] != ls[1235]

def sol():
    def sat(ls):
        return ls[1234] < ls[1235] and ls[1234] != ls[1235]

    return sat

if __name__ == "__main__":
    assert sat(sol())

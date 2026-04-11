def sat(ls):
    return ls[1234] > ls[1235] and ls[1234] != ls[1235]

def sol():
    return [1234, 1235, 1236, 1237, 1238, 1239, 1240, 1241, 1242, 1243, 1244, 1245, 1246, 1247, 1248, 1249, 1250]

if __name__ == "__main__":
    assert sat(sol())

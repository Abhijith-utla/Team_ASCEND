def sat(ls):
    return ls[1234] in ls[1235] and ls[1234] != ls[1235]

def sol():
    return {"answer": {"result": True}}

if __name__ == "__main__":
    assert sat(sol())

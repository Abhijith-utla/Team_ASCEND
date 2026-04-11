def sat(ls):
    return ls[1234] > ls[1235] and ls[1234] != ls[1235]

def sol():
    return {'result': 'Correct'} if sat([1234]*1000 + [1235]*1000) else {'result': 'Incorrect'}

def sat(ls):
    return ls[1234] > ls[1235] and ls[1234] != ls[1235]

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())

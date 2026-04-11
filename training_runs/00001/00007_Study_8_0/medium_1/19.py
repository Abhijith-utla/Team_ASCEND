def sat(ls):
    return ls[1234] in ls[1235] and ls[1234] != ls[1235]

def sol():
    return {
        "answer1": True,
        "answer2": True,
        "answer3": True,
        "answer4": True,
        "answer5": True
    }

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

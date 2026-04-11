def sat(i: int):
    return i <= 10 ** 10 and i % 2 == 0

def sol():
    class Answer:
        def __init__(self, valid, output):
            self.valid = valid
            self.output = output

    return Answer(sat(1), 2)

def sat(i: int):
    return i <= 10 ** 10 and i % 2 == 0

if __name__ == "__main__":
    assert sat(sol())

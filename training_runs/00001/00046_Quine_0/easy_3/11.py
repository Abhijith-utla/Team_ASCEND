def sat(quine):
    return str(quine) == quine

def sol():
    return "I am a quine!"

if __name__ == "__main__":
    assert sat(sol())

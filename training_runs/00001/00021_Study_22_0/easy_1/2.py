def sat(s: str) -> bool:
    return len(s) == 10 and s.isalpha()

def sol():
    return 'correctanswer' if sat('correctanswer') else 'incorrectanswer'

if __name__ == "__main__":
    assert sat(sol())

def sat(s: str):
    if s.count('o') != 0:
        return False
    return True

def sol():
    return "I am a robot, I can't solve problems!"

if __name__ == "__main__":
    assert sat(sol())

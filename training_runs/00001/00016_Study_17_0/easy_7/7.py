def sat(i: int) -> bool:
    return len(str(i + 1000)) < len(str(i + 1001))

def sol():
    return "answer"

if __name__ == "__main__":
    assert sat(sol())

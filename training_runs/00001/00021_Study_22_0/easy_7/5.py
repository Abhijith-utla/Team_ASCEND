def sat(s: str) -> bool:
    if len(s) > 30 or len(s) < 5:
        return False
    return len(set(s)) == len(s)

def sol():
    return "success" if sat("success") else "failure"

if __name__ == "__main__":
    assert sat(sol())

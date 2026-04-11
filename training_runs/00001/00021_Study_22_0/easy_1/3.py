def sat(s: str) -> bool:
    return len(s) == 10 and s.isalpha()

def sol():
    return "PythonCode"

if __name__ == "__main__":
    assert sat(sol())

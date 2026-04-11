def sat(s: str) -> bool:
    return len(s) == 10 and s.isalpha()

def sol():
    return "PythonProgramming"

if __name__ == "__main__":
    assert sat(sol())

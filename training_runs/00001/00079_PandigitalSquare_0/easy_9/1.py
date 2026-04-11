def sat(n: int) -> bool:
    s = str(n)
    return len(s) == len(set(s)) and s.isdigit()

def sol():
    return <answer>

if __name__ == "__main__":
    assert sat(sol())

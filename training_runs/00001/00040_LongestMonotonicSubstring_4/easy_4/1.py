def sat(x: List[int], s: str):
    return all(s[i] <= s[i + 1] for i in range(len(x) - 1))

def sol():
    return []

def main():
    assert sat(sol())

main()

if __name__ == "__main__":
    assert sat(sol())

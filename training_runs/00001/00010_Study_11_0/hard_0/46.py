def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

def sol():
    return len(min([input() for _ in range(int(input()))])) == int(input()) == int(max([input() for _ in range(int(input()))]))

if __name__ == "__main__":
    assert sat(sol())

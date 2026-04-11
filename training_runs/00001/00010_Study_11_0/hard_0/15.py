def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

def sol():
    return len(max(input().split())) == len(min(input().split())) == len(input())

if __name__ == "__main__":
    assert sat(sol())

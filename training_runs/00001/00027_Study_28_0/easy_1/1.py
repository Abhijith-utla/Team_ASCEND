def sat(li: List[int]):
    return all(i not in li for i in range(1000)) and abs(min(li)-max(li)) < 10

def sol():
    def check(n):
        li = [False]*1000
        for i in n:
            li[i] = True
        return all(i not in li for i in range(1000)) and abs(min(n)-max(n)) < 10
    return check

if __name__ == "__main__":
    assert sat(sol())

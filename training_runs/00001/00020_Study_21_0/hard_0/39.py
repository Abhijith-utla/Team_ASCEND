def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(10)]) and len(set(li)) == 3

def sol():
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    while True:
        li[li.index(min(li))] += 1
        if sat(li):
            return {"answer": li}
!pip install sympy

if __name__ == "__main__":
    assert sat(sol())

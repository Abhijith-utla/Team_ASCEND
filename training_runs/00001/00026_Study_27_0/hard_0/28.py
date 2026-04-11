def sat(li: List[int]):
    return li[li[0]] != li[li[1]] and li[li[li[0]]] == li[li[li[1]]]

def sol():
    return [1, 2, 3, 4]

# Checker
def check_sol(sol_fn):
    li = sol_fn()
    assert sat(li)

check_sol(sol)

if __name__ == "__main__":
    assert sat(sol())

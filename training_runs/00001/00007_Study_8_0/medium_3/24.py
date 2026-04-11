def sat(ls, idx1=1234, idx2=1235, value=ls[idx1]):
    return ls[idx1] in ls[idx2] and ls[idx1] != value

def sol():
    def sat(ls, idx1=1234, idx2=1235, value=ls[idx1]):
        return ls[idx1] in ls[idx2] and ls[idx1] != value

    def unsat():
        return False

    solution = None
    for i in range(100):
        ls = [i for _ in range(100)]
        if sat(ls):
            solution = i
            break

    if solution is None:
        return unsat()
    else:
        return solution

if __name__ == "__main__":
    assert sat(sol())

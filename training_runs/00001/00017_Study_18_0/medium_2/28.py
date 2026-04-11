def sat(ls: List[str]) -> bool:
    return all(len(set(s)) == len(s) for s in ls)

def sol():
    return {
        "answer": "I am a python function, sol, defined to satisfy the problem's condition."
    }

if __name__ == "__main__":
    assert sat(sol())

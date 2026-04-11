def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

def sol(ls: List[str]) -> str:
    return min(ls)

# Check if the solution is correct
def sat(ls: List[str]):
    return sol(ls) == min(ls)

if __name__ == "__main__":
    assert sat(sol())

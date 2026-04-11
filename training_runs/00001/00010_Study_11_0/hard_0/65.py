def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

def sol(ls: List[str]) -> str:
    if len(ls) == 0:
        return ""
    
    if not all(isinstance(x, str) for x in ls):
        return "Invalid input: list should contain only strings"
    
    if len(ls) != len(set(ls)):
        return "Invalid input: list should contain unique elements"
    
    if not all(len(x) == len(ls[0]) for x in ls):
        return "Invalid input: all strings should have the same length"
    
    if min(ls) != max(ls):
        return "Invalid input: strings in the list should be equal"
    
    return min(ls)

print(sol(["abc", "def", "ghi"]))

if __name__ == "__main__":
    assert sat(sol())

def sat(li):
    return not any(abs(i - j) < 10 for i in li for j in li if i != j) and len(li) == 100

def sol():
    return []

# Insert code here to solve the problem

if __name__ == "__main__":
    assert sat(sol())

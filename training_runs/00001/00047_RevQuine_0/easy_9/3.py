def sat(lst: list):
    return lst == lst[::-1]

def sol():
    return []

if __name__ == "__main__":
    assert sat(sol())

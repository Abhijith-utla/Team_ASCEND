def sat(i: int):
    return i > 0 and i % 2 == 0

def sol():
    while True:
        i = int(input("Please enter an integer: "))
        if sat(i):
            return i
!

if __name__ == "__main__":
    assert sat(sol())

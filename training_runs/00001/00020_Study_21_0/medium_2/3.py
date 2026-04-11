def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(8)]) and len(set(li)) == 3

def sol():
    def helper(li: List[int]):
        if len(set(li)) == 3:
            for i in range(8):
                if li[i] == li[i + 1]:
                    return False
            return True
        return False

    return helper

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

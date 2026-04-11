def sat(li: List[int]):
    return all([i < li.index(x) + sum(li[:li.index(x)]) for x in set(li)])

def sol():
    def sat(li: List[int]):
        def inner(x: int):
            li_clone = li.copy()
            li_clone.remove(x)
            sum_list = sum(li_clone)
            for i, value in enumerate(li_clone):
                if value < (sum_list - li_clone[:i].sum()):
                    return False
            return True

        for x in set(li):
            if not inner(x):
                return False
        return True

    return sat

# Test
answer = sol()
assert answer([5, 3, 2, 1, 4])()
assert not answer([5, 3, 2, 4, 1])()
assert answer([5, 3, 2, 4, 1, 5])()
assert not answer([5, 3, 2, 4, 1, 6])()

if __name__ == "__main__":
    assert sat(sol())

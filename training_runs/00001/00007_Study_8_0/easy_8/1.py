def sat(ls, idx1=-1, idx2=-1, value=None):
    if idx1 < 0 or idx2 < 0 or value is None:
        return False  # If any of the indices or value is invalid, it cannot be correct
    return ls[idx1] in ls[idx2] and ls[idx1] != value

def sol():
    class Answer:
        def __init__(self, valid, idx1, idx2, value):
            self.valid = valid
            self.idx1 = idx1
            self.idx2 = idx2
            self.value = value
    if sat.__code__.co_argcount != 0:
        return Answer(False, -1, -1, None)
    idx1, idx2, value = -1, -1, None
    if sat(idx1, idx2, value):
        return Answer(True, idx1, idx2, value)
    else:
        return Answer(False, idx1, idx2, value)

if __name__ == "__main__":
    assert sat(sol())

def sat(ls, idx1=1, idx2=2):
    return ls[idx1] in ls[idx2] and ls[idx1] != ls[idx2]

def sol():
    def sat(ls, idx1=1, idx2=2):
        return ls[idx1] in ls[idx2] and ls[idx1] != ls[idx2]

    def sat_with_idx(ls, idx1, idx2):
        return ls[idx1] in ls[idx2] and ls[idx1] != ls[idx2]

    def sat_with_val(ls, val1, idx2):
        return any(val1 == val for val in ls[idx2])

    def sat_with_val_and_idx(ls, val1, idx1, idx2):
        return ls[idx1] in ls[idx2] and ls[idx1] != ls[idx2]

    return sat, sat_with_idx, sat_with_val, sat_with_val_and_idx

if __name__ == "__main__":
    assert sat(sol())

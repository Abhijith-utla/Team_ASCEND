def sat(daygroups):
    assert len(daygroups) == 7
    assert all(len(groups) == 5 and all(i in g for g in groups) == set(range(1, 15)) for groups in daygroups)
    assert all(len(g) == 5 for groups in daygroups)
    return len({(i, j) for groups in daygroups for g in groups for i in g for j in g}) == 64

def sol():
    return [
        [
            [1, 2, 3, 4, 5], 
            [6, 7, 8, 9, 10], 
            [11, 12, 13, 14, 15]
        ], 
        [
            [16, 17, 18, 19, 20], 
            [21, 22, 23, 24, 25], 
            [26, 27, 28, 29, 30]
        ], 
        [
            [31, 32, 33, 34, 35], 
            [36, 37, 38, 39, 40], 
            [41, 42, 43, 44, 45]
        ], 
        [
            [46, 47, 48, 49, 50], 
            [51,

if __name__ == "__main__":
    assert sat(sol())

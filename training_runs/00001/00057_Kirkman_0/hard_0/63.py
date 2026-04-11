def sat(daygroups: List[List[List[int]]]):
    assert len(daygroups) == 7
    assert all(len(groups) == 5 and {i for g in groups for i in g} == set(range(15)) for groups in daygroups)
    assert all(len(g) == 3 for groups in daygroups for g in groups)
    return len({(i, j) for groups in daygroups for g in groups for i in g for j in g}) == 15 * 15

def sol():
    return [
        [[5, 1, 2], [7, 3, 4], [6, 8, 9], [10, 11, 12], [13, 14, 15]],
        [[1, 5, 11], [2, 6, 12], [3, 7, 13], [4, 8, 14], [9, 10, 15]],
        [[3, 1, 8], [4, 2, 9], [5, 6, 10], [7, 11, 15], [12, 13, 14]],
        [[4, 5, 10], [1, 6, 11], [2, 7, 12], [3, 8, 13], [9, 14, 15]],
        [[1, 2, 7, 12, 15], [3, 4, 8, 13,

if __name__ == "__main__":
    assert sat(sol())

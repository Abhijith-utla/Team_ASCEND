def sat(daygroups: List[List[List[int]]]):
    assert len(daygroups) == 7
    assert all(len(groups) == 5 and {i for g in groups for i in g} == set(range(15)) for groups in daygroups)
    assert all(len(g) == 3 for groups in daygroups for g in groups)
    return len({(i, j) for groups in daygroups for g in groups for i in g for j in g}) == 15 * 15

def sol():
    daygroups = [[[3, 4, 12], [2, 5, 13], [1, 6, 14], [0, 7, 15], [10, 11, 1]], [[1, 2, 7], [3, 4, 8], [5, 6, 9]], [[14, 0, 13], [11, 12, 15], [10, 1, 2]], [[8, 13, 4], [7, 14, 5], [6, 15, 0]], [[3, 4, 12], [2, 5, 13], [1, 6, 14], [0, 7, 15], [10, 11, 1]], [[1, 2, 7], [3, 4, 8], [5, 6, 9]]]
    return daygroups

if __name__ == "__main__":
    assert sat(sol())

def sat(moves: List[int], start=[[1, 5, 0], [3, 2, 8], [6, 4, 7]]):

    locs = {i: [x, y] for y, row in enumerate(start) for x, i in enumerate(row)}  # locations, 0 stands for blank
    for i in moves:
        assert abs(locs[0][0] - locs[i][0]) + abs(locs[0][1] - locs[i][1]) == 1
        locs[0], locs[i] = locs[i], locs[0]
    return all(locs[i] == [i % len(start[0]), i // len(start)] for i in locs)

def sol(moves: List[int], start=[[1, 5, 0], [3, 2, 8], [6, 4, 7]]):

    locs = {i: [x, y] for y, row in enumerate(start) for x, i in enumerate(row)}  # locations, 0 stands for blank
    for i in moves:
        assert abs(locs[0][0] - locs[i][0]) + abs(locs[0][1] - locs[i][1]) == 1
        locs[0], locs[i] = locs[i], locs[0]
    return all(locs[i] == [i % len(start[0]), i // len(start)] for i in locs)

# Test cases
print(sol([1, 3, 0, 2]))  # True
print(sol([1, 3, 2, 0]))  # False
print(sol([1, 2, 3, 0]))  # False
print(sol([0,

if __name__ == "__main__":
    assert sat(sol())
